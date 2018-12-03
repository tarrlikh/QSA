import elementaries as el
import ansatzes as ans
import hamiltonians as ham
import numpy as np
from scipy.optimize import minimize


def optimize_expectation(ansatz_id, observable, method=None):
    ansatz=el.list_of_strings(ansatz_id)
    
    expectation = lambda ansatz_parameters: -np.real( ans.ansatz_state(ansatz, ansatz_parameters) .dot(observable.dot(np.transpose([ans.ansatz_state(ansatz, ansatz_parameters)])) ) )
    
    return( minimize( expectation, 0.*np.ones(len(ansatz_id)) , method=method) )

def optimize_fidelity(ansatz_id, target_state, method=None):
    ansatz=el.list_of_strings(ansatz_id)
    
    fidelity = lambda ansatz_parameters: -np.real( ( ans.ansatz_state(ansatz, ansatz_parameters) ).dot(target_state) )**2
    
    return( minimize( fidelity, 0.*np.ones(len(ansatz)) , method=method) )



def optimize_fidelity_hessianmethods(ansatz_id, target_state, method=None):
    
    ansatz=el.list_of_strings(ansatz_id)
    
    fidelity = lambda ansatz_parameters: -np.real( ( ans.ansatz_state(ansatz, ansatz_parameters) ).dot(target_state) )**2 
    
    observable=-np.transpose([target_state]).dot(np.array([target_state]))
    
    first, sec = ans.hessian_preparation(ansatz_id)
    
    return( minimize( fidelity, 0.*np.ones(len(ansatz_id)), jac=lambda thetas: ans.jacobian_computation(observable, ansatz, thetas, first), method=method) )
#     return( minimize( fidelity, np.ones(len(ansatz)), jac=lambda thetas: ans.jacobian_computation(observable, ansatz, thetas, first), hess=lambda thetas: ans.hessian_computation(observable, ansatz, thetas, first, sec) , method=method) )