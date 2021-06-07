import cv2

import numpy as np

from matplotlib import pyplot as plt

from matplotlib.colors import Normalize

import matplotlib.cm as cm


def _main():
    # cut an image up into blocks of 8x8 pixels blocksize

    # print height and width

    # the image is cropped, such that its height and width is a multiple of blocksize

    B = 8

    fn3 = 'C:/Users/robjl/Documents/DKE 2020/Introduction to Image and Video Processing/Project_3/images/texas.jpg'

    img1 = cv2.imread(fn3, 0)

    h, w = np.array(img1.shape[:2]) // B * B

    print(h)

    print(w)

    img1 = img1[:h, :w]

    # run each block through an 8x8 2D Discrete Cosine Transform (cv2.dct())

    # the transformed image is stored in a variable (trans) and saved into the file 'transformed.jpg'

    blocksV = h // B

    blocksH = w // B

    vis0 = np.zeros((h, w), np.float32)

    trans = np.zeros((h, w), np.float32)

    vis0[:h, :w] = img1

    for row in range(blocksV):

        for col in range(blocksH):
            currentblock = cv2.dct(vis0[row * B:(row + 1) * B, col * B:(col + 1) * B])

            trans[row * B:(row + 1) * B, col * B:(col + 1) * B] = currentblock

    cv2.imwrite('transformed.jpg', trans)

    plt.imshow(img1, cmap="gray")

    point = plt.ginput(1)

    block = np.floor(np.array(point) / B)  # first component is col, second component is row

    print(block)

    col = block[0, 0]

    row = block[0, 1]

    plt.plot([B * col, B * col + B, B * col + B, B * col, B * col],
             [B * row, B * row, B * row + B, B * row + B, B * row])

    plt.axis([0, w, h, 0])

    plt.title("Original Image")

    # the selected block and its DCT-transform are then plotted into a second Matplotlib-figure

    plt.figure()

    plt.subplot(1, 2, 1)

    selectedImg = img1[row * B:(row + 1) * B, col * B:(col + 1) * B]

    N255 = Normalize(0, 255)  # Normalization object, used by imshow()

    plt.imshow(selectedImg, cmap="gray", norm=N255, interpolation='nearest')

    plt.title("Image in selected Region")

    plt.subplot(1, 2, 2)

    selectedTrans = trans[row * B:(row + 1) * B, col * B:(col + 1) * B]

    plt.imshow(selectedTrans, cmap=cm.jet, interpolation='nearest')

    plt.colorbar(shrink=0.5)

    plt.title("DCT transform of selected Region")

    # the IDCT is applied to reconstruct the original image from the transformed representation.

    # the reconstructed image is stored in the variable back0 and it is saved to the file 'BackTransformed.jpg'

    # rebuild an image in the spatial domain from the frequencies obtained

    back0 = np.zeros((h, w), np.float32)

    for row in range(blocksV):

        for col in range(blocksH):
            currentblock = cv2.idct(trans[row * B:(row + 1) * B, col * B:(col + 1) * B])

            back0[row * B:(row + 1) * B, col * B:(col + 1) * B] = currentblock

    cv2.imwrite('BackTransformed.jpg', back0)

    # verify that DCT and IDCT are lossless, the Mean Absolute Difference (MAD) between the original and the reconstructed image is calculated and printed to the console

    diff = back0 - img1

    print(diff.max())

    print(diff.min())

    MAD = np.sum(np.abs(diff)) / float(h * w)

    print("Mean Absolute Difference: ", MAD)

    plt.figure()

    plt.imshow(back0, cmap="gray")

    plt.title("Backtransformed Image")

    plt.show()


if __name__ == '__main__':
    _main()
