
import cv2
import tkinter as tk

def open_surveillance_window(root):
    def start_camera():
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            cv2.imshow("Surveillance", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        cap.release()
        cv2.destroyAllWindows()

    window = tk.Toplevel(root)
    window.title("Video Surveillance")
    tk.Button(window, text="Start Camera", command=start_camera).pack(padx=20, pady=20)
