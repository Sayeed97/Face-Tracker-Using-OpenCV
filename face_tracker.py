import sys
import time
import cv2

def enable_face_tracking():
    # Creating an object from Cascade classifier class for object detection.
    obj_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    # Creating a videocapture object for receiving feed from the laptop web cam
    cap = cv2.VideoCapture(0)
    # getting or reading the image frames from the camera feed
    _, frame = cap.read()
    # prints the shape or dimensions of the camera feed window
    print(frame.shape)
    # Centre of the video feed window
    frame_centre = ((frame.shape[1]//2), (frame.shape[0]//2))
    # a while loop to run the algorithm on each frame
    while 1:
        # reading the image frames from the camera feed (ret is bool, if: frame received then it is true else: it is false)
        ret, img = cap.read()
        # draws a red cirlce at the centre of the camera feed window
        img = cv2.circle(img, frame_centre, 5, (0,0,255), -1)
        # converts the color image to gray image
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # it returns the positions of detected faces
        faces = obj_cascade.detectMultiScale(gray, 1.3, 5)
        # if faces is not empty that is if a human face is detected
        if len(faces) > 0:
            # draws a rectangular bordor around the detected face in the image
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),4)
            # calculates the centroid of the face
            obj_centre = (x + w//2, y + h//2)
            # draws a circle at the centroid of the detected face
            img = cv2.circle(img, obj_centre, 5, (0,255,0), -1)
            # draws an arrow to show the displacement from the window frame centroid to the face centroid
            img = cv2.arrowedLine(img, frame_centre, obj_centre, [0, 255, 0], 4)
            
            # calculate the x-axis and y-axis error
            x_error = frame_centre[0] - obj_centre[0]
            y_error = frame_centre[1] - obj_centre[1]

            # print(x_error, y_error) that is displacement 
            cv2.putText(img, f"X Error: {x_error}", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
            cv2.putText(img, f"Y Error: {y_error}", (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
        # displays the processed image
        cv2.imshow('img',img)
        # waits till escape key is pressed if pressed breaks out of the loop 
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    # releasing the video capture object as it is not required anymore 
    cap.release()
    # destroys all the image windows 
    cv2.destroyAllWindows()
    # waits for 2 seconds 
    time.sleep(2)
    # ends the program
    print("End of Program")
    sys.exit(0)
    
enable_face_tracking()