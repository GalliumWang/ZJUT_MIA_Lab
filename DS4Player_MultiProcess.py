import musicalbeeps
import pygame
import signal
import subprocess
import os

noteConverter = {"do": "C", "re": "D", "mi": "E", "fa": "F", "so": "G", "la": "A", "si": "B"}
used_button=[4,5,6,7,1,2,3]
button_to_note_dict={4:"do",5:"re",6:"mi",7:"fa",3:"so",2:"la",1:"si"}

play_thread_pool={4:None,5:None,6:None,7:None,3:None,2:None,1:None}

currentScale = 4
playSwitch = True

def process_down_event(button_num:int):
    global noteConverter
    global used_button
    global button_to_note_dict
    global currentScale

    global play_thread_pool

    if play_thread_pool[button_num]:
        return
    
    note=button_to_note_dict[button_num]
    trueNote=noteConverter[note]
    scale = str(currentScale)
    playLoads = trueNote + scale

    play_thread_pool[button_num]=subprocess.Popen(["python3",
                                                 "singleNotePlay.py",
                                                 playLoads], 
                                                 shell=False,
                                                 preexec_fn=os.setsid)

def process_up_event(button_num:int):
    global noteConverter
    global used_button
    global button_to_note_dict
    global currentScale

    global play_thread_pool

    if not play_thread_pool[button_num]:
        return
    
    os.killpg(os.getpgid(play_thread_pool[button_num].pid), signal.SIGTERM)
    play_thread_pool[button_num]=None


#main prog

pygame.init()
j = pygame.joystick.Joystick(0)
j.init()


try:
    while True:
        if playSwitch:
            events = pygame.event.get()
            for _ in events:
                for button_num in used_button:
                    if j.get_button(button_num):
                        process_down_event(button_num)
                    else:
                        process_up_event(button_num)

                if j.get_button(8):
                    if currentScale > 1:
                        currentScale -= 1
                        print("音阶下降:{}".format(currentScale))
                    else:
                        print("已经到达最低音阶")
                if j.get_button(9):
                    if currentScale < 8:
                        currentScale += 1
                        print("音阶上升:{}".format(currentScale))
                    else:
                        print("已经到达最高音阶")
                if j.get_button(10):
                    playSwitch = False
                    print("停止演奏")


        else:   # open intr
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.JOYBUTTONDOWN:  
                    if j.get_button(10):
                        playSwitch = True
                        print("开始演奏")


except KeyboardInterrupt:  # handle for ctrl+C
    # kill all playing thread
    for key in button_to_note_dict:
        if button_to_note_dict[key]:
            os.killpg(os.getpgid(button_to_note_dict[key].pid), signal.SIGTERM)
    print("用户结束程序")
    j.quit()