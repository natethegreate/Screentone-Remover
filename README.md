# Screentone-Remover
Script with GUI that removes screentones, or the "printed" effect in manga and doujins, using DSP.
This process is necessary for use with [DeepCreamPy](https://github.com/deeppomf/DeepCreamPy), by deeppomf. 
Gaussian blur is applied to an image, then an averaging blur afterwards. This removes high frequency signals (screentones).
The output of this is sharpened with a Laplacian kernel, to retain some edge.

Here is a visual example:
![srsfwexample](screentoneexsfw.jpg)
NOTE: More blurring will remove heavier screentones, but will result in more loss of quality from the image. You may need to experiment with the 3 blurring levels depending on the artists screentone usage.

## Getting Started
You should have whatever doujin or images you want in .png format, in some folder. You should also create an output folder.
I require .png because DeepCreamPy requires png format. nhentai.net may download jpg files, but you can batch convert using this [jpg2png](https://jpg2png.com/) 

### Prerequisites
Windows, tested on windows 10.

Python 3 if you want to run the source codes. Uses opencv (cv2) libs, numpy, and tkinter for the UI.

Note that the .exe file is quite large. The signal processing utilizes a large library of signal processing related functions, opencv.

### Downloads

* v.[1.5](https://github.com/natethegreate/Screentone-Remover/releases/tag/1.5)

* v. [1.4](https://github.com/natethegreate/Screentone-Remover/releases/tag/1.4)

* v. [1.3](https://github.com/natethegreate/Screentone-Remover/releases/tag/1.3)

* v. [1.2](https://github.com/natethegreate/Screentone-Remover/releases/tag/1.2)

### Installing

* Executable

  Simply follow the link above and download the package.zip. 
  Extract the program from the zip. I would reccommend creating an input folder and output folder in the same directory for ease of use.
  There is a slim chance that the file directory dialogue can trigger your Anti-virus. I was able to bypass this by just closing the app and restarting it again. 

```
stremove.exe
```

* Source Code
  Simply run stremove.py. I use anaconda on my windows machine.

```
py stremove.py
```

## Deployment

You should use this in tandem with my other project, hentAI, and eventually [DeepCreamPy](https://github.com/deeppomf/DeepCreamPy), by deeppomf.

## Contributing

Any contributions are welcome, I am still a student with limited resources and time and appreciate any help I can get.

## Versioning

1.5 * Cut down on unneeded libs (file size unchanged), fixed bug where .PNG wasn't recognized

1.41: * Greatly improved sharpening process, which was brightening images unecessarily due to a miscalculation. Updated labels and defaults.

1.4: * Sharpening is now parameterized. You can customize the filter to suit whatever art style you encounter. Defaults are still visible. For more information on the filter params, check out [this page](https://homepages.inf.ed.ac.uk/rbf/HIPR2/log.htm)

1.3: * Updated blurring process. Secondary blur is now a bilateral filter, which retains edges and removes toning much better. 
     * Removed secondary sharpening because it can add noise in some circumstances.
     * Default slider position is now on 2.
     
1.2: Removed redundant modules. Created exe file.

1.1: GUI, directory selection, batch screentone removing, variable removal

1.0: Can remove screentones from an image

## Todo

* Allow custom kernel types for blurring and sharpening
* Parameterize Bilateral Filtering inputs for Sigma Space
* Better UI
* Find optimal default values
* Remember and autofill Input/Output directories
* Somehow reduce file size

## Authors

* **Nathan Cueto** - *Everything* - [My GitHub](https://github.com/natethegreate)

## License

This project is licensed under MIT
