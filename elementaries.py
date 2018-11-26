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

number_of_qubits=3

def starting_state():
    state=np.zeros(2**number_of_qubits)
    state[0]=1
    return(state)

def identity():
    return(np.eye(2**number_of_qubits, dtype='complex'))

def pauli_operator(position_of_pauli, type_of_pauli):
    u=trivial_operator
    for i in range(number_of_qubits):
        if i==position_of_pauli:
            u=np.kron( u , pauli[type_of_pauli] )
        else:
            u=np.kron( u , pauli[0] )
    return(u)

def pauli_string_operator(list_of_paulis):
    string_operator=identity()
    
    
    #list of paulis contains pairs of elements: 0 - position of a pauli, 1 - type of a pauli
    for i in range(len(list_of_paulis)):
        string_operator=string_operator.dot( pauli_operator(list_of_paulis[i][0] , list_of_paulis[i][1]) )
    
    return(string_operator)

def list_of_string_operators(list_of_strings):
    lis=[]
    
    #list of strings contains elements which are lists of paulis
    
    for i in range(len(list_of_strings)):
        lis+=pauli_string_operator(list_of_strings[i])
    
    return(lis)

def string_iexp(string, theta):
    return(np.cos(theta)*identity()+1j*np.sin(theta)*pauli_string_operator(string))




    

