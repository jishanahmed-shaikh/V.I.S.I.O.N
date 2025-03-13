import cv2
import numpy as np
import os

# Paths to the two videos
video_path1 = r"C:\Users\kaise\OneDrive\Desktop\VISION\RESR\5.Resized\upscaled_video_resized_1.mp4"  # Original 30 FPS
video_path2 = r"C:\Users\kaise\OneDrive\Desktop\VISION\RESR\8.Interpolated\Interpolated_real.mp4"  # RIFE 120 FPS
# Output video path
output_folder = r"C:\Users\kaise\OneDrive\Desktop\VISION\RESR\9.Interpolated_Comparison_real"
output_video_path = os.path.join(output_folder, "comparison 30v120 4xslow.mp4")

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Open both videos
cap1 = cv2.VideoCapture(video_path1)  # 30 FPS
cap2 = cv2.VideoCapture(video_path2)  # 120 FPS

# Get FPS and frame size
fps1 = int(cap1.get(cv2.CAP_PROP_FPS))  # 30
fps2 = int(cap2.get(cv2.CAP_PROP_FPS))  # 120
frame_width1 = int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height1 = int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_width2 = int(cap2.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height2 = int(cap2.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Ensure both videos open correctly
if not cap1.isOpened() or not cap2.isOpened():
    print("Error: Unable to open one or both video files.")
    exit()

# Set frame size to match the larger video
frame_size = (max(frame_width1, frame_width2), max(frame_height1, frame_height2))

# Video writer setup
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for MP4
output_fps = fps2  # Use 120 FPS for smooth playback
video_writer = cv2.VideoWriter(output_video_path, fourcc, output_fps, (frame_size[0] * 2, frame_size[1]))

frame1 = None  # Store last frame of 30 FPS video
frame_count_30fps = 0  # Frame counter for 30 FPS video
frame_count_120fps = 0  # Frame counter for 120 FPS video

while True:
    if frame_count_120fps % 4 == 0:  # Get a new frame from 30 FPS video every 4th frame
        ret1, frame1 = cap1.read()
        if not ret1:
            break
        frame_count_30fps += 1  # Increase frame count for 30 FPS

    ret2, frame2 = cap2.read()  # Get a new frame from 120 FPS video

    if not ret2:
        break  # Stop if second video ends

    frame_count_120fps += 1  # Increase frame count for 120 FPS

    # Resize both frames to match the largest frame size
    frame1_resized = cv2.resize(frame1, frame_size)
    frame2_resized = cv2.resize(frame2, frame_size)

    # Concatenate frames side by side
    combined_frame = np.hstack((frame1_resized, frame2_resized))

    # Add titles
    title1 = "Upscaled 30 FPS Video"
    title2 = "Upscaled+Interpolated 120 FPS Video"

    # Text settings
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1.2
    font_thickness = 3
    text_color = (255, 255, 255)

    # Put text on the first frame
    cv2.putText(combined_frame, title1, (50, 50), font, font_scale, text_color, font_thickness)

    # Put text on the second frame
    cv2.putText(combined_frame, title2, (frame_size[0] + 50, 50), font, font_scale, text_color, font_thickness)

    # **Frame Number for 30 FPS Video (Top Right of Left Video)**
    frame_number_text_30 = f"Frame: {frame_count_30fps}"
    text_size_30 = cv2.getTextSize(frame_number_text_30, font, 1.2, 3)[0]  # Get text size
    text_x_30 = frame_size[0] - text_size_30[0] - 20  # Align to right
    text_y_30 = 80  # Position below top edge
    cv2.putText(combined_frame, frame_number_text_30, (text_x_30, text_y_30), font, 1.2, (0, 255, 0), 3)

    # **Frame Number for 120 FPS Video (Top Right of Right Video)**
    frame_number_text_120 = f"Frame: {frame_count_120fps}"
    text_size_120 = cv2.getTextSize(frame_number_text_120, font, 1.2, 3)[0]  # Get text size
    text_x_120 = (frame_size[0] * 2) - text_size_120[0] - 20  # Align to right
    text_y_120 = 80  # Position below top edge
    cv2.putText(combined_frame, frame_number_text_120, (text_x_120, text_y_120), font, 1.2, (0, 255, 255), 3)

    # Write frame to output video
    video_writer.write(combined_frame)

    # Display the combined video
    cv2.imshow("FPS Comparison: 30 FPS vs. 120 FPS", combined_frame)

    # Use 120 FPS timing to keep playback smooth
    wait_time = int(1000 / (fps2 / 4))
    if cv2.waitKey(wait_time) & 0xFF == ord('q'):
        break

# Release resources
cap1.release()
cap2.release()
video_writer.release()
cv2.destroyAllWindows()

print(f"✅ Video saved successfully: {output_video_path}")
