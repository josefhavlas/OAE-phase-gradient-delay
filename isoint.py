"""
Isointensity phase-gradient delays (at isolated frequencies)

Author: havlajos
Created: 13/04/2023
Last Update: 09/07/2023

Description: Script processing phase-gradient delays of reference nonlinear cochlear model OAE data.
"""

import scipy.io
import numpy as np
from peak_picking import *
from gradient_delay import *


def processIsoInt(file_path):
    """
        processIsoInt: computes a gradient-delay reference value for ISOINT data which are contained in a .mat file

        INPUT:
            file_path -  path from which we upload data, shape: Matlab matrix file (.mat)

        OUTPUT: 
            freq_ISOINT - frequency axis of the output gradient-delay, shape: (n_elem, )
            group_delay_ISOINT - values of the gradient-delay on the frequency axis, shape: (n_elem, )
            maximum_ISOINT - global maximum of the basilar-membrane transfer function (ROI), shape: (n_elem, )
    """
    mat_ISOINT = scipy.io.loadmat(file_path)  # loading the .mat file

    # NOT EVENLY SPACED!!!
    freq_ISOINT = mat_ISOINT['frekax'].flatten()  # frequency axis
    if "Y" in mat_ISOINT:
        Y = mat_ISOINT['Y'].flatten()  # BM deviation
    elif "Ybm" in mat_ISOINT:
        Y = mat_ISOINT['Ybm'].flatten()  # BM deviation
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
