import argparse
import cv2
import glob
import os
from basicsr.archs.rrdbnet_arch import RRDBNet
from realesrgan import RealESRGANer

def main():
    """Modified Real-ESRGAN inference for anime video frames."""
    input_folder = r'C:\Users\kaise\OneDrive\Desktop\VISION\RESR\2.Video_Frames'
    output_folder = r'C:\Users\kaise\OneDrive\Desktop\VISION\RESR\3.Output_Frames'
    weights_path = r'C:\Users\kaise\OneDrive\Desktop\VISION\RESR\weights\RealESRGAN_x4plus_anime_6B.pth'
    # Model configuration for RealESRGAN_x4plus_anime_6B
    model = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64, num_block=6, num_grow_ch=32, scale=4)  #Residual in Residual Dense Block
    netscale = 4

    # Restorer setup
    upsampler = RealESRGANer(
        scale=netscale,
        model_path=weights_path,
        model=model,
        tile=0,          # Adjust tile size if memory issues arise
        tile_pad=10,
        pre_pad=0,
        half=True        # Use fp16 for faster inference
    )

    os.makedirs(output_folder, exist_ok=True)
    paths = sorted(glob.glob(os.path.join(input_folder, '*')))

    for idx, path in enumerate(paths):
        imgname, extension = os.path.splitext(os.path.basename(path))
        print(f'Processing frame {idx + 1}/{len(paths)}: {imgname}')

        img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
        if len(img.shape) == 3 and img.shape[2] == 4:
            img_mode = 'RGBA'
        else:
            img_mode = None

        try:
            output, _ = upsampler.enhance(img, outscale=4)
        except RuntimeError as error:
            print('Error:', error)
            print('If you encounter CUDA out of memory, try reducing the tile size.')
            continue

        save_path = os.path.join(output_folder, f'{imgname}_upscaled.png')
        cv2.imwrite(save_path, output)

if __name__ == '__main__':
    main()
