
import cv2   
vid = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("...")
while 1:
    
    
    ret, frame = vid.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.4, 1)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow('video',frame)

  
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



vid.release()
cv2.destroyAllWindows()
