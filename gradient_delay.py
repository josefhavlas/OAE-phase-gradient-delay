"""
Phase-gradient delay of OAE data

Author: havlajos
Created: 07/04/2023
Last Update: 09/07/2023

Description: Function calculating the phase-gradient delay of OAE data.
"""

import numpy as np


def calcDelay(x_axis, arr):
    """
        calcDelay: calculates the gradient delay of an OAE

        INPUT:
            x_axis - axis (of OAE) on which we want to calculate the gradient, shape: (n_elem, )
            arr - OAE data

        OUTPUT: 
            group_delay - gradient delay of input OAE, shape: (n_elem, )
    """
    # unwrapped phase of SFOAE and its gradient ~ phase delay
    phase_unwrap = np.unwrap(np.angle(arr))
    # difference between neighbour samples on the frequency axis (evenly spaced)
    # step_size_SFOAE = freq_SFOAE[1] - freq_SFOAE[0]
    # phase_grad_SFOAE = np.gradient(phase_unwrap_SFOAE, step_size_SFOAE)
    phase_gradient = np.gradient(phase_unwrap, x_axis)
    group_delay = -phase_gradient/(2*np.pi)

    return group_delay
