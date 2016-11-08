from evdev import InputDevice, categorize, ecodes
import time

controller = InputDevice('/dev/input/event2')

iList = ['Start', 'Select', 'Guide', 'A', 'B', 'X', 'Y', 'R1',
         'L1', 'R2', 'L2', 'D Up', 'D Down', 'D Left', 'D Right']

f = open('controllerCodes.txt', 'w')
i = 0

for button in iList:
    print 'Press ' + button + ' now: \n'
    time.sleep(1)

    for event in controller.read_loop():
        if (event.value != 0):

            f.write(button + ': \n')
        # Codes are unique
            f.write("code %d " % event.code)

        # types are semi-unique
            f.write("type %d " % event.type)

        # value is value dude (1 is pressed 0 is not)
            f.write("value %d \n\n" % event.value)
            print 'Button Collected'
            time.sleep(1)
            break

    i = 0
# elif event.type == ecodes.EV_ABS:
# 	print categorize(event)
f.close()
