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
import Power_Tools as pt  # read Documentation for more info

# create an instance of the class, variables can be change
tv = ActionScript()  # if more than 1 device use: tv = ActionScript("Device ID")
rc = SonyRCKey()
app = AppList()

# Print Requirements
print("Requirements:")
print("Antenna Autoprogram completed")
print("TV key is programmed to RF Input")
print("IR Blaster setup on HDMI1")
print("Blu-Ray Player connected on HDMI2 with disk inside")
print("TV connected to a network\n")

# Print Instructions
print("1. Launch TV Input and do Trickplay")
print("2. Do Volume change while on TV antenna")
print("3. Tune to HDMI1 and do Trickplay")
print("4. Do Volume change while on HDMI1")
print("5. Tune to HDMI2 and play Blu-Ray disk")
print("6. Do trick play and volume change on HDMI2")
print("7. Launch Sony Select and verify if its working")
print("8. Press Dicover and verify it is working\n")

start = input("Press Enter to start")

# Automation Start
# ----------------------- TV Input Test -----------------------------
# Tune to RF
pt.playback_rf(1)
pt.volume_change(1, 4)
pt.trickplay_hdmi(1, 3)

# ------------------------- HDMI Test -------------------------------
pt.playback_hdmi(rc.HDMI1, 1)
pt.trickplay_hdmi(1, 3)
pt.volume_change(1, 4)

# -------------------------- BDP Test --------------------------------
pt.playback_hdmi(rc.HDMI2, 1)
tv.press_rc_key(rc.ENTER)
tv.wait_in_minute(2)
pt.volume_change(1, 4)
pt.trickplay_amazon(1, 2)

# -------------------------- Other Test --------------------------------
tv.press_rc_key(rc.HOME)
tv.wait_in_second(10)
tv.clear_launch_app(app.SONY_SELECT_PKG, app.SONY_SELECT_ACT)
tv.wait_in_second(10)
for i in range(1, 11):
    tv.press_rc_key(rc.DOWN)
    print(f'Down presses count: {i}')
tv.press_rc_key(rc.HOME)
tv.wait_in_second(10)

tv.press_rc_key(rc.DISCOVER)

# ----------------------- Keep terminal open -----------------------------
close = input("Press Enter to close terminal")
