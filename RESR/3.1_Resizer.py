import cv2

# Paths
input_video = r"C:\Users\kaise\OneDrive\Desktop\VISION\RESR\4.Upscaled_Video\upscaled_video_1.mp4"
output_video = r"C:\Users\kaise\OneDrive\Desktop\VISION\RESR\5.Resized\upscaled_video_resized_1.mp4"

# Target resolution
target_width = 1920
target_height = 1080

# Open video file
cap = cv2.VideoCapture(input_video)

# Get original FPS
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 'mp4v' codec for MP4
out = cv2.VideoWriter(output_video, fourcc, fps, (target_width, target_height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # Exit when video ends

    # Resize frame to 1920x1080
    resized_frame = cv2.resize(frame, (target_width, target_height))

    # Write frame to output video
    out.write(resized_frame)

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()

print("✅ Video has been resized to 1920x1080 and saved as:", output_video)
