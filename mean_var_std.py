import numpy as np
import pprint

def calculate(input_list):

    if len(input_list) != 9:
        raise ValueError('List must contain nine numbers')

    list_num = np.array(input_list)
    matrix_list = list_num.reshape(3,3)

    mean = [list(np.mean(matrix_list, axis= 0)), list(np.mean(matrix_list, axis=1)), np.mean(matrix_list)]
    variance_value = [list(np.var(matrix_list, axis=0)), list(np.var(matrix_list, axis=1)), np.var(matrix_list)]
    standard_value = [list(np.std(matrix_list, axis= 0)), list(np.std(matrix_list, axis=1)), np.std(matrix_list)]
    max_values = [list(np.max(matrix_list, axis= 0)), list(np.max(matrix_list, axis=1)), np.max(matrix_list)]
    min_values = [list(np.min(matrix_list, axis= 0)), list(np.min(matrix_list, axis=1)), np.min(matrix_list)]
    sum_values = [list(np.sum(matrix_list, axis= 0)), list(np.sum(matrix_list, axis=1)), np.sum(matrix_list)]

    calculations = {
        'Mean': mean,
        'Variance' : variance_value,
        'Standard_deviation' : standard_value,
        'Max' : max_values,
        'Min' : min_values,
        'Sum' : sum_values
    }


    return calculations

try:
   pprint.pprint(calculate([0,1,2,3,4,5,6,7,8]))
except ValueError as e:
   print(e)        

