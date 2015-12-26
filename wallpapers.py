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
def createPixelTiles(color, imageFormat):
    '''
    creating 1x1 pixel size tiles based on input color
    '''
    os.chdir("c:/pythoncode/programs/wallpapergenerator/colors/pixel")

    imageHandle = Image.new('RGBA', (1, 1), color)
    imageName = colorToImageName(color, imageFormat)
    imageHandle.save(imageName)


#producing same images as before; conditions not working; code too repetitive
def createTriangleTiles(foregroundColorImage, backgroundColorImage):
    '''
    create image tile with triangle in foreground on the square backgroundColorImage
    '''
    os.chdir("c:/pythoncode/programs/wallpapergenerator/colors")

    imageBackgroundHandle = Image.open('background/' + backgroundColorImage)
    xLimit, yLimit = imageBackgroundHandle.size

    imageForegroundHandle = Image.open('pixel/' + foregroundColorImage)

    os.chdir("c:/pythoncode/programs/wallpapergenerator/colors/triangle/")

    imageBackgroundCopyHandle = imageBackgroundHandle.copy()
    for y in range(yLimit):
        for x in range(y):
            imageBackgroundCopyHandle.paste(imageForegroundHandle, (x, y))
    imageName = '1-' + foregroundColorImage[:-4] + '-' + backgroundColorImage
    imageBackgroundCopyHandle.save(imageName)

    imageBackgroundCopyHandle = imageBackgroundHandle.copy()
    for x in range(xLimit):
        for y in range(x):
            imageBackgroundCopyHandle.paste(imageForegroundHandle, (x, y))
    imageName = '2-' + foregroundColorImage[:-4] + '-' + backgroundColorImage
    imageBackgroundCopyHandle.save(imageName)

    imageBackgroundCopyHandle = imageBackgroundHandle.copy()
    for x in range(xLimit, -1, -1):
        for y in range(x):
            imageBackgroundCopyHandle.paste(imageForegroundHandle, (x, y))
    imageName = '3-' + foregroundColorImage[:-4] + '-' + backgroundColorImage
    imageBackgroundCopyHandle.save(imageName)

    imageBackgroundCopyHandle = imageBackgroundHandle.copy()
    for y in range(yLimit, -1, -1):
        for x in range(y):
            imageBackgroundCopyHandle.paste(imageForegroundHandle, (x, y))
    imageName = '4-' + foregroundColorImage[:-4] + '-' + backgroundColorImage
    imageBackgroundCopyHandle.save(imageName)


#DONE
def createCircleTiles(foregroundColorImage, backgroundColorImage, style):
    '''
    create image tile of input style in foregroundColor on the square backgroundColorImage
    '''
    os.chdir("c:/pythoncode/programs/wallpapergenerator/colors")

    imageBackgroundHandle = Image.open('background/' + backgroundColorImage)
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
        imageBackgroundHandle = Image.open('background/' + backgroundColorImage)
        imageBackgroundCopyHandle = imageBackgroundHandle.copy()
        imageForegroundHandle = Image.open('pixel/' + foregroundColorImage)

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


        imageName = str(i) + '-' +foregroundColorImage[:-4] + '-' + backgroundColorImage
        if style == 'quartercircle':
            imageBackgroundCopyHandle.save('quartercircle/' + imageName)
        elif style == 'semicircle':
            imageBackgroundCopyHandle.save('semicircle/' + imageName)

#DONE
def createSquareTiles(xLimit, yLimit, color):
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


#NOT SATISFACTORY
def createRandomBurstWallpaper():
    imageBackgroundHandle = Image.new('RGBA', (1000, 1800), (52, 53, 54, 255))
    xLimit, yLimit = imageBackgroundHandle.size

    imageForegroundHandle1 = Image.open('colors/offwhite-1p.jpg')
    imageForegroundHandle2 = Image.open('colors/lightblue-1p.jpg')
    imageForegroundHandle3 = Image.open('colors/red-1p.jpg')
    imageForegroundHandle4 = Image.open('colors/green-1p.jpg')
    imageForegroundHandle5 = Image.open('colors/orange-1p.jpg')
    imageForegroundHandle6 = Image.open('colors/blue-1p.jpg')

    colors = [imageForegroundHandle1, imageForegroundHandle2, imageForegroundHandle3, imageForegroundHandle4, imageForegroundHandle5, imageForegroundHandle6]

    for i in range(1000000):
        color = random.randint(0, len(colors) - 1)
        x = random.randint(0, xLimit)
        y = random.randint(0, yLimit)
        imageBackgroundHandle.paste(colors[color], (x,y))

    imageWallpaperName = 'burst.jpg'
    os.chdir("c:/pythoncode/programs/wallpapergenerator/output/mobile")
    imageBackgroundHandle.save(imageWallpaperName)


def getWallpaperSpecs():
    orientation = input('\nEnter the orientation of wallpaper [mobile/desktop]: ')

    imageFormat = input('\nEnter the image format [jpg/png]: ')

    style = input('\nEnter wallpaper style [boxes/rows/columns/random]: ')

    if orientation != 'mobile' and orientation != 'desktop' and orientation != 'square':
        print('Invalid orientation entered!')
        orientation = 'mobile'

    if imageFormat != 'jpg' and imageFormat != 'png':
        print('Invalid image format entered!')
        imageFormat = 'jpg'

    if style != 'boxes' and style !='rows' and style != 'columns' and style != 'random':
        print('Invalid style entered!')
        style = 'boxes'


    createSquareWallpaper(orientation, imageFormat, style)
