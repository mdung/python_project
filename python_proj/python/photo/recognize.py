import cv2
import tkinter as tk
from tkinter import filedialog

import numpy as np
from PIL import Image, ImageTk

# Load YOLO model
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
classes = []

with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

class ObjectDetectionApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Object Detection App")

        self.image_path = None
        self.image_label = tk.Label(self.master)
        self.image_label.pack()

        self.browse_button = tk.Button(self.master, text="Browse Image", command=self.browse_image)
        self.browse_button.pack()

        self.detect_button = tk.Button(self.master, text="Detect Objects", command=self.detect_objects)
        self.detect_button.pack()

    def browse_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.image_path = file_path
            self.display_image()

    def display_image(self):
        img = cv2.imread(self.image_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = img.resize((400, 300))
        img = ImageTk.PhotoImage(img)
        self.image_label.config(image=img)
        self.image_label.image = img

    def detect_objects(self):
        if self.image_path:
            img = cv2.imread(self.image_path)
            height, width, channels = img.shape

            # Detecting objects
            blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
            net.setInput(blob)
            outs = net.forward(output_layers)

            # Showing information on the screen
            class_ids = []
            confidences = []
            boxes = []

            for out in outs:
                for detection in out:
                    scores = detection[5:]
                    class_id = np.argmax(scores)
                    confidence = scores[class_id]
                    if confidence > 0.5:
                        # Object detected
                        center_x = int(detection[0] * width)
                        center_y = int(detection[1] * height)
                        w = int(detection[2] * width)
                        h = int(detection[3] * height)

                        # Rectangle
