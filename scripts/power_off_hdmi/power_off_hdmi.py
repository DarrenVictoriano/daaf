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
# this is for pre-made functions. read Documentation for more info
import Power_Tools as pt

# create an instance of the class, variables can be change
tv = ActionScript()  # if more than 1 device use: tv = ActionScript("Device ID")
rc = SonyRCKey()
app = AppList()

# Print Requirements
print("Requirements:")
print("HDMI1 with IRBlaster setup")
print("Amazon, Netflix, Hulu and Vudu are signed in\n")

# Print Instructions
print("This is what the script does:")
print("Tune to HDMI for 1 hour")
print("Then change channel every 10 minutes")
print("Launch Netflix for 1 hour")
print("Launch Amazon for 1 hour")
print("Tune back to HDMI1 for 1 hour")
print("Power OFF TV\n")

print("What HDMI input your IRB is setup?")
hdmiInput = input("Enter number: 1, 2, 3 or 4: ")

# Automation Start
# ------------------------------- HDMI1 ----------------------------------
rcHDMI = pt.select_hdmi_input(hdmiInput)
tv.press_rc_key(rcHDMI)
tv.wait_in_second(8)
# channel up
for i in range(1, 4):
    tv.press_rc_key(rc.CHANNEL_UP)
    tv.wait_in_minute(10)  # playback time
    print(f'CHANNEL UP loop count: {i}')
# channel down
for i in range(1, 4):
    tv.press_rc_key(rc.CHANNEL_DOWN)
    tv.wait_in_minute(10)  # playback time
    print(f'CHANNEL DOWN loop count: {i}')

# ------------------------------- Netflix ---------------------------------
tv.clear_launch_app(app.NETFLIX_PKG, app.NETFLIX_ACT)
tv.wait_in_second(8)  # Wait load netflix
tv.press_rc_key(rc.ENTER)
tv.wait_in_second(2)
tv.press_rc_key(rc.DOWN)
tv.wait_in_second(1.5)
tv.press_rc_key(rc.ENTER)
tv.wait_in_second(1.5)
tv.press_rc_key(rc.ENTER)
tv.wait_in_hour(1)  # playback time
tv.press_rc_key(rc.HOME)
tv.wait_in_second(5)

# ------------------------------- Amazon ---------------------------------
tv.clear_launch_app(app.AMAZON_PKG, app.AMAZON_ACT)
tv.wait_in_second(8)  # wait load amazon
tv.press_rc_key(rc.DOWN)
tv.wait_in_second(1.5)
tv.press_rc_key(rc.ENTER)
tv.wait_in_second(1.5)
tv.press_rc_key(rc.ENTER)
tv.wait_in_hour(1)  # playback time
tv.press_rc_key(rc.HOME)
tv.wait_in_second(5)

# ------------------------------- HDMI1 ----------------------------------
rcHDMI = pt.select_hdmi_input(hdmiInput)
tv.press_rc_key(rcHDMI)
tv.wait_in_second(8)
# channel up
for i in range(1, 4):
    tv.press_rc_key(rc.CHANNEL_UP)
    tv.wait_in_minute(10)  # playback time
    print(f'CHANNEL UP loop count: {i}')
# channel down
for i in range(1, 4):
    tv.press_rc_key(rc.CHANNEL_DOWN)
    tv.wait_in_minute(10)  # playback time
    print(f'CHANNEL DOWN loop count: {i}')

# RC OFF TV
tv.press_rc_key(rc.POWER)

# ------------------------- Keep terminal open ---------------------------
close = input("Press Enter to close terminal")
