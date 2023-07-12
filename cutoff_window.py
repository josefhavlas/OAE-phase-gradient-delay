"""
Cutoff window using recursive-exponential filter

Author: havlajos
Created: 16/03/2023
Last Update: 09/07/2023

Description: The window is used to cut off specific quefrencies in the cepstral analysis method.
"""

import numpy as np


def getGammaLarge(n, x_axis):
    """
        getGammaLarge: calculates the large gamma according to Shera, Zweig (1993) algorithm

        INPUT:
            n - order of the smoothing function, shape: scalar
            x_axis - axis on which we want to cut off, shape: (n_elem, )

        OUTPUT: 
            gamma - calculated large gamma for given x-axis, shape: (n_elem, )
    """
    gamma = np.exp(x_axis**2)  # initiating value for n=1
    for _ in range(2, n):  # continue for the rest iterations
        gamma = np.exp(gamma - 1)

    return gamma


def getGammaSmall(n):
    """
        getGammaSmall: calculates the small gamma according to Shera, Zweig (1993) algorithm

        INPUT:
            n - order of the smoothing function, shape: scalar

        OUTPUT: 
            gamma - calculated small gamma, shape: scalar
    """
    gamma = 1  # initiating value for n=1
    for _ in range(2, n):  # continue for the rest iterations
        gamma = np.log(gamma + 1)

    return gamma


def getWindow(x_axis, cutoff, n):
    """
        getWindow: calculates the window using the "recursive-exponential" filter

        INPUT:
            x_axis - axis on which we want to cut off, shape: (n_elem, )
            cutoff - the symmetric cutoff on the x-axis, shape: scalar
            n - order of the smoothing function, shape: scalar

        OUTPUT: 
            S_n - cutoff window, shape: (n_elem, )
    """
    # both gammas given recursively
    g_n = getGammaSmall(n)

    # scaling the x_axis
    scale_factor = np.sqrt(g_n)  # lambda in the paper
    t = scale_factor*x_axis/cutoff
    G_n = getGammaLarge(n, t)

    S_n = 1/G_n  # the final window
    return S_n
