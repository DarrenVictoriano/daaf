# include path for /tools folder
import sys
import os.path
tool_dir = (os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', '..')) + '/tools/')
sys.path.append(tool_dir)

# import the required tools
from ADB_Action_Scipt import ActionScript
from RC_Code import SonyRCKey
from AppList import AppList
import Power_Tools as pt  # this is for pre-made functions. read Documentation for more info

# create an instance of the class, variables can be change
tv = ActionScript()  # if more than 1 device use: tv = ActionScript("Device ID")
rc = SonyRCKey()
app = AppList()

# Print Requirements
print("Requirements:")
print("HDMI1 with IRBlaster setup")
print("Amazon, Netflix, Hulu and Vudu are signed in")
print("Auto program completed for RF\n")

# Print Instructions
print("This is what the script does:")
print("Tune to HDMI1 for 1 hour")
print("Then change channel every 10 minutes")
print("Launch Netflix for 1 hour")
print("Launch Amazon for 1 hour")
print("Tune back to HDMI1 for 1 hour")
print("Power OFF TV\n")


start = input("Press Enter to start")

# Automation Start
pt.playback_netflix(45)

# ----------------------- Keep terminal open -----------------------------
close = input("Press Enter to close terminal")
