from evdev import InputDevice, categorize, ecodes

controller = InputDevice('/dev/input/event2')

for event in controller.read_loop():
    # if event.type == ecodes.EV_KEY:
    # print categorize(event)

    # Codes are unique
    print "code %d" % event.code

    # types are semi-unique
    print "type %d" % event.type

    # value is value dude (1 is pressed 0 is not)
    print "value %d\n\n" % event.value

    # elif event.type == ecodes.EV_ABS:
    # 	print categorize(event)


# catch KeyboardInterrupt
    # exit()
