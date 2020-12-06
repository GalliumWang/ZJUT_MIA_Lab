from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse
import datetime
import imutils
import time
import cv2
import threading


#also used as for module part
def StartBarcodeScan(BarcodeSet,vs):
	# loop over the frames from the video stream
	while True:
		# grab the frame from the threaded video stream and resize it to
		# have a maximum width of 400 pixels
		frame = vs.read()
		frame = imutils.resize(frame, width=400)
		# find the barcodes in the frame and decode each of the barcodes
		barcodes = pyzbar.decode(frame)	# loop over the detected barcodes

		AcceptedBarcodeType=["QRCODE"]

		for barcode in barcodes:
			# extract the bounding box location of the barcode and draw
			# the bounding box surrounding the barcode on the image
			(x, y, w, h) = barcode.rect
			cv2.rectangle(frame, (x, y), (x + w, y + h), (130, 38, 166), 4)

			# the barcode data is a bytes object so if we want to draw it
			# on our output image we need to convert it to a string first
			barcodeData = barcode.data.decode("utf-8")
			barcodeType = barcode.type

			# draw the barcode data and barcode type on the image
			# text = "{} ({})".format(barcodeData, barcodeType)
			cv2.putText(frame, barcodeData, (x, y - 10),
				cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

			# if the barcode text is currently not in our CSV file, write
			# the timestamp + barcode to disk and update the set
			if (barcodeData not in found):#and (barcodeType in AcceptedBarcodeType):
				found.add(barcodeData)
				print("新增一个二维码")

		# show the output frame
		cv2.imshow("Code Scanner", frame)
		key = cv2.waitKey(1) & 0xFF

		# if the `q` key was pressed, break from the loop
		if key == ord("q"):
			break


# 设置启动参数
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


