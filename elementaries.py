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

basis=np.eye(2,dtype='complex')

number_of_qubits=5

def starting_state():
    state=np.zeros(2**number_of_qubits)
    state[0]=1
    return(state)

def identity():
    return(np.eye(2**number_of_qubits, dtype='complex'))

def pauli_operator(position_of_pauli, type_of_pauli):
    '''
    Calculates a single pauli operator.
    '''    
   
    u=trivial_operator
    for i in range(number_of_qubits):
        if i==position_of_pauli:
            u=np.kron( u , pauli[type_of_pauli] )
        else:
            u=np.kron( u , pauli[0] )
            
    return(u)

# def pauli_string_operator(string_identifier):
#     '''
#     Calculates a pauli string operator.
    
#     Inputs a string identifier, i.e. a list of string's paulis. List elements are pairs: [position of a pauli, type of a pauli].
#     '''    
    
#     string_operator=identity()
    
#     #String identifier contains pairs of elements: 0 - position of a pauli, 1 - type of a pauli
#     for i in range(len(string_identifier)):
#         string_operator=string_operator.dot( pauli_operator(string_identifier[i][0] , string_identifier[i][1]) )
    
#     return(string_operator)

def pauli_string_operator(string_identifier):
    '''
    Calculates a pauli string operator.
    
    Inputs a string identifier, i.e. a list of string's paulis. List elements are pairs: [position of a pauli, type of a pauli].
    '''    
    
    string_operator=trivial_operator
    
    j=0
    
    for i in range(number_of_qubits):
        if i==string_identifier[j][0]:
            string_operator=np.kron( string_operator , pauli[string_identifier[j][1]] )
            if j<(len(string_identifier)-1):
                j+=1
        else:
            string_operator=np.kron( string_operator , pauli[0] )
            
    return(string_operator)

def list_of_string_operators(list_of_string_identifiers):
    '''
    Calculates a list of Pauli string operators.
    
    Inputs a list of string identifiers.
    '''
    
    lis=[]
    
    #list of strings contains elements which are lists of paulis
    
    for i in range(len(list_of_string_identifiers)):
        lis+=pauli_string_operator(list_of_string_identifiers[i])
    
    return(lis)

def string_iexp(string, theta):
    '''
    Calculates an imaginary exponential of a Pauli string, multiplied by parameter theta.
    
    Inputs a string identifier and the angle theta, outputs a Hilbert space operator.
    '''
    return(np.cos(theta)*identity()+1j*np.sin(theta)*pauli_string_operator(string))

def YXXstring_computational_basis_action(YXX_string, state_bitstring, prefactor):
    '''
    Computes an action of a Pauli string on a computational basis state, on the level of corresponding bitstrings and complex prefactors.
    
    Inputs a bitstring and a prefactor of an old state, outputs the bitstring and a prefactor of a new state.
    '''
    
    new_prefactor=prefactor
    new_state_bitstring=state_bitstring.copy()
    
    for element in YXX_string:
        if (element[1]==2):
            new_prefactor*=(1j)*(-1)**(state_bitstring[element[0]])
        new_state_bitstring[element[0]]=np.mod(state_bitstring[element[0]]+1,2)
    
    return(new_state_bitstring, new_prefactor)

def state_from_bitstring(bitstring, prefactor=1):
    '''
    Creates a 2^N dimensional computational basis state vector. 

    Inputs a corresponding bitstring [s1,s2..s_N] with s_i=0,1, and a prefactor c:
    
    [s1,s2,..s_N], c ---> c*|s1,s2,s3,..s_N>
    '''
    
    state=trivial_operator*prefactor
    
    for element in bitstring:
        state=np.kron(state,basis[element])
    
    return(state)


    

