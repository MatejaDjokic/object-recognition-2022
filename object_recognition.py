from pyautogui import screenshot
from cv2 import (
    CascadeClassifier,
    COLOR_BGR2GRAY,
    VideoCapture,
    rectangle,
    cvtColor,
    flip,
)
from tkinter import (
    PhotoImage,
    Canvas,
    NW,
    Tk,
)


# Tkinter window init
root = Tk()
root.title("Face Recognition")
root.resizable(True, True)
root.minsize(640, 480)
root.config(background="white")

# Colors
color_red = (0, 0, 255)
color_green = (0, 255, 0)
color_blue = (255, 0, 0)

# Data
front_face_data = CascadeClassifier(r"data/front_default.xml")
front_face1_data = CascadeClassifier(r"data/front_alt.xml")
front_face2_data = CascadeClassifier(r"data/front_alt2.xml")
eye_data = CascadeClassifier(r"data/eye.xml")
profile_data = CascadeClassifier(r"data/profile_face.xml")

# Cord init
front_face_cord = [[0, 0, 0, 0]]
front_face1_cord = [[0, 0, 0, 0]]
front_face2_cord = [[0, 0, 0, 0]]
eye_cord = [[0, 0, 0, 0]]
smile_cord = [[0, 0, 0, 0]]

# Taking the direct feed from the webcam
videoCapture = VideoCapture(0)


# Photo input
def photo_image(img):
    h, w = img.shape[:2]
    data = f"P6 {w} {h} 255 ".encode() + img[..., ::-1].tobytes()
    return PhotoImage(width=w, height=h, data=data, format="PPM")


# Update func for canvas and image creation and edit
def update():
    ret, img = videoCapture.read()
    img = flip(img, 1)
    gray = cvtColor(img, COLOR_BGR2GRAY)

    # Sceen object detection
    front_face_cord = front_face_data.detectMultiScale(gray)
    front_face1_cord = front_face1_data.detectMultiScale(gray)
    front_face2_cord = front_face2_data.detectMultiScale(gray)
    eye_cord = eye_data.detectMultiScale(gray)
    profile_cord = profile_data.detectMultiScale(gray)

    # Drawing rectangles
    # Triple face object display
    for x, y, w, h in front_face_cord:
        rectangle(
            img,
            (x, y),
            (x + w, y + h),
            color_green,
            2,
        )
    for x, y, w, h in front_face1_cord:
        rectangle(
            img,
            (x, y),
            (x + w, y + h),
            color_green,
            2,
        )
    for x, y, w, h in front_face2_cord:
        rectangle(
            img,
            (x, y),
            (x + w, y + h),
            color_green,
            2,
        )

    # Eye and profile object display
    for x, y, w, h in eye_cord:
        rectangle(
            img,
            (x, y),
            (x + w, y + h),
            color_red,
            2,
        )
    for x, y, w, h in profile_cord:
        rectangle(
            img,
            (x, y),
            (x + w, y + h),
            color_blue,
            2,
        )

    if ret:
        photo = photo_image(img)
        canvas.create_image(0, 0, image=photo, anchor=NW)
        canvas.image = photo

    root.after(15, update)


# Main part of the program coudl be in a main func
canvas = Canvas(
    root,
    width=640,
    height=480,
    background="black",
)
canvas.pack()
update()
root.mainloop()
videoCapture.release()
