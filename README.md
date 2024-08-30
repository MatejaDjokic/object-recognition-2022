# Object Recognition 2022

- This is a school project made in my 2nd year of high school for a programming class.
- The focus of the project is using [Artificial Inteligence]() for regocnition purposes, to recognize faces, eyes.
- The datasets used for object recognition are [here](https://github.com/opencv/opencv/tree/master/data/haarcascades).

# Libraries

- [OpenCV](https://opencv.org/) for python - used for analyzing the current frame buffer and determining are there any wanted objects to highlight in the later stages
- [Tkinter](https://docs.python.org/3/library/tkinter.html) - a python gui library; used to rendera application window where the camera feed as well as the hightlighted objects are displayed
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) - also a python library with many automation capabilities; here I use it for taking screenshots of the application window and saving them into computer memory

# Coloring Schema

| Square Color  |  Object  |
|---------------|----------|
|     Red       |  Eyes    |
|     Blue      |  Profile |
|     Green     |  Face    | 

 - there are 3 green squares for 3 different face detection data sets

