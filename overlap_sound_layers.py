from pydub import AudioSegment
import os
import pprint

EXTENSION = "wav"

ROOT_PATH = "./CNPMGenerativeSounds/"
OUTPUT_PATH = "./Output/main/sounds/before_shuffle/"
LAYERS = sorted(os.listdir(path=ROOT_PATH))

track_data = []

for layer in LAYERS:
    track_data.append(os.listdir(path=ROOT_PATH+layer+'/'))

for melody in track_data[0]:
    if EXTENSION not in melody:
        continue
    melody_file = AudioSegment.from_file(ROOT_PATH + LAYERS[0] + '/' + melody, EXTENSION)

    for backing in track_data[1]:
        if EXTENSION not in backing:
            continue
        backing_file = AudioSegment.from_file(ROOT_PATH + LAYERS[1] + '/' + backing, EXTENSION)

        for rhythm in track_data[2]:
            if EXTENSION not in rhythm:
                continue
            rhythm_file = AudioSegment.from_file(ROOT_PATH + LAYERS[2] + '/' + rhythm, EXTENSION)

            combined_track = rhythm_file.overlay(backing_file, 0).overlay(melody_file, 0)
            combined_track_name = \
                OUTPUT_PATH + melody.split('.')[0] + '-' + backing.split('.')[0] + '-' + rhythm.split('.')[0] + '.' + EXTENSION

            combined_track.export(combined_track_name, format=EXTENSION)
            print('generated: ' + combined_track_name)