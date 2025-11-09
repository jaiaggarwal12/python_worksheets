import numpy as np

def q1_array_creation():
    arr1 = np.arange(5, 26)  
    arr2 = np.random.randint(10, 51, size=(3,4))  
    return arr1, arr2

def q2_attributes(arr1, arr2):
    info1 = {'shape': arr1.shape, 'size': arr1.size, 'dtype': arr1.dtype}
    info2 = {'shape': arr2.shape, 'size': arr2.size, 'dtype': arr2.dtype}
    return info1, info2

def q3_array_operations():
    a1 = np.array([2,4,6,8,10])
    a2 = np.array([1,3,5,7,9])
    add = a1 + a2
    sub = a1 - a2
    mul = a1 * a2
    div = a1 / a2
    return add, sub, mul, div

def q4_broadcasting():
    base = np.arange(1,10).reshape(3,3)
    scaled = base * 5
    return base, scaled

def q5_slicing_indexing():
    arr = np.arange(10,26).reshape(4,4)
    second_row = arr[1,:]
    last_col = arr[:, -1]
    arr[0,:] = 0
    return arr, second_row, last_col

def q6_boolean_indexing():
    arr = np.random.randint(20,41, size=10)
    greater_30 = arr[arr > 30]
    return arr, greater_30

def q7_reshaping():
    one_d = np.arange(11, 11+12)
    reshaped = one_d.reshape(3,4)
    return one_d, reshaped

def q8_matrix_ops():
    A = np.array([[1,2],[3,4]])
    B = np.array([[5,6],[7,8]])
    matmul = A @ B
    transpose_A = A.T
    return A, B, matmul, transpose_A

def q9_stats():
    arr = np.random.randint(10,61,size=15)
    mean = arr.mean()
    median = np.median(arr)
    std = arr.std()
    return arr, mean, median, std

def q10_linear_algebra():
    A = np.array([[2,1,3],[0,5,6],[7,8,9]], dtype=float)
    det = np.linalg.det(A)
    inv = None
    eigvals = None
    eigvecs = None
    try:
        inv = np.linalg.inv(A)
        eigvals, eigvecs = np.linalg.eig(A)
    except np.linalg.LinAlgError:
        inv = None
    return A, det, inv, eigvals, eigvecs

def q11_robot_distances():
    pts = np.array([[0,0],[2,3],[4,7],[7,10],[10,15]])
    # 11.1 Euclidean distance between first and last:
    d_first_last = np.linalg.norm(pts[-1]-pts[0])
    # 11.2 total path length:
    diffs = np.diff(pts, axis=0)
    step_distances = np.linalg.norm(diffs, axis=1)
    total = step_distances.sum()
    return pts, d_first_last, step_distances, total

if __name__ == "__main__":
    print("Q1..Q11 outputs:")
    print("Q1:", q1_array_creation())
    print("Q2:", q2_attributes(*q1_array_creation()))
    print("Q3:", q3_array_operations())
    print("Q4:", q4_broadcasting())
    print("Q5:", q5_slicing_indexing())
    print("Q6:", q6_boolean_indexing())
    print("Q7:", q7_reshaping())
    print("Q8:", q8_matrix_ops())
    print("Q9:", q9_stats())
    print("Q10:", q10_linear_algebra())
    print("Q11:", q11_robot_distances())
