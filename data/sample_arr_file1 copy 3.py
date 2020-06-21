import os
import sys
import numpy as np
import pickle

file_directory = './data/files'

arr = np.loadtxt('C:/Users/ahn/Downloads/675029_1187469_compressed_road-transport-brazil.csv/road-transport-brazil.txt', 
                 delimiter=";", dtype=str)

print(len(arr))
print(arr.dtype)
print(arr[0])

np.save('./data/files/txt_save_arr1', arr)

covid_arr = np.loadtxt('C:/Users/ahn/Downloads/551982_1215420_compressed_cord_19_embeddings_cord_19_embeddings_2020-06-04.csv/cord_19_embeddings_2020-06-04.csv', 
                 dtype=str)

print(len(covid_arr))
print(covid_arr.dtype)
print(covid_arr[0])

np.save('./data/files/txt_save_arr2', covid_arr)



