import pygame
import time
from pynput.keyboard import Controller, Key
from pynput.mouse import Controller as MouseController

BUTTON_A = 0
BUTTON_B = 1
BUTTON_X = 2
BUTTON_Y = 3
BUTTON_L1 = 4
BUTTON_R1 = 5
BUTTON_L2 = 2
BUTTON_R2 = 5
BUTTON_R3 = 9

DPAD_UP = (0, 1)
DPAD_DOWN = (0, -1)
DPAD_LEFT = (-1, 0)
DPAD_RIGHT = (1, 0)

LEFT_X_AXIS = 0
LEFT_Y_AXIS = 1

last_time = 0
DELAY = 0.2
DEADZONE = 0.2
SCROLL_SPEED = 1.5


def trigger():
    global last_time
    now = time.time()
    if now - last_time > DELAY:
        last_time = now
        return True
    return False


def main():
    keyboard = Controller()
    mouse = MouseController()

    pygame.init()
    pygame.joystick.init()

    if pygame.joystick.get_count() == 0:
        raise RuntimeError("No controller detected")

    joy = pygame.joystick.Joystick(0)
    joy.init()

    print("Controller media control active")

    while True:
        pygame.event.pump()

        # Play/Pause
        if joy.get_button(BUTTON_A) and trigger():
            keyboard.press(Key.space)
            keyboard.release(Key.space)

        # Toggle Full-screen
        if joy.get_button(BUTTON_B) and trigger():
            keyboard.press("f")
            keyboard.release("f")

        # Mute/Unmute
        if joy.get_button(BUTTON_X) and trigger():
            keyboard.press("m")
            keyboard.release("m")

        # Toggle Captions
        if joy.get_button(BUTTON_Y) and trigger():
            keyboard.press("c")
            keyboard.release("c")

        # Next tab in browser
        if joy.get_button(BUTTON_L1) and trigger():
            keyboard.press(Key.ctrl)
            keyboard.press(Key.tab)
            keyboard.release(Key.tab)
            keyboard.release(Key.ctrl)

        # Previous tab in browser
        if joy.get_button(BUTTON_R1) and trigger():
            keyboard.press(Key.ctrl)
            keyboard.press(Key.shift)
            keyboard.press(Key.tab)
            keyboard.release(Key.tab)
            keyboard.release(Key.shift)
            keyboard.release(Key.ctrl)

        # Reload current tab
        if joy.get_button(BUTTON_R3) and trigger():
            keyboard.press(Key.ctrl)
            keyboard.press("r")
            keyboard.release("r")
            keyboard.release(Key.ctrl)

        # Next window
        if joy.get_axis(BUTTON_R2) > 0.5 and trigger():
            keyboard.press(Key.alt)
            keyboard.press(Key.shift)
            keyboard.press(Key.tab)
            keyboard.release(Key.tab)
            keyboard.release(Key.shift)
            keyboard.release(Key.alt)

        hat = joy.get_hat(0)

        # Seek forward
        if hat == DPAD_LEFT and trigger():
            keyboard.press(Key.left)
            keyboard.release(Key.left)

        # Seek backward
        elif hat == DPAD_RIGHT and trigger():
            keyboard.press(Key.right)
            keyboard.release(Key.right)

        # Volume up
        elif hat == DPAD_UP and trigger():
            keyboard.press(Key.media_volume_up)
            keyboard.release(Key.media_volume_up)

        # Volume down
        elif hat == DPAD_DOWN and trigger():
            keyboard.press(Key.media_volume_down)
            keyboard.release(Key.media_volume_down)

        lx = joy.get_axis(LEFT_X_AXIS)
        ly = joy.get_axis(LEFT_Y_AXIS)

        # Scroll up/down
        if abs(ly) > DEADZONE:
            mouse.scroll(0, int(-ly * SCROLL_SPEED))

        # Scroll left/right
        if abs(lx) > DEADZONE:
            mouse.scroll(int(lx * SCROLL_SPEED), 0)

        time.sleep(0.01)


if __name__ == "__main__":
    main()
