from evdev import InputDevice

device = InputDevice('/dev/input/event3')

for thing in device.capabilities(verbose=True):
	print thing
	for subthing in thing: 
		print subthing