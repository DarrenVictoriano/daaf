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
import Power_Tools as pt

# create an instance of the class, variables can be change
tv = ActionScript()  # if more than 1 device use: tv = ActionScript("Device ID")
rc = SonyRCKey()
app = AppList()

# Print Requirements
print("Requirements:")
print("HDMI1 with IRBlaster setup")
print("Amazon, Netflix, Hulu and PS Vue are signed in")
print("Auto program completed for RF\n")

# Print Instructions
print("This is what the script does:")
print("Tune to HDMI1 for 1 hour")
print("Then change channel every 10 minutes")
print("Launch Netflix for 1 hour")
print("Launch Amazon for 1 hour")
print("Tune to PS Vue for 1 hour")
print("Then change channel every 10 minutes")
print("Power OFF TV\n")

start = input("Press Enter to start")

# Automation Start
pt.playback_hdmi(rc.HDMI1, 10)  # let playback for 10 minutes
pt.trickplay_hdmi(10, 3)  # then trickplay every 10minutes for 1 hour

pt.playback_netflix(60)
pt.playback_amazon(60)

pt.playback_psvue(10)
pt.trickplay_psvue(10, 3)

tv.press_rc_key(rc.POWER)

# ----------------------- Keep terminal open -----------------------------
close = input("Press Enter to close terminal")
