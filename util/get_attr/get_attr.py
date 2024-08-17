#!/usr/bin/env python3
import numpy as np

class array:
    '''
    Simple test case for array data
    '''
    def __init__(self, size, default):
        self.size = size
        self.default = default
        self.data = np.ones(size)*default

    def __getattr__(self, name):
        return self.data




if __name__=="__main__":
    arr = array(10, 2)
    print(arr.fuck)
