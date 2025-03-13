import cv2
import os
import glob

def get_video_fps(video_path):
    """Calculate and return the frame rate (FPS) of the input video."""
    video = cv2.VideoCapture(video_path)
    if not video.isOpened():
        print(f"Error: Cannot open video file at {video_path}")
        return None

    fps = int(video.get(cv2.CAP_PROP_FPS))  # Get FPS and convert to integer
    video.release()
    return fps

def frames_to_video(input_folder, output_video_path, fps):
    """Combine image frames into a video with a dynamically set FPS."""
    
    images = sorted(glob.glob(os.path.join(input_folder, '*.*')))
    if not images:
        print("No images found in the input folder!")
        return

    frame = cv2.imread(images[0])
    if frame is None:
        print(f"Error reading image: {images[0]}")
        return

    height, width, layers = frame.shape
    video_writer = cv2.VideoWriter(
        output_video_path,
        cv2.VideoWriter_fourcc(*'mp4v'),  # Use 'mp4v' codec for .mp4 videos
        fps,  # Dynamically set FPS
        (width, height)
    )

    for img_path in images:
        frame = cv2.imread(img_path)
        if frame is None:
            print(f"Skipping unreadable image: {img_path}")
            continue
        video_writer.write(frame)

    video_writer.release()
    print(f"Video saved to: {output_video_path} at {fps} FPS")


# Paths
input_video_folder = r"C:\Users\kaise\OneDrive\Desktop\VISION\RESR\1.Input_Video"
input_frames_folder = r"C:\Users\kaise\OneDrive\Desktop\VISION\RESR\3.Output_Frames"
output_video_path = r"C:\Users\kaise\OneDrive\Desktop\VISION\RESR\4.Upscaled_Video\upscaled_video_chirag.mp4"

# Find the first video file in the input folder
input_video_file = None
for file in os.listdir(input_video_folder):
    if file.endswith(('.mp4', '.avi', '.mkv', '.mov')):
        input_video_file = os.path.join(input_video_folder, file)
        break

if input_video_file:
    fps = get_video_fps(input_video_file)  # Get FPS dynamically
    if fps:
        print(f"Using dynamically calculated FPS: {fps}")
        frames_to_video(input_frames_folder, output_video_path, fps)
    else:
        print("Error: Could not determine FPS. Using default FPS = 30.")
        frames_to_video(input_frames_folder, output_video_path, fps=30)
else:
    print("No video files found in the input folder!")
