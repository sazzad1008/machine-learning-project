"""
Python entrypoint scaffold generated from notebook: face classifiction.ipynb
"""

def main() -> None:
    """Run this project entrypoint."""
    print("Run notebook logic from: face classifiction.ipynb")


if __name__ == "__main__":
    main()

# Notebook code reference:
# Cell 1
# import numpy as np
# import cv2
# import matplotlib
# from matplotlib import pyplot as plt
# %matplotlib inline
#
# Cell 2
# img=cv2.imread('./test_images/sharapova1.jpg')
# img.shape
#
# Cell 3
# plt.imshow(img)
#
# Cell 4
# gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#
# Cell 5
# plt.imshow(gray,cmap='gray')
#
# Cell 6
# faceclassifier=cv2.CascadeClassifier('./celbrity face/model/opencv/haarcascades/haarcascade_frontalface_default.xml')
# eyeclassifier=cv2.CascadeClassifier('./celbrity face/model/opencv/haarcascades/haarcascade_eye.xml')
#
# Cell 7
# face=faceclassifier.detectMultiScale(gray, 1.3, 5)
# face
#
# Cell 8
# (x,y,w,h)=face[0]
#
# Cell 9
# face_img=cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
#
# Cell 10
# plt.imshow(face_img)
#
# Cell 11
#  r=face_img[y:y+h, x:x+w]
#
# Cell 12
# plt.imshow(r)
#
# Cell 13
# cv2.destroyAllWindows()
#
# Cell 14
#
#
#  for x,y,w,h in face:
#     face_img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
#     roi_gray=gray[y:y+h,x:x+w]
#     roi_colr=face_img[y:y+h,x:x+w]
#     eyes=eyeclassifier.detectMultiScale(roi_gray)
#     for ex,ey,ew,eh in eyes:
#         cv2.rectangle(roi_colr,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
#
# Cell 15
# plt.imshow(roi_colr)
#
# Cell 16
# def classifier(imagepath):
#     img=cv2.imread(imagepath)
#     gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#     faces=faceclassifier.detectMultiScale(gray, 1.3, 5)
#     for (x,y,w,h) in faces:
#         face_img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
#         roi_gray=gray[y:y+h,x:x+w]
#         roi_colr=img[y:y+h,x:x+w]
#         eyes=eyeclassifier.detectMultiScale(roi_gray)
#         if len(eyes) >=2:
#             return roi_colr
#
# Cell 17
# cropped=classifier('./test_images/sharapova1.jpg')
# plt.imshow(cropped)
#
# Cell 18
# pp=cv2.imread('./test_images/sharapova1.jpg')
#
# Cell 19
# pathdata='.\\images_dataset'
# pathcrop='./datasets/cropped'
#
# Cell 20
# import os
# img_dirs = []
# for entry in os.scandir(pathdata):
#         img_dirs.append(entry.path)
#
# Cell 21
# img_dirs
#
#
# Cell 22
# import shutil
# if os.path.exists(pathcrop):
#     shutil.rmtree(pathcrop)
# os.mkdir(pathcrop)
#
# Cell 23
# for img_dir in img_dirs:
#     celebrityname=img_dir.split('/')[-1]
#     print(celebrityname)
#     for entry in os.scandir(img_dir):
#         print(entry.path)
#
#
# Cell 24
# cropped_image_dirs = []
# celebrity_file_names_dict = {}
#
# for img_dir in img_dirs:
#     count = 1
#     celebrity_name = img_dir.split('/')[-1]
#     print(celebrity_name)
#
#     celebrity_file_names_dict[celebrity_name] = []
#
#     for entry in os.scandir(img_dir):
#         roi_color = classifier(entry.path)
#         if roi_color is not None:
#             cropped_folder = pathcrop + celebrity_name
#             if not os.path.exists(cropped_folder):
#                 os.makedirs(cropped_folder)
#                 cropped_image_dirs.append(cropped_folder)
#                 print("Generating cropped images in folder: ",cropped_folder)
#
#             cropped_file_name = celebrity_name + str(count) + ".png"
#             cropped_file_path = cropped_folder + "/" + cropped_file_name
#
#             cv2.imwrite(cropped_file_path, roi_color)
#             celebrity_file_names_dict[celebrity_name].append(cropped_file_path)
#             count += 1
#
# Cell 25
# classifier('.\\images_dataset\lionel_messi\28003-1510231943.jpg')
#
# Cell 26
# cc=cv2.imread('./images_dataset/lionel_messi\136054219.jpg.0.jpg')
#
# Cell 27
# cc.shape
#
# Cell 28
# plt.imshow(cc)
#
# Cell 29
#
#
