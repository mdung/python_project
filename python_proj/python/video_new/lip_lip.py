import cv2
from tkinter import Tk, Button, Label, filedialog

def modify_frame(frame):
    # Replace this function with your actual lip-sync algorithm
    # This is just an example; you should implement the logic that suits your needs
    # For now, let's just add a red circle to the center of the frame
    height, width, _ = frame.shape
    cv2.circle(frame, (width // 2, height // 2), 30, (0, 0, 255), -1)
    return frame

def lip_sync(video_path, output_filename):
    cap = cv2.VideoCapture(video_path)
    frames = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Modify the frame using your lip-sync algorithm
        modified_frame = modify_frame(frame)

        frames.append(modified_frame)

    cap.release()

    # Save the modified frames as a new video
    height, width, _ = frames[0].shape
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_filename, fourcc, 30.0, (width, height))

    for frame in frames:
        out.write(frame)

    out.release()

def upload_video():
    file_path = filedialog.askopenfilename(title="Select a video file", filetypes=[("Video files", "*.mp4;*.avi")])
    video_path_label.config(text=file_path)

def process_video():
    video_path = video_path_label.cget("text")
    output_filename = f"modified_{video_path.split('/')[-1]}"
    lip_sync(video_path, output_filename)
    result_label.config(text=f"Output saved as {output_filename}")

# GUI setup
root = Tk()
root.title("Lip Sync App")

upload_button = Button(root, text="Upload Video", command=upload_video)
upload_button.pack()

video_path_label = Label(root, text="No video selected")
video_path_label.pack()

process_button = Button(root, text="Process Video", command=process_video)
process_button.pack()

result_label = Label(root, text="")
result_label.pack()

root.mainloop()
