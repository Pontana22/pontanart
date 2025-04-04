# GdocAsciiConverter
Created by Pontus Martinsson as a school project

## NOTE

An improved version of this project is currently under development and is expected to be released sometime during spring 2025

## Requirements:

- Python 3.10.7 or greater
- The pip package management tool
- A Google Cloud project with the Google Docs API

## How to use:

1. Clone the repo and run `pip install -r requirements.txt`
2. Create a Google Cloud project and follow [Google's quickstart quide](https://developers.google.com/docs/api/quickstart/python) up until "Install the Google client library"
3. Download your OAuth client file, rename it to credentials.json and place it in the root folder
4. Place the image you want to convert in the **img** folder
5. Run `python main.py` and follow the instructions in the terminal
6. Done! Your image/document should have appeared on your Google drive

## WARNING!

When you've given the program access to your drive, the file **token.json** will be created
**DO NOT SHARE THIS FILE** as anyone who posess it has full access to your Google drive

## General info:

### How the program works
The program works by taking your selected characters and sorts them by how many pixels they contain. For instance "M" contains a lot of pixels, while "." contains very few. Your selected image will be rescaled to your desired width (height is calculated automatically to match the original ratio) and converted to grayscale. Each pixel will then be translated into a character based on how light7dark it is. Finally, the finished text is transfered to a brand new Google Doc on your Google Drive.

### Settings + presets
Every time you run the program, you are given the choice of whether you want to do a manual setup or load a preset. If you cohoose to use a preset, a list of available presets is displayed, and all you have to do is pick the one you want. The presets are stored in the **presets** folder in **.txt** format, which means that you are free to edit/create presets as you please. In the manual setup, you get to pick each value to fit your specific situation (more on this below). After completing a manual setup, you will be given the choice to save your settings as a preset.

### Other
The font used is Courier Prime

## Manual setup info:

### Quality
**Low quality mode** will use the entire range `0-255` from completely black `0` to completely white `255` regardless of what pixels actually exist in the image. This means that some of the chosen characters might be excluded. This mode generally works well with only a few characters (5 or so), but I suggest you play around a bit and see what works best for you.

**Examples:** (characters, values)

`"abc", [0, 100, 200, 255]`     --> abcc

`"abc", [200, 200, 255, 255]`   --> bbcc

`"abc", [255, 0, 0, 255]`       --> caac

`"abc", [0, 1, 2, 3]`           --> aaaa

`"abc", [255, 254, 253, 252]`   --> cccc

**High quality mode** will find the darkest and lightest pixels **in each row of pixels** (because I did the low quality mode first and couldn't be bothered to make it not work row by row) and only use that range when converting it to characters. This means that all chosen characters will usually be included, it is however still possible for characters to be excluded as seen in the examples. Due to this mode treating each row as a separate image, some images might turn out with strange artifacts such as dark/light spots where there shouldn't be. The name "High quality" might be a bit misleading, but you do generally get more details using this mode. This mode generally works well with as many different characters as possible, but I once again suggest you play around for a bit and see what works best for you.

**Examples:** (characters, values)

`"abc", [0, 100, 200, 255]`     --> abcc

`"abc", [200, 200, 255, 255]`   --> aacc

`"abc", [255, 0, 0, 255]`       --> caac

`"abc", [0, 1, 2, 3]`           --> abbc

`"abc", [255, 254, 253, 252]`   --> cbba

**Generally, I suggest using low quality mode as the results will be more predictable.**

Better high quality mode that actually looks at the entire image at once will be included in the improved version of this project

### Characters
I would recommend you only use [ASCII printable characters](https://www.ascii-code.com/characters/printable-characters) (including space) as other ones might be converted into multiple characters, thus probably making the image all wonky. There is however nothing really stopping you from exploring additional characters.

The same character is allowed more than once, but will consequently occupy a greater range.

**Examples:** (characters, values)

`"abc", [0, 100, 200, 255]`     --> abcc

`"aabc", [0, 100, 200, 255]`    --> aabc

### Font size
The font size is entirely up to you, I find that 3 gives good results, but anything goes.

### Width
This determines how many characters each row will consist of. Usually you'll want to keep this value below the maximum amount of characters that fit in one row with your selected font size, for instance, with font size 3, 250 characters will fit on one row. There is however nothing stopping you from exceeding this amount in case you would like to do something special.

### Row spacing
Determines the row spacing. For whatever reason, Google Docs will divide this value by 100. This means that if you were to input 60, Google Docs would display it as 0.6. I have fount that 60 works well for small font sizes, but you might want to adapt this to fit your chosen font size.
