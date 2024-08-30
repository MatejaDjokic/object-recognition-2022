# Object Recognition 2022

- This is a school project made in my 2nd year of high school for a programming class.
- The focus of the project is using [Artificial Inteligence]() for regocnition purposes, to recognize faces, eyes.
- The datasets used for object recognition are [here](https://github.com/opencv/opencv/tree/master/data/haarcascades).

# Libraries

- [OpenCV](https://opencv.org/) for python - used for analyzing the current frame buffer and determining are there any wanted objects to highlight in the later stages
- [Tkinter](https://docs.python.org/3/library/tkinter.html) - a python gui library; used to rendera application window where the camera feed as well as the hightlighted objects are displayed

# Installing Libraries

```
$ pip install -r requirements.txt
```

# Coloring Schema

| Square Color             | Object                    |
| ------------------------ | ------------------------- |
| $${\color{red}Red}$$     | $${\color{red}Eyes}$$     |
| $${\color{blue}Blue}$$   | $${\color{blue}Profile}$$ |
| $${\color{green}Green}$$ | $${\color{green}Face}$$   |
