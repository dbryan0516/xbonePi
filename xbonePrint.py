from evdev import InputDevice, categorize, ecodes
import time

# Path to controller event
controller = InputDevice('/dev/input/event2')

# Event.code corresponding to Xbox One Controller
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

# TODO: Make Dictionary?
# Button States; 1 is pressed 0 is not
ACTIVE_START = 0
ACTIVE_SELECT = 0
ACTIVE_GUIDE = 0
ACTIVE_A = 0
ACTIVE_B = 0
ACTIVE_X = 0
ACTIVE_Y = 0
ACTIVE_R1 = 0
ACTIVE_L1 = 0
ACTIVE_R2 = 0
ACTIVE_L2 = 0
ACTIVE_D_UP = 0
ACTIVE_D_DOWN = 0
ACTIVE_D_LEFT = 0
ACTIVE_D_RIGHT = 0

try:

    for event in controller.read_loop():
        if (event.value != 0):
            # Button Pressed
            if (event.code == START):
                ACTIVE_START = 1
                print 'Start'
            elif (event.code == SELECT):
                ACTIVE_SELECT = 1
                print 'Select'
            elif (event.code == GUIDE):
                ACTIVE_GUIDE = 1
                print 'Guide'
            elif (event.code == A):
                ACTIVE_A = 1
                print 'A'
            elif (event.code == B):
                ACTIVE_B = 1
                print 'B'
            elif (event.code == X):
                ACTIVE_X = 1
                print 'X'
            elif (event.code == Y):
                ACTIVE_Y = 1
                print 'Y'
            elif (event.code == L1):
                ACTIVE_L1 = 1
                print 'L1'
            elif (event.code == R1):
                ACTIVE_R1 = 1
                print 'R1'
            elif (event.code == R2):
                ACTIVE_R2 = 1
                print 'R2'
            elif (event.code == L2):
                ACTIVE_L2 = 1
                print 'L2'
            elif (event.code == D_VERTICAL):
                if (event.value == -1):
                    ACTIVE_D_UP = 1
                    print 'D Up'
                else:
                    ACTIVE_D_DOWN = 1
                    print 'D Down'
            elif (event.code == D_HORIZONTAL):
                if (event.value == -1):
                    ACTIVE_D_LEFT = 1
                    print 'D Left'
                else:
                    ACTIVE_D_RIGHT = 1
                    print 'D Right'
        else:
            # Button Released
            if (event.code == START and ACTIVE_START == 1):
                ACTIVE_START = 0
                print 'Start Released'
            elif (event.code == SELECT and ACTIVE_SELECT == 1):
                ACTIVE_SELECT = 0
                print 'Select Released'
            elif (event.code == GUIDE and ACTIVE_GUIDE == 1):
                ACTIVE_GUIDE = 0
                print 'Guide Released'
            elif (event.code == A and ACTIVE_A == 1):
                ACTIVE_A = 0
                print 'A Released'
            elif (event.code == B and ACTIVE_B == 1):
                ACTIVE_B = 0
                print 'B Released'
            elif (event.code == X and ACTIVE_X == 1):
                ACTIVE_X = 0
                print 'X Released'
            elif (event.code == Y and ACTIVE_Y == 1):
                ACTIVE_Y = 0
                print 'Y Released'
            elif (event.code == L1 and ACTIVE_L1 == 1):
                ACTIVE_L1 = 0
                print 'L1 Released'
            elif (event.code == R1 and ACTIVE_R1 == 1):
                ACTIVE_R1 = 0
                print 'R1 Released'
            elif (event.code == R2 and ACTIVE_R2 == 1):
                ACTIVE_R2 = 0
                print 'R2 Released'
            elif (event.code == L2 and ACTIVE_L2 == 1):
                ACTIVE_L2 = 0
                print 'L2 Released'
            elif (event.code == D_VERTICAL):

                if (ACTIVE_D_UP == 1):
                    ACTIVE_D_UP = 0
                    print 'D Up Released'
                elif (ACTIVE_D_DOWN == 1):
                    ACTIVE_D_DOWN = 0
                    print 'D Down Released'

            elif (event.code == D_HORIZONTAL):

                if (ACTIVE_D_LEFT == 1):
                    ACTIVE_D_LEFT = 0
                    print 'D Left Released'
                elif (ACTIVE_D_RIGHT == 1):
                    ACTIVE_D_RIGHT = 0
                    print 'D Right Released'

except (KeyboardInterrupt, SystemExit):
    exit()
