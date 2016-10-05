#!../../vendor/micropython/unix/micropython
import sys
sys.path.append('../../src')

from trezor import ui

ui.display.backlight(255)


# header
ui.display.bar(0, 0, 240, 30, ui.ORANGE, ui.BLACK, 4)
ui.display.bar(0, 10, 240, 20, ui.ORANGE)
ui.display.text(10, 23, 'Installing firmware', ui.BOLD, ui.WHITE, ui.ORANGE)

ui.display.text_center(120, 192 + 32, "In progress ...", 1, ui.WHITE, ui.BLACK)

p = 0
while True:

    ui.display.loader(p, ui.BLUE, ui.BLACK)
    ui.display.text_center(120, 240 // 2 + 14 // 2, "%d%%" % (p // 10), 2, ui.WHITE, ui.BLACK)

    ui.display.refresh()

    p = (p + 1) % 1000