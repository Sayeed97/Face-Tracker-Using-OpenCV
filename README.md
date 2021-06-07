# Brief 
This program captures each frame from the computer camera and performs cascade classfication on each frame to identify a human face. In this case a human face is the Region Of Interest (ROI). It finds the ROI centre and finds the x and y axis displacement of the object centre from the frame centre.  

# Cascade Classifier 
Object Detection using Haar feature-based cascade classifiers is an effective object detection method. It is a machine learning based approach where a cascade function is trained from a lot of positive and negative images. It is then used to detect objects in other images.

# Contents
- face_tracker.py - Source code
- haarcascade_frontalface_default.xml - Necessary xml file for object detection

# Code Sequence
1. Create an object from Cascade classifier class for object detection
2. Create a videocapture object
3. Calculate the frame centre
4. Read each frame from the camera feed
5. Draws a red dot in the centre of the frame
6. Draws a rectangular box around the ROI (Human face)
7. Draws a circle around the detected face centre
8. Draws a arrow line between the frame centre and the face centre
9. Calculates the x and y axis displacement error between the frame and the ROI centre
10. Display the modified image
11. Checks if esc key is pressed, if not repeat from step 4
12. Release the video capture object and destroy all the created windows
