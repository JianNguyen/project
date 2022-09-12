import imageio
import os
import cv2

image_list = os.listdir(r'C:\Users\MVP\Downloads\data_0405-20220504T054811Z-001\data_0405\station_6_ng\bavia_ren')

train_img = [
    (r'C:\Users\MVP\Downloads\data_0405-20220504T054811Z-001\data_0405\station_6_ng\bavia_ren/' + file)
    for file in image_list]
#
# with imageio.get_writer(r'C:\Users\MVP\Desktop\hehe/hehe.gif', mode='I', duration=0.5) as writer:
#     for filename in train_img:
#         image = imageio.imread(filename)
#         writer.append_data(image)

# Here's the number you're looking for
# number_of_frames = len(gif)
count = 1
for path in train_img:
    gif = imageio.get_reader(uri=path, mode="I")
    for frame in gif:
        cv2.imwrite(fr'C:\Users\MVP\Desktop\hehe/{count}.jpg', frame)
        count += 1
    