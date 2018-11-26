import numpy as np
import elementaries as el
import itertools

def QSA_paulis(string):
    lis=[]
    switch=0
    
    for element in string:
        
        if switch == 1:
            lis+=[[element,1]]
        
        if switch == 0:
            lis+=[[element, 2]]
            switch+=1
        

    return(lis)

def ansatz_operator(list_of_strings, list_of_thetas):
    operator=el.identity()
    
    for i in range(len(list_of_strings)):
        operator=operator.dot(el.string_iexp(list_of_strings[i], list_of_thetas[i]) )
    
    return(operator)

def k0QSA(k0):
    
    #returns subsets of k0 elements from the ordered list of qubits (from 1 to N); 
    #some extra massaging performed, so that a list of lists is returned
    
    string_list=list(map(list,itertools.combinations(list(range(el.number_of_qubits)),k0)))
    
    string_list_with_paulis=list(map(QSA_paulis, string_list))
    
    return(string_list_with_paulis)

def kQSA(k):
    
    lis=[]
    for k0 in range(1,k+1):
        lis+=k0QSA(k0)
    
    return(lis)  