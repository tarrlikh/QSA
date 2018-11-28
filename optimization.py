import elementaries as el
import ansatzes as ans
import hamiltonians as ham
import numpy as np
from scipy.optimize import minimize



def optimize_fidelity_nonhessianmethods(ansatz, target_state, method=None):
    fidelity = lambda ansatz_parameters: -np.real( ( ans.ansatz_state(ansatz, ansatz_parameters) ).dot(target_state) )**2 
    return( minimize( fidelity, np.ones(len(ansatz)) , method=method) )



def optimize_fidelity_hessianmethods(ansatz, target_state, method):
    fidelity = lambda ansatz_parameters: -np.real( ( ans.ansatz_state(ansatz, ansatz_parameters) ).dot(target_state) )**2 
    
    observable=-np.transpose([target_state]).dot(np.array([target_state]))
    
    first, sec = ans.hessian_preparation(ansatz)
    
    return( minimize( fidelity, np.ones(len(ansatz)), jac=lambda thetas: ans.jacobian_computation(observable, ansatz, thetas, first), method=method) )
#     return( minimize( fidelity, np.ones(len(ansatz)), jac=lambda thetas: ans.jacobian_computation(observable, ansatz, thetas, first), hess=lambda thetas: ans.hessian_computation(observable, ansatz, thetas, first, sec) , method=method) )