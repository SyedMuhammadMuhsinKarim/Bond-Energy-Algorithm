import numpy as np
query_attr = np.array([[1, 0, 1, 0], 
                       [0, 1, 1, 0], 
                       [0, 1, 0, 1], 
                       [0, 0, 1, 1]])
query_access = np.array([[15, 20, 10], 
                         [5, 0, 0], 
                         [25, 25, 25], 
                         [3, 0, 0]])
aa_matrix = np.zeros((4,4))

def position_checker(positions):
  aa_elem = []
  for j in positions[0]:
    aa_elem.append(np.sum(query_access[j:j+1, :]))
  aa_matrix[i,k] = sum(aa_elem)

def dot_prod(vec_a, vec_b):
  return np.dot(vec_a.flatten(), vec_b.flatten())

## AA_MARIX GENERATION
for i in range(4):
  for k in range(4):
    if i == k:
      attr = query_attr[:, k:k+1].flatten()
      positions = np.where(attr == 1)
      position_checker(positions)
    else:
      attr_i = query_attr[:, i:i+1].flatten()
      attr_k = query_attr[:, k:k+1].flatten()
      positions = np.where((attr_i == 1) & (attr_k == 1))
      position_checker(positions)

# BOND ENERGY ALGORITHM - GET INITIAL CC_MATRIX
cc_matrix = aa_matrix[:, :2]
cc_matrix = np.append(np.zeros((4,1)), cc_matrix, axis=1)
cc_matrix = np.append(cc_matrix,np.zeros((4,1)), axis=1)

# BOND ENERGY ALGORITHM - CC_MATRIX GENERATION
for k in range(2, len(aa_matrix)):
  i, j = 0, 1
  get_values = []
  while j < cc_matrix.shape[1]:
    print(i,k,j, len(cc_matrix))
    get_values.append(2 * dot_prod(cc_matrix[:, i:i+1], aa_matrix[:, k:k+1]) + 
                      2 * dot_prod(aa_matrix[:, k:k+1], cc_matrix[:, j:j+1]) - 
                      2 * dot_prod(cc_matrix[:, i:i+1], cc_matrix[:, j:j+1]))  
    i = j
    j+=1
  pos = np.argmax(get_values) + 1
  cc_matrix = np.insert(cc_matrix, pos, aa_matrix[k:k+1], axis=1)

# BOND ENERGY ALGORITHM - REMOVES ZEROS COLUMNS
cc_matrix = np.delete(cc_matrix, 0, axis=1)
cc_matrix = np.delete(cc_matrix, cc_matrix.shape[1]-1, axis=1)

print(cc_matrix)