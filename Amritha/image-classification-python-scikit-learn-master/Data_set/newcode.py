import os
import shutil
import numpy as np
from PIL import Image
from keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions
import tkinter as tk
from tkinter import filedialog, messagebox

dog_breeds = {
    "affenpinscher": "dog",
    "afghan_hound": "dog",
    "airedale_terrier": "dog",
    "akita": "dog",
    "alaskan_malamute": "dog",
    "american_bulldog": "dog",
    "american_cocker_spaniel": "dog",
    "american_english_coonhound": "dog",
    "american_eskimo_dog": "dog",
    "american_foxhound": "dog",
    "american_hairless_terrier": "dog",
    "american_leopard_hound": "dog",
    "american_pit_bull_terrier": "dog",
    "american_staffordshire_terrier": "dog",
    "american_water_spaniel": "dog",
    "anatolian_shepherd_dog": "dog",
    "appenzeller_sennenhund": "dog",
    "australian_cattle_dog": "dog",
    "australian_kelpie": "dog",
    "australian_shepherd": "dog",
    "australian_terrier": "dog",
    "azawakh": "dog",
    "barbet": "dog",
    "basenji": "dog",
    "basset_hound": "dog",
    "beagle": "dog",
    "bearded_collie": "dog",
    "beauceron": "dog",
    "bedlington_terrier": "dog",
    "belgian_laeekenois": "dog",
    "belgian_malinois": "dog",
    "belgian_sheepdog": "dog",
    "belgian_tervuren": "dog",
    "bergamasco": "dog",
    "berger_picard": "dog",
    "bernese_mountain_dog": "dog",
    "bichon_frise": "dog",
    "black_and_tan_coonhound": "dog",
    "black_russian_terrier": "dog",
    "bloodhound": "dog",
    "bluetick_coonhound": "dog",
    "boerboel": "dog",
    "bolognese": "dog",
    "border_collie": "dog",
    "border_terrier": "dog",
    "borzoi": "dog",
    "boston_terrier": "dog",
    "bouvier_des_flandres": "dog",
    "boxer": "dog",
    "boykin_spaniel": "dog",
    "bracco_italiano": "dog",
    "braque_du_bourbonnais": "dog",
    "braque_francais_pyrenean": "dog",
    "briard": "dog",
    "brittany": "dog",
    "broholmer": "dog",
    "brussels_griffon": "dog",
    "bull_terrier": "dog",
    "bulldog": "dog",
    "bullmastiff": "dog",
    "cairn_terrier": "dog",
    "canaan_dog": "dog",
    "cane_corso": "dog",
    "cardigan_welsh_corgi": "dog",
    "catahoula_leopard_dog": "dog",
    "caucasian_shepherd_dog": "dog",
    "cavalier_king_charles_spaniel": "dog",
    "central_asian_shepherd_dog": "dog",
    "cesky_terrier": "dog",
    "chesapeake_bay_retriever": "dog",
    "chihuahua": "dog",
    "chinese_crested": "dog",
    "chinese_shar_pei": "dog",
    "chinook": "dog",
    "chow_chow": "dog",
    "cirneco_dell_etna": "dog",
    "clumber_spaniel": "dog",
    "cockapoo": "dog",
    "cocker_spaniel": "dog",
    "collie": "dog",
    "corgi": "dog",
    "coton_de_tulear": "dog",
    "curly_coated_retriever": "dog",
    "dachshund": "dog",
    "dalmatian": "dog",
    "dandie_dinmont_terrier": "dog",
    "danish_swedish_farmdog": "dog",
    "deutsche_bracke": "dog",
    "doberman_pinscher": "dog",
    "dogo_argentino": "dog",
    "dogue_de_bordeaux": "dog",
    "dutch_shepherd": "dog",
    "english_bulldog": "dog",
    "english_cocker_spaniel": "dog",
    "english_foxhound": "dog",
    "english_setter": "dog",
    "english_springer_spaniel": "dog",
    "english_toy_spaniel": "dog",
    "entlebucher_mountain_dog": "dog",
    "estrela_mountain_dog": "dog",
    "eurasier": "dog",
    "field_spaniel": "dog",
    "finnish_lapphund": "dog",
    "finnish_spitz": "dog",
    "flat_coated_retriever": "dog",
    "fox_terrier": "dog",
    "french_bulldog": "dog",
    "german_longhaired_pointer": "dog",
    "german_pinscher": "dog",
    "german_shepherd": "dog",
    "german_shorthaired_pointer": "dog",
    "german_spaniel": "dog",
    "german_spitz": "dog",
    "german_wirehaired_pointer": "dog",
    "giant_schnauzer": "dog",
    "glen_of_imaal_terrier": "dog",
    "golden_retriever": "dog",
    "gordon_setter": "dog",
    "grand_basset_griffon_vendeen": "dog",
    "great_dane": "dog",
    "great_pyrenees": "dog",
    "greater_swiss_mountain_dog": "dog",
    "greyhound": "dog",
    "hamiltonstovare": "dog",
    "harrier": "dog",
    "havanese": "dog",
    "hokkaido": "dog",
    "hound": "dog",
    "hovawart": "dog",
    "ibizan_hound": "dog",
    "icelandic_sheepdog": "dog",
    "irish_red_and_white_setter": "dog",
    "irish_setter": "dog",
    "irish_terrier": "dog",
    "irish_water_spaniel": "dog",
    "irish_wolfhound": "dog",
    "italian_greyhound": "dog",
    "japanese_chin": "dog",
    "japanese_spitz": "dog",
    "jindo": "dog",
    "kai_ken": "dog",
    "karelian_bear_dog": "dog",
    "keeshond": "dog",
    "kerry_blue_terrier": "dog",
    "king_charles_spaniel": "dog",
    "klee_kai": "dog",
    "komondor": "dog",
    "kromfohrlander": "dog",
    "kuvasz": "dog",
    "labradoodle": "dog",
    "labrador_retriever": "dog",
    "lagotto_romagnolo": "dog",
    "lakeland_terrier": "dog",
    "lancashire_heeler": "dog",
    "leonberger": "dog",
    "lhasa_apso": "dog",
    "lowchen": "dog",
    "maltese": "dog",
    "manchester_terrier": "dog",
    "mastiff": "dog",
    "miniature_bull_terrier": "dog",
    "miniature_pinscher": "dog",
    "miniature_schnauzer": "dog",
    "mixed_breed": "dog",
    "mountain_cur": "dog",
    "mudi": "dog",
    "neapolitan_mastiff": "dog",
    "newfoundland": "dog",
    "norfolk_terrier": "dog",
    "norwegian_buhund": "dog",
    "norwegian_elkhound": "dog",
    "norwegian_lundehund": "dog",
    "norwich_terrier": "dog",
    "nova_scotia_duck_tolling_retriever": "dog",
    "old_english_sheepdog": "dog",
    "otterhound": "dog",
    "papillon": "dog",
    "parson_russell_terrier": "dog",
    "pekingese": "dog",
    "pembroke_welsh_corgi": "dog",
    "perro_de_presa_canario": "dog",
    "peruvian_inca_orchid": "dog",
    "petit_basset_griffon_vendeen": "dog",
    "pharaoh_hound": "dog",
    "plott": "dog",
    "pointer": "dog",
    "polish_lowland_sheepdog": "dog",
    "pomeranian": "dog",
    "poodle": "dog",
    "porcelaine": "dog",
    "portuguese_podengo": "dog",
    "portuguese_pointer": "dog",
    "portuguese_water_dog": "dog",
    "pug": "dog",
    "puli": "dog",
    "pumi": "dog",
    "pyrenean_mastiff": "dog",
    "pyrenean_shepherd": "dog",
    "rafeiro_do_alentejo": "dog",
    "rat_terrier": "dog",
    "redbone_coonhound": "dog",
    "rhodesian_ridgeback": "dog",
    "rottweiler": "dog",
    "russian_spaniel": "dog",
    "russian_toy": "dog",
    "russian_tsvetnaya_bolonka": "dog",
    "saint_bernard": "dog",
    "saluki": "dog",
    "samoyed": "dog",
    "schapendoes": "dog",
    "schipperke": "dog",
    "scottish_deerhound": "dog",
    "scottish_terrier": "dog",
    "sealyham_terrier": "dog",
    "shetland_sheepdog": "dog",
    "shiba_inu": "dog",
    "shihtzu": "dog",
    "shikoku": "dog",
    "siberian_husky": "dog",
    "silky_terrier": "dog",
    "skye_terrier": "dog",
    "sloughi": "dog",
    "small_munsterlander_pointer": "dog",
    "soft_coated_wheaten_terrier": "dog",
    "spaniel": "dog",
    "spanish_water_dog": "dog",
    "spinone_italiano": "dog",
    "stabyhoun": "dog",
    "staffordshire_bull_terrier": "dog",
    "standard_schnauzer": "dog",
    "sussex_spaniel": "dog",
    "swedish_lapphund": "dog",
    "swedish_vallhund": "dog",
    "taiwan_dog": "dog",
    "teddy_roosevelt_terrier": "dog",
    "thai_ridgeback": "dog",
    "tibetan_mastiff": "dog",
    "tibetan_spaniel": "dog",
    "tibetan_terrier": "dog",
    "tosa": "dog",
    "toy_fox_terrier": "dog",
    "treeing_tennessee_brindle": "dog",
    "treeing_walker_coonhound": "dog",
    "vizsla": "dog",
    "weimaraner": "dog",
    "welsh_springer_spaniel": "dog",
    "welsh_terrier": "dog",
    "west_highland_white_terrier": "dog",
    "whippet": "dog",
    "white_shepherd": "dog",
    "wire_fox_terrier": "dog",
    "wirehaired_pointing_griffon": "dog",
    "wirehaired_vizsla": "dog",
    "working_kelpie": "dog",
    "xoloitzcuintli": "dog",
    "yakutian_laika": "dog",
    "yorkshire_terrier": "dog",
}

