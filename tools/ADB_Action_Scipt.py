import subprocess
import time


class ActionScript:
    """This is an ADB shell action script framework"""

    def __init__(self, deviceID="none"):
        self.deviceID = deviceID

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
        if self.deviceID == "none":
            return self.__execute_cmd(f'adb {cmd}'.split(" "))
        else:
            return self.__execute_cmd(f'adb -s {self.deviceID} {cmd}'.split(" "))
            # adb -s {device} {cmd}'.split(" ") for specific device

    def launch_app(self, app_pkg):
        """Launch the app_pkg via adb using monkey command"""
        try:
            out = self.send_adb(f'shell monkey -p {app_pkg} 1')
            print(f'{app_pkg} has been launch!')
        except Exception as e:
            print(e)
            print(f'Error while executing command\n {out}\n error was: {e}')

    def clear_launch_app(self, app_pkg, app_activity):
        """Launch the app pkg and act via adb using am start command"""
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
    def wait_in_second(sec):
        """Pauses the script based on specified time (in seconds)"""
        try:
            sec = float(sec)
        except ValueError:
            print("Only Integer or Float is acceptable")
        print(f'pause for {sec} seconds')
        time.sleep(sec)

    @staticmethod
    def wait_in_minute(min):
        """Pauses the script based on specified time (in seconds)"""
        try:
            sec = float(min) * 60.0
            out = float(sec)
        except ValueError:
            print("Only Integer or Float is acceptable")
        print(f'pause for {min} minute/s')
        time.sleep(out)

    @staticmethod
    def wait_in_hour(hr):
        """Pauses the script based on specified time (in seconds)"""
        try:
            sec = float(hr) * 3600.0
            out = float(sec)
        except ValueError:
            print("Only Integer or Float is acceptable")
        print(f'pause for {hr} hour/s')
        time.sleep(out)

    def get_activity(self, app_pkg):
        """get the main activity of the given app package"""
        try:
            out = subprocess.check_output(
                f'adb shell "cmd package resolve-activity --brief {app_pkg} | tail -n 1"')
            print(out)
            return out
        except Exception as e:
            print(e)
            return f'Error while executing command\n {out}\n error was: {e}'

    def get_activity_mfocus(self):
        """get the main activity of the given app package"""
        try:
            out = subprocess.check_output(
                "adb shell dumpsys window windows | grep -E 'mCurrentFocus|mFocusedApp'")
            print(out)
            return out
        except Exception as e:
            print(e)
            return f'Error while executing command\n {out}\n error was: {e}'

# adb shell settings put system accelerometer_rotation 0
