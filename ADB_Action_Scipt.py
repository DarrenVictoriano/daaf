import subprocess
import time


class ActionScript:
    """This is an ADB shell action script framework"""

    @staticmethod
    def __execute_cmd(adb):
        """this will send the command to the shell"""
        try:
            out = subprocess.check_call(adb)
            return out
        except Exception as e:
            print(e)

    def send_adb(self, cmd, device=""):
        """compose the command as an adb shell command"""
        return self.__execute_cmd(f'adb -s {device} {cmd}'.split(" "))

    def launch_app(self, app_pkg):
        """Launch the app_pkg via adb using monkey command"""
        try:
            out = self.send_adb(f'shell monkey -p {app_pkg} 1')
            return f'{app_pkg} has been launch!'
        except Exception as e:
            print(e)
            return f'Error while executing command\n {out}\n error was: {e}'

    def launch_activity(self, app_pkg, app_activity):
        """Launch the app_pkg via adb using am start command, requires activity"""
        try:
            out = self.send_adb(f'shell am start -S {app_pkg}/{app_activity}')
            return f'{app_pkg} has been launch!'
        except Exception as e:
            print(e)
            return f'Error while executing command\n {out}\n error was: {e}'

    def press_rc_key(self, rc_key):
        """press the specified remote control key code"""
        try:
            out = self.send_adb(f'shell input keyevent {rc_key}')
            return f'{rc_key} sent!'
        except Exception as e:
            print(e)
            return f'Error while executing command\n {out}\n error was: {e}'

    @staticmethod
    def wait_a_sec(sec=1.0):
        """Pauses the script based on specified time (in seconds)"""
        try:
            sec = float(sec)
        except ValueError:
            print("Only Integer or Float is acceptable")
        time.sleep(sec)

    def get_activity(self, app_pkg):
        """get the main activity of the given app package"""
        try:
            out = self.send_adb(f'shell "cmd package resolve-activity --brief {app_pkg} | tail -n 1"')
            return out
        except Exception as e:
            print(e)
            return f'Error while executing command\n {out}\n error was: {e}'


#############################################
# Below is the list of RC keys for Sony TVs #
#############################################
class SonyRCKey:
    """A list of remote control key codes for Sony TV"""

    def __init__(self):
        """initialize key codes"""
        self.POWER = 'KEYCODE_POWER'


####################################################
# Below is the list of app packages and activities #
####################################################
class AppLists:
    """A list of activities and packages of android app"""

    def __init__(self):
        """initialize app pkgs and activities"""
        # List of app pkgs
        self.NETFLIX_pkg = "com.ninja"

        # List of app activities
        self.NETFLIX_act = "com.ninja.activity"
