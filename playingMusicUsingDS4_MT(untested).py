import musicalbeeps
import pygame
import threading

player = musicalbeeps.Player(volume=0.3, mute_output=False)


def note_play(note: str, scale: int = 4, duration: float = 10, player=player):
    noteConverter = {"do": "C", "re": "D", "mi": "E", "fa": "F", "so": "G", "la": "A", "si": "B"}

    trueNote = noteConverter[note]
    scale = str(scale)
    playLoads = trueNote + scale

    player.play_note(playLoads, duration)


# init
pygame.init()
j = pygame.joystick.Joystick(0)
j.init()

currentNote = None
playingThread = None
currentScale = 4
playSwitch = True


def bgPlay():
    while True:
        if (currentNote == None):
            continue
        note_play(currentNote, currentScale)


playingThread = threading.Thread(target=bgPlay)
playingThread.start()

try:
    while True:
        if (playSwitch):
            for event in pygame.event.get():
                if event.type == pygame.JOYBUTTONDOWN:
                    if j.get_button(4):
                        currentNote = "do"
                    elif j.get_button(5):
                        currentNote = "re"
                    elif j.get_button(6):
                        currentNote = "mi"
                    elif j.get_button(7):
                        currentNote = "fa"
                    elif j.get_button(3):
                        currentNote = "so"
                    elif j.get_button(2):
                        currentNote = "la"
                    elif j.get_button(1):
                        currentNote = "si"
                    elif j.get_button(8):
                        if currentScale > 1:
                            currentScale -= 1
                            print("音阶下降:{}".format(currentScale))
                        else:
                            print("已经到达最低音阶")
                    elif j.get_button(9):
                        if currentScale < 8:
                            currentScale += 1
                            print("音阶上升:{}".format(currentScale))
                        else:
                            print("已经到达最高音阶")
                    elif j.get_button(10):
                        # print("POWER BUTTON")
                        playSwitch = False
                        currentNote = None  # 暂停后台播放线程
                        print("停止演奏")

                elif event.type == pygame.JOYBUTTONUP:
                    # FIXME
                    # figure out code of corresponding get_button method
                    currentNote=None

        else:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.JOYBUTTONDOWN:
                    if j.get_button(10):
                        playSwitch = True
                        print("开始演奏")  #


except KeyboardInterrupt:  # handle for ctrl+C
    print("用户结束程序")
    j.quit()
