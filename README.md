# RP2040PicoW
RP2040 Pico W, Sunfounder Kepler kit, Waveshare and Pimoroni code for sharing.

Initial day, starting out on Day's of yorecode.

First up is a little text scrolling routine for insertion in Paul McWhorter's lcd1602.py, which is configured for Pin 6,7 an I<sup>2</sup>C 1.

New to github, this is not a fork, pull request yet, just a code fragment for inclusion in the LCD class of lcd1602.py, add to the bottom of the LCD class.
First day, will polish, maybe.

```python
    def scrollright(self, x, y, str):
        if x < 0:
            x = 0
        if x > 15:
            x = 15
        if y < 0:
            y = 0
        if y > 1:
            y = 1

        # Loop while clearing and shuffling
        while x < 16 - len(str):
            self.clear()

            # Move cursor
            addr = 0x80 + 0x40 * y + x
            self.send_command(addr)

            for chr in str:
                self.send_data(ord(chr))

            x = x + 1
            time.sleep(0.3)

    def scrollleft(self, x, y, str):
        pos = 0
        if x < 0:
            x = 0
        if x > 15:
            x = 15
        if y < 0:
            y = 0
        if y > 1:
            y = 1

        # Loop while clearing and shuffling
        while pos < len(str) - 16:
            self.clear()

            # Move cursor
            addr = 0x80 + 0x40 * y + x
            self.send_command(addr)

            for chr in str[pos:]:
                self.send_data(ord(chr))

            pos = pos + 1
            time.sleep(0.3)
```
