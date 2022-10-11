from tkinter import NW, Tk, Canvas, PhotoImage
from tkinter import ttk
from tkinter import *
import cv2 
import pyautogui

# Tkinter window init
root = Tk()
root.title("Face Recognition")
root.resizable(True,True)
root.minsize(640, 480)
root.config(background = "white")

# COLORS
color_red = (0, 0, 255)
color_green = (0, 255, 0)
color_blue = (255, 0, 0) 

# DATA
front_face_data = cv2.CascadeClassifier(r'data/front_default.xml')
front_face1_data = cv2.CascadeClassifier (r'data/front_alt.xml')
front_face2_data = cv2.CascadeClassifier (r'data/front_alt2.xml')
eye_data = cv2.CascadeClassifier(r'data/eye.xml')
profile_data = cv2.CascadeClassifier(r'data/profile_face.xml')

# CORD INIT
front_face_cord = [[0,0,0,0]] 
front_face1_cord = [[0,0,0,0]] 
front_face2_cord = [[0,0,0,0]] 
eye_cord = [[0,0,0,0]]
smile_cord = [[0,0,0,0]]

# taking the direct feed from the webcam
cap = cv2.VideoCapture(0)

# photo input
def photo_image(img):
    h, w = img.shape[:2]
    data = f'P6 {w} {h} 255 '.encode() + img[..., ::-1].tobytes()
    return PhotoImage(width=w, height=h, data=data,format='PPM')

# update func for canvas and image creation and edit
def update(): 
    ret, img = cap.read()
    img = cv2.flip(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # SCEEN OBJECT DETECTION
    front_face_cord = front_face_data.detectMultiScale(gray)
    front_face1_cord = front_face1_data.detectMultiScale(gray) 
    front_face2_cord = front_face2_data.detectMultiScale(gray)
    eye_cord = eye_data.detectMultiScale(gray)
    profile_cord = profile_data.detectMultiScale(gray)

# DRAWING RECTANGLES
    # triple face object display
    for (x, y, w, h) in front_face_cord:
        cv2.rectangle(img, (x, y),(x+w,y+h), color_green, 2)
    for (x, y, w, h) in front_face1_cord:
        cv2.rectangle(img, (x, y),(x+w,y+h), color_green, 2)     
    for (x, y, w, h) in front_face2_cord:
        cv2.rectangle(img, (x, y),(x+w,y+h), color_green, 2)

    # eye and profile object display
    for (x, y, w, h) in eye_cord:
        cv2.rectangle(img, (x,y),(x+w,y+h), color_red, 2)
    for(x, y, w, h) in profile_cord:
        cv2.rectangle(img, (x, y), (x+w, y+h), color_blue , 2)
    if ret:
        photo = photo_image(img)
        canvas.create_image(0, 0, image=photo, anchor=NW)
        canvas.image = photo
    root.after(15, update)



# main part of the program coudl be in a Main() func
canvas = Canvas(root, width=640, height=480, background = "black")
canvas.pack() 
update() 
root.mainloop()
cap.release()

# taking and saving a screenshot with pyAutoGui
s = pyautogui.screenshot()
s.save(r"screenshots/s.jpeg")

# just to see if the code went 
#all the way to the end with no mistakes
print("Code Complete")