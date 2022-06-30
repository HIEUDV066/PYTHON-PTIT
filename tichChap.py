import numpy as np

import convolute_lib as cnn


in_img = np.array([[0, 0, 0, 0, 0, 0, 0],
                    [0, 5, 7, 4, 4, 4, 0],
                    [0, 7, 2, 4, 4, 6, 0],
                    [0, 1, 5, 1, 3, 1, 0],
                    [0, 5, 1, 3, 4, 2, 0],
                    [0, 7, 6, 4, 6 ,6, 0],
                    [0, 0, 0, 0, 0, 0, 0]
                    ])

kernel = np.array([[-1, -2, -1],
                   [0, 0, 0],
                   [1, 2, 1]])



out_img = cnn.convolve_np2(in_img, kernel)
with np.printoptions(suppress=True):
    print(out_img)