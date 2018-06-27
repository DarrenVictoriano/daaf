# include path for /tools folder
import sys
import os.path

tool_dir = (os.path.abspath(
	os.path.join(os.path.dirname(__file__), '..', '..')) + '/tools/')
sys.path.append(tool_dir)

from ADB_Action_Scipt import ActionScript
from RC_Code import SonyRCKey
from AppList import AppList

# create an instance of the class, variables can be change
tv = ActionScript()
rc = SonyRCKey()
app = AppList()

counter = 0

# Print Requirements
print("This script is for checking Parental Locks on external inputs:")
print("Requirements:")
print("keep the parental lock password as 0000")
print("Parental lock should be OFF initially after every input check\n")


def navigateToParentalLocks():
	tv.clear_launch_app(app.PARENTALLOCK_PKG, app.PARENTALLOCK_ACT)

def parentalLock_counter_to_zero():
	global counter
	counter = 0
	tv.clear_launch_app(app.PARENTALLOCK_PKG, app.PARENTALLOCK_ACT)
	for i in range(0, 5):
		tv.press_rc_key(rc.ENTER)
	tv.press_rc_key(rc.HOME)


def lock_hdmi1():
	navigateToParentalLocks()
	global counter
	counter = 1
	for i in range(0, 4):
		tv.press_rc_key(rc.ENTER)

	tv.press_rc_key(rc.ENTER)

	for i in range(0, 3):
		tv.press_rc_key(rc.DOWN)

	tv.press_rc_key(rc.ENTER)

	# Select HDMI1
	tv.press_rc_key(rc.ENTER)
	tv.wait_in_second(3)

	# Switching to HDMI1
	tv.press_rc_key(rc.HDMI1)
	print("Verify that the lock is ON\n")
	tv.wait_in_second(3)

	tv.press_rc_key(rc.HOME)
	navigateToParentalLocks()

	for i in range(0, 4):
		tv.press_rc_key(rc.ENTER)

	for i in range(0, 3):
		tv.press_rc_key(rc.DOWN)

	tv.press_rc_key(rc.ENTER)
	tv.press_rc_key(rc.ENTER)

	# Confirm HDMI is unlocked
	tv.press_rc_key(rc.HDMI1)
	print("Confirm that the input is unlocked")
	tv.wait_in_second(3)
	print("Switching to Home screen")
	tv.press_rc_key(rc.HOME)
	restart = input("Press any key to restart or q to quit!")
	if restart == "q":
		restart = False


def lock_hdmi2():
	navigateToParentalLocks()
	global counter
	counter = 1

	for i in range(0, 4):
		tv.press_rc_key(rc.ENTER)

	tv.press_rc_key(rc.ENTER)

	for i in range(0, 3):
		tv.press_rc_key(rc.DOWN)

	tv.press_rc_key(rc.ENTER)

	# Select HDMI2
	tv.press_rc_key(rc.DOWN)
	tv.press_rc_key(rc.ENTER)
	tv.wait_in_second(3)

	# Switching to HDMI2
	tv.press_rc_key(rc.HDMI2)
	print("Verify that the lock is ON")
	tv.wait_in_second(3)

	tv.press_rc_key(rc.HOME)
	navigateToParentalLocks()

	for i in range(0, 4):
		tv.press_rc_key(rc.ENTER)

	for i in range(0, 3):
		tv.press_rc_key(rc.DOWN)

	tv.press_rc_key(rc.ENTER)
	tv.press_rc_key(rc.DOWN)
	tv.press_rc_key(rc.ENTER)

	# Confirm HDMI2 is unclocked
	tv.press_rc_key(rc.HDMI2)
	print("Confirm that the input is unlocked")
	tv.wait_in_second(3)
	print("Switching to Home screen")
	tv.press_rc_key(rc.HOME)
	restart = input("Press any key to restart or q to quit!")
	if restart == "q":
		restart = False


