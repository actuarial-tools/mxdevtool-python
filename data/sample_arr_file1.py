import os
import numpy as np
import pickle

file_directory = './data/files'

def save_data(name, data, save_type, compress = False):
    if save_type == 'npz':
        if compress:
            np.savez_compressed(os.path.join(file_directory, name), data)
        else:
            np.savez(os.path.join(file_directory, name), data)
    elif save_type == 'npy':
        np.save(os.path.join(file_directory, name), data)
    elif save_type == 'pkl':
        with open(os.path.join(file_directory, name),'wb') as f: pickle.dump(data, f)
    else:
        pass

x = np.array([[10, 20, 30], [40, 50, 60]])
x_obj = np.array([['10', 20, 30], [40, 0.0390, 60],[40, 50, 'test',0]])
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
arr1 = np.random.randint(5, 50, size = (5, 8))
arr2 = np.array([[[ 7, 24, 24, 22], [24, 10, 16,  2], [ 1, 16, 7, 16]],
                 [[22, 23, 12, 39], [16, 30, 37, 15],[16, 17,  3, 19]]])
arr3 = np.random.rand(2, 3, 1320, 15)

print(arr2.dtype, arr2.shape)

data_arr = [x, arr, arr1, arr2, arr3]
data_dict = {"x":x, "arr":arr, "arr1":arr1, "arr2":arr2, "arr3":arr3}

save_data('sample_arr_file1', arr, 'npy')
save_data('sample_arr_file1_simple_array', x, 'npy')
save_data('sample_arr_file1_simple_object_pickle', x_obj, 'npy')
save_data('sample_arr_file1_array_parameter', data_arr, 'npy')
save_data('sample_arr_file1_dict_parameter', data_dict, 'npy')

save_data('sample_arr_file1_z_array_parameter', data_arr, 'npz')
save_data('sample_arr_file1_dict_parameter', data_dict, 'npz')

save_data('sample_arr_file1_z_comp_array_parameter', data_arr, 'npz', compress=True)
save_data('sample_arr_file1_z_comp_dict_parameter', data_dict, 'npz', compress=True)

save_data('pickle_arr_x', x, 'pkl')
save_data('pickle_arr_arr', arr, 'pkl')
save_data('pickle_arr_arr1', arr1, 'pkl')
save_data('pickle_arr_arr2', arr2, 'pkl')
save_data('pickle_arr_arr3', arr3, 'pkl')

np.savez('./data/files/sample_arr_file1_z2_params', x=x, arr=arr, arr1=arr1, arr2=arr2, arr3=arr3)
np.savez_compressed('./data/files/sample_arr_file1_z_comp2_params',x=x, arr=arr, arr1=arr1, arr2=arr2, arr3=arr3)
