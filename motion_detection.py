import cv2 
cap=cv2.VideoCapture('vtest.mp4')

fourcc=cv2.VideoWriter_fourcc(* 'XVID')

out=cv2.VideoWriter('motion_detection.avi',fourcc,24.0,(768,576))


#cap.set(4,480)
#cap.set(3,120)
_,frame1=cap.read()
_,frame2=cap.read()


print(frame1.shape)
while(cap.isOpened()):

	diff=cv2.absdiff(frame1,frame2)
	gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
	blur=cv2.GaussianBlur(gray,(5,5),0)
	_,thresh=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
	dilated=cv2.dilate(thresh,None,iterations=3)
	contours,hierarchy=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)


	for i in contours:
		(x,y,w,h)=cv2.boundingRect(i)
		if cv2.contourArea(i)<2000:
			continue
		cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)

		font=cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(frame1,'STATUS : (MOVEMENT)'.format('MOVEMENT'),(40,90),font,0.8,(255,0,0),2,cv2.LINE_AA)

#	cv2.drawContours(frame1,contours,-1,(0,0,255),2)

	cv2.imshow('feed',frame1)
	out.write(frame1)
	frame1=frame2
	_,frame2=cap.read()


		#out.write(frame)
		#cv2.imshow('f',frame)

	if cv2.waitKey(24) ==ord('q'):
		break
	
		

cap.release()
out.release()
#cv2.destroytAllWindows()