# lazy-scrcpy
Launches scrcpy with saved arguments

# Installation
copy zconfig.json and zlazy_scrcpy.py to scrcpy folder

# Usage
1. double-click zlazy_scrcpy.py to launch scrcpy
2. if attached android device has any saved arguments, scrcpy will use those
3. else scrcpy will launch with default arguments- `--stay-awake --turn-screen-off`

# How to save/modify arguments for my device?
1. connect your device to computer and double-click zsave_arguments.py
2. when prompted, enter the arguments you want and press enter
3. lazy-scrcpy will launch scrcpy using these arguments while your device is connected

# How to modify default arguments?
1. double-click zsave_arguments.py
2. it will ask if you want to modify default arguments. enter `y`
3. when prompted, enter arguments you want and press enter
4. these arguments will be applied to devices which donot have any saved arguments
