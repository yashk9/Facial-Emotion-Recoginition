from keras.models import load_model
from time import sleep
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
import cv2
import numpy as np

face_classifier = cv2.CascadeClassifier(r'C:\\Users\\wel\\Desktop\\BE\\CODING SEM 2\\FER VERSION !\\work\\haarcascade_frontalface_default.xml')
classifier =load_model(r'C:\\Users\\wel\\Desktop\\BE\\CODING SEM 2\\FER VERSION !\\model.h5')

emotion_labels = ['Angry','Disgust','Fear','Happy','Neutral', 'Sad', 'Surprise']

#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

img_counter=0
imgc = 7
while True:
    _, frame = cap.read()
    labels = []
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray)

    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
        
        roi_gray = gray[y:y+h,x:x+w]
        roi_gray = cv2.resize(roi_gray,(48,48),interpolation=cv2.INTER_AREA)

        
        label1 = "Neutral"
        if np.sum([roi_gray])!=0:
            while 0 < imgc <=7:
                roi = roi_gray.astype('float')/255.0
                roi = img_to_array(roi)
                roi = np.expand_dims(roi,axis=0)
                prediction = classifier.predict(roi)[0]
                label = emotion_labels[prediction.argmax()]
                label_position = (x,y)
               
                cv2.putText(frame,label,label_position,cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
                #print(label)
                
                if(label != label1):
                    print(label1)
                    label1 = label
                    print(label1)
                    imgc = imgc - 1
                    print("Exiting......")

                else:
                    continue    
        else:
            cv2.putText(frame,'No Faces',(30,80),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
                # label2= label
                # if(label != label2):
        

        
        


    cv2.imshow('Emotion Detector',frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    #elif k%256 == 32:
        # SPACE pressed
        
        
       # print("{} written!".format(img_name))
       
    #if cv2.waitKey(1) & 0xFF == ord('q'):
        #break

#  while True:
#                 img_name = label+"_{}.png".format(img_counter)
#                 cv2.imwrite("C:\\Users\\wel\\Desktop\\IMAGES\\"+img_name, frame)
#                 img_counter += 1
#                 break

cap.release()
cv2.destroyAllWindows()