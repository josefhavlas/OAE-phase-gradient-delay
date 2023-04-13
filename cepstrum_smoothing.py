import numpy as np
from scipy.signal import savgol_filter


def smoothedPhi(unwrapped_phase):

    # returns smoothed phi as in paper
    # smoothing the phase with a Savitzky-Golay filter
    smoothed_phase = savgol_filter(unwrapped_phase, 5, 1)
    # smoothing is necessary here to render the transformation monotonic
    # the minus sign then guarantees that phi increases with f
    phi = -smoothed_phase/(2*np.pi)

    return phi  # an estimate of the secular variation of the unwrapped phase from which much of the phase rippling pattern has been ironed out