def lock_hdmi3():
	navigateToParentalLocks()
	global counter
	counter = 1

	for i in range(0, 4):
		tv.press_rc_key(rc.ENTER)

	tv.press_rc_key(rc.ENTER)

	for i in range(0, 3):
		tv.press_rc_key(rc.DOWN)

	tv.press_rc_key(rc.ENTER)

	# Select HDMI3
	tv.press_rc_key(rc.DOWN)
	tv.press_rc_key(rc.DOWN)
	tv.press_rc_key(rc.ENTER)
	tv.wait_in_second(3)

	# Switching to HDMI3
	tv.press_rc_key(rc.HDMI3)
	print("Verify that the lock is ON")
	tv.wait_in_second(3)

	tv.press_rc_key(rc.HOME)
	navigateToParentalLocks()

	for i in range(0, 4):
		tv.press_rc_key(rc.ENTER)

	for i in range(0, 3):
		tv.press_rc_key(rc.DOWN)

	tv.press_rc_key(rc.ENTER)
	tv.press_rc_key(rc.DOWN)
	tv.press_rc_key(rc.DOWN)
	tv.press_rc_key(rc.ENTER)

	# Confirm HDMI3 is unlocked
	tv.press_rc_key(rc.HDMI3)
	print("Confirm that the input is unlocked")
	tv.wait_in_second(3)
	print("Switching to Home screen")
	tv.press_rc_key(rc.HOME)
	restart = input("Press any key to restart or q to quit!")
	if restart == "q":
		restart = False


def lock_hdmi4():
	navigateToParentalLocks()
	global counter
	counter = 1

	for i in range(0, 4):
		tv.press_rc_key(rc.ENTER)

	tv.press_rc_key(rc.ENTER)

	for i in range(0, 3):
		tv.press_rc_key(rc.DOWN)

	tv.press_rc_key(rc.ENTER)

	# Select HDMI4
	tv.press_rc_key(rc.DOWN)
	tv.press_rc_key(rc.DOWN)
	tv.press_rc_key(rc.DOWN)
	tv.press_rc_key(rc.ENTER)
	tv.wait_in_second(3)

	# Switching to HDMI4
	tv.press_rc_key(rc.HDMI4)
	print("Verify that the lock is ON")
	tv.wait_in_second(3)

	tv.press_rc_key(rc.HOME)
	navigateToParentalLocks()

	for i in range(0, 4):
		tv.press_rc_key(rc.ENTER)

	for i in range(0, 3):
		tv.press_rc_key(rc.DOWN)

	tv.press_rc_key(rc.ENTER)
	tv.press_rc_key(rc.DOWN)
	tv.press_rc_key(rc.DOWN)
	tv.press_rc_key(rc.DOWN)
	tv.press_rc_key(rc.ENTER)

	# Confirm HDMI4 is unlocked
	tv.press_rc_key(rc.HDMI4)
	print("Confirm that the input is unlocked")
	tv.wait_in_second(3)
	print("Switching to Home screen")
	tv.press_rc_key(rc.HOME)
	restart = input("Press any key to restart or q to quit!")
	if restart == "q":
		restart = False


start = input("Press Enter when ready to start the script")
print("\n")
restart = True

while restart == True:

	#start = input("Please tune to Home screen and press enter\n")
	hdmiInput = int(input("Please enter which HDMI is being tested (1,2,3 or 4):"))
	print("\n")
	# Navigating to settings and opening Parental locks
	if counter != 0:
		print("Switching Parental lock off")
		parentalLock_counter_to_zero()

	elif hdmiInput == 1:
		lock_hdmi1()

	elif hdmiInput == 2:
		lock_hdmi2()

	elif hdmiInput == 3:
		lock_hdmi3()

	elif hdmiInput == 4:
		lock_hdmi4()

	else:
		print("Wrong input please run script again:")
		restart = input("Press any key to restart or q to quit!")
		if restart == "q":
			restart = False
