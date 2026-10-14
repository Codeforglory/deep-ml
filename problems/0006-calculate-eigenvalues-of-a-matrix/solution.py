def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	import numpy as np
	matrix_np = np.array(matrix)

	r,c = matrix_np.shape 
	a = 1
	b = -np.sum(np.array(matrix)*np.identity(2))

	c = round(np.linalg.det(matrix),1)
	D = np.sqrt(b*b - 4*a*c)
	eigen1,eigen2 = (-b + D)/(2*a),(-b - D)/(2*a)
	
	return [eigen1,eigen2]