import cv2

face_cascade = cv2.CascadeClassifier('face-checker/cascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('face-checker/cascades/haarcascade_eye_tree_eyeglasses.xml')
nose_cascade = cv2.CascadeClassifier("face-checker/cascades/haarcascade_mcs_nose.xml")
mouth_cascade = cv2.CascadeClassifier("face-checker/cascades/haarcascade_mcs_mouth.xml")

cap = cv2.VideoCapture(0)

while 1:
	ret, img = cap.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in faces:
		h = int(h + 0.1*h)
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = img[y:y+h, x:x+w]

		eyes = eye_cascade.detectMultiScale(roi_gray)
		for (ex,ey,ew,eh) in eyes:
			cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2)
		nose = nose_cascade.detectMultiScale(roi_gray, 1.3, 5)
		for (nx,ny,nw,nh) in nose:
			nw = int(nw - 0.25*nw)
			nx = int(nx + 0.2*nw)
			ny = int(ny - 0.4*nh)
			nh = int(nh + 0.15*nh)
			cv2.rectangle(roi_color, (nx, ny), (nx+nw,ny+nh), (0,255,255), 2)
		mouth = mouth_cascade.detectMultiScale(roi_gray, 1.7, 8)
		for (mx,my,mw,mh) in mouth:
			my = int(my + 0.15*mh)
			mh = int(mh - 0.25*mh)
			cv2.rectangle(roi_color, (mx,my), (mx+mw,my+mh), (0,0,255), 2)

	cv2.imshow('Result:',img)

	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break

cap.release()
cv2.destroyAllWindows()