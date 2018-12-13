import elementaries as el
import ansatzes as ans
import hamiltonians as ham
import numpy as np
from scipy.optimize import minimize


def evaluate_expectation(ansatz_id, observable, ansatz_parameters):
    ansatz=el.list_of_strings(ansatz_id)
    
    return(ans.ansatz_state(ansatz, ansatz_parameters) .dot(observable.dot(np.transpose([ans.ansatz_state(ansatz, ansatz_parameters)])) ) )

def optimize_expectation(ansatz_ids, observable, method=None, starting_state=np.array([None]),tol=0.0000001):
    
    expectation = lambda ansatz_parameters: np.real( ans.ansatz_state(ansatz, ansatz_parameters) .dot(observable.dot(np.transpose([ans.ansatz_state(ansatz, ansatz_parameters)])) ) )[0]
    
    if starting_state.any()==None:
        starting_state=np.zeros(len(ansatz_ids[0]))
    
    ansatz_id=[]
    
    minimizations=[]
    
    logs=[]
    
    for i in range(len(ansatz_ids)-1):
        ansatz_id+=ansatz_ids[i]
        ansatz=el.list_of_strings(ansatz_id)
        
#         expectation func to be inserted?
        
        minimizations+=[minimize(expectation, starting_state , method=method)]
        
        new_starting_state=minimizations[i].x
        
        starting_state=np.array(list(new_starting_state)+[0. for j in range(len(ansatz_ids[i+1]))])
        
        logs+=[expectation]
            
    ansatz_id+=ansatz_ids[len(ansatz_ids)-1]
    
    ansatz=el.list_of_strings(ansatz_id)
    
    minimizations+=[minimize(expectation, starting_state , method=method, tol=tol)]
    
    return( minimizations)

def optimize_fidelity(ansatz_ids, target_state, method=None, starting_state=np.array([None])):
    
    fidelity = lambda ansatz_parameters: -np.real( ( ans.ansatz_state(ansatz, ansatz_parameters) ).dot(target_state) )**2
    
    if starting_state.any()==None:
        starting_state=np.zeros(len(ansatz_ids[0]))
    

    
    ansatz_id=[]
    
    minimizations=[]
    
    for i in range(len(ansatz_ids)-1):
        ansatz_id+=ansatz_ids[i]
        ansatz=el.list_of_strings(ansatz_id)
        
#         fidelity = lambda ansatz_parameters: -np.real( ( ans.ansatz_state(ansatz, ansatz_parameters) ).dot(target_state) )**2
        
        minimizations+=[minimize( fidelity, starting_state , method=method)]
        
        new_starting_state=minimizations[i].x
        
        starting_state=np.array(list(new_starting_state)+[0. for j in range(len(ansatz_ids[i+1]))])
            
    ansatz_id+=ansatz_ids[len(ansatz_ids)-1]
    
    ansatz=el.list_of_strings(ansatz_id)
    
#     fidelity = lambda ansatz_parameters: -np.real( ( ans.ansatz_state(ansatz, ansatz_parameters) ).dot(target_state) )**2
    
    minimizations+=[minimize( fidelity, starting_state , method=method)]
    
    return(minimizations)


def optimize_fidelity_hessianmethods(ansatz_id, target_state, method=None):
    
    ansatz=el.list_of_strings(ansatz_id)
    
    fidelity = lambda ansatz_parameters: -np.real( ( ans.ansatz_state(ansatz, ansatz_parameters) ).dot(target_state) )**2 
    
    observable=-np.transpose([target_state]).dot(np.array([target_state]))
    
    first, sec = ans.hessian_preparation(ansatz_id)
    
    return( minimize( fidelity, 0.*np.ones(len(ansatz_id)), jac=lambda thetas: ans.jacobian_computation(observable, ansatz, thetas, first), method=method) )
#     return( minimize( fidelity, np.ones(len(ansatz)), jac=lambda thetas: ans.jacobian_computation(observable, ansatz, thetas, first), hess=lambda thetas: ans.hessian_computation(observable, ansatz, thetas, first, sec) , method=method) )