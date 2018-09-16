# macOS Initial Setup Script

This script aims to automate the process of setting up common features and software on your Mac as much as possible. It is build to be highly configurable and it can be set exactly according to your needs.

**NOTE:** In order for this script to work properly, 'Terminal' and 'Script Editor' apps need to be added to Accessibility Assist allowed apps.

## Disclaimer

Please note that this script is still a **very early work in progress**. Some of the advertised functionality may not work properly or not may not be there at all. Please **USE AT YOUR OWN RISK**. I will not be held responsible for any damage that might occur on your Mac as a result of using this script.


## Getting Started

### Installing

Clone the repository by:
```
 $ git clone https://github.com/SlavDimov/macOS-Initial-Setup-Script
```
or if you are on a fresh macOS install, that still doesn't have the XCode Command Developer Tools, download and unzip it.

## Usage

The script consists of separate functions, each of which contains one tweak. The functions can be grouped to presets.

**NOTE:** You can find information about what each function does by opening one of the containing **.py** files in the root directory, with any text editor, and reading the description for each function.

There are several ways to use this script:

### Using the default configuration preset
In the project's root directory you will find a file called **default-config.preset**. It contains the set of functions to be executed by the script.

To run the script with this default configuration file simply open up a terminal in the root of the directory and type:
```
$ python ./macOS-Initial-Setup-Script.py
```

### Creating your own configuration preset
Feel free to create your own configuration file that will setup your Mac exactly the way you want it:

There are just a couple of rules:

* One function name per line
* No commas, dots, semicolons, question marks, etc.
* No whitespaces
* Comments on separate lines or after the function name, starting with ```#```

After that you can simply point the script to the newly created preset:
```
$ python ./macOS-Initial-Setup-Script.py preset=myPreset.preset
```

### Specifying functions from the command line

Sometimes you just want to quickly execute one or two specific functions without bothering to create a new configuration preset.

This can be achieved in the following way:
```
$ python ./macOS-Initial-Setup-Script.py <function_name_1> <function_name_2> ...
```


