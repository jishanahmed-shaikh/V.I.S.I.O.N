import cv2
import os

def get_video_frame_count(video_path):
    """Calculate and return the total number of frames in the video."""
    video = cv2.VideoCapture(video_path)
    if not video.isOpened():
        print(f"Error: Cannot open video file at {video_path}")
        return 0

    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))  # Get total frame count
    video.release()
    return frame_count

# Function to get frame rate of a video
def get_video_fps(video_path):
    video = cv2.VideoCapture(video_path)
    if not video.isOpened():
        print(f"Error: Cannot open video file at {video_path}")
        return None

    fps = video.get(cv2.CAP_PROP_FPS)  # Get FPS
    video.release()
    return fps

# Example usage
video_path = r"C:\Users\kaise\OneDrive\Desktop\VISION\RESR\1.Input_Video\input.mp4"  # Replace with your video path
fps = get_video_fps(video_path)

if fps:
    print(f"Frame Rate: {fps} FPS")


def split_video_into_frames(input_video_path, output_frames_folder):
    """Split video into frames and save them as images."""
    
    # Calculate total frames first
    total_frames = get_video_frame_count(input_video_path)
    if total_frames == 0:
        print("Error: Could not retrieve frame count.")
        return

    print(f"Total frames in video: {total_frames}")

    # Check if output folder exists, if not, create it
    os.makedirs(output_frames_folder, exist_ok=True)

    # Open the video file
    video = cv2.VideoCapture(input_video_path)

    if not video.isOpened():
        print(f"Error: Cannot open video file at {input_video_path}")
        return

    frame_count = 0

    # Read frames from the video
    while frame_count < total_frames:
        success, frame = video.read()
        if not success:
            break

        # Save each frame as an image file
        frame_filename = os.path.join(output_frames_folder, f"frame_{frame_count:04d}.png")
        cv2.imwrite(frame_filename, frame)
        frame_count += 1

    # Release the video capture object
    video.release()
    print(f"Successfully saved {frame_count}/{total_frames} frames to {output_frames_folder}")

# Paths for input video and output frames
input_video_folder = r"C:\Users\kaise\OneDrive\Desktop\VISION\RESR\1.Input_Video"
output_frames_folder = r"C:\Users\kaise\OneDrive\Desktop\VISION\RESR\2.Video_Frames"

# Find the first video file in the folder
input_video_file = None
for file in os.listdir(input_video_folder):
    if file.endswith(('.mp4', '.avi', '.mkv', '.mov')):
        input_video_file = os.path.join(input_video_folder, file)
        break

if input_video_file:
    split_video_into_frames(input_video_file, output_frames_folder)
else:
    print(f"No video files found in {input_video_folder}")
