#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
	 """
   	 function that computes the square
  	 value of all integers of a matrix.
  	 """
	new_matrix = []
	for i in matrix:
		new_sub_array = []
		for j in i:
			new_sub_array.append(j * j)
		new_matrix.append(new_sub_array)
	return new_matrix
