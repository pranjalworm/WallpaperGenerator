# WallpaperGenerator

Here is some detailed information on how to use Wallpaper Generator (DOCUMENTATION NOT FINISHED)

<ul>
<li><code>createPixelTile(color, imageFormat)</code> use this function to create 1x1 size image which can be later pasted onto a bigger tile to make shapes like triangles, quartercircles, semicircles etc.<br>
<code>color</code> : color tuple like (198, 74, 78, 255) <br>
<code>imageFormat</code> : string ('jpg', 'png')<br>
Output Examples: see colors/pixel dir
</li>

<li><code>createSquareTile(xLimit, yLimit, color)</code> use this function to create an image of specified size and color<br>
<code>xLimit</code> : width of output image<br>
<code>yLimit</code> : height of output image<br>
<code>color</code> : color tuple like (198, 74, 78, 255)<br>
Output examples: see colors/background dir
</li>

<li><code>createTriangleTile(foregroundColor, backgroundColor)</code> use this function to create all possible tiles with triangles in foreground on square background<br>
<code>foregroundColor</code> : color tuple of the 1x1 size image (it should already exist or use <code>createPixelTile()</code> first)<br>
<code>backgroundColor</code> : color tuple of the image to be used as background (it should already exist or use <code>createSquareTile()</code> first)<br>
Output examples: see colors/triangle dir
</li>

<li><code>createCircleTile(foregroundColor, backgroundColor, style)</code> use this function to create all possible tiles with quartercircle/semicircle (specified through style) in foreground on square background<br>
<code>foregroundColor</code> : color tuple of the 1x1 size image (it should already exist or use <code>createPixelTile()</code> first)<br>
<code>backgroundColor</code> : color tuple of the image to be used as background (it should already exist or use <code>createSquareTile()</code> first)<br>
<code>style</code> : string ('quartercircle', 'semicircle')<br>
Output examples: see colors/circle dir
</li>

<li><code>createSquareWallpaper(foregroundColor, backgroundColor, imageFormat)</code> use this function to create Square themed wallpaper<br>
<code>foregroundColor</code> : color tuple of foreground image (it should already exist or use <code>createSquareTile()</code> first)<br>
<code>backgroundColor</code> : color tuple of image to be used as background (it should already exist or use <code>createSquareTile()</code> first)<br>
<code>imageFormat</code> : string ('jpg', 'png')
</li>


<li><code>createTriangleWallpaper(foregroundColor, backgroundColor, imageFormat)</code> use this function to create Triangle themed wallpaper<br>
<code>foregroundColor</code> : color tuple of foreground image (it should already exist of use <code>createTriangleTile()</code> first)<br>
<code>backgroundColor</code> : color tuple of image to be used as background (it should already exists or use <code>createSquareTile()</code> first)<br>
<code>imageFormat</code> : string ('jpg', 'png')
</li>

<li><code>createCircleWallpaper(foregroundColor, backgroundColor, style, imageFormat)</code> use this function to create Circle themed wallpaper<br>
<code>foregroundColor</code> : color tuple of foreground image (it should already exist of use <code>createCircleTile()</code> first)<br>
<code>backgroundColor</code> : color tuple of image to be used as background (it should already exists or use <code>createSquareTile()</code> first)<br>
<code>style</code> : string ('semicircle', 'quartercircle')<br>
<code>imageFormat</code> : string ('jpg', 'png')
</li>
