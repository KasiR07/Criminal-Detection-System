
import cv2

def detect_faces(gray_image):
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)
    return faces

def open_detect_window(root):
    import tkinter as tk
    from tkinter import filedialog
    import PIL.Image, PIL.ImageTk

    def detect():
        file_path = filedialog.askopenfilename()
        if not file_path:
            return
        img = cv2.imread(file_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detect_faces(gray)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.imshow("Detected", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    window = tk.Toplevel(root)
    window.title("Detect Criminal")
    tk.Button(window, text="Select Image and Detect", command=detect).pack(padx=20, pady=20)
