import time
from BeatsInfo import notes
from BeatsInfo import beat_maps
import random
import musicalbeeps

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
            _index = random.randint(0, len(indices)-1)
            index = indices[_index]
        else:
            pass

        # process for current indexed int
        newMelody.append(melody[index])
        newTempo.append((tempo[index]))

        index = (index + 1) % BeatLength

    return newMelody, newTempo


# def playSong(songname:str):
# 	print("play "+songname)
# 	newMelody,newTempo=BeatMapRepermute(beat_maps[songname][0], beat_maps[songname][1])
# 	play(newMelody,newTempo,
# 		 beat_maps[songname][2], beat_maps[songname][3])

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


playSongToHDMI("Super Mario Theme")