cat_breeds = {
    "abyssinian": "cat",
    "american_bobtail": "cat",
    "american_curl": "cat",
    "american_shorthair": "cat",
    "american_wirehair": "cat",
    "balinese": "cat",
    "bengal": "cat",
    "birman": "cat",
    "bombay": "cat",
    "british_longhair": "cat",
    "british_shorthair": "cat",
    "burmese": "cat",
    "burmilla": "cat",
    "chartreux": "cat",
    "chausie": "cat",
    "cornish_rex": "cat",
    "cymric": "cat",
    "devon_rex": "cat",
    "egyptian_mau": "cat",
    "european_burmese": "cat",
    "exotic_shorthair": "cat",
    "havana_brown": "cat",
    "himalayan": "cat",
    "japanese_bobtail": "cat",
    "javanese": "cat",
    "korat": "cat",
    "laperm": "cat",
    "maine_coon": "cat",
    "manx": "cat",
    "munchkin": "cat",
    "nebelung": "cat",
    "norwegian_forest": "cat",
    "ocicat": "cat",
    "oriental": "cat",
    "persian": "cat",
    "pixiebob": "cat",
    "ragamuffin": "cat",
    "ragdoll": "cat",
    "russian_blue": "cat",
    "savannah": "cat",
    "scottish_fold": "cat",
    "selkirk_rex": "cat",
    "siamese": "cat",
    "siberian": "cat",
    "singapura": "cat",
    "snowshoe": "cat",
    "somali": "cat",
    "sphynx": "cat",
    "tonkinese": "cat",
    "toyger": "cat",
    "turkish_angora": "cat",
    "turkish_van": "cat",
    "tabby":"cat"
}
D="dog"
C="cat"
# Load the VGG16 model
model = VGG16(weights='imagenet')
# Define the output directory for each class
output_directories = {
    'dog': 'Dogs',
    'cat': 'Cats'
}

