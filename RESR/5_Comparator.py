import cv2
import numpy as np
from skimage.metrics import peak_signal_noise_ratio as psnr
from skimage.metrics import structural_similarity as ssim
import pandas as pd
import time

def compare_videos(video_path1, video_path2, output_csv=None):
    # Open both videos
    cap1 = cv2.VideoCapture(video_path1)
    cap2 = cv2.VideoCapture(video_path2)

    if not cap1.isOpened() or not cap2.isOpened():
        print("Error: Unable to open one or both videos.")
        return

    # Ensure both videos have the same number of frames
    frame_count1 = int(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_count2 = int(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
    if frame_count1 != frame_count2:
        print("Warning: Videos have different frame counts!")

    # Initialize metrics
    psnr_values = []
    ssim_values = []
    mae_values = []
    frame_results = []

    # Start comparison
    start_time = time.time()
    frame_idx = 0

    while True:
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()

        # Break if either video ends
        if not ret1 or not ret2:
            break

        # Convert frames to grayscale for SSIM
        gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

        # Resize frames if dimensions don't match
        if frame1.shape != frame2.shape:
            frame2 = cv2.resize(frame2, (frame1.shape[1], frame1.shape[0]))
            gray2 = cv2.resize(gray2, (gray1.shape[1], gray1.shape[0]))

        # Compute PSNR
        psnr_value = psnr(frame1, frame2, data_range=255)
        psnr_values.append(psnr_value)

        # Compute SSIM
        ssim_value, _ = ssim(gray1, gray2, full=True)
        ssim_values.append(ssim_value)

        # Compute MAE
        mae_value = np.mean(np.abs(frame1.astype(np.float32) - frame2.astype(np.float32)))
        mae_values.append(mae_value)

        # Add results to table
        frame_results.append([frame_idx + 1, psnr_value, ssim_value, mae_value])

        frame_idx += 1

    # End comparison
    end_time = time.time()
    cap1.release()
    cap2.release()

    # Compute averages
    avg_psnr = np.mean(psnr_values)
    avg_ssim = np.mean(ssim_values)
    avg_mae = np.mean(mae_values)
    runtime = end_time - start_time

    # Print summary
    print(f"Frames compared: {frame_idx}")
    print(f"Average PSNR: {avg_psnr:.2f} dB")
    print(f"Average SSIM: {avg_ssim:.3f}")
    print(f"Average MAE: {avg_mae:.2f}")
    print(f"Comparison runtime: {runtime:.2f} seconds")

    # Save results to DataFrame and optionally to CSV
    columns = ["Frame", "PSNR (dB)", "SSIM", "MAE"]
    results_df = pd.DataFrame(frame_results, columns=columns)
    results_df.loc["Average"] = ["-", avg_psnr, avg_ssim, avg_mae]

    if output_csv:
        results_df.to_csv(output_csv, index=False)
        print(f"Frame-wise comparison saved to {output_csv}")

    # Display results
    print(results_df)

# Paths to videos
video_path1 = r"C:\Users\kaise\Downloads\Compare-1080.mp4"
video_path2 = r"C:\Users\kaise\OneDrive\Desktop\BE\MAJOR PROJECT\Main\Real-ESRGAN\Real-ESRGAN-master\4.Upscaled_Video\upscaled_video.mp4"
output_csv = r"C:\Users\kaise\OneDrive\Desktop\BE\MAJOR PROJECT\Main\Real-ESRGAN\Real-ESRGAN-master\5.Comparison\frame_comparison_1.csv"

# Run the comparison
compare_videos(video_path1, video_path2, output_csv)
