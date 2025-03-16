# Note: Currently the firmware is only for testing the hardware. Pins are correct
import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

from kmk.extensions.RGB import RGB

from kmk.modules.encoder import EncoderHandler


# Inits
keyboard = KMKKeyboard()


# Modules
encoder_handler = EncoderHandler()

keyboard.modules = [encoder_handler]


# Extension - RGB
rgb = RGB(pixel_pin=board.GP1, num_pixels=85)
keyboard.extensions.append(rgb)


# Matrix config
keyboard.col_pins = (
    board.GP4,
    board.GP5,
    board.GP6,
    board.GP7,
    board.GP8,
    board.GP9,
    board.GP10,
    board.GP11,
    board.GP12,
)
keyboard.row_pins = (
    board.GP13,
    board.GP14,
    board.GP15,
    board.GP16,
    board.GP17,
    board.GP18,
    board.GP21,
    board.GP35,
    board.GP36,
    board.GP37,
)
keyboard.diode_orientation = DiodeOrientation.COL2ROW


# Encoder config
encoder_handler.pins = ((board.GP45, board.GP46, board.GP47, False),)


# TODO: Add status and effect leds: Needs to be handled separately
# TODO: Fillin keymap - research special keys with KMK, MacOS support, different languages

# Keymap
keyboard.keymap = []

encoder_handler.map = [
    ((KC.UP, KC.DOWN, KC.MUTE),),
]


# Loop
if __name__ == "__main__":
    keyboard.go()
