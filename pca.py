from scipy.optimize import curve_fit
import numpy as np


def fitCurve(x_values, y_values):
    """
        fitCurve: finds a best fit, i.e. a curve that is fitted between given points

        INPUT:
            x_values - values measured on the x-axis, shape: (n, )
            y_values - values measured on the y-axis (w.r.t. the x-axis), shape: (n, )

        OUTPUT:
            curve - fitted curve (n, )
    """
    def curve_fcn(x_values, a, b, c):
        # return a*x_values + b  # linear function

        return a*x_values**2 + b*x_values + c
        # return a * np.exp(b * x_values)
        # return a * np.sin(b * x_values)

    # optimization
    params, _ = curve_fit(curve_fcn, x_values, y_values)

    # reconstruction of the line
    curve = curve_fcn(x_values, params[0], params[1], params[2])
    return curve


def fitLin(A, k):
    """
        fitLin: fits a linear subspace of dimension k between points given in matrix A

        INPUT:
            A - given points, shape: (n_dim, n_points),
            k - dimension of the approximation (must be less then dim(A)), shape: scalar

        OUTPUT:
            U - orthogonal basis in columns of desired linspace, shape: (n_dim, k),
            C - columns contain coordinates w.r.t. the basis, shape: (k, n_points)
    """
    lambdas, vectors = np.linalg.eig(np.dot(A, A.T))
    # sorting lambdas in ascending trend (and also vectors)
    lambdas_sorted = np.argsort(lambdas)
    vectors = vectors[:, lambdas_sorted]

    n = np.size(vectors, axis=1)
    U = vectors[:, n-k:]  # span of desired linspace

    B = np.dot(U, np.dot((U.T), A))
    C = np.dot(U.T, B)
    return U, C


def fitAff(A, k):
    """
        fitAff: fits an affine subspace of dimension k between points given in matrix A

        INPUT:
            A - given points, shape: (n_dim, n_points),
            k - dimension of the approximation (must be less then dim(A)), shape: scalar

        OUTPUT:
            B - matrix with approximated points, shape: (n_dim, n_points),
    """
    centroid = np.mean(A, axis=1)  # points aligned in columns of matrix A
    centroid = np.reshape(centroid, (np.size(centroid), 1))

    A_shift = A - centroid  # shifting the set of points to the origin

    U, C = fitLin(A_shift, k)
    b0 = centroid

    # points on the line which was found
    B = np.dot(b0, np.ones((1, np.size(C, axis=1)))) + np.dot(U, C)
    return B


def plot2DFitLine(B, ax):
    """
        plot2DFitLine: plots a line in 2-D which was previously fitted between given points

        INPUT:
            B - points which were found and should be on the line, shape: (2, n_points),
            ax - axis feature of a figure gained from plt.subplots()

        OUTPUT:
            Nothing. Just a plotted line.
    """
    # indeces of edges (x-axis)
    min_idx = np.argmin(B, axis=1)[0]
    max_idx = np.argmax(B, axis=1)[0]

    # bounds of the line
    init_point = B[:, min_idx]
    end_point = B[:, max_idx]

    edges_x = np.array([init_point[0], end_point[0]])
    edges_y = np.array([init_point[1], end_point[1]])

    # plotting the fitted line
    ax.plot(edges_x, edges_y, "m", label='line fitted with PCA')

    return