# Function to classify and move images
def classify_and_move_images():
    # Prompt user to select the input directory
    input_directory = filedialog.askdirectory(title='Select Input Directory')
    if not input_directory:
        return
    
    # Create output directories if they don't exist
    for directory in output_directories.values():
        if not os.path.exists(directory):
            os.makedirs(directory)
    
    # Get a list of input images
    input_images = os.listdir(input_directory)
    final_value="None"
    
    # Process each image
    for image_name in input_images:
        image_path = os.path.join(input_directory, image_name)
        
        # Load and preprocess the image
        img = Image.open(image_path)
        img = img.resize((224, 224))  # Resize the image to match VGG16 input size
        x = np.expand_dims(img, axis=0)
        x = preprocess_input(x)
        
        # Classify the image
        preds = model.predict(x)
        decoded_preds = decode_predictions(preds, top=1)[0]
        class_name = decoded_preds[0][1]
        if (any(class_name.lower() in key.lower() for key in dog_breeds) or (D in class_name)):
            final_value = "dog"
        if (any(class_name.lower() in key.lower() for key in cat_breeds) or (C in class_name)):
            print("atleast here")
            final_value = "cat"
        # Move the image to the corresponding output directory
        if final_value in output_directories:
            output_directory = output_directories[final_value]
            shutil.move(image_path, output_directory)
            print(f"Image '{image_name}' classified as '{final_value}' and moved to '{output_directory}'")
        else:
            print(f"Image '{image_name}' does not belong to a valid category rather than '{class_name}")
    
    # Display a message box indicating the completion
    messagebox.showinfo("Image Classification", "Image classification completed!")

# Create the GUI
root = tk.Tk()
root.title("Image Classification")
root.geometry("300x100")

# Create a button to trigger the image classification process
classify_button = tk.Button(root, text="Classify Images", command=classify_and_move_images)
classify_button.pack(pady=20)

# Start the GUI event loop
root.mainloop()
