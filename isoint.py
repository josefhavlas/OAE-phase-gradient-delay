import scipy.io
import numpy as np
from peak_picking import *
from gradient_delay import *


def processIsoInt(file_path):
    mat_ISOINT = scipy.io.loadmat(file_path)

    # NOT EVENLY SPACED!!!
    freq_ISOINT = mat_ISOINT['frekax'].flatten()  # frequency axis
    Y = mat_ISOINT['Y'].flatten()  # BM deviation
    Yme = mat_ISOINT['Yme'].flatten()  # stapes deviation
    # maximum index on the frequency axis
    # freq_range_ISOINT = np.size(freq_ISOINT)

    # sound wave in decibels
    filter_ISOINT = Y/Yme  # filter transfer function
    maximum_ISOINT = findGlobalMaximum(
        np.real(20*np.log10(np.abs(filter_ISOINT))))

    group_delay_ISOINT = calcDelay(freq_ISOINT, filter_ISOINT)
    group_delay_ISOINT *= 2  # Shera and Bergevin say so :)

    return freq_ISOINT, group_delay_ISOINT, maximum_ISOINT
