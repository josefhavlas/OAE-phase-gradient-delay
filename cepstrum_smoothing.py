import numpy as np
from scipy.signal import savgol_filter
from peak_picking import *


def smoothedPhi(unwrapped_phase):
    """
        smoothedPhi: smooths the input phase with a Savitzky-Golay filter and transforms it to phi variable (Eq. 17)

        INPUT:
            unwrapped_phase -  unwrapped phase of OAE data, shape: (n_elem, )

        OUTPUT: 
            phi - transformed and smoothed phase, shape: (n_elem, )
    """
    # smoothing the phase with a Savitzky-Golay filter
    smoothed_phase = savgol_filter(unwrapped_phase, 5, 1)
    # smoothing is necessary here to render the transformation monotonic
    # the minus sign then guarantees that phi increases with f
    phi = -smoothed_phase/(2*np.pi)

    # an estimate of the secular variation of the unwrapped phase from which much of
    # the phase rippling pattern has been ironed out
    return phi


def makeIncreasing(x_axis, y_signal, x_axis_target):
    """
        makeIncreasing: smooths the input phase with a Savitzky-Golay filter and transforms it to phi variable (Eq. 17)

        INPUT:
            x_axis -  ???, shape: (n_elem, )
            y_signal -  ???, shape: (n_elem, )
            x_axis_target -  ???, shape: (n_elem, )

        OUTPUT: 
            y_signal - ???, shape: (???, )
    """
    first_loc_max = findLocalMaxima(y_signal)[0]
    while (x_axis[first_loc_max] <= x_axis_target):
        y_signal = np.delete(y_signal, first_loc_max)
        first_loc_max = findLocalMaxima(y_signal)[0]

    return y_signal


def adjustPeaks(peaks_idx, x_axis_short):
    """
        adjustPeaks: 

        INPUT:
            peaks_idx -  indeces list of SFOAE local maxima, shape: (n_peaks, )
            x_axis_short -  cutoff frequency axis, shape: (m_elems, )

        OUTPUT: 
            peaks_adjusted - ???, shape: (x, )
    """
    peaks_adjusted = peaks_idx
    for peak in np.flip(peaks_idx):
        if peak > np.size(x_axis_short) - 1:
            peaks_adjusted = np.delete(
                peaks_adjusted, np.where(peaks_adjusted == peak))
        else:
            break

    return peaks_adjusted
