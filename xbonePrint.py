from evdev import InputDevice, categorize, ecodes
import time

controller = InputDevice('/dev/input/event2')

# Event.code
START = 315
SELECT = 314
GUIDE = 316
A = 304
B = 305
X = 307
Y = 308
R1 = 311
L1 = 310
R2 = 313
L2 = 312
D_VERTICAL = 17
D_HORIZONTAL = 16


try:

    for event in controller.read_loop():
           if (event.value != 0):
            if (event.code == START):
                print 'Start'
            elif (event.code == SELECT):
                print 'Select'
            elif (event.code == GUIDE):
                print 'Guide'
            elif (event.code == A):
                print 'A'
            elif (event.code == B):
                print 'B'
            elif (event.code == X):
                print 'X'
            elif (event.code == Y):
                print 'Y'
            elif (event.code == L1):
                print 'L1'
            elif (event.code == R1):
                print 'R1'
            elif (event.code == R2):
                print 'R2'
            elif (event.code == L2):
                print 'L2'
            elif (event.code == D_VERTICAL):
                if (event.value == -1):
                    print 'D Up'
                else:
                    print 'D Down'
            elif (event.code == D_HORIZONTAL):
                if (event.value == -1):
                    print 'D Left'
                else:
                    print 'D Right'

except (KeyboardInterrupt, SystemExit):
    exit()
