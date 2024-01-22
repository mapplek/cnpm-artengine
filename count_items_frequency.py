import collections
import csv
import glob
import os
import pprint

ROOT_PARTS = "./CNPMGenerativeIllusts/"
ROOT_OUTPUT = "./Output/"

LAYERS = sorted(os.listdir(path=ROOT_PARTS+'close/'))
GENE_ART = os.listdir(path=ROOT_OUTPUT+'main/images/close/')
# GENE_ART = os.listdir(path=ROOT_OUTPUT+"sub/images/close/")

CHARACTER_NAME = [
    "Leelee", "Narukami", "Mitama", "Orochi", 
    "Luna", "Yama", "Makami"
]

###
# Collect parts each layer in material
##
'''
parts_each_layer_material
  [0] -> Character + Body
  [1] -> Character + Cosplay
  [2] -> Character + Instrument
  [3] -> Background
'''
parts_each_layer_material = [[],[],[],[]]

for layer in LAYERS:
    if layer == LAYERS[1]:
        for file in glob.glob(ROOT_PARTS + 'close/' + layer + '/*.png', recursive=True):
            parts_each_layer_material[3].append(os.path.basename(file).split('#')[0])
    if layer == LAYERS[2]:
        for file in glob.glob(ROOT_PARTS + 'close/' + layer + '/*/*.png', recursive=True):
            parts_each_layer_material[0].append(file.split('/')[-2] + os.path.basename(file).split('#')[0])
    if layer == LAYERS[3]:
        for file in glob.glob(ROOT_PARTS + 'close/' + layer + '/*/*.png', recursive=True):
            parts_each_layer_material[1].append(file.split('/')[-2] + os.path.basename(file).split('#')[0])
    if layer == LAYERS[4]:
        for file in glob.glob(ROOT_PARTS + 'close/' + layer + '/*.png', recursive=True):
            for character in CHARACTER_NAME:
                parts_each_layer_material[2].append(character + os.path.basename(file).split('.')[0])


###
# Collect parts each layer in output arts
###
'''
parts_each_layer_output_arts
  [0] -> Character + Body
  [1] -> Character + Cosplay
  [2] -> Character + Instrument
  [3] -> Background
'''
parts_each_layer_output_arts = [[],[],[],[]]

for art in GENE_ART:
    parts = art.split('-')
    parts_each_layer_output_arts[0].append(parts[1] + parts[3])
    parts_each_layer_output_arts[1].append(parts[1] + parts[4])
    parts_each_layer_output_arts[2].append(parts[1] + parts[5].split('.')[0])
    parts_each_layer_output_arts[3].append(parts[2])


###
# Count frequency parts each layer
###
table_frequency_items = []

for layer in LAYERS:
    if layer == LAYERS[1]:
        array_freq = collections.Counter(parts_each_layer_output_arts[3])

        for item in parts_each_layer_material[3]:
            table_frequency_items.append([layer, item, array_freq[item]])
    
    if layer == LAYERS[2]:
        array_freq = collections.Counter(parts_each_layer_output_arts[0])

        for item in parts_each_layer_material[0]:
            table_frequency_items.append([layer, item, array_freq[item]])
    
    if layer == LAYERS[3]:
        array_freq = collections.Counter(parts_each_layer_output_arts[1])

        for item in parts_each_layer_material[1]:
            table_frequency_items.append([layer, item, array_freq[item]])
    
    if layer == LAYERS[4]:
        array_freq = collections.Counter(parts_each_layer_output_arts[2])

        for item in parts_each_layer_material[2]:
            table_frequency_items.append([layer, item, array_freq[item]])

pprint.pprint(table_frequency_items)

with open('count_items_frequency_main.csv', 'w') as file:
    writer = csv.writer(file, lineterminator='\n')
    writer.writerows(table_frequency_items)