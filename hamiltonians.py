import numpy as np
import elementaries as el
from numpy import random


def single_qubit_paulis (alpha):
    
    pauli_ids=[[[i, alpha]] for i in range(el.number_of_qubits)]
    paulis=[el.pauli_string_operator(pauli_ids[i]) for i in range(el.number_of_qubits)]
    
    return(paulis)

def two_qubit_strings (alpha, beta):
    
    string_ids=[[[[i, alpha], [j, beta]] for i in range(el.number_of_qubits)] for j in range(el.number_of_qubits)]
    strings=[[el.pauli_string_operator(string_ids[i][j]) for i in range(el.number_of_qubits)] for j in range(el.number_of_qubits)]
    
    return(strings)

def constant_subhamiltonian (magnitude, generators):
    
    hamiltonian=0*el.identity
    
    for element in generators:
        hamiltonian+=magnitude*element
    
    return(hamiltonian)

def random_subhamiltonian (disorder_strength, generators):
    hamiltonian=0*el.identity
    
    for row in generators:
        for element in row:
            hamiltonian=hamiltonian+random.normal(0,disorder_strength)*element
    
    return(hamiltonian)