import cv2
import numpy as np
import os

# Paths to videos
video_path1 = r"C:\Users\kaise\Downloads\1080_real.mp4"  # Input 480p video
video_path2 = r"C:\Users\kaise\OneDrive\Desktop\VISION\RESR\8.Interpolated\Interpolated_real.mp4"  # Output 1080p video

# Output video path
output_folder = r"C:\Users\kaise\OneDrive\Desktop\VISION\RESR\6.Upscaled_Comparison_real"
output_video_path = os.path.join(output_folder, "comparison.mp4")

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Open both videos
cap1 = cv2.VideoCapture(video_path1)
cap2 = cv2.VideoCapture(video_path2)

# Get video properties
fps1 = int(cap1.get(cv2.CAP_PROP_FPS))
fps2 = int(cap2.get(cv2.CAP_PROP_FPS))
frame_width1 = int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height1 = int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))

frame_width2 = int(cap2.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height2 = int(cap2.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Ensure both videos open correctly
if not cap1.isOpened() or not cap2.isOpened():
    print("Error: Unable to open one or both video files.")
    exit()

# Set video frame size (match larger resolution)
frame_size = (max(frame_width1, frame_width2), max(frame_height1, frame_height2))

# Video writer setup
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for MP4
output_fps = max(fps1, fps2)  # Use the highest FPS between the two videos
video_writer = cv2.VideoWriter(output_video_path, fourcc, output_fps, (frame_size[0] * 2, frame_size[1]))

while True:
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    if not ret1 or not ret2:
        break  # Stop if either video ends

    # Resize frames to match the larger frame size
    frame1 = cv2.resize(frame1, frame_size)
    frame2 = cv2.resize(frame2, frame_size)

    # Concatenate frames horizontally
    combined_frame = np.hstack((frame1, frame2))

    # Add titles
    title1 = "Source 1080p Video"
    title2 = "Our upscaled 1080p Video"

    # Draw titles on the frames
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_thickness = 2
    text_color = (255, 255, 255)

    # Put text on the first frame
    cv2.putText(combined_frame, title1, (100, 100), font, font_scale, text_color, font_thickness)
    
    # Put text on the second frame
    cv2.putText(combined_frame, title2, (frame_size[0] + 100, 100), font, font_scale, text_color, font_thickness)

    # Write frame to output video
    video_writer.write(combined_frame)

    # Display the combined frame
    cv2.imshow("Video Comparison: Input vs. Output", combined_frame)

    # Wait for key press, exit on 'q'
    if cv2.waitKey(int(1000 / output_fps)) & 0xFF == ord('q'):
        break

# Release resources
cap1.release()
cap2.release()
video_writer.release()
cv2.destroyAllWindows()

print(f"✅ Video saved successfully: {output_video_path}")
