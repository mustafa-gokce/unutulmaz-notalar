import os
import pathlib
import cv2

folder_old = "/home/m/ZANotalar/Notalar/"
folder_new = "/home/m/Notalar/"
contents = list(pathlib.Path(folder_old).iterdir())

for content in contents:
    full_path_old = str(content.absolute())
    stem = content.stem
    suffix = content.suffix
    if suffix == ".tif":
        full_path_new = str(pathlib.Path(folder_new + stem + ".png").absolute())
        if not os.path.exists(full_path_new):
            image = cv2.imread(full_path_old)
            cv2.imwrite(full_path_new, image)
            print("Processed:", full_path_new)
        else:
            print("Already processed:", full_path_new)
    else:
        print("Error:", full_path_old)
