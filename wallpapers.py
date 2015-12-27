#importing vendor modules
from PIL import Image
import random, sys, os, math

#DONE
def colorToImageName(color, imageFormat):
    '''
    convert input color to imageName of input imageFormat
    '''
    imageName = ''
    for i in range(len(color)):
        if i == len(color) - 1:
            imageName += str(color[i]) + '.' + imageFormat
        else:
            imageName += str(color[i]) + '-'

    return imageName

#DONE
def createPixelTile(color, imageFormat):
    '''
    creating 1x1 pixel size tile based on input color
    '''
    os.chdir("c:/pythoncode/programs/wallpapergenerator/colors/pixel")

    imageHandle = Image.new('RGBA', (1, 1), color)
    imageName = colorToImageName(color, imageFormat)
    imageHandle.save(imageName)


#not working at all and code is obviously incorrect; but not in the mood right now...
def createTriangleTile(foregroundColor, backgroundColor):
    '''
    create image tile with triangle in foreground on the square backgroundColorImage
    '''
    os.chdir("c:/pythoncode/programs/wallpapergenerator/colors")

    imageBackgroundHandle = Image.open('background/' + colorToImageName(backgroundColorImage, 'jpg'))
    xLimit, yLimit = imageBackgroundHandle.size

    imageForegroundHandle = Image.open('pixel/' + colorToImageName(foregroundColorImage, 'jpg'))

    os.chdir("c:/pythoncode/programs/wallpapergenerator/colors/triangle/")

    for i in range(0, 1):
        if i == 0:
            a = 0
            b = 0
            start1 = 0
            end1 =  xLimit
            step1 = 1
            start2 = 0
            end2 = a
            step2 = 1
            p = a
            q = b

        elif i == 1:
            a = 0
            b = 0
            start1 = 0
            end1 = xLimit
            step1 = 1
            start2 = 0
            end2 = a
            step2 = 1
            p = a
            q = b

        elif i == 2:
            a = 0
            b = 0
            start1 = 0
            end1 = xLimit
            step1 = 1
            start2 = 0
            end2 = a
            step2 = 1
            p = a
            q = b

        else:
            a = 0
            b = 0
            start1 = 0
            end1 = xLimit
            step1 = 1
            start2 = 0
            end2 = a
            step2 = 1
            p = a
            q = b

        imageBackgroundCopyHandle = imageBackgroundHandle.copy()
        for a in range(start1, end1, step1):
            for b in range(start2, end2, step2):
                print(a, b, start1, end1, step1, start2, end2, step2, p, q)
                imageBackgroundCopyHandle.paste(imageForegroundHandle, (p, q))
        imageName = str(i+1) + '-' + colorToImageName(foregroundColorImage, 'jpg')[:-4] + '-' + colorToImageName(backgroundColorImage, 'jpg')
        imageBackgroundCopyHandle.save(imageName)

# to test createTriangleTiles()
# createTriangleTiles((194, 74, 74, 255), (48, 48, 48, 255))

