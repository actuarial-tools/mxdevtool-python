import numpy as np
import pickle
x = np.array([[10, 20, 30], [40, 50, 60]])
x_obj = np.array([['10', 20, 30], [40, 0.0390, 60],[40, 50, 'test',0]])
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
arr1 = np.random.randint(5, 50, size = (5, 8))
arr2 = np.array([[[ 7, 24, 24, 22], [24, 10, 16,  2], [ 1, 16, 7, 16]],
                 [[22, 23, 12, 39], [16, 30, 37, 15],[16, 17,  3, 19]]])

data_arr = [x, arr, arr1, arr2]
data_dict = {"x":x, "arr":arr, "arr1":arr1, "arr2":arr2}

np.save('./data/files/sample_arr_file1', arr) # x_save.npy

np.save('./data/files/sample_arr_file1_simple_object_pickle', x_obj) # x_save.npy - unicode로 박힘 U2 - 완료
np.save('./data/files/sample_arr_file1_array_parameter', data_arr) # 이거는 arr pickle 로 들어감
np.save('./data/files/sample_arr_file1_dict_parameter', data_dict) # 이거는 dict pickle 로 들어감

np.savez('./data/files/sample_arr_file1_z_array_parameter', data_arr)
np.savez('./data/files/sample_arr_file1_z_dict_parameter', data_dict)

np.savez_compressed('./data/files/sample_arr_file1_z_comp_array_parameter', data_arr)
np.savez_compressed('./data/files/sample_arr_file1_z_comp_dict_parameter', data_dict)

np.savez('./data/files/sample_arr_file1_z2_params', x=x, arr=arr, arr1=arr1, arr2=arr2)
np.savez_compressed('./data/files/sample_arr_file1_z_comp2_params',x=x, arr=arr, arr1=arr1, arr2=arr2)

with open('./data/files/pickle_arr_x','wb') as f: pickle.dump(x, f)
with open('./data/files/pickle_arr_arr','wb') as f: pickle.dump(arr, f)
with open('./data/files/pickle_arr_arr1','wb') as f: pickle.dump(arr1, f)
with open('./data/files/pickle_arr_arr2','wb') as f: pickle.dump(arr2, f)
