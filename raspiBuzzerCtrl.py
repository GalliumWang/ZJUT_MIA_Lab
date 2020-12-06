#---------------------------------------------------
#		Passive buzzer 			   Pi 
#			VCC ----------------- 3.3V
#			GND ------------------ GND
#			SIG ---------------- Pin Gpio27
#
#		some notes for melodies were taken from:
#		http://www.astlessons.com/pianoforkids1.html
#		http://www.astlessons.com/pianoforkids2.html
#---------------------------------------------------
import RPi.GPIO as GPIO
import time
from BeatsInfo import notes
from BeatsInfo import beat_maps

buzzer_pin = 27

def buzz(frequency, length):	 #create the function "buzz" and feed it the pitch and duration)

	if(frequency==0):
		time.sleep(length)
		return
	period = 1.0 / frequency 		 #in physics, the period (sec/cyc) is the inverse of the frequency (cyc/sec)
	delayValue = period / 2		 #calcuate the time for half of the wave
	numCycles = int(length * frequency)	 #the number of waves to produce is the duration times the frequency
	
	for i in range(numCycles):		#start a loop from 0 to the variable "cycles" calculated above
		GPIO.output(buzzer_pin, True)	 #set pin 27 to high
		time.sleep(delayValue)		#wait with pin 27 high
		GPIO.output(buzzer_pin, False)		#set pin 27 to low
		time.sleep(delayValue)		#wait with pin 27 low

def setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(buzzer_pin, GPIO.IN)
	GPIO.setup(buzzer_pin, GPIO.OUT)
	
def destroy():
	GPIO.cleanup()				# Release resource
	

def play(melody,tempo,pause,pace=0.800):
	
	for i in range(0, len(melody)):		# Play song
		
		noteDuration = pace/tempo[i]
		buzz(melody[i],noteDuration)	# Change the frequency along the song note
		
		pauseBetweenNotes = noteDuration * pause
		time.sleep(pauseBetweenNotes)
	
	

def StartControlBuzzer(CurrentCode:list)
	try:
		setup()


		print "Super Mario Theme"
		play(beat_maps["Super Mario Theme"][0], beat_maps["Super Mario Theme"][1],
			 beat_maps["Super Mario Theme"][2], beat_maps["Super Mario Theme"][3])

		time.sleep(2)

		print "Super Mario Underworld Theme"
		play(beat_maps["Super Mario Underworld Theme"][0], beat_maps["Super Mario Underworld Theme"][1],
			 beat_maps["Super Mario Underworld Theme"][2], beat_maps["Super Mario Underworld Theme"][3])
		
		destroy()

	except KeyboardInterrupt:  	# When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()