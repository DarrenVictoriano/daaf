# include path for /tools folder
import sys
import os.path
TOOL_DIR = (os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', '..')))
sys.path.append(TOOL_DIR)

# import the required tools
from ADB_Action_Scipt import ActionScript
from RC_Code import SonyRCKey
from AppList import AppList
import Power_Tools as pt  # read Documentation for more info

# create an instance of the class, variables can be change
tv = ActionScript()  # if more than 1 device use: tv = ActionScript("Device ID")
rc = SonyRCKey()
app = AppList()

# Print Requirements
print("Requirements:")
print("Amazon is signed in")
print("Netflix is signed in")
print("Hulu is signed in")

# Print Instructions
print("What is does:")
print("1. Launch Netflix and play content")
print("2. Do trickplay every 5 minutes")
print("3. Launch Amazon and play content")
print("4. Do trickplay every 5 minutes")
print("5. Launch Hulu and play content")
print("6. Do trickplay every 5 minutes")
print("Then repeat step 1 for as many loop as you enter")
print("Then power off TV")


start = input("Please enter how many loops you want: ")

# Automation Start
for x in range(1, int(start)):
    pt.playback_netflix(5)
    for i in range(0, 6):
        pt.trickplay_netflix(5, 6)
        tv.wait_in_minute(5)

    pt.playback_amazon(5)
    for i in range(0, 6):
        pt.trickplay_amazon(5, 2)
        tv.wait_in_minute(5)

    pt.playback_hulu(5)
    for i in range(0, 6):
        pt.trickplay_hulu(5, 10)
        tv.wait_in_minute(5)

    print(f'loop count: {x}')

tv.press_rc_key(rc.POWER)

# ----------------------- Keep terminal open -----------------------------
close = input("Press Enter to close terminal")
