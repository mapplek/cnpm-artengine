from natsort import natsorted
from PIL import Image
import glob
import os
import pprint
import random
import sys

CHARACTER_NAME = [
    "Leelee", "Narukami", "Orochi", "Mitama",
    "Luna", "Yama", "Makami"
]

ALLOWED_REDO_BY_DUPLICATION = 10

ROOT_PATH = "./CNPMGenerativeIllusts/"

OUTPUT_PATH_MAIN = "./Output/main/images/"
OUTPUT_PATH_SUB = "./Output/sub/images/"

OPEN_PATH = "open/"
CLOSE_PATH = "close/"

OUTPUT_PATH_SOUND = "./Output/main/sounds/after_shuffle/"

EXTENTION = ".png"

output_sounds = natsorted(os.listdir(path=OUTPUT_PATH_SOUND))
OPEN_LAYERS = sorted(os.listdir(path=ROOT_PATH+OPEN_PATH))
CLOSE_LAYERS = sorted(os.listdir(path=ROOT_PATH+CLOSE_PATH))
generated_dna = []

# SOUNDS_NUM = len(output_sounds)
SOUNDS_NUM = 10000

for num_nft in range(SOUNDS_NUM * 2):
# for num_nft in range(SOUNDS_NUM):
    iteration_count = 0

    while True:
        selected_items = []
        close_items_path = []

        for layer in OPEN_LAYERS:
            idx_selected_item = 0
            items = []

            ###
            # Select item from Record layer
            ###
            if layer == OPEN_LAYERS[0]:
                items = os.listdir(path=ROOT_PATH+OPEN_PATH+layer+'/')

                for item in items:
                    if item.split('.')[0] in output_sounds[num_nft % SOUNDS_NUM]:
                        selected_items.append(
                            [
                                ROOT_PATH + OPEN_PATH + layer + '/' + item,
                                item.split('.')[0]
                            ]
                        )

                        close_items_path.append(ROOT_PATH + CLOSE_PATH + layer + '/' + item)

            ###
            # Select item from Background/Body/Cosplay layer
            ###
            elif (layer == OPEN_LAYERS[1]) or (layer == OPEN_LAYERS[2]) or (layer == OPEN_LAYERS[3]):
                character_dir = ''
                if (layer == OPEN_LAYERS[2]) or (layer == OPEN_LAYERS[3]):
                    character_dir = selected_items[0][1] + '/'
                
                items = os.listdir(path=ROOT_PATH+OPEN_PATH+layer+'/'+character_dir)

                weights_items = [int(item.split('#')[-1].split('.')[0]) for item in items]
                total_weight = sum(weights_items)
                rand = random.randint(1, total_weight)

                for idx in range(len(weights_items)):
                    rand -= weights_items[idx]
                    if rand <= 0:
                        idx_selected_item = idx
                        break
                
                selected_items.append(
                    [
                        ROOT_PATH + OPEN_PATH + layer + '/' + character_dir + items[idx_selected_item],
                        items[idx_selected_item].split('#')[0]
                    ]
                )

                close_items_path.append(ROOT_PATH + CLOSE_PATH + layer + '/' + character_dir + items[idx_selected_item])

            ###
            # Select item from Instrument layer
            ###
            else:
                items = os.listdir(path=ROOT_PATH+OPEN_PATH+layer+'/')

                for item in items:
                    if item.split('.')[0] in output_sounds[num_nft % SOUNDS_NUM].split('-')[2]:
                        selected_items.append(
                            [
                                ROOT_PATH + OPEN_PATH + layer + '/' + item,
                                item.split('.')[0]
                            ]
                        )

                        close_items_path.append(ROOT_PATH + CLOSE_PATH + layer + '/' + item)

        
        ###
        # Generate DNA and check duplication
        ###
        element_dna = []
        
        for selected_item in selected_items:
            element_dna.append(selected_item[1])

        if '-'.join(element_dna) in generated_dna:
            iteration_count += 1
            if iteration_count > ALLOWED_REDO_BY_DUPLICATION:
                print('---------------------------------------------------')
                print('Reached ALLOWED_REDO_BY_DUPLICATION.')
                print('Force the application to stop.')
                sys.exit()
            else:
                print('#' + str(num_nft + 1) + ': dna already exists(iteration_count: ' + str(iteration_count) + '/' + str(ALLOWED_REDO_BY_DUPLICATION) + ')')
                continue
        else:
            generated_dna.append('-'.join(element_dna))

            ###
            # Generate an overlapping picture
            ###
            overlapped_picture = Image.new("RGBA", (2048, 2048), (255, 255, 255, 0))
            overlapped_picture_close = Image.new("RGBA", (2048, 2048), (255, 255, 255, 0))

            for selected_item in selected_items:
                tmp_layer = Image.open(selected_item[0])
                overlapped_picture = Image.alpha_composite(overlapped_picture, tmp_layer)
            
            for selected_item in close_items_path:
                tmp_layer = Image.open(selected_item)
                overlapped_picture_close = Image.alpha_composite(overlapped_picture_close, tmp_layer)
            
            if num_nft < SOUNDS_NUM:
                overlapped_picture.save(OUTPUT_PATH_MAIN + OPEN_PATH + str(num_nft + 1) + "-" + "-".join(element_dna) + EXTENTION, format='PNG')
                overlapped_picture_close.save(OUTPUT_PATH_MAIN + CLOSE_PATH + str(num_nft + 1) + "-" + "-".join(element_dna) + EXTENTION, format='PNG')
            else:
                overlapped_picture.save(OUTPUT_PATH_SUB + OPEN_PATH + str(num_nft + 1) + "-" + "-".join(element_dna) + EXTENTION, format='PNG')
                overlapped_picture_close.save(OUTPUT_PATH_SUB + CLOSE_PATH + str(num_nft + 1) + "-" + "-".join(element_dna) + EXTENTION, format='PNG')

            print('#' + str(num_nft + 1) + ': generated ' + '-'.join(element_dna))
        break
