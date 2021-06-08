''' Load an image from file and print as ASCII art to the screen! '''
import numpy as np
import pygame as pg

## Pre-calculated values:

# Dimensions of a single, fixed-width character:
# (determined for Courier New: cour.ttf)
char_width = 12
char_height = 20
char_hw_ratio = char_height / char_width

# A list of characters that you can use in your ASCII art...
characters = ['M', 'W', 'Q', 'B', 'E', 'R', 'N', '@', 'H', 'q', 'p', 'g', 'K', 'A', '#', 'm', 'b', '8', '0', 'd', 'X',
              'D', 'G', 'F', 'P', 'e', 'h', 'U', '9', '6', 'k', 'Z', '%', 'S', '4', 'O', 'x', 'y', 'T', '5', 'w', 'f',
              'a', 'V', 's',
              '2', 'L', '$', 'Y', '&', 'n', '3', 'C', 'J', 'u', 'o', 'z', 'I', 'j', 'v', 'c', 'r', 't', 'l', 'i', '1',
              '=', '?', '7', '>', '<', ']', '[', '(', ')', '+', '*', ';', '}', '{', ':', '/', '\\', '!', '|', '_', ',',
              '^', '-', '~', '.', ' ']
n_characters = len(characters)

# ... and the corresponding grayscale values
grayscale = np.array([217.56944444, 218.82291667, 219.89236111, 220.19444444,
                      222.14583333, 222.94097222, 223.0625, 223.17361111,
                      223.22222222, 223.23958333, 223.45486111, 223.60416667,
                      224.05208333, 224.09722222, 224.33333333, 225.25,
                      225.59722222, 225.62152778, 225.91666667, 225.96180556,
                      226.10763889, 226.74305556, 226.80208333, 227.04861111,
                      227.42361111, 228.45833333, 228.61458333, 228.73958333,
                      228.76736111, 228.80555556, 228.8125, 228.90625,
                      228.98611111, 229.06597222, 229.28472222, 229.61805556,
                      229.96527778, 230.07291667, 230.17361111, 230.21875,
                      230.60416667, 230.62847222, 230.84375, 231.03472222,
                      231.05555556, 231.46875, 231.55555556, 231.9375,
                      232.04861111, 232.07291667, 232.64583333, 232.68055556,
                      233.16319444, 233.53472222, 233.70138889, 234.20833333,
                      234.40625, 234.76388889, 234.93055556, 235.30208333,
                      235.36805556, 235.44791667, 235.5, 236.53472222,
                      237.32986111, 237.67361111, 237.70138889, 238.61458333,
                      238.61805556, 238.78125, 238.78472222, 238.79166667,
                      238.98611111, 239.07638889, 239.08680556, 239.97569444,
                      240.32291667, 240.78125, 241.50694444, 241.57291667,
                      243.13194444, 243.18055556, 243.31944444,
                      244.30208333, 244.61805556, 245.03819444, 246.62847222,
                      247.58333333, 247.60763889, 248.62847222, 255.00000000])


# Start writing your code here!


# Resize the image according to its new width and height (using the variables provided to us above
# Maybe i will skip it for now

# Convert the image to grayscale
def grayscale_converter(image):
    arr = pg.surfarray.array3d(image)
    # luminosity filter
    avgs = [[(r * 0.298 + g * 0.587 + b * 0.114) for (r, g, b) in col] for col in arr]
    arr = np.array([[[avg, avg, avg] for avg in col] for col in avgs])
    return pg.surfarray.make_surface(arr)


# Converting each pixel to a string of ASCII characters
def get_char_for_value(val, min_val, max_val, char_list, char_grayscale):
    # The height to width ratio given to us in the template is 20/12.
    # Given that our chosen patch width is 6, this ration yields us 10 for th e patch height
    patch_width = 6
    patch_height = 10
    # I am assuming we cannot use patchify :/ otherwise this would be a bag

    ind = 0
    return char_list[ind]


def _main():
    pg.init()

    path = "images/asciiart.png"

    try:
        image = pg.image.load(path)
    except:
        print(path, " is not a valid path for the image")

    window = (900, 700)
    screen = pg.display.set_mode(window)

    image = grayscale_converter(image)

    screen.blit(image, (100, 100))

    pg.display.flip()
    done = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

    pg.quit()


if __name__ == '__main__':
    _main()
