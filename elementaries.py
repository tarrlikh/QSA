import numpy as np

trivial_operator=np.array([1])

sx=np.zeros((2,2),dtype='complex')
sx[0,1]=1
sx[1,0]=1

sy=np.zeros((2,2),dtype='complex')
sy[0,1]=-1j
sy[1,0]=1j

sz=np.zeros((2,2),dtype='complex')
sz[0,0]=1
sz[1,1]=-1

unity=np.eye(2,dtype='complex')

pauli=[unity,sx,sy,sz]

def identity(number_of_qubits):
    return(np.eye(2**number_of_qubit, dtype='complex'))

def pauli_single(number_of_qubits, position_of_pauli, type_of_pauli):
    u=np.array([1])
    for i in range(number_of_qubits):
        if i==position_of_pauli:
            u=np.kron( u , pauli[type_of_pauli] )
        else:
            u=np.kron( u , pauli[0] )
    return(u)

def pauli_string(number_of_qubits, paulis_from_string):
    string=identity(number_of_qubits)
    
    for i in range(len(paulis_from_string)):
        string=string.dot(pauli_single(number_of_qubits, paulis_from_string[i][0], paulis_from_string[i][1]))
    
    return(string)

def string_catalogue(number_of_qubits, labels_of_strings):
    catalogue=[]
    
    for i in range(len(labels_of_strings)):
        catalogue.append(pauli_string(number_of_qubits, labels_of_strings[i]))
    
    return(string)

def string_iexp(number_of_qubits, string, theta):
    return(np.cos(theta)*identity(number_of_qubits)+1j*np.sin(theta)*string)
    

