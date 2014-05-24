# CollageRecipe

Easy and straightforward way to create beatuful collages like this one:
No dealing with heavyweight clunky image-editing software like GIMP or Photoshop.
Create your collages manually, or programmatically.

![Bay to breakers](https://dl.dropboxusercontent.com/s/xjnb5dpws0wkhr7/bay2breakers_good_small.jpg)

## Programmable photo collage

All you need to do is to select the images (which you have to do anyway) and describe which image goes to which row of images, at which possition.
In other words you create the "recipe" that looks like this

```
   file11.jpg
   file12.png
   file13.jpeg
   file14.jpg

   file21.jpg
   file22.jpg
   file23.jpg

   ...
```

where file{i}{j}.jpg is the j-th file on the i-th row. Note the new-line separation between rows.

## Getting started (on Mac OS X)

1. Install homebrew. Go to 
```   
   http://brew.sh/ 
```   
and follow the instructions. It is pretty simple. You only need it in order to install webkit2png in the next step.
2. Install webkit2png. Collagerecipe uses it for rendering the collage to PNG image.
```   
   cd collagerecipe/
   ./install.sh
```   
3. Create local server. This is how we the images that you have reach the rendering system
```   
   ./setup.sh
```   
4. Verify that everything is setup correctly
```   
   ./collagerecipe example.recipe `whoami`
```   
You should see an image that looks like the image above. Awesome! You are ALL SET to create your own collages by now!

The new image file should be in the directory where you installed collagerecipe:
```   
   ls | grep full.png
```   
5. Create your recipe! 
   
* See example.recipe and example_data see the recipe format. The format is pretty minimal. All you can do is say which images go in which order on which line
* copy your images over. Create a folder called "images" or "birthday_collage" or whatever you want *within* the collagerecipe main folder and put your images there. It is important that your images are within the collagerecipe folder so that they are served by the server you setup in step 3. 
* decide which images should be on which row. Create "mycollage.recipe" or "my.collage" or "birthday.images" or whatever you want text file and add the paths to the images you like. 
* run 
```   
  ./collagerecipe RECIPE_FILE COLLAGE_NAME
```   
replacing RECIPE_FILE with the file you just made including the images, and COLLAGE_NAME with the name of output file you want. You can then see your collage.
* Iterate! You can change the order of the images. You can also use your favorite image editing software to crop the images or add any effects. I usually just crop them in Preview to the desired part of the image. You can also open collage.js or index.html and add effects in bulk.

## Getting started (Windows or Linux)

Unfortunately I haven't tested on these platforms but I bet there exist a simple way to run collagerecipe. All you'd need is 1) python, 2) some webkit -> image tool. 

Would love it if anybody figures it out and fork it or send me a pull request.

## Under the hood:

1. A simple python script parses out the recipe file and creates JSON representation "images.json"
2. The localhost server serves index.html which uses d3.js library to arrange the images described in images.json into rows and to add some simple effects like shadows, rotation and reductions in contrast and saturation. If you open localhost:8000 in a webkit browser such as Chrome, you'd see the collage.
3. webkit2png renders whatever is available on localhost:8000 to PNG. There's the collage.

## Pull request wish list

Collagerecipe is functional and useful as it is now, but it could be improved.

* multi-platform support (Windows, Linux)
* easy way to add filters like in Instagram per image. This would make the collages really beautuful. 
* Some way to ballance contrast, and saturation over all the images. For example, the ImageQuilt Chrome extension does a pretty good job of it. 


