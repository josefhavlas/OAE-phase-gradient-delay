import numpy as np


def findLocalMaxima(arr):
    """
        findLocalMaxima: finds all local maxima (their indeces)

        INPUT:
            arr - array where we want to find the maxima, shape: (n_elem, )

        OUTPUT: 
            max - array containing indeces where maxima occur, shape: (n_max_el, )
    """
    len = np.size(arr)
    max = []  # to store indeces of local maxima

    if (arr[0] > arr[1]):  # if the first point local maxima or not
        max.append(0)

    for i in range(1, len-1):  # iteration through whole arr
        if (arr[i-1] < arr[i] > arr[i + 1]):
            max.append(i)  # adding a new local maximum

    if (arr[-1] > arr[-2]):
        max.append(len-1)  # if the last point local maxima or not

    return max


def findGlobalMaximum(arr):
    """
        findGlobalMaximum: finds global maximum in arr (its index)

        INPUT:
            arr - array where we want to find the maximum, shape: (n_elem, )

        OUTPUT: 
            max - index where the global maximum is located in arr, shape: scalar
    """
    max = np.argmax(arr)
    return max


def peakNeighbours(peak_arr, shift, freq_range):
    """
        peakNeighbours: finds the nearest samples from a (peak) point in both directions

        INPUT:
            peak_arr - array containing indeces of peaks, shape: (n, ),
            shift - number of desired points in both directions +-, shape: scalar,
            freq_range - maximum index on the frequency axis, shape: scalar

        OUTPUT: 
            peaks_ext - array containing indeces of peaks extended by their neighbourhood, shape: (n*(2*shift + 1), )
    """
    peaks_ext = []  # to be returned (extended peaks)
    n = np.size(peak_arr)  # number of given peaks

    for i in range(0, n):
        for j in range(-shift, shift+1):
            new_neigh = peak_arr[i]+j
            if new_neigh >= 0 and new_neigh < freq_range:  # if not out of range
                peaks_ext.append(new_neigh)

    return peaks_ext
