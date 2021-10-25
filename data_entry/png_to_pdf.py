import os.path
import PIL.Image

folder_old = "/home/m/Notalar/"
folder_new = "/home/m/pdfs/"

i = 1
while i < 15851:

    if os.path.exists("{0}{1}.pdf".format(folder_new, i)):
        print("Already converted:", i)
    else:

        if os.path.exists("{0}{1}.png".format(folder_old, i)):
            print("Found:", i)
            image = PIL.Image.open("{0}{1}.png".format(folder_old, i))
            image = image.convert("RGB")
            image.save("{0}{1}.pdf".format(folder_new, i))
        elif os.path.exists("{0}{1}_1.png".format(folder_old, i)):
            j = 1
            pages = []
            images = []
            while True:
                if os.path.exists("{0}{1}_{2}.png".format(folder_old, i, j)):
                    pages.append(j)
                    image = PIL.Image.open("{0}{1}_{2}.png".format(folder_old, i, j))
                    image = image.convert("RGB")
                    images.append(image)
                else:
                    break
                j += 1
            print("Found:", i, pages)
            images[0].save("{0}{1}.pdf".format(folder_new, i), save_all=True, append_images=images[1:])
        else:
            print("Not found:", i)

    i += 1
