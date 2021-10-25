import os
import pathlib

folder = "/home/m/Notalar/"
contents = list(pathlib.Path(folder).iterdir())

for content in contents:
    full_path_old = str(content.absolute())
    stem = content.stem
    suffix = content.suffix
    stem = stem.replace("-", "_")
    stem = stem.split("_")
    stem = "_".join([str(int(x)) for x in stem])
    full_path_new = str(pathlib.Path(folder + stem + suffix).absolute())
    os.rename(full_path_old, full_path_new)
    print(full_path_old, full_path_new)
