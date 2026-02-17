import RPi.GPIO as GPIO
import signal_generator as sg
import time
import RPi.GPIO as GPIO

def decimal2binary(n):
    return [int(bit) for bit in bin(n)[2:].zfill(8)]

class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose=False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial=GPIO.LOW)

    def deinit(self):
        GPIO.output(self.gpio_bits, GPIO.LOW)
        GPIO.cleanup(self.gpio_bits)

    def set_number(self, number):
        number = max(0, min(255, int(number)))
        bits = decimal2binary(number)
        GPIO.output(self.gpio_bits, bits)

    def set_voltage(self, voltage):
        if voltage < 0.0:
            clamped = 0.0
        elif voltage > self.dynamic_range:
            clamped = self.dynamic_range
            if self.verbose:
                print(f"Напряжение превышает максимум ({self.dynamic_range:.3f} В)")
        else:
            clamped = voltage

        number = int(clamped / self.dynamic_range * 255)
        number = max(0, min(255, number))
        self.set_number(number)


if __name__ == '__main__':
    amplitude = 3.2
    signal_frequency = 10
    sampling_frequency = 1000

    GPIO_PINS = [16, 20, 21, 25, 26, 17, 27, 22]
    DYNAMIC_RANGE = 3.183

    dac = None
    try:
        dac = R2R_DAC(gpio_bits=GPIO_PINS, dynamic_range=DYNAMIC_RANGE, verbose=True)
        start_time = time.time()

        while True:
            t = time.time() - start_time
            norm_amp = sg.get_sin_wave_amplitude(signal_frequency, t)
            voltage = norm_amp * amplitude
            dac.set_voltage(voltage)
            sg.wait_for_sampling_period(sampling_frequency)


    finally:
        if dac is not None:
            dac.deinit()