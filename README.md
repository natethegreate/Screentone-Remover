# Screentone-Remover
Script with GUI that removes screentones, or the "printed" effect in manga and doujins, using DSP.
This process is necessary for use with [DeepCreamPy](https://github.com/deeppomf/DeepCreamPy), by deeppomf. 
Gaussian blur is applied to an image, then an averaging blur afterwards. This removes high frequency signals (screentones).
The output of this is sharpened with a Laplacian kernel, to retain some edge.
NOTE: More blurring will remove heavier screentones, but will result in more loss of quality from the image. You may need to experiment with the 3 blurring levels depending on the artists screentone usage.

## Getting Started
You should have whatever doujin or images you want in .png format, in some folder. You should also create an output folder.

### Prerequisites
Windows, tested on windows 10.

Python 3 if you want to run the source codes.

Note that the .exe file is quite large. The signal processing utilizes a large library of signal processing related functions, opencv.

### Downloads

v. 1.3
v. [1.2](https://github.com/natethegreate/Screentone-Remover/releases/tag/1.2)

### Installing

* Executable
  Simply follow the link above and download the package.zip. 
  Extract the program from the zip. I would reccommend creating an input folder and output folder in the same directory for ease of use.
  There is a slim chance that the file directory dialogue can trigger your Anti-virus. I was able to bypass this by just closing the app and restarting it again.

```
Give the example
```

* Source Code
  Simply run stremove.py. I use anaconda on my windows machine.

```
py stremove.py
```

## Deployment

You should use this in tandem with my other projects, and eventually [DeepCreamPy](https://github.com/deeppomf/DeepCreamPy), by deeppomf.

## Contributing

All codes made by me.

## Versioning

1.3: * Updated blurring process. Secondary blur is now a bilateral filter, which retains edges and removes toning much better. 
     * Removed secondary sharpening because it can add noise in some circumstances.
     * Default slider position is now on 2.
1.2: Removed redundant modules. Created exe file.
1.1: GUI, directory selection, batch screentone removing, variable removal
1.0: Can remove screentones from an image

## Authors

* **Nathan Cueto** - *Initial work* - [My GitHub](https://github.com/natethegreate)

## License

This project is licensed under 
