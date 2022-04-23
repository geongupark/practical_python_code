from PIL import Image

# image open
target_image = Image.open("dog1.jpg")

# new size, should be int
new_height = int(target_image.height * 0.5)
new_width = int(target_image.width * 0.5)

# resize the image
target_image_resize = target_image.resize((new_height, new_width))
target_image_resize.save("dog_copy1.jpg")
