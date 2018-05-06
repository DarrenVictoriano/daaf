"""This is an ADB shell action script framework"""
import subprocess
import time


def launch_app(app_pkg):
    """Launch the app_pkg via adb"""
    try:
        out = subprocess.check_call(f'adb shell monkey -p {app_pkg} 1')
        # return out.decode('utf-8')
    except Exception as e:
        print(e)
        return f'Error while executing command\n {out}\n error was: {e}'


def press_rc_key(rc_keycode):
    """press the specified remote control key code"""
    try:
        out = subprocess.check_call(f'adb shell input keyevent {rc_keycode}')
        wait_in_seconds(.500)
        # return out.decode('utf-8')
    except Exception as e:
        print(e)
        return f'Error while executing command\n {out}\n error was: {e}'


def wait_a_sec(sec=1):
    """Pauses the script based on specified time (in seconds)"""
    try:
        sec = float(sec)
    except ValueError:
        print("Enter only Integer or a Float")
    time.sleep(sec)


