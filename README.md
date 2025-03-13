# V.I.S.I.O.N
V.I.S.I.O.N - Video Interpolation &amp; Super-Resolution  for Intelligent Optimization in Neural Processing


This is a work in progress project... so bear with me till I have everything in order. 
Note that I am primarily working on optimization of the pipeline. 

The credit for Real ESRGAN (Enhanced Super Resolution Generative Adversarial Netwrork) goes to the owners(s) of the following repository:
https://github.com/xinntao/Real-ESRGAN

The credit for RIFE (Real Time Intermediate Flow Estimation) goes to the owner(s) of the following repository:
https://github.com/hzwer/ECCV2022-RIFE

I will try my best to upload everything in such a manner that this becomes a quick download and run project along with all necessary and generalized Documentation!
Along with any issues that I faced in the time I built this project.

Link to Weights:
https://drive.google.com/drive/folders/1FsvxalXW-f3zsypSa8n8r0hq7SNhFO0M?usp=drive_link

simply download the following weights and paste into RESR/weights:
RealESRGAN_x4plus.pth
RealESRGAN_x4plus_anime_6B.pth

I am currently working on making the inputs dynamic in nature. Right now the path of folders is hardcoded into the scripts.
Please change the paths according to your system directory to ensure that it works correctly.

also download the following and paste into the RIFE/train_log folder:
flownet.pkl
IFNet_HDv3.py
refine.py
RIFE_HDv3.py

If anyone has any issues. You may reach out to me at: kaiser.momin47@gmail.com

