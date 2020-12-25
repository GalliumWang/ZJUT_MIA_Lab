import musicalbeeps
import pygame
import signal
import subprocess
import os

pro = None


# pro = subprocess.Popen(cmd, stdout=subprocess.PIPE,
#                        shell=True, preexec_fn=os.setsid)

# os.killpg(os.getpgid(pro.pid), signal.SIGTERM)  # Send the signal to all the process groups


def note_play(note: str, scale: int = 4):
    global pro

    if pro is not None:
        os.killpg(os.getpgid(pro.pid), signal.SIGTERM)  # kill previous pro
        pro = None

    noteConverter = {"do": "C", "re": "D", "mi": "E", "fa": "F", "so": "G", "la": "A", "si": "B"}

    trueNote = noteConverter[note]
    scale = str(scale)
    playLoads = trueNote + scale

    pro = subprocess.Popen(["python3", "singleNotePlay.py", playLoads], shell=False,
                           preexec_fn=os.setsid)


def stopNotePlay():
    global pro
    if pro is not None:
        os.killpg(os.getpgid(pro.pid), signal.SIGTERM)  # kill previous pro
        pro = None


pygame.init()
j = pygame.joystick.Joystick(0)
j.init()

currentScale = 4

playSwitch = True

try:
    while True:
        if playSwitch:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.JOYBUTTONDOWN:
                    if j.get_button(4):
                        note_play("do", currentScale)
                    elif j.get_button(5):
                        note_play("re", currentScale)
                    elif j.get_button(6):
                        note_play("mi", currentScale)
                    elif j.get_button(7):
                        note_play("fa", currentScale)
                    elif j.get_button(1):
                        note_play("si", currentScale)
                    elif j.get_button(2):
                        note_play("la", currentScale)
                    elif j.get_button(3):
                        note_play("so", currentScale)
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
                        playSwitch = False
                        print("停止演奏")

                elif event.type == pygame.JOYBUTTONUP:
                    stopNotePlay()
        else:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.JOYBUTTONDOWN:
                    if j.get_button(10):
                        playSwitch = True
                        print("开始演奏")


except KeyboardInterrupt:  # handle for ctrl+C
    print("用户结束程序")
    j.quit()
