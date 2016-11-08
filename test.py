from evdev import InputDevice, categorize, ecodes

controller = InputDevice('/dev/input/event2')

for event in controller.read_loop():
	# if event.type == ecodes.EV_KEY:
	# print categorize(event)

	##Codes are unique
	print "code %d" %event.code
	
	##sec is time (im like 99% sure)
	print "sec %d" %event.sec
	
	##types are semi-unique
	print "type %d" %event.type
	
	##usec is unknown probably related to time as well
	print "usec %d" %event.usec

	#value is value dude (1 is pressed 0 is not)
	print "value %d" %event.value
	

	# elif event.type == ecodes.EV_ABS:
	# 	print categorize(event)


# catch KeyboardInterrupt
	# exit()
