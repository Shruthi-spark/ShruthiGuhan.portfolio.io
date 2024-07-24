import base64

with open("D:\my projects\Portfolio recent\IMG_20240611_234856.jpg", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode()

print(encoded_string)
