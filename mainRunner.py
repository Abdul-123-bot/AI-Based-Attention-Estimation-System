#all imports 
from keras.models import load_model
from time import sleep
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
import cv2
import numpy as np
from GazeTracking.gaze_tracking import GazeTracking
import xlsxwriter     
import time      

#function to return the mapping for label to the values of the emotions
def get_number(label):
    if(label==0):
        return 0.788
    elif(label==1):
        return 0.511
    elif(label==2):
        return 0.788
    elif(label==3):
        return 0.847
    elif(label == 4):
        return 0.7083
    elif(label==5):
        return 0.725
    elif(label ==6):
        return  1
    else:
        return 0

webcam = cv2.VideoCapture(0) #open the camera

gaze = GazeTracking() #gaze tracking object
cascade_classifier=cv2.CascadeClassifier(r'C:\Users\majaa\OneDrive\Desktop\images\haarcascade_frontalface_default.xml') #model to search for face in an image
model=load_model(r'C:\Users\majaa\OneDrive\Desktop\images\Emotion2.h5') #emotion detection model
class_labels=['Angry','Disgust','Fear','Happy','Neutral','Sad','Surprise'] #classes of the emotions

#create an excel sheet to write write data
book = xlsxwriter.Workbook(r'C:\Users\majaa\OneDrive\Documents\MajorProject-main\Data\sheets\data.xlsx')     
sheet = book.add_worksheet('data')
row = 0    
column = 0   

#Time information variables
TT =2400 #runs for 1200 frames
sleep_time = 0.5 #sleeps for 0.499 ~ 0.5 secs, so runs at 2fps
t=0

i=0
while (TT > 0):
    _, frame = webcam.read()
    labels = [] #labels initialized as an empty list 

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # gray scale the image
    faces = cascade_classifier.detectMultiScale(gray,1.3,5) #detect the faces

    #for each face detected in the image
    for (x,y,w,h) in faces:

        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,0),2) #put a rectagle on the face
        roi_gray = gray[y:y+h,x:x+w] #cut out the face in gray
        roi_gray = cv2.resize(roi_gray,(48,48),fx=100,fy=100,interpolation=cv2.INTER_CUBIC) #resize the face
        crop = frame[y:y+h,x:x+w] #save the face in color formate
        
        if np.sum([roi_gray])!=0: #is face is present, and the image is not all dark
            
            #EMotion Detection part
            roi = roi_gray.astype('float')/255.0
            roi = img_to_array(roi)
            roi = np.expand_dims(roi,axis=0)

            preds = model.predict(roi)[0] #do the prediction
            label=class_labels[preds.argmax()] #get the label
            label_position = (x,y)  #make a tuple of the coordinates where the face begins
            cv2.putText(frame,label,label_position,cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,255),3) #print stuff on the frame

            #Gaze Tracking part
            gaze.refresh(frame) #give the source image to the gaze tracking object
            frame = gaze.annotated_frame() #set the markings on the pupils
            hr=gaze.horizontal_ratio()
            vr=gaze.vertical_ratio()
            label_position = (x-2,y-50)
            label = get_number(label)
            l=[]  
            l.append(hr)
            l.append(vr)
            l.append(preds.argmax())
            #seconds = time.time()
           # local_time = time.ctime(seconds)
            #l.append(local_time)
            for x in l:
                print()
                sheet.write(row, column, x)
                column+=1
            row += 1
            column=0
            cv2.imshow("Demo", frame)
            cv2.imwrite(r'C:\Users\majaa\OneDrive\Documents\MajorProject-main\Data\Images\kang'+str(i)+'.jpg',crop)
            sheet.insert_image(row-1,3,r'C:\Users\majaa\OneDrive\Documents\MajorProject-main\Data\Images\kang'+str(i)+'.jpg')            
            i+=1
    if cv2.waitKey(1) == 27:
        break
    time.sleep(sleep_time) #sleeps till the amount of time specified in 'sleep_time' variable
    TT = TT -1 #reduce the number of frames captured
book.close()
