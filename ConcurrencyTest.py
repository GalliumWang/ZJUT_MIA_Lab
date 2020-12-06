from imutils.video import VideoStream
import argparse
import time
import cv2
import threading
from barcode_scanner_video import StartBarcodeScan

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
found = set()

BarcodeScanThread = threading.Thread(target=StartBarcodeScan, args=(found,vs,))
BarcodeScanThread.start()
BarcodeScanThread.join()


# close the output CSV file do a bit of cleanup
print("[INFO] 结束opencv进程")

# csv.close()
cv2.destroyAllWindows()
vs.stop()