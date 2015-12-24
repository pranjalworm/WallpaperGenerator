from PIL import Image
import random, sys

'''
#creating color tiles: NOT DONE
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

#creating color tiles
def createColorTiles():
    #creating PURPLE color tile
    imageHandlePurple = Image.new('RGBA', (100, 100), (124, 72, 149, 255))
    imageHandlePurple.save('colors/purple.jpg')

    #creating RED color tile
    imageHandleRed = Image.new('RGBA', (100, 100), (156, 58, 58, 255))
    imageHandleRed.save('colors/red.jpg')

    #creating BLUE color tile
    imageHandleRed = Image.new('RGBA', (100, 100), (49, 69, 131, 255))
    imageHandleRed.save('colors/blue.jpg')

    #creating GREEN color tile
    imageHandleRed = Image.new('RGBA', (100, 100), (58, 124, 65, 255))
    imageHandleRed.save('colors/green.jpg')

    #creating ORANGE color tile
    imageHandleRed = Image.new('RGBA', (100, 100), (205, 140, 64, 255))
    imageHandleRed.save('colors/orange.jpg')

#creating background image
def createBackground(orientation, imageFormat, style):
    createColorTiles()

    imageHandleRed = Image.open('colors/red.jpg')
    imageHandleBlue = Image.open('colors/blue.jpg')
    imageHandleGreen = Image.open('colors/green.jpg')
    imageHandleOrange = Image.open('colors/orange.jpg')
    imageHandlePurple = Image.open('colors/purple.jpg')

    colorTiles = [imageHandleRed, imageHandleBlue, imageHandleGreen, imageHandleOrange, imageHandlePurple]

    #choosing image orientation
    if orientation == 'mobile':
        backgroundHandle = Image.new('RGBA', (400, 600))
        xLimit = 401
        yLimit = 601
    elif orientation == 'desktop':
        backgroundHandle = Image.new('RGBA', (1200, 800))
        xLimit = 1201
        yLimit = 801
    else:
        backgroundHandle = Image.new('RGBA', (800, 800))
        xLimit = 801
        yLimit = 801

    colorTile = 0

    #choosing image style
    if style == 'rows':
        for y in range(0, yLimit, 100):
            colorTile = random.randint(0, len(colorTiles) - 1)
            for x in range(0, xLimit, 100):
                backgroundHandle.paste(colorTiles[colorTile], (x, y))

    elif style == 'columns':
        for x in range(0, xLimit, 100):
            colorTile = random.randint(0, len(colorTiles) - 1)
            for y in range(0, yLimit, 100):
                backgroundHandle.paste(colorTiles[colorTile], (x, y))

    elif style == 'random':
        for y in range(0, yLimit, 100):
            for x in range(0, xLimit, 100):
                colorTile = random.randint(0, len(colorTiles) - 1)
                backgroundHandle.paste(colorTiles[colorTile], (x, y))

    else:
        count = 0
        for y in range(0, yLimit, 100):
            for x in range(0, xLimit, 100):
                colorTile = count % len(colorTiles)
                count += 1
                backgroundHandle.paste(colorTiles[colorTile], (x, y))

    #choosing image format
    if imageFormat == 'png':
        imageFormat = '.png'
    else:
        imageFormat = '.jpg'

    #creating image filename
    backgroundName = orientation + '-' + style + imageFormat
    backgroundHandle.save(backgroundName)

    print('\nAll done...!\t' + backgroundName + ' created!')


#taking background specifications from user
def getBackgroundSpecs():
    orientation = input('\nEnter the orientation of background [mobile/desktop/square]: ')

    imageFormat = input('\nEnter the image format [jpg/png]: ')

    style = input('\nEnter background style [boxes/rows/columns/random]: ')

    if orientation != 'mobile' and orientation != 'desktop' and orientation != 'square':
        print('Invalid orientation entered!')
        orientation = 'mobile'

    if imageFormat != 'jpg' and imageFormat != 'png':
        print('Invalid image format entered!')
        imageFormat = 'jpg'

    if style != 'boxes' and style !='rows' and style != 'columns' and style != 'random':
        print('Invalid background style entered!')
        style = 'boxes'


    createBackground(orientation, imageFormat, style)

#RUN PROGRAM
getBackgroundSpecs()

#createColorTiles2()
