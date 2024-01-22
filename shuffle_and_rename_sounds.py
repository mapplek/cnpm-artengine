import os
import pprint
import random
import shutil

PATH_BEFORE_SHUFFLE = "./Output/main/sounds/before_shuffle/"
PATH_AFTER_SHUFFLE = "./Output/main/sounds/after_shuffle/"

CHARACTER_NAME = [
    "Leelee", "Narukami", "Orochi", "Mitama",
    "Luna", "Yama", "Makami"
]

shuffle_list = os.listdir(path=PATH_BEFORE_SHUFFLE)
random.shuffle(shuffle_list)

idx = 0

for sound in shuffle_list:
    idx += 1

    for character in CHARACTER_NAME:
        if character in sound:
            instrument = sound.split('-')[0].split(character)[1]
            sound_file_name = sound.replace(sound.split('-')[0], str(idx) + '-' + character + '-' + instrument)
            shutil.move(PATH_BEFORE_SHUFFLE + sound, PATH_AFTER_SHUFFLE + sound_file_name)
