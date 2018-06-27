# include path for /tools folder
import sys
import os.path
tool_dir = (os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', '..')) + '/tools/')
sys.path.append(tool_dir)

# First import the ADB_Action_Script.py it must be on the same folder
from ADB_Action_Scipt import ActionScript
# then import the RC keys and App PKGs for easy scripting
from RC_Code import SonyRCKey
from AppList import AppList

# create an instance of the class, variables can be change
tv = ActionScript()
rc = SonyRCKey()
app = AppList()

# ---------------------------Pre-built Functions Settings--------------------------


# ------------------------- re-built Functions HDMI or RF ------------------------
def playback_hdmi(hdmi, time=0):
    """Launch selected HDMI and playback"""
    tv.press_rc_key(hdmi)
    tv.wait_in_minute(time)  # wait to load hdmi


def playback_rf(time=0, down=6):
    """Tune to RF Input then playback"""
    tv.press_rc_key(rc.HOME)
    tv.wait_in_second(10)
    for i in range(1, down):
        tv.press_rc_key(rc.DOWN)
        print(f'Down press count: {i}')
    tv.press_rc_key(rc.ENTER)
    tv.wait_in_minute(time)


def volume_change(time=2, loop=4):
    """ Volume up and Volume down based on loop count"""
    # volume up
    for i in range(1, loop):
        tv.press_rc_key(rc.VOLUME_UP)
        print(f'Volume Up press count: {i}')
    tv.wait_in_minute(time)
    # volume down
    for i in range(1, loop):
        tv.press_rc_key(rc.VOLUME_DOWN)
        print(f'Volume Down press count: {i}')
    tv.wait_in_minute(time)


def trickplay_hdmi(time=2, loop=4):
    """Do channel change on HDMI with default value of 10min and 4 loops"""
    # requires playback_hdmi to run 1st
    # channel up
    for i in range(0, loop):
        tv.press_rc_key(rc.CHANNEL_UP)
        tv.wait_in_minute(time)  # playback time
        print(f'CHANNEL UP loop count: {i}')
    # channel down
    for i in range(0, loop):
        tv.press_rc_key(rc.CHANNEL_DOWN)
        tv.wait_in_minute(time)  # playback time
        print(f'CHANNEL DOWN loop count: {i}')


def select_hdmi_input(hdmi):
    """Select HDMI Input you want to test"""
    if hdmi == '1':
        return rc.HDMI1
    elif hdmi == '2':
        return rc.HDMI2
    elif hdmi == '3':
        return rc.HDMI3
    elif hdmi == '4':
        return rc.HDMI4
    else:
        print("Invalid argurment, please enter str 1, 2, 3 or 4")
        print("Launching HDMI1 as default")
        return rc.HDMI1


# ---------------------------Pre-built Functions Netflix--------------------------
def playback_netflix(time=0):
    """Launch Netflix then playback content based on given time"""
    tv.clear_launch_app(app.NETFLIX_PKG, app.NETFLIX_ACT)
    tv.wait_in_second(10)  # Wait load netflix
    tv.press_rc_key(rc.ENTER)
    tv.wait_in_second(2)
    tv.press_rc_key(rc.DOWN)
    tv.wait_in_second(1.5)
    tv.press_rc_key(rc.ENTER)
    tv.wait_in_second(1.5)
    tv.press_rc_key(rc.ENTER)
    tv.wait_in_minute(time)  # playback time


def trickplay_netflix(time=2, speed=6):
    """ FF and RW speed is 10 seconds per second """
    # requires playback_netflix to run 1st
    # trickplay starts FF
    tv.press_rc_key(rc.FF)
    tv.wait_in_second(speed)  # trickplay time
    tv.press_rc_key(rc.ENTER)
    tv.wait_in_minute(time)  # playback time
    # trickplay starts RW
    tv.press_rc_key(rc.RW)
    tv.wait_in_second(speed)  # trickplay time
    tv.press_rc_key(rc.ENTER)
    tv.wait_in_minute(time)  # playback time


# ---------------------------Pre-built Functions Amazon--------------------------
def playback_amazon(time=0):
    """Launch Amazon then playback content based on given time"""
    tv.clear_launch_app(app.AMAZON_PKG, app.AMAZON_ACT)
    tv.wait_in_second(10)  # wait load amazon
    tv.press_rc_key(rc.DOWN)
    tv.wait_in_second(1.5)
    tv.press_rc_key(rc.ENTER)
    tv.wait_in_second(1.5)
    tv.press_rc_key(rc.ENTER)
    tv.wait_in_minute(time)  # playback time


def trickplay_amazon(time=2, speed=2):
    """FF and RW speed x2 is 40 seconds per second"""
    # requires playback_amazon to run 1st
    # trickplay start FF
    tv.press_rc_key(rc.FF)
    tv.wait_in_second(1)
    tv.press_rc_key(rc.FF)
    tv.wait_in_second(speed)  # speed time
    tv.press_rc_key(rc.PLAY)
    tv.wait_in_minute(time)  # playback time
    # trickplay start RW
    tv.press_rc_key(rc.RW)
    tv.wait_in_second(1)
    tv.press_rc_key(rc.RW)
    tv.wait_in_second(speed)  # speed time
    tv.press_rc_key(rc.PLAY)
    tv.wait_in_minute(time)  # playback time


# ---------------------------Pre-built Functions Hulu--------------------------
def playback_hulu(time=0):
    """Launch Hulu then playback content based on given time"""
    tv.clear_launch_app(app.HULU_PKG, app.HULU_ACT)
    tv.wait_in_second(10)  # wait load hulu
    tv.press_rc_key(rc.DOWN)
    tv.wait_in_second(1)
    tv.press_rc_key(rc.DOWN)
    tv.wait_in_second(1)
    tv.press_rc_key(rc.ENTER)
    tv.wait_in_second(1)
    tv.press_rc_key(rc.ENTER)
    tv.wait_in_minute(time)  # playback time


def trickplay_hulu(time=2, speed=10):
    """FF and RW speed is 10 seconds per RC press"""
    # requires playback_hulu to run 1st
    # trickplay start FF
    for i in range(0, speed):  # speed
        tv.press_rc_key(rc.RIGHT)
        print(f'FF loop count: {i}')
    tv.press_rc_key(rc.ENTER)
    tv.wait_in_minute(time)  # playback time
    # trickplay start TW
    for i in range(0, speed):  # speed
        tv.press_rc_key(rc.LEFT)
        print(f'RW loop count: {i}')
    tv.press_rc_key(rc.ENTER)
    tv.wait_in_minute(time)  # playback time


# ---------------------------Pre-built Functions PSVue--------------------------
def playback_psvue(time=0):
    """Launch PSVue then playback content based on given time"""
    tv.clear_launch_app(app.PSVUE_PKG, app.PSVUE_ACT)
    tv.wait_in_second(10)  # wait to load psvue
    tv.press_rc_key(rc.ENTER)
    tv.wait_in_second(10)  # wait to load playback
    tv.press_rc_key(rc.ENTER)
    tv.wait_in_minute(time)  # playback time


def trickplay_psvue(time=2, loop=4):
    """Do channel change on PS Vue with default value of 10min and 4 loops"""
    # requires playback_psvue to run 1st
    # channel up loop
    for i in range(0, loop):
        tv.press_rc_key(rc.CHANNEL_UP)
        tv.wait_in_minute(time)  # playback time
        print(f'CHANNEL UP loop count: {i}')
    # channel down loop
    for i in range(0, loop):
        tv.press_rc_key(rc.CHANNEL_DOWN)
        tv.wait_in_minute(time)  # playback time
        print(f'CHANNEL UP loop count: {i}')
