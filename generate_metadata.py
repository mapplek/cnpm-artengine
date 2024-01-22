from natsort import natsorted

import json
import os

MAX_SUPPLY = 10000

ANIMATIONS_PATH = "./Output/main/sounds/"

JSON_PATH_OPEN = "./Output/prod/json/open/"
IMAGES_PATH_OPEN = "./Output/main/images/open/"

JSON_PATH_CLOSE = "./Output/prod/json/close/"
IMAGES_PATH_CLOSE = "./Output/main/images/close/"

AWS_IMAGE_URL_OPEN = "https://gene.cnp-music.jp/images/0/open/"
AWS_IMAGE_URL_CLOSE = "https://gene.cnp-music.jp/images/0/close/"

AWS_ANIMATION_URL = "https://gene.cnp-music.jp/animations/0/"

images = os.listdir(IMAGES_PATH_OPEN)
images = natsorted(images)

sounds = os.listdir(ANIMATIONS_PATH)
sounds = natsorted(sounds)

character_names = {
    "Leelee": "リーリー",
    "Narukami": "ナルカミ",
    "Mitama": "ミタマ",
    "Orochi": "オロチ",
    "Luna": "ルナ",
    "Yama": "ヤーマ",
    "Makami": "マカミ"
}

for num_nft in range(MAX_SUPPLY):
    ###
    # Prepare for character name
    ###
    image_layer_items = images[num_nft].split('-')
    sound_layer_items = sounds[num_nft].split('-')

    body_name = image_layer_items[1]

    if image_layer_items[3] != 'None':
        body_name = body_name + '-' + image_layer_items[3]
    

    ###
    # Prepare description
    ###
    description = image_layer_items[1] + " who is " + sound_layer_items[2] + " player struggle to restore the value of music also today!  \n" + \
        sound_layer_items[2] + " playerの" + character_names[image_layer_items[1]] + "は、今日も音楽の価値を取り戻すため、演奏に奮闘しています！"


    ###
    # Generate metadata
    ###
    metadata_open = {
        "name": body_name + " #" + str(num_nft + 1).zfill(5),
        "description": description,
        "image": AWS_IMAGE_URL_OPEN + str(num_nft + 1) + ".png",
        "animation_url": AWS_ANIMATION_URL + str(num_nft + 1) + ".wav",
        "edition": (num_nft + 1),
        "attributes": [
            {
                "trait_type": "Character",
                "value": image_layer_items[1]
            },
            {
                "trait_type": "Body",
                "value": image_layer_items[3]
            },
            {
                "trait_type": "Cosplay",
                "value": image_layer_items[4]
            },
            {
                "trait_type": "Background",
                "value": image_layer_items[2]
            },
            {
                "trait_type": "Instrument",
                "value": sound_layer_items[2]
            },
            {
                "trait_type": "Backing",
                "value": sound_layer_items[3]
            },
            {
                "trait_type": "Rhythm",
                "value": sound_layer_items[4].split('.')[0]
            }
        ]
    }

    metadata_close = {
        "name": body_name + "(closed) #" + str(num_nft + 1).zfill(5),
        "description": description,
        "image": AWS_IMAGE_URL_CLOSE + str(num_nft + 1) + ".png",
        "edition": (num_nft + 1),
        "attributes": [
            {
                "trait_type": "Character",
                "value": image_layer_items[1]
            },
            {
                "trait_type": "Body",
                "value": image_layer_items[3]
            },
            {
                "trait_type": "Cosplay",
                "value": image_layer_items[4]
            },
            {
                "trait_type": "Background",
                "value": image_layer_items[2]
            },
            {
                "trait_type": "Instrument",
                "value": sound_layer_items[2]
            },
            {
                "trait_type": "Backing",
                "value": sound_layer_items[3]
            },
            {
                "trait_type": "Rhythm",
                "value": sound_layer_items[4].split('.')[0]
            }
        ]
    }


    ###
    # Write metadata as json file
    ###
    with open(JSON_PATH_OPEN + str(num_nft + 1) + '.json', 'w') as f:
        json.dump(metadata_open, f, indent=2, ensure_ascii=False)

    with open(JSON_PATH_CLOSE + str(num_nft + 1) + '.json', 'w') as f:
        json.dump(metadata_close, f, indent=2, ensure_ascii=False)