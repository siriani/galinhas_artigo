import moviepy
from moviepy.editor import *

#combine video clips

clip1 = VideoFileClip("pD17_C1_vermelho_20190502153000_1005_1.avi")
clip2 = VideoFileClip("pD17_C2_branco_20190502153000_1005_2.avi")
clip3 = VideoFileClip("pD17_C3_verde_20190502153000_1005_3.avi")

final_clip = clips_array([[clip1,clip2,clip3]])

final_clip.write_videofile("final_clip.mp4")

