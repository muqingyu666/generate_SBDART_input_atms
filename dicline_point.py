'''
Developed by Mu

simple code to round up the matrix

2020-10-10
'''

def matrixRound(M, decPts):
    # 对行循环
    for index in range(len(M)):
        # 对列循环
        for _index in range(len(M[index])):
            M[index][_index] = round(M[index][_index], decPts)  


n = np.random.rand(4,4)
for i in range(0,37):
    matrixRound(o31[i,:,:],8)
    matrixRound(z1[i,:,:],5)
    matrixRound(q1[i,:,:],8)
    matrixRound(t1[i,:,:],3)

