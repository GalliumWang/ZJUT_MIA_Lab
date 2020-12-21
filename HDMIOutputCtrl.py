import time
from BeatsInfo import notes
from BeatsInfo import beat_maps
import random
import musicalbeeps  # for music output

from imutils.video import VideoStream
from barcode_scanner_video import StartBarcodeScan
import argparse
import cv2
import threading  # for qrcode scan

player = musicalbeeps.Player(volume=0.3, mute_output=False)
markov = True


def play(melody, tempo, pause, pace=0.800):
    for i in range(0, len(melody)):  # Play song

        noteDuration = pace / tempo[i]
        buzz(melody[i], noteDuration)  # Change the frequency along the song note

        pauseBetweenNotes = noteDuration * pause
        time.sleep(pauseBetweenNotes)


def BeatMapRepermute(melody: list, tempo: list) -> tuple:
    # para Error
    # if len(list) != len(tempo):
    #     raise RuntimeError

    newMelody = []
    newTempo = []

    BeatLength = len(melody)

    index = 0
    for _ in range(BeatLength):
        CaseInt = random.randint(1, 10)
        if (CaseInt == 10):
            # jump to same symbol
            currentNote = melody[index]
            indices = [i for i, x in enumerate(melody) if x == currentNote]
            _index = random.randint(0, len(indices) - 1)
            index = indices[_index]
        else:
            pass

        # process for current indexed int
        newMelody.append(melody[index])
        newTempo.append((tempo[index]))

        index = (index + 1) % BeatLength

    return newMelody, newTempo


def playSong(melody: list, tempo: list, pace=0.015, rate=0.015):
    if markov:
        melody, tempo = BeatMapRepermute(melody, tempo)
    else:
        pass
    for i in range(len(melody)):
        player.play_note(melody[i], tempo[i] * rate)
        player.play_note("pause", pace)


def playSongToHDMI(songName):
    melody = beat_maps[songName][0]
    tempo = beat_maps[songName][1]
    playSong(melody, tempo)


CurrentCode = [""]  # TODO: to be improved
# TODO:add mutex for code that modify it
CurrentCode_mutex = threading.Lock()


def PrepareForCodeScan():
    ap = argparse.ArgumentParser()
    ap.add_argument("-o", "--output", type=str,  # default="./barcode_data/barcodes.csv",
                    help="path to output CSV file containing barcodes")
    ap.add_argument("-c", "--camera", type=str, default="pc",
                    help="choose")
    args = vars(ap.parse_args())
    if args["output"]:
        pass
    print("[INFO] 启动摄像头...")
    # select camera
    if (args["camera"] == "pc"):
        vs = VideoStream(src=0).start()  # running on pc
    elif (args["camera"] == "ras"):
        vs = VideoStream(usePiCamera=True).start()  # running on raspi
    else:
        print("camera parameter is wrong")
        exit(1)
    time.sleep(2.0)
    print("摄像头开启")
    # prevent one code to be add to found list multipletimes in short time
    BarcodeScanThread = threading.Thread(target=StartBarcodeScan, args=(CurrentCode, CurrentCode_mutex, vs,))
    return BarcodeScanThread, vs

BarcodeScanThread, vs = PrepareForCodeScan()
BarcodeScanThread.start()
