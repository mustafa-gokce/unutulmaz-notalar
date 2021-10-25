import os.path

folder_old = "/home/m/Notalar/"
folder_new = "/home/m/pdfs/"

i = 1
while i < 15851:
    if os.path.exists("{0}{1}.png".format(folder_old, i)):
        print("Found:", i)
    elif os.path.exists("{0}{1}_1.png".format(folder_old, i)):
        j = 1
        pages = []
        while True:
            if os.path.exists("{0}{1}_{2}.png".format(folder_old, i, j)):
                pages.append(j)
            else:
                break
            j += 1
        print("Found:", i, pages)
    else:
        _ = 0
        print("Not found:", i)
    i += 1
