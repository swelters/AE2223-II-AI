import os
import pandas as pd
import cv2

train_folder = 'C:/Users/sebas/OneDrive - Delft University of Technology/GitHub/AE2223-II-AI/Train.pill.big-1'

dirs = os.listdir(train_folder)

images = []
labels = []
counter = 0

for _dir in dirs:
    filename, file_extension = os.path.splitext(_dir)
    if file_extension:
        continue
    files = sorted(os.listdir(os.path.join(train_folder, _dir)))
    counter = 0
    for _file in files:
        # if counter >= 130:
        #     break
        filename, file_extension = os.path.splitext(_file)
        # if file_extension == '.png':
        #     continue
        images.append(os.path.join(_dir, _file).replace("\\", "/"))
        labels.append(_dir)
        counter += 1

df = pd.DataFrame({'images': images,
                   'labels': labels
                   })

df.to_csv(os.path.join(train_folder, 'data.cvs'), header=["images", "labels"], index=False)
