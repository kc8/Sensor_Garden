"""
Class used to help manage GPIO pins. Would like to add more functionality as time
goes on

"""

class GPIOPins:

    def __init__(self, *args):
        """class that sets up our GPIO pin configuration. This will keep track of the PINS for any
        sensor or other pin being used on the Raspberry Pi
        :args: *args: an unsorted list of GPIO pins (type int)

        TO-DO: Implement this
        """
        self._pins = list(*args)

    def get_pins(self):
        """

        :return: A generator object for each pin
        """
        for pin in self._pins:
            yield pin
