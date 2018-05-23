# First import the ADB_Action_Script.py it must be on the same folder
from ADB_Action_Scipt import ActionScript
# then import the RC keys and App PKGs for easy scripting
from ADB_Action_Scipt import SonyRCKey
from ADB_Action_Scipt import AppLists

# create an instance of the class, variables can be change
uroboros = ActionScript()
rc = SonyRCKey()
app = AppLists()

# user input
loop_count = input("Enter how many loop: ")

# start scripting
uroboros.launch_app(app.NETFLIX_pkg)
uroboros.wait_a_sec() # will wait 1 seconds
uroboros.press_rc_key(rc.POWER)
uroboros.wait_a_sec(23) # will wait 23 seconds

# force stop app first then launch it
# usefull if TV is slow
uroboros.clear_launch_app(app.NETFLIX_pkg)

# using for loop from 1 to 10
for i in range(1, 10):
    uroboros.press_rc_key(rc.POWER)
    uroboros.wait_a_sec(2)
    print(f'loop count: {i}')

# using for loop from 1 to loop_count
for i in range(1, loop_count):
    uroboros.press_rc_key(rc.POWER)
    uroboros.wait_a_sec(2)
    print(f'loop count: {i}')
