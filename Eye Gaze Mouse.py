import cv2
import mediapipe as mp
import pyautogui
cam =cv2.VideoCapture(0)
face_mesh =mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)#refine_landmark is used to get much more refined landmark
screen_w,screen_h =pyautogui.size()
while True:
    _,frame=cam.read()
    #flipping vertically 1
    frame=cv2.flip(frame,1)
    rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output=face_mesh.process(rgb_frame)
    landmark_points=output.multi_face_landmarks
    frame_h,frame_w,_=frame.shape
    if landmark_points:
        landmarks =landmark_points[0].landmark
        #enumerate gives two points one as id and another is landmark
        for id, landmark in enumerate(landmarks[474:478]):#last four landmarks presnt over eye
            #There are four point on eye so by using enumerate we can choose one point as id and we move the mouse
            x=int(landmark.x *frame_w)
            y=int(landmark.y *frame_h)
            cv2.circle(frame,(x,y),3,(0,255,0))
            if id ==1:
                #screen_x = int(landmark.x * screen_w) to increase to cursor speed
                screen_x =screen_w/frame_w*x
                #screen_y = int(landmark.y * screen_h)
                screen_y =screen_h/frame_h*y
                pyautogui.moveTo(screen_x,screen_y)
        left=[landmarks[145],landmarks[159]]
        for landmark in left:#to find another landmark 145,159 (upper and lower landmark of eye) to click over mouse
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))
        if(left[0].y-left[1].y)<0.004:
             pyautogui.click()
             pyautogui.sleep(1)
             #to find difference to find whether the eye is closed are not
    cv2.imshow('Eye Controlled Mouse',frame)
    cv2.waitKey(1)
