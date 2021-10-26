import pathlib
import cv2


def overlay_transparent(bg_img, img_to_overlay_t):
    # Extract the alpha mask of the RGBA image, convert to RGB
    b, g, r, a = cv2.split(img_to_overlay_t)
    overlay_color = cv2.merge((b, g, r))

    mask = cv2.medianBlur(a, 5)

    # Black-out the area behind the logo in our original ROI
    img1_bg = cv2.bitwise_and(bg_img.copy(), bg_img.copy(), mask=cv2.bitwise_not(mask))

    # Mask out the logo from the logo image.
    img2_fg = cv2.bitwise_and(overlay_color, overlay_color, mask=mask)

    # Update the original image with our new ROI
    bg_img = cv2.add(img1_bg, img2_fg)

    return bg_img


folder = "/home/m/Notalar/"
contents = list(pathlib.Path(folder).iterdir())
overlay_t = cv2.imread("watermark.png", -1)

for content in contents:
    full_path = str(content.absolute())
    img = cv2.imread(full_path)
    cv2.imwrite(full_path, overlay_transparent(img, overlay_t))
    print(full_path)