#DONE
def createCircleTile(foregroundColor, backgroundColor, style):
    '''
    create image tile of input style in foregroundColor on the square backgroundColorImage
    '''
    os.chdir("c:/pythoncode/programs/wallpapergenerator/colors")

    imageBackgroundHandle = Image.open('background/' + colorToImageName(backgroundColor, 'jpg'))
    xLimit, yLimit = imageBackgroundHandle.size


    originsQuarterCircle = {'corner1' : {'xOrigin' : xLimit, 'yOrigin' : yLimit},
                            'corner2' : {'xOrigin' : 0, 'yOrigin' : yLimit},
                            'corner3' : {'xOrigin' : xLimit, 'yOrigin' : 0},
                            'corner4' : {'xOrigin' : 0, 'yOrigin' : 0}}

    originsSemiCircle = {'corner1' : {'xOrigin' : xLimit // 2, 'yOrigin' : 0},
                         'corner2' : {'xOrigin' : 0, 'yOrigin' : yLimit // 2},
                         'corner3' : {'xOrigin' : xLimit, 'yOrigin' : yLimit // 2},
                         'corner4' : {'xOrigin' : xLimit // 2, 'yOrigin' : yLimit}}

    for i in range(1, 5):
        imageBackgroundHandle = Image.open('background/' + colorToImageName(backgroundColor, 'jpg'))
        imageBackgroundCopyHandle = imageBackgroundHandle.copy()
        imageForegroundHandle = Image.open('pixel/' + colorToImageName(foregroundColor, 'jpg'))

        if style == 'quartercircle':
            xOrigin = originsQuarterCircle['corner' + str(i)]['xOrigin']
            yOrigin = originsQuarterCircle['corner' + str(i)]['yOrigin']

        elif style == 'semicircle':
            xOrigin = originsSemiCircle['corner' + str(i)]['xOrigin']
            yOrigin = originsSemiCircle['corner' + str(i)]['yOrigin']

        for y in range(yLimit):
            for x in range(xLimit):
                distance = int(pow((pow((x - xOrigin), 2) + pow((y - yOrigin), 2)), (1/2)))
                if (style == 'quartercircle' and distance <= xLimit) or (style == 'semicircle' and distance <= xLimit // 2):
                    imageBackgroundCopyHandle.paste(imageForegroundHandle, (x, y))


        imageName = str(i) + '-' + colorToImageName(foregroundColor, 'jpg')[:-4] + '-' + colorToImageName(backgroundColor, 'jpg')
        if style == 'quartercircle':
            imageBackgroundCopyHandle.save('quartercircle/' + imageName)
        elif style == 'semicircle':
            imageBackgroundCopyHandle.save('semicircle/' + imageName)



#DONE
def createSquareTile(xLimit, yLimit, color):
    '''
    create square image of input color of input dimensions
    '''
    os.chdir("c:/pythoncode/programs/wallpapergenerator/colors/background/")
    imageHandle = Image.new('RGBA', (xLimit, yLimit), color)

    imageName = ''
    for i in range(len(color)):
        if i == len(color) - 1:
            imageName += str(color[i]) + '.jpg'
        else:
            imageName += str(color[i]) + '-'

    imageHandle.save(imageName)

#DONE
def createCircleWallpaper(foregroundColor, backgroundColor, style, imageFormat):
    '''
    create wallpaper with of input style (quartercircle, semicircle) of input imageFormat based on input foregroundColor & backgroundColor tuples
    '''
    os.chdir("c:/pythoncode/programs/wallpapergenerator")

    imageWallpaperHandle = Image.new('RGBA', (1000, 1800))
    xLimit, yLimit = imageWallpaperHandle.size

    colorTiles = [None, None, None, None]
    for i in range(1, 5):
        filename = str(i) + '-' + colorToImageName(foregroundColor, imageFormat)[:-4] + '-' + colorToImageName(backgroundColor, imageFormat)
        if style == 'quartercircle':
            colorTiles[i-1] = Image.open('colors/quartercircle/' + filename)
        elif style == 'semicircle':
            colorTiles[i-1] = Image.open('colors/semicircle/' + filename)


    for y in range(0, yLimit, 100):
        for x in range(0, xLimit, 100):
            colorTile = random.randint(0, len(colorTiles) - 1)
            imageWallpaperHandle.paste(colorTiles[colorTile], (x, y))

    os.chdir("c:/pythoncode/programs/wallpapergenerator/output/mobile/")
    imageWallpaperName = colorToImageName(foregroundColor, imageFormat)[:-4] + '-' + colorToImageName(backgroundColor, imageFormat)[:-4]

    if style == 'quartercircle':
         imageWallpaperName += '-quartercircle.jpg'
    elif style == 'semicircle':
         imageWallpaperName += '-semicircle.jpg'

    imageWallpaperHandle.save(imageWallpaperName)


#DONE
def createTriangleWallpaper(foregroundColor, backgroundColor, imageFormat):
    '''
    create wallpaper with triangle tiles
    '''
    os.chdir("c:/pythoncode/programs/wallpapergenerator")

    imageWallpaperHandle = Image.new('RGBA', (1000, 1800))
    xLimit, yLimit = imageWallpaperHandle.size

    colorTiles = [None, None, None, None]
    for i in range(1, 5):
        filename = str(i) + '-' + colorToImageName(foregroundColor, imageFormat)[:-4] + '-' + colorToImageName(backgroundColor, imageFormat)
        colorTiles[i-1] = Image.open('colors/triangle/' + filename)

    for y in range(0, yLimit, 100):
        for x in range(0, xLimit, 100):
            colorTile = random.randint(0, len(colorTiles) - 1)
            imageWallpaperHandle.paste(colorTiles[colorTile], (x, y))

    os.chdir("c:/pythoncode/programs/wallpapergenerator/output/mobile/")
    imageWallpaperName = colorToImageName(foregroundColor, imageFormat)[:-4] + '-' + colorToImageName(backgroundColor, imageFormat)
    imageWallpaperHandle.save(imageWallpaperName)

#DONE
def createSquareWallpaper(foregroundColor, backgroundColor, imageFormat):
    '''
    create wallpaper with input foregroundColor & backgroundColor of specified imageFormat
    '''
    os.chdir("c:/pythoncode/programs/wallpapergenerator/colors/background/")

    imageWallpaperHandle = Image.new('RGBA', (1000, 1800))
    xLimit, yLimit = imageWallpaperHandle.size

    imageForegroundHandle = Image.open(colorToImageName(foregroundColor, imageFormat))

    imageBackgroundHandle = Image.open(colorToImageName(backgroundColor, imageFormat))

    colorTiles = [imageForegroundHandle, imageBackgroundHandle]
    for y in range(0, yLimit, 100):
        for x in range(0, xLimit, 100):
            colorTile = random.randint(0, len(colorTiles) - 1)
            imageWallpaperHandle.paste(colorTiles[colorTile], (x, y))

    os.chdir("c:/pythoncode/programs/wallpapergenerator/output/mobile/")
    imageWallpaperName = colorToImageName(foregroundColor, imageFormat)[:-4] + '-' + colorToImageName(backgroundColor, imageFormat)
    imageWallpaperHandle.save(imageWallpaperName)


#NOT FINISHED
def createRandomBurstWallpaper(backgroundColor, imageFormat):
    '''
    create wallpaper of input backgroundColor with randomly chosen foregroundColor(s) and styles of specified imageFormat
    '''
    os.chdir("c:/pythoncode/programs/wallpapergenerator/colors/")

    imageBackgroundHandle = Image.new('RGBA', (1000, 1800), backgroundColor)
    xLimit, yLimit = imageBackgroundHandle.size
