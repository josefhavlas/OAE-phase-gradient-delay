import numpy as np


def calcDelay(x_axis, arr):

    # unwrapped phase of SFOAE and its gradient ~ phase delay
    phase_unwrap = np.unwrap(np.angle(arr))
    # difference between neighbour samples on the frequency axis (evenly spaced)
    # step_size_SFOAE = freq_SFOAE[1] - freq_SFOAE[0]
    # phase_grad_SFOAE = np.gradient(phase_unwrap_SFOAE, step_size_SFOAE)
    phase_gradient = np.gradient(phase_unwrap, x_axis)
    group_delay = -phase_gradient/(2*np.pi)

    return group_delay