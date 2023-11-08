#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
	new_matrix = []
	for i in matrix:
		new_sub_array = []
		for j in i:
			new_sub_array.append(j * j)
		new_matrix.append(new_sub_array)
