from imutils.video import VideoStream
from pyzbar import pyzbar
import imutils
import time
import cv2


def barScan():
	print(" Starting video streaming...")
	vs = VideoStream(src=0).start()
	time.sleep(2.0)


	save = open("qrcode.csv","w")
	found = set()

	while True:
		frame = vs.read()
		frame = imutils.resize(frame, width=400)
		qrs = pyzbar.decode(frame)

		for qr in qrs:

			(x,y,w,h) = qr.rect
			cv2.rectangle(frame, (x,y), (x+w,y+h),(0,0,255), 2)

			qrData = qr.data.decode("utf-8")
			qrType = qr.type

			text = "{} ({})".format(qrData, qrType)
			cv2.putText(frame, text, (x,y-10),
				cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)
			print(text)
			save.close()
			cv2.destroyAllWindows()
			vs.stop()

			return text;
			if qrData not in found:
				save.write("{}\n".format(qrData))
				save.flush()
				found.add(qrData)


		cv2.imshow("QRCode Scanner", frame)
		key = cv2.waitKey(1) & 0xFF
		if key == ord("q"):
			break

	print(" \n flushing....")

	save.close()
	cv2.destroyAllWindows()
	vs.stop()


#barScan()
