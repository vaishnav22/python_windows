import pytesseract

from PIL import Image

im = Image.open("ab.jpg")
text = pytesseract.image_to_string(im)
print(text)


