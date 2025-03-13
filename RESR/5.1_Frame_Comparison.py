import cv2
import numpy as np
from skimage.metrics import peak_signal_noise_ratio as psnr
from skimage.metrics import structural_similarity as ssim

def compare_frames_with_metrics(frame1_path, frame2_path, output_path=None):
    """
    Compare two frames by displaying them side by side with PSNR and SSIM values.

    Parameters:
        frame1_path (str): Path to the first frame (image).
        frame2_path (str): Path to the second frame (image).
        output_path (str, optional): Path to save the side-by-side comparison image.
    """
    # Load the two frames
    frame1 = cv2.imread(frame1_path)
    frame2 = cv2.imread(frame2_path)

    # Check if frames are loaded successfully
    if frame1 is None or frame2 is None:
        print("Error: Could not load one or both frames. Check the file paths.")
        return

    # Resize frames to the same dimensions if they differ
    if frame1.shape != frame2.shape:
        height, width = frame1.shape[:2]
        frame2 = cv2.resize(frame2, (width, height))

    # Convert frames to grayscale for SSIM calculation
    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    # Calculate PSNR and SSIM
    psnr_value = psnr(frame1, frame2, data_range=255)
    ssim_value, _ = ssim(gray1, gray2, full=True)

    # Concatenate the frames side by side
    combined_frame = np.hstack((frame1, frame2))

    # Add PSNR and SSIM text to the combined frame
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.8
    color = (0, 255, 0)  # Green text
    thickness = 2

    text = f"PSNR: {psnr_value:.2f} dB, SSIM: {ssim_value:.3f}"
    combined_frame = cv2.putText(combined_frame, text, (10, 30), font, font_scale, color, thickness, cv2.LINE_AA)

    # Display the combined frame
    cv2.imshow("Frame Comparison with Metrics", combined_frame)

    # Save the combined frame if an output path is provided
    if output_path:
        cv2.imwrite(output_path, combined_frame)
        print(f"Comparison saved to {output_path}")

    # Wait for a key press and close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Paths to the two frames
frame1_path = r"C:\Users\kaise\OneDrive\Desktop\VISION\RESR\2.Video_Frames\frame_0469.png"
frame2_path = r"C:\Users\kaise\OneDrive\Desktop\VISION\RESR\3.Output_Frames\frame_0469_upscaled.png"

# Optional: Path to save the output comparison image
output_path = r"C:\Users\kaise\OneDrive\Desktop\VISION\RESR\7.Frame Comparison\Frame_Comparison_chirag.png"

# Compare the frames and display metrics
compare_frames_with_metrics(frame1_path, frame2_path, output_path)
