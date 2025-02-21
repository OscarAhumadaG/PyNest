

import numpy as np

"""
Create a function named calculate() in mean_var_std.py that uses Numpy to output 
the mean, variance, standard deviation, max, min, and sum of the rows, columns, 
and elements in a 3 x 3 matrix.The input of the function should be a list 
containing 9 digits. The function should convert the list into a 3 x 3 Numpy array, 
and then return a dictionary containing the mean, variance, standard deviation, 
max, min, and sum along both axes and for the flattened matrix. The returned dictionary
 should follow this format:
{
  'mean': [axis1, axis2, flattened],
  'variance': [axis1, axis2, flattened],
  'standard deviation': [axis1, axis2, flattened],
  'max': [axis1, axis2, flattened],
  'min': [axis1, axis2, flattened],
  'sum': [axis1, axis2, flattened]
}
"""

def calculate(data_list):
    if len(data_list) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(data_list).reshape((3,3))

    calculations = {
        "mean" : [np.mean(matrix, axis=0).tolist(), np.mean(matrix, axis=1).tolist(), float(np.mean(matrix))],
        "variance" :  [np.var(matrix, axis=0).tolist(), np.var(matrix, axis=1).tolist(), float(np.var(matrix))],
        'standard deviation' : [np.std(matrix, axis=0).tolist(), np.std(matrix, axis=1).tolist(), float(np.std(matrix))],
        'max' : [np.max(matrix, axis=0).tolist(), np.max(matrix, axis=1).tolist(), float(np.max(matrix))],
        'min': [np.min(matrix, axis=0).tolist(), np.min(matrix, axis=1).tolist(), float(np.min(matrix))],
        'sum': [np.sum(matrix, axis=0).tolist(), np.sum(matrix, axis=1).tolist(), float(np.sum(matrix))],
    }
    return calculations

l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]

print(calculate(l1))