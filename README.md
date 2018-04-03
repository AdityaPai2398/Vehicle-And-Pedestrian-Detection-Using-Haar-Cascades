# Vehicle-And-Pedestrian-Detection-Using-Haar-Cascades
<h1>Real Time Detection and Classification of Vehicles and Pedestrians Using Haar Cascade Classifier with Background Subtraction</h1>

Computer Vision Plays a vital role in traffic management and surveillance systems and has been an active research area in the past years. In systems like these, the detection of vehicles and also classification of the vehicle plays a major role. The datasets are traffic videos of urban environment taken from various cities around the world which were used to train the classifier hence generating a robust classifier. The proposed approach is computationally less expensive with faster processing speed. The experiments on-road prove it to be a robust and real time algorithm which is highly competitive with the existing architecture.

This System has the following Haar Cascades:
1) Haar Cascade for Car detection
2) Haar Cascade for Bus Detection
3) Haar Cascade for Two-Wheeler Detection
4) Haar Cascade for Pedestrian Detection



The Results of the system are as shown below:

![car](https://user-images.githubusercontent.com/19201530/34076958-a52a5908-e31b-11e7-8350-38e583a13374.PNG)


![bus](https://user-images.githubusercontent.com/19201530/34076957-a4e07644-e31b-11e7-8c89-f7b208d42782.PNG)


![pedestrian](https://user-images.githubusercontent.com/19201530/34076959-a5720d52-e31b-11e7-8842-e25c4a3b9553.PNG)

![two wheeler](https://user-images.githubusercontent.com/19201530/34076961-a5ba531e-e31b-11e7-97f9-063c5e282bfd.PNG)

<b>Steps To Run The Project</b>

System Requirements to Run the Vehicle Detection Project.
____________________________________________________________________________________________________________________
1) Python 3.6 Or above
2) Opencv-python -> Python 3.4+ comes with an easy installation tool called pip to install additional packages. (package manager) 
     So to Install opencv-python open the cmd in administrator mode and then type->    pip install opencv-python 
     Also numpy may be required so also type->    pip install numpy
Successfull installation of above packages may be checked by moving into python shell and typing "import cv2"
If nothing shows up then installation was successful.
	 
So now all the software requirements are satisified.
We had used python 3.6.1 but any version higher than 3.6.1 will also do.

**** THE PROJECT WON'T RUN ON VERSIONS OF PYTHON BELOW PYTHON 3.X     
_______________________________________________________________________________________________________________________________


The Project Folders have 4 sub folders
1)Car 
2)Two Wheeler
3)Bus
4)Pedestrian 

In each of the subfolder there will be two videos ,one haarcascade ,two python scripts (one for each of the videos).
(only pedestrian detection has one video rest all have 2 viddeos)	 

Double Clicking on any of the python scripts will run the program.(or even right click _>Open in idle and run will also do)


To Create Your Own Haar Cascade Refer This: https://www.google.co.in/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwjE89XbrJDYAhWMp48KHXXnDWsQFggrMAA&url=https%3A%2F%2Fwww.cs.auckland.ac.nz%2F~m.rezaei%2FTutorials%2FCreating_a_Cascade_of_Haar-Like_Classifiers_Step_by_Step.pdf&usg=AOvVaw0BAeKbBkefnCykzazRxCol

