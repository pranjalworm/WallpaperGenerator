from PIL import Image
import random, sys, os

'''
#making the program more modular
def createColorTiles2():
    colors = {
                'red' : (156, 58, 58, 255),
                'purple' : (124, 72, 149, 255),
                'blue' : (49, 69, 131, 255),
                'green' : (58, 124, 65, 255),
                'orange' : (205, 140, 64, 255)
             }

    tileLength = 100
    tileBreadth = 100
    for color, value in colors:
        colorImageHandle = Image.new('RGBA', (tileLength, tileBreadth), value)
        colorImageHandle.save('colors/' + color + '.jpg')
'''

def createPixelColorTiles():
    '''
    creating 1x1 pixel size tiles
    '''

    #creating ORANGE color 1 pixel tile
    imageHandleOrange = Image.new('RGBA', (1, 1), (205, 140, 64, 255))
    imageHandleOrange.save('colors/orange-1p.jpg')

    #creating PURPLE color 1 pixel tile
    imageHandlePurple = Image.new('RGBA', (1, 1), (124, 72, 149, 255))
    imageHandlePurple.save('colors/purple-1p.jpg')

    #creating RED color 1 pixel tile
    imageHandleRed = Image.new('RGBA', (1, 1), (156, 58, 58, 255))
    imageHandleRed.save('colors/red-1p.jpg')

    #creating BLUE color 1 pixel tile
    imageHandleBlue = Image.new('RGBA', (1, 1), (49, 69, 131, 255))
    imageHandleBlue.save('colors/blue-1p.jpg')

    #creating GREEN color 1 pixel tile
    imageHandleGreen = Image.new('RGBA', (1, 1), (58, 124, 65, 255))
    imageHandleGreen.save('colors/green-1p.jpg')

    #creating GREY color 1 pixel tile
    imageHandleGrey = Image.new('RGBA', (1, 1), (86, 88, 88, 255))
    imageHandleGrey.save('colors/grey-1p.jpg')


def createTriangleTiles():
    '''
    create image tile with triangle in foreground on a square background
    '''
    imageBackgroundHandle1 = Image.open('colors/grey.jpg')
    imageBackgroundHandle2 = Image.open('colors/grey.jpg')
    xLimit, yLimit = imageBackgroundHandle1.size

    imageForegroundHandle = Image.open('colors/red-1p.jpg')

    for y in range(yLimit):
        for x in range(y):
            imageBackgroundHandle1.paste(imageForegroundHandle, (x, y))

    for x in range(xLimit):
        for y in range(x):
            imageBackgroundHandle2.paste(imageForegroundHandle, (x, y))

    os.chdir("c:/pythoncode/programs/wallpapergenerator/colors")
    imageBackgroundName = 'grey-red-triangle-tile1.jpg'
    imageBackgroundHandle1.save(imageBackgroundName)
    imageBackgroundName = 'grey-red-triangle-tile2.jpg'
    imageBackgroundHandle2.save(imageBackgroundName)

def createTriangleWallpaper():
    '''
    create wallpapers with triangle tiles
    '''

    os.chdir("c:/pythoncode/programs/wallpapergenerator")

    imageBackgroundHandle = Image.new('RGBA', (1000, 1900))
    xLimit, yLimit = imageBackgroundHandle.size

    imageTriangleHandle1 = Image.open('colors/grey-red-triangle-tile1.jpg')
    imageTriangleHandle2 = Image.open('colors/grey-red-triangle-tile2.jpg')

    colorTiles = [imageTriangleHandle1, imageTriangleHandle2]

    for y in range(0, yLimit, 100):
        for x in range(0, xLimit, 100):
            colorTile = random.randint(0, len(colorTiles) - 1)
            imageBackgroundHandle.paste(colorTiles[colorTile], (x, y))

    os.chdir("c:/pythoncode/programs/wallpapergenerator/output/mobile")
    imageBackgroundName = 'grey-red-triangle.jpg'
    imageBackgroundHandle.save(imageBackgroundName)


def createColorTiles():
    #creating PURPLE color tile
    imageHandlePurple = Image.new('RGBA', (100, 100), (124, 72, 149, 255))
    imageHandlePurple.save('colors/purple.jpg')

    #creating RED color tile
    imageHandleRed = Image.new('RGBA', (100, 100), (156, 58, 58, 255))
    imageHandleRed.save('colors/red.jpg')

    #creating BLUE color tile
    imageHandleBlue = Image.new('RGBA', (100, 100), (49, 69, 131, 255))
    imageHandleBlue.save('colors/blue.jpg')

    #creating GREEN color tile
    imageHandleGreen = Image.new('RGBA', (100, 100), (58, 124, 65, 255))
    imageHandleGreen.save('colors/green.jpg')
    #creating ORANGE color tile

    imageHandleOrange = Image.new('RGBA', (100, 100), (205, 140, 64, 255))
    imageHandleOrange.save('colors/orange.jpg')

    #creating GREY color tile
    imageHandleGrey = Image.new('RGBA', (100, 100), (59, 60, 60, 255))
    imageHandleGrey.save('colors/grey.jpg')

#creating wallpaper image
def createSquareWallpaper(orientation, imageFormat, style):
    createColorTiles()

    imageHandleRed = Image.open('colors/red.jpg')
    imageHandleBlue = Image.open('colors/blue.jpg')
    imageHandleGreen = Image.open('colors/green.jpg')
    imageHandleOrange = Image.open('colors/orange.jpg')
    imageHandlePurple = Image.open('colors/purple.jpg')

    colorTiles = [imageHandleRed, imageHandleBlue, imageHandleGreen, imageHandleOrange, imageHandlePurple]

    #choosing image orientation
    if orientation == 'mobile':
        wallpaperHandle = Image.new('RGBA', (400, 600))
        xLimit = 401
        yLimit = 601
    else:
        wallpaperHandle = Image.new('RGBA', (1200, 800))
        xLimit = 1201
        yLimit = 801

    colorTile = 0

    #choosing image style
    if style == 'rows':
        for y in range(0, yLimit, 100):
            colorTile = random.randint(0, len(colorTiles) - 1)
            for x in range(0, xLimit, 100):
                wallpaperHandle.paste(colorTiles[colorTile], (x, y))

    elif style == 'columns':
        for x in range(0, xLimit, 100):
            colorTile = random.randint(0, len(colorTiles) - 1)
            for y in range(0, yLimit, 100):
                wallpaperHandle.paste(colorTiles[colorTile], (x, y))

    elif style == 'random':
        for y in range(0, yLimit, 100):
            for x in range(0, xLimit, 100):
                colorTile = random.randint(0, len(colorTiles) - 1)
                wallpaperHandle.paste(colorTiles[colorTile], (x, y))

    else:
        count = 0
        for y in range(0, yLimit, 100):
            for x in range(0, xLimit, 100):
                colorTile = count % len(colorTiles)
                count += 1
                wallpaperHandle.paste(colorTiles[colorTile], (x, y))

    #choosing image format
    if imageFormat == 'png':
        imageFormat = '.png'
    else:
        imageFormat = '.jpg'

    #creating image filename
    wallpaperName = orientation + '-' + style + imageFormat
    os.chdir("c:/pythoncode/programs/wallpapergenerator/output/" + orientation)
    wallpaperHandle.save(wallpaperName)

    print('\nAll done...!\t' + wallpaperName + ' created!')


#taking wallpaper specifications from user
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

#RUN PROGRAM
#getWallpaperSpecs()

createColorTiles()
createPixelColorTiles()
createTriangleTiles()
createTriangleWallpaper()
