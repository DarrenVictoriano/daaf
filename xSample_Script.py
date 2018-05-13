# First import the ADB_Action_Script.py it must be on the same folder
from ADB_Action_Scipt import ActionScript
# then import the RC keys and App PKGs for easy scripting
from ADB_Action_Scipt import SonyRCKey
from ADB_Action_Scipt import AppLists

# create an instance of the class
uroboros = ActionScript()
rc = SonyRCKey()
app = AppLists()

# start scripting
uroboros.launch_app(app.NETFLIX_pkg)
uroboros.wait_a_sec(2)
uroboros.press_rc_key(rc.POWER)

# some apps requires an activity to be able to launch.
# in this case use this method below.
uroboros.launch_activity(app.NETFLIX_pkg, app.NETFLIX_act)

# using for loop from 1 to 10
for i in range(1, 11):
    uroboros.press_rc_key(rc.POWER)
    uroboros.wait_a_sec(2)
    print(f'loop count: {i}')
