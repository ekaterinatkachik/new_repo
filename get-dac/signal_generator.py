import numpy as np
import time

def get_sin_wave_amplitude(freq, t):
    sin_val = np.sin(2 * np.pi * freq * t)
    return (sin_val + 1.0) / 2.0

def wait_for_sampling_period(sampling_frequency):    
    period = 1.0 / float(sampling_frequency)
    time.sleep(period)