from imutils.video import VideoStream
import argparse
import time
import cv2
import threading
from barcode_scanner_video import StartBarcodeScan

CurrentCode = [""]	# TODO: to be improved
					# TODO:add mutex for code that modify it
CurrentCode_mutex=threading.Lock()

def PrepareForCodeScan():
	ap = argparse.ArgumentParser()
	ap.add_argument("-o", "--output", type=str, #default="./barcode_data/barcodes.csv",
		help="path to output CSV file containing barcodes")
	ap.add_argument("-c", "--camera", type=str, default="pc",
		help="choose")
	args = vars(ap.parse_args())
	if args["output"]:
		pass
	print("[INFO] 启动摄像头...")
	#select camera
	if(args["camera"]=="pc"):
		vs = VideoStream(src=0).start()	#running on pc
	elif(args["camera"]=="ras"):
		vs = VideoStream(usePiCamera=True).start() #running on raspi
	else:
		print("camera parameter is wrong")
		exit(1)
	time.sleep(2.0)
	print("摄像头开启")
	#prevent one code to be add to found list multipletimes in short time
	BarcodeScanThread = threading.Thread(target=StartBarcodeScan, args=(CurrentCode,CurrentCode_mutex, vs,))
	return BarcodeScanThread,vs

BarcodeScanThread,vs=PrepareForCodeScan()
BarcodeScanThread.start()


SwichControl=True
CodeProcessed=""
while(True):
	CurrentCode_mutex.acquire()
	try:
		if(SwichControl and CurrentCode[0]!=CodeProcessed):
			CodeProcessed=CurrentCode[0]
			print(CodeProcessed)
	finally:
		CurrentCode_mutex.release()


BarcodeScanThread.join()
# close the output CSV file do a bit of cleanup
print("[INFO] 结束opencv进程")
# csv.close()
cv2.destroyAllWindows()
vs.stop()