import elementaries as el
import ansatzes as ans
import hamiltonians as ham
import numpy as np
from scipy.optimize import minimize



def fidelity(ansatz_parameters):
    return(-np.real( ( ans.ansatz_operator(fidelity_ansatz,ansatz_parameters).dot( el.starting_state() ) ).dot(fidelity_target_state) ) )

def maximize_fidelity(ansatz, target_state):
    global fidelity_ansatz
    fidelity_ansatz=ansatz
    global fidelity_target_state
    fidelity_target_state=target_state
    return( minimize( fidelity, np.zeros(len(ansatz)) ) )
    