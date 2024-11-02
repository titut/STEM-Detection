# Importing all necessary libraries 
import cv2 
import os

VIDEO_PATH = "video1.mp4" #"path/to/video/folder" # Change this
IMAGE_PATH = "images"

EXTENSION = ".jpg"
vid = cv2.VideoCapture(VIDEO_PATH)
fps = round(vid.get(cv2.CAP_PROP_FPS))
target_frame_rate = 6

hop = round(fps/target_frame_rate)
print(hop)
curr_frame = 0
frame_number = 0
while(True):
    ret, frame = vid.read()
    if not ret:
        break
    if curr_frame % hop == 0 and curr_frame > 100:
        name = os.path.join("images", "image_" + str(frame_number) + EXTENSION)
        cv2.imwrite(name, frame)
        frame_number = frame_number + 1
    curr_frame = curr_frame + 1

vid.release()