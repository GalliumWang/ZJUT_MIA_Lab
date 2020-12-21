import musicalbeeps
import pygame


player = musicalbeeps.Player(volume = 0.3,mute_output = False)

def note_play(note:str,scale:int=4,duration:float=0.2,player=player):
    noteConverter = {"do": "C", "re": "D", "mi": "E", "fa": "F", "so": "G", "la": "A", "si":"B"}

    trueNote=noteConverter[note]
    scale=str(scale)
    playLoads=trueNote+scale

    player.play_note(playLoads, duration)



pygame.init()
j = pygame.joystick.Joystick(0)
j.init()

currentScale=4

playSwitch=True

try:
    while True:
        if(playSwitch):
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.JOYBUTTONDOWN:
                    if j.get_button(4):
                        #print("L1")
                        note_play("do",currentScale)
                    elif j.get_button(5):
                        #print("R1")
                        note_play("re", currentScale)
                    elif j.get_button(6):
                        #print("L2")
                        note_play("mi", currentScale)
                    elif j.get_button(7):
                        #print("R2")
                        note_play("fa", currentScale)
                    elif j.get_button(0):
                        #print("X")
                        pass
                    elif j.get_button(1):
                        #print("CIRCLE")
                        note_play("si", currentScale)
                    elif j.get_button(2):
                        #print("TRIANGLE")
                        note_play("la", currentScale)
                    elif j.get_button(3):
                        #print("SQUARE")
                        note_play("so", currentScale)
                    elif j.get_button(8):
                        #print("SHARE")
                        if(currentScale>1):
                            currentScale-=1
                            print("音阶下降:{}".format(currentScale))
                        else:
                            print("已经到达最低音阶")
                    elif j.get_button(9):
                        #print("OPTION")
                        if(currentScale<8):
                            currentScale+=1
                            print("音阶上升:{}".format(currentScale))
                        else:
                            print("已经到达最高音阶")
                    elif j.get_button(10):
                        #print("POWER BUTTON")
                        playSwitch=False
                        print("停止演奏")

                    # elif j.get_button(11):
                    #     print("RIGHT ANALOG PRESS")   #FIXME:what button is applied to num 11

                    # elif j.get_button(12):
                    #     #print("RIGHT STICK PRESS")
                    #     if(currentScale<8):
                    #         currentScale+=1
                    #         print("音阶上升")
                    #     else:
                    #         print("已经到达最高音阶")
                    # elif j.get_button(13):
                    #     #print("LEFT STICK PRESS")
                    #     if(currentScale>1):
                    #         currentScale-=1
                    #         print("音阶下降")
                    #     else:
                    #         print("已经到达最低音阶")     #FIXME:fix crash for button apllied to num 13

                elif event.type == pygame.JOYBUTTONUP:
                    # print("TOUCHPAD PRESS")
                    pass
        else:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.JOYBUTTONDOWN:
                    if j.get_button(10):
                        playSwitch=True
                        print("开始演奏")


except KeyboardInterrupt:   #handle for ctrl+C
    print("用户结束程序")
    j.quit()