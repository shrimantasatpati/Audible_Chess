from PIL import Image
import pyautogui as pg
import sys
sys.path.insert(1, '../models/')
from chessboard_finder import *


def getCorners(img):
    print("Loading img %s..." % img)
    color_img = Image.open(img)

    # Fail if can't load image
    if color_img is None:
        print('Couldn\'t load image: %s' % img)
        return

    if color_img.mode != 'RGB':
        color_img = color_img.convert('RGB')
    print("Processing...")
    a = time()
    img_arr = np.asarray(color_img.convert("L"), dtype=np.float32)
    corners = findChessboardCorners(img_arr)
    print("Took %.4fs" % (time()-a))
    # corners = [x0, y0, x1, y1] where (x0,y0)
    # is top left and (x1,y1) is bot right

    if corners is not None:
        print("Found corners for %s: %s" % (img, corners))
        link = getVisualizeLink(corners, img)
        # print(link)
        return corners
    else:
        print('No corners found in image')
        print("Please open the the board properly")
        return None


def getAllCoordinates(imgName):
    '''returns corrdinates of all tiles in dictionary format'''
    corners = getCorners(str(imgName))
    # print(corners)

    # 01 --> top left corner
    # 12 --> nothing
    # 23 --> right bottom corner
    # 03 -->  left bottom corner
    if corners is None:
        return corners
    else:
        edge = corners[3] - corners[1]
        # print(edge)

        tile = edge/8
        tile_mid = tile/2

        Y = corners[1] + tile_mid
        # print(Y)

        allCoordinates = {}
        for i in range(8, 0, -1):  # rank
            X = corners[0] + tile_mid
            for j in range(0, 8):  # file
                pos = chr(97+j) + str(i)
                allCoordinates[pos] = (X, Y)
                X = X + tile
            Y = Y + tile
        return allCoordinates



# myDict = {}
# c = 1
# d = 1
# ls = []
# c = 1
# d = 8
# while True:
#     if d == 0:
#         break
#     state = win32api.GetKeyState(0x01)

#     if state < 0:  # if mouse left button is pressed
#         ls.append(p.position())

#     if state == 0 or state == 1:
#         if len(ls) != 0:
#             a = ls[-1].x, ls[-1].y

#             if c > 8:
#                 c = 1
#                 d -= 1
#             c += 1
#             ls = []
#             b = chr(95+c) + str(d)
#             myDict[b] = a

#     else:  # if mouse left button is not pressed
#         pass

# print(myDict)