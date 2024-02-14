import numpy as np
import pprint

def calculate(list):

    if len(list) != 9:
        raise ValueError('List must contain nine numbers')

    list_num = np.array(list)
    matrix_list = list_num.reshape(3,3)
    flatten_list = matrix_list.flatten()
    mean ,variance, standard, max_value, min_value =  matrix_list.mean(axis=0), matrix_list.var(axis=0),matrix_list.std(axis=0),matrix_list.max(axis=0),matrix_list.min(axis=0)
    mean_num ,variance_num, standard_num, max_value_num, min_value_num =  matrix_list.mean(axis=1), matrix_list.var(axis=1),matrix_list.std(axis=1),matrix_list.max(axis=1),matrix_list.min(axis=1)
    mean_list ,variance_list, standard_list, max_value_list, min_value_list =  flatten_list.mean(), flatten_list.var(),flatten_list.std(),flatten_list.max(),flatten_list.min()

    calculations = {
        'Mean' : [mean.tolist(), mean_num.tolist(), mean_list.tolist()],
        'Variance' : [variance.tolist(), variance_num.tolist(),variance_list.tolist()],
        'Standard deviation' : [standard.tolist(), standard_num.tolist(), standard_list.tolist()],
        'Max' : [max_value.tolist(), max_value_num.tolist(), max_value_list.tolist()],
        'Min' : [min_value.tolist(), min_value_num.tolist(), min_value_list.tolist()]
    }

    return calculations

try:
   pprint.pprint(calculate([0,1,2,3,4,5,6,7,8]))
except ValueError as e:
   print(e)        

