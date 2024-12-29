# GUI: Load and process image
def process_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
    if not file_path:
        return

    image = cv2.imread(file_path)
    processed_image, results, sleeping_count = process_frame(image)

    # Show results
    messagebox.showinfo("Drowsiness Detection", f"Sleeping People: {sleeping_count}\nDetails: {results}")
    cv2.imshow("Processed Image", processed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# GUI: Load and process video
def process_video():
    file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4 *.avi *.mkv")])
    if not file_path:
        return

    cap = cv2.VideoCapture(file_path)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        processed_frame, results, sleeping_count = process_frame(frame)

        # Display frame
        cv2.imshow("Processed Video", processed_frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


# GUI: Live webcam feed
def process_webcam():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        processed_frame, results, sleeping_count = process_frame(frame)

        # Display frame
        cv2.imshow("Live Webcam", processed_frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


# GUI: Main application
def main():
    root = tk.Tk()
    root.title("Drowsiness Detection")
    root.geometry("400x300")

    tk.Label(root, text="Drowsiness Detection System", font=("Helvetica", 16)).pack(pady=20)
    tk.Button(root, text="Process Image", command=process_image, width=20).pack(pady=10)
    tk.Button(root, text="Process Video", command=process_video, width=20).pack(pady=10)
    tk.Button(root, text="Live Webcam", command=process_webcam, width=20).pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()