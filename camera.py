from keras.models import load_model
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
import cv2
import numpy as np

face_classifier = cv2.CascadeClassifier(r'C:\\Users\\manvi moza\\Desktop\\ALL CODES\\FERcodebase\\Emotion_Detection_CNN\\haarcascade_frontalface_default.xml')
classifier = load_model(r'C:\\Users\\manvi moza\\Desktop\\ALL CODES\\FERcodebase\\Emotion_Detection_CNN\\cnnModel.h5')

emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']

img_counter = 0
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    labels = []
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 224, 224), 2)

        roi_gray = gray[y:y + h, x:x + w]
        roi_gray = cv2.resize(roi_gray, (48,48), interpolation=cv2.INTER_AREA)

        if np.sum([roi_gray]) != 0:
            roi = roi_gray.astype('float') / 255.0
            roi = img_to_array(roi)
            roi = np.expand_dims(roi, axis=0)

            prediction = classifier.predict(roi)[0]
            label = emotion_labels[prediction.argmax()]
            label_position = (x, y)

            cv2.putText(frame, label, label_position, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            img_name = label + "_{}.png".format(img_counter)
            cv2.imwrite("C:\\Users\\manvi moza\\Desktop\\ALL CODES\\FERcodebase\\Images\\{}\\".format(
                label.lower()) + img_name, frame)
            img_counter += 1

        else:
            cv2.putText(frame, 'No Faces', (30, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('Emotion Detector', frame)

    k = cv2.waitKey(1)
    if k % 256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break

cap.release()
cv2.destroyAllWindows()
import fileHandling as fh
fh()




