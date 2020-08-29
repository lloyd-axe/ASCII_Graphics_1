import PIL.Image
#acii chars - in decending order in intensity
ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]

#resize image
def resize_img(image, new_width=100):
    width, height = image.size
    img_ratio =  height/width
    new_height = int(new_width * img_ratio)
    rez_img = image.resize((new_width, new_height))
    return rez_img

#conver to grayscale
def grayify(image):
    grayscale_img = image.convert("L")
    return grayscale_img

#convert pixels to string
def p_to_a(image):
    pixels = image.getdata()
    chars = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return chars

def main(new_width = 100):
    #attemp to open image
    path = input("Enter Image\n")
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "is not valid")

    #convert image to ascii
    new_image_data = p_to_a(grayify(resize_img(image)))

    #format
    pixel_count = len(new_image_data)
    ascii_img = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))

    #print
    print(ascii_img)

    #save
    with open("ascii_img.txt", "w") as f:
        f.write(ascii_img)

main()
