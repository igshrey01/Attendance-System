# Attendance-System-Using-Real-time-Face-Recognition
Attendance System Using Real Time Face Recognition

Libraries Required:-
1)	OpenCV :- OpenCV (Open Source Computer Vision Library) is an open-source computer vision and machine learning software library. We need it to take pictures using our webcam and some manipulation needed to be done in the image.
2)	Pillow :-  The Python Imaging Library adds image processing capabilities to your Python interpreter.This library provides extensive file format support, an efficient internal representation, and fairly powerful image processing capabilities.
3)	CSV :- The csv module implements classes to read and write tabular data in CSV format.
4)	Datetime :-  The Datetime module supplies classes for manipulating dates and times.
5)	Tkinter :- Tkinter is a simple GUI module used for implementing fairly simple GUI and helps us to interact with code in a simple way.
6)	Time :- This module provides functions for working with times, and for converting between representations.
7)	OS :- The OS module in Python provides a way of using operating system dependent functionality.The functions that the OS module provides allows you to interface with the underlying operating system that Python is running on – be that Windows, Mac or Linux.
8)	NumPy :- NumPy is the fundamental package for scientific computing in Python which provides a multidimensional array object. We just need it to convert our images into some form of an array so that we can store the model that has been trained.


Instructions:-
1) Create a directory named as Face Recognition.
2) Create an attendance folder inside the directory and make two csv files (MorningAttendance.csv and EveningAttendance.csv)
3) For creating a csv file , open excel and save the file as MorningAttendance/EveningAttendance.csv(comma delimited)
4) Then create a folder named as Training Images .
5) Download the haarcascade frontal face default xml file from https://github.com/opencv/opencv/tree/master/data/haarcascades.
6) Create a trainer folder and save trainer.yml file in it.
7) Create a UserDetails csv file that will store id and name of employee that are registered within our program.


Using The AttendanceSystem GUI
1) Run the code and a GUI will be opened.
2) The main window of the GUI will be used to mark the attendance.
3) If you are a new user , click on New Employee ! Sign Up.
4) Enter the Employee Id and Employee Name respectively and click on Take Images.
5) Take Images button will open a webcam window that will click 40 images  and will close on its          own.
6) Then click on Train Images button that will train all the images present in Training Images folder.
7) Then click on Return to Main Menu to return to the main window.
8) For marking attendance , type employee id and employee name and click on Morning Attendance or Evening Attendance button as per the need.
9) The button will open a webcam window that will display employee id + employee name at the top and confidence at the bottom.
10) Press Escape button after a few seconds and the attendance will be updated in the respective csv folder.
 

