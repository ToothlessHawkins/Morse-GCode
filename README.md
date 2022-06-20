# Morse-GCode
Simple command line utility to convert from English to Morse Code to GCODE

1. Run it in the terminal with python3 like `python en_morse_gcode.py`

2. Enter the string you want to be converted to morse/GCode.

3. First the morse code translation will be spat out, followed by the GCode instructions.

You can use this to make your 3D printer play morse code at pre-determined points. 
I use it to alert me when a print is complete or a pause point has been reached.
Some printers come with speakers that support multiple tones, so they can play musical tones. 
My printer can only play a single tone, so I figure morse code is about as creative as I can get with it.

This is not the most elegant or efficient code, but it does work and it does generate the fewest possible lines of GCode for the given string.
YMMV
