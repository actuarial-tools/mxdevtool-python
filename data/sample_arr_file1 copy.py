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

dtypes = [np.int, np.int8, np.int16, np.int32, np.int64, 
          np.uint8, np.uint16, np.uint, np.uint64,
          np.float, np.float64, np.unicode]

data_arr = []

shape = (10, 20, 30, 40)
total_num = np.prod(shape)

print(total_num)
for typ in dtypes:
    arr = np.zeros(total_num, typ)
    
    for i in range(total_num):
        arr[i] = i*10
    arr = np.reshape(arr, shape)
    data_arr.append(arr)

np.savez('./data/files/sample_dtypes', *data_arr)

