import cv2

cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	face_cascade = cv2.CascadeClassifier("haarcascades\haarcascade_frontalface_alt.xml.xml")
	
	faces = face_cascade.detectMultiScale(gray, 1.1, 2)
	
	for (x,y,w,h) in faces:
		cv2.rectangle(frame,(x,y),(w+h,y+h),(0,255,255),2)

	
	cv2.imshow("webcam feed", frame)
	if cv2.waitKey(1) and 0xFF == ord(" "):
		break

cap.release()
cv2.destroyAllWindows()
