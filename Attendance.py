# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 19:24:19 2020

@author: Shrey
"""
import cv2
import csv
import tkinter as tk 
from PIL import Image 
import os
import numpy as np  

import datetime
import time
class tkinterApp(tk.Tk): 
    def __init__(self, *args, **kwargs):  
        tk.Tk.__init__(self, *args, **kwargs) 
        container = tk.Frame(self,bg='black')
        container.pack(side = "top", fill = "both", expand = True)  
        container.grid_rowconfigure(0, weight = 1) 
        container.grid_columnconfigure(0, weight = 1) 
   
        self.frames = {}   
        
        for F in (StartPage, Page1): 
            frame = F(container, self) 
            self.frames[F] = frame  
            frame.grid(row = 0, column = 0, sticky ="nsew") 
            self.show_frame(StartPage) 
         
    def show_frame(self, cont): 
        frame = self.frames[cont] 
        frame.tkraise() 
        
    
        
    def TakeImages(self,txt1,txt2):
        webcam=cv2.VideoCapture(0)
        id =int(txt1.get())  
        name =(txt2.get())
        
        def id_is_num(id1):
            try:
                int(id1)
                return True
            except ValueError:
                pass
        
        def CheckForEmployeeId(id1):
            f = open('UserDetails.csv')
            csv_f = csv.reader(f)
            for line in csv_f:
                for word in line:
                    if word==str(id1):
                        print("Employee Id Already Registered")
                        return True
            return False         
                        
        
        if(id_is_num(id) and name.isalpha() and not CheckForEmployeeId(id)) :
            face_detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
            print('Camera Opening. Focus On Camera')
            count=0
            while(1):
                ret,img=webcam.read()
                gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                faces=face_detector.detectMultiScale(gray,1.3,5)
                for(x,y,w,h) in faces:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                    cv2.imwrite('Training Images/Users.'+str(id)+'.'+str(count)+'.jpg',gray[y:y+h,x:x+w])
                    count=count+1
                    cv2.imshow('Video Capture',img)
                if count>=40:
                    break
                k=cv2.waitKey(100) & 0xff
                if k==27:
                    break
            webcam.release()
            cv2.destroyAllWindows()   
            row = [id,name]  
            with open(r"UserDetails.csv", 'a+') as csvFile: 
                writer = csv.writer(csvFile) 
                # Entry of the row in csv file 
                writer.writerow(row)  
            csvFile.close()
    
    def train_images(a):
        path = 'Training Images'
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        
        FaceSamples=[]
        ids = []
        def getImagesAndLabels(path):
            imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
            for imagePath in imagePaths:
                PIL_img = Image.open(imagePath).convert('L') # convert it to grayscale
                img_numpy = np.array(PIL_img,'uint8')
                id = int(os.path.split(imagePath)[-1].split(".")[1])
                FaceSamples.append(img_numpy)
                ids.append(id)
                
            return FaceSamples,ids
    
        print ("Training faces. Wait a few seconds ...")
        faces,ids = getImagesAndLabels(path)
        recognizer.train(faces, np.array(ids))
        recognizer.save('trainer/trainer.yml') 
        print("Number of faces trained : ",format(len(np.unique(ids))))
    
    def Morning_Attendance(self):
        i=1
        def UserDetails(id):
            j=0
            f = open('UserDetails.csv')
            csv_f = csv.reader(f)
            for line in csv_f:
                for a in line:
            
                    if(a==str(id)):
                        j=1
                        continue
                    if(j==1):
                        return a
        
              
                
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read('trainer/trainer.yml')   
        faceCascade = cv2.CascadeClassifier("D:\Face Recognition\haarcascade_frontalface_default.xml");
        font = cv2.FONT_HERSHEY_SIMPLEX


        cam = cv2.VideoCapture(0)
        cam.set(3, 640) 
        cam.set(4, 480) 
        
        while True:

            ret, img =cam.read()
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray,1.3,5)
            for(x,y,w,h) in faces:
                cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
                id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
                if (confidence < 50):
                    ts = time.time()      
                    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                    timeStamp = datetime.datetime.fromtimestamp(ts).strftime("%H:%M:%S")
                    
                    id1=id
                    id=str(id)+' '+UserDetails(id)
                    confidence = "  {0}%".format(round(confidence))
                    if(i==1):
            
                        row = [id1,UserDetails(id1),date,timeStamp]  
                        with open(r"Attendance\MorningAttendance.csv", 'a+') as csvFile: 
                            writer = csv.writer(csvFile) 
                            writer.writerow(row)  
                        csvFile.close() 
                        i=i+1
               
                elif (confidence > 75):
                    id = "Unknown"
                    
                    
                cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
                cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
  
            cv2.imshow('Camera',img) 

            k = cv2.waitKey(10) & 0xff 
            if k == 27:
                break


        cam.release()
        cv2.destroyAllWindows()
        
    def Evening_Attendance(a):
        i=1
        def UserDetails(id):
            i=0
            f = open('UserDetails.csv')
            csv_f = csv.reader(f)
            for line in csv_f:
                for a in line:
            
                    if(a==str(id)):
                        i=1
                        continue
                    if(i==1):
                        return a
        
                
                
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read('trainer/trainer.yml')   
        faceCascade = cv2.CascadeClassifier("D:\Face Recognition\haarcascade_frontalface_default.xml");
        font = cv2.FONT_HERSHEY_SIMPLEX


        cam = cv2.VideoCapture(0)
        cam.set(3, 640) 
        cam.set(4, 480) 
        
        while True:

            ret, img =cam.read()
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray,1.3,5)
            for(x,y,w,h) in faces:
                cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
                id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
                if (confidence <50):
                    ts = time.time()      
                    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                    timeStamp = datetime.datetime.fromtimestamp(ts).strftime("%H:%M:%S")
                    
                    id1=id
                    id=str(id)+' '+UserDetails(id)
                    confidence = "  {0}%".format(round(confidence))
                    if(i==1):
            
                        row = [id1,UserDetails(id1),date,timeStamp]  
                        with open(r"Attendance\EveningAttendance.csv", 'a+') as csvFile: 
                            writer = csv.writer(csvFile) 
                            # Entry of the row in csv file 
                            writer.writerow(row)  
                        csvFile.close() 
                        i=i+1
                elif (confidence>75):
                    id = "Unknown"
                    confidence = "  {0}%".format(round(100 - confidence))
                    #attendance=attendance.drop_duplicates(subset=['Id'],keep='first') 
                cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
                cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
  
            cv2.imshow('Camera',img) 

            k = cv2.waitKey(10) & 0xff 
            if k == 27:
                break


        cam.release()
        cv2.destroyAllWindows()        

class StartPage(tk.Frame): 
    def __init__(self, parent, controller):  
        tk.Frame.__init__(self, parent,bg='black') 
        
        message = tk.Label( 
            self, text ="Face-Recognition-System",  
            bg ="purple", fg = "white", width = 55,  
            height = 3, font = ('times', 30, 'bold'))
        message.place(x = 0, y = 0)
        
        lbl= tk.Label(self, text = "Enter Your Details ",  
                      width = 20, height = 2, fg ="white",  
                      bg = "black", font = ('times', 15, ' bold ') )  
        lbl.place(x = 500, y = 150) 

        lbl1 = tk.Label(self, text = "Employee Id : ",  
                    width = 20, height = 2, fg ="white",  
                    bg = "black", font = ('times', 15, ' bold ') )  
        lbl1.place(x = 400, y = 200) 
        
        txt1 = tk.Entry(self,  
                    width = 20, bg ="white",  
                    fg ="black", font = ('times', 15, ' bold ')) 
        txt1.place(x = 600, y = 215) 
  
        lbl2 = tk.Label(self, text ="Employee_Name : ",  
                    width = 20, fg ="white", bg ="black",  
                    height = 2, font =('times', 15, ' bold '))  
        lbl2.place(x = 400, y = 250) 
    
        txt2 = tk.Entry(self, width = 20,  
                    bg ="white", fg ="black",  
                    font = ('times', 15, ' bold ')  ) 
        txt2.place(x = 600, y = 265)
        
        MorningAttendance = tk.Button(self, text ="Morning Attendance ",  
                                  command=lambda:controller.Morning_Attendance(), fg ="white", bg ="purple",  
                                  width = 15, height = 2, activebackground = "Red",  
                                  font =('times', 15, ' bold '))
        MorningAttendance.place(x = 380, y = 350)

        EveningAttendance = tk.Button(self, text ="Evening Attendance ",  
                                  command=lambda:controller.Evening_Attendance(), fg ="white", bg ="purple",  
                                  width = 15, height = 2, activebackground = "Red",  
                                  font =('times', 15, ' bold '))
        EveningAttendance.place(x = 650, y = 349) 
 
        SignUp = tk.Button(self, text ="New Employee ! Sign Up ",  
                        command = lambda : controller.show_frame(Page1), fg ="white", bg ="purple",  
                        width = 20, height = 2, activebackground = "Red",  
                        font =('times', 15, ' bold '))
        SignUp.place(x = 500, y = 450)      
         
        
           
   
   

class Page1(tk.Frame): 
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent,bg='black') 
        
        message = tk.Label( 
                self, text ="Face-Recognition-System",  
                bg ="purple", fg = "white", width = 55,  
                height = 3, font = ('times', 30, 'bold'))
        message.place(x = 0, y = 0)
        
        lbl= tk.Label(self, text = "Sign Up",  
                              width = 20, height = 2, fg ="white",  
                              bg = "black", font = ('times', 25, ' bold ') )  
        lbl.place(x = 400, y = 150)  
        
         
        
        lbll= tk.Label(self, text = "Enter Your Details ",  
                               width = 20, height = 2, fg ="white",  
                               bg = "black", font = ('times', 15, ' bold ') )  
        lbll.place(x = 470, y = 220) 

        lbl3 = tk.Label(self, text = "Employee Id : ",  
                                width = 20, height = 2, fg ="white",  
                                bg = "black", font = ('times', 15, ' bold ') )  
        lbl3.place(x = 400, y = 270) 
        
        txt1 = tk.Entry(self,  width = 20, bg ="white",  
                                fg ="black", font = ('times', 15, ' bold ')) 
        txt1.place(x = 600, y = 285) 
  
        lbl2 = tk.Label(self, text ="Employee_Name : ",  
                                width = 20, fg ="white", bg ="black",  
                                height = 2, font =('times', 15, ' bold '))  
        lbl2.place(x = 400, y = 320) 
    
        txt2 = tk.Entry(self, width = 20,  
                                bg ="white", fg ="black",  
                                font = ('times', 15, ' bold ')  ) 
        txt2.place(x = 600, y = 335)
                
        TakeImage = tk.Button(self, text ="Take Images",  
                                  command=lambda:controller.TakeImages(txt1,txt2), fg ="white", bg ="purple",  
                                  width = 15, height = 2, activebackground = "Red",  
                                  font =('times', 15, ' bold '))
        TakeImage.place(x = 380, y = 420)

        TrainImage = tk.Button(self, text ="Train Images ",  
                                       command=lambda:controller.train_images(), fg ="white", bg ="purple",  
                                       width = 15, height = 2, activebackground = "Red",  
                                       font =('times', 15, ' bold '))
        TrainImage.place(x = 650, y = 419)
                
        MainMenu = tk.Button(self, text ="Return To Main Menu", 
                                     command = lambda : controller.show_frame(StartPage),fg='white'
                                     ,bg='purple' ,width=15,height=2,activebackground='red' ,
                                     font =('times', 15, ' bold '))
        MainMenu.place(x = 520 ,y=500) 
                                  
        message1 = tk.Label( 
            self, text ="Note : First Enter Employee Id and Employee Name . Then click on Take Images. ",  
            bg='black',fg = "white", width = 100,  
            height = 1, font = ('times', 18, 'bold'))
        message1.place(x = 0, y = 580)
                
        message2 = tk.Label( 
                     self, text ="The Software will click your images . Then click on Train Image and Then Return to Main Menu",  
                     bg ="black", fg = "white", width = 100,  
                     height = 1, font = ('times', 18, 'bold'))
        message2.place(x = 0, y = 610)
   
   
app = tkinterApp() 
app.mainloop()