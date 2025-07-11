import numpy as np

def calculate(list):
    if len(list)!=9:
        raise ValueError("List must contain nine numbers.")
    else: 
        A=np.array(list).reshape(3,3)
        calculations={
            'mean':[np.mean(A,axis=0).tolist(),np.mean(A,axis=1).tolist(),np.mean(A).tolist()],
            'variance':[np.var(A,axis=0).tolist(),np.var(A,axis=1).tolist(),np.var(A).tolist()],
            'standard deviation':[np.std(A,axis=0).tolist(),np.std(A,axis=1).tolist(),np.std(A).tolist()],
            'max':[np.max(A,axis=0).tolist(),np.max(A,axis=1).tolist(),np.max(A).tolist()],
            'min':[np.min(A,axis=0).tolist(),np.min(A,axis=1).tolist(),np.min(A).tolist()],
            'sum':[np.sum(A,axis=0).tolist(),np.sum(A,axis=1).tolist(),np.sum(A).tolist()]}
        return calculations
        

lista=[0,1,2,3,4,5,6,7,8]
print(calculate(lista))
