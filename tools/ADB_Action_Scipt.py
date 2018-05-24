import subprocess
import time


class ActionScript:
    """This is an ADB shell action script framework"""

    @staticmethod
    def __execute_cmd(adb):
        """this will send the command to the shell"""
        try:
            out = subprocess.check_output(adb)
            return out
        except Exception as e:
            print(e)

    def send_adb(self, cmd):
        """compose the command as an adb shell command"""
        # adb -s {device} {cmd}'.split(" ") for specific device
        return self.__execute_cmd(f'adb {cmd}'.split(" "))

    def launch_app(self, app_pkg):
        """Launch the app_pkg via adb using monkey command"""
        try:
            out = self.send_adb(f'shell monkey -p {app_pkg} 1')
            print(f'{app_pkg} has been launch!')
        except Exception as e:
            print(e)
            print(f'Error while executing command\n {out}\n error was: {e}')

    def clear_launch_app(self, app_pkg, app_activity):
        """Launch the app_pkg via adb using am start command, requires activity"""
        try:
            out = self.send_adb(f'shell am start -S {app_pkg}/{app_activity}')
            print(f'{app_pkg} has been launch!')
        except Exception as e:
            print(e)
            print(f'Error while executing command\n {out}\n error was: {e}')

    def press_rc_key(self, rc_key):
        """press the specified remote control key code"""
        try:
            out = self.send_adb(f'shell input keyevent {rc_key}')
            print(f'{rc_key} sent!')
        except Exception as e:
            print(e)
            print(f'Error while executing command\n {out}\n error was: {e}')

    @staticmethod
    def wait_a_sec(sec=1.0):
        """Pauses the script based on specified time (in seconds)"""
        try:
            sec = float(sec)
            print(f'pause for {sec} seconds')
        except ValueError:
            print("Only Integer or Float is acceptable")
        time.sleep(sec)

    def get_activity(self, app_pkg):
        """get the main activity of the given app package"""
        try:
            out = subprocess.check_output(f'adb shell "cmd package resolve-activity --brief {app_pkg} | tail -n 1"')
            print(out)
            return out
        except Exception as e:
            print(e)
            return f'Error while executing command\n {out}\n error was: {e}'

    def get_activity_mfocus(self):
        """get the main activity of the given app package"""
        try:
            out = subprocess.check_output("adb shell dumpsys window windows | grep -E 'mCurrentFocus|mFocusedApp'")
            print(out)
            return out
        except Exception as e:
            print(e)
            return f'Error while executing command\n {out}\n error was: {e}'

# adb shell settings put system accelerometer_rotation 0

#############################################
# Below is the list of RC keys for Sony TVs #
#############################################
class SonyRCKey:
    """A list of remote control key codes for Sony TV"""

    def __init__(self):
        """initialize key codes"""
        self.POWER = 'KEYCODE_POWER'
        self.INPUT = "KEYCODE_TV_INPUT"
        self.BRAIVA_SYNC_MENU = "KEYCODE_BUTTON_3"
        self.STB_MENU = "KEYCODE_BUTTON_10"

        self.NUMBER_0 = "KEYCODE_0"
        self.NUMBER_1 = "KEYCODE_1"
        self.NUMBER_2 = "KEYCODE_2"
        self.NUMBER_3 = "KEYCODE_3"
        self.NUMBER_4 = "KEYCODE_4"
        self.NUMBER_5 = "KEYCODE_5"
        self.NUMBER_6 = "KEYCODE_6"
        self.NUMBER_7 = "KEYCODE_7"
        self.NUMBER_8 = "KEYCODE_8"
        self.NUMBER_9 = "KEYCODE_9"
        self.DOT = "KEYCODE_PERIOD"

        self.GOOGLE_PLAY = "KEYCODE_BUTTON_8"
        self.NETFLIX = "KEYCODE_BUTTON_4"
        self.YOUTUBE = "KEYCODE_BUTTON_9"
        self.YELLOW = "KEYCODE_PROG_YELLOW"
        self.BLUE = "KEYCODE_PROG_BLUE"
        self.RED = "KEYCODE_PROG_RED"
        self.GREEN = "KEYCODE_PROG_GREEN"

        self.ACTION_MENU = "KEYCODE_BUTTON_2"
        self.GUIDE = "KEYCODE_GUIDE"
        self.APPS = "KEYCODE_ALL_APPS"
        self.BACK = "KEYCODE_BACK"
        self.HOME = "KEYCODE_HOME"
        self.TV = "KEYCODE_TV"

        self.NAV_UP = "KEYCODE_DPAD_UP"
        self.NAV_DOWN = "KEYCODE_DPAD_DOWN"
        self.NAV_LEFT = "KEYCODE_DPAD_LEFT"
        self.NAV_RIGHT = "KEYCODE_DPAD_RIGHT"
        self.NAV_ENTER = "KEYCODE_DPAD_CENTER"

        self.VOLUME_UP = "KEYCODE_VOLUME_UP"
        self.VOLUME_DOWN = "KEYCODE_VOLUME_DOWN"
        self.JUMP = "KEYCODE_LAST_CHANNEL"
        self.MUTE = "KEYCODE_VOLUME_MUTE"
        self.CHANNEL_UP = "KEYCODE_CHANNEL_UP"
        self.CHANNEL_DOWN = "KEYCODE_CHANNEL_DOWN"

        self.AUDIO = "KEYCODE_MEDIA_AUDIO_TRACK"
        self.FF = "KEYCODE_MEDIA_FAST_FORWARD"
        self.PLAY = "KEYCODE_MEDIA_PLAY"
        self.RW = "KEYCODE_MEDIA_REWIND"
        self.SUBTITLE = "KEYCODE_CAPTIONS"
        self.PREV = "KEYCODE_MEDIA_PREVIOUS"
        self.PAUSE = "KEYCODE_MEDIA_PLAY_PAUSE"
        self.NEXT = "KEYCODE_MEDIA_NEXT"
        self.HELP = "KEYCODE_HELP"
        self.WIDE = "KEYCODE_TV_ZOOM_MODE"
        self.STOP = "KEYCODE_MEDIA_STOP"


####################################################
# Below is the list of app packages and activities #
####################################################
class AppLists:
    """A list of activities and packages of android app"""

    def __init__(self):
        """initialize app pkgs and activities"""
        # List of app pkgs
        self.NETFLIX_pkg = "com.netflix.ninja"
        self.AMAZON_pkg = "com.amazon.amazonvideo.livingroom"
        self.HULU_pkg = "com.hulu.livingroomplus"
        self.YOUTUBE_pkg = "com.google.android.youtube.tv"
        self.VUDU_pkg = "air.com.vudu.air.DownloaderTablet"

        # List of app app_activity
        self.NETFLIX_act = "com.netflix.ninja.MainActivity"
        self.AMAZON_act = "com.amazon.ignition.IgnitionActivity"
        self.HULU_act = "com.hulu.livingroomplus.MainActivity"
        self.YOUTUBE_act = "com.google.android.apps.youtube.tv.cobalt.activity.ShellActivity"
        self.VUDU_act = "com.vudu.android.app.activities.NavigationListActivity"
