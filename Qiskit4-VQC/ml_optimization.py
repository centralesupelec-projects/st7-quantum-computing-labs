from qiskit.circuit import ParameterVector
from qiskit import QuantumCircuit
import numpy as np
from utils import get_cost, runSample
from scipy.optimize import minimize

## VQC - Variational Quantum Computing ##
# Step 1 - parameterized quantum circuit, or ansatz.
# Step 2 - Use a classical optimizer to iteratively update the parameters
# with the goal of minimizing a cost function
# Step 3 - Use the approximate solution with classical post-processing
# to solve the eigenvalue or optimization problem

# Step 2 and 3

def param_circuit():
    qc = QuantumCircuit(5)
    pv1 = np.random.random(5)
    pv2 = ParameterVector("theta", 5)
    for i in range(5):
        qc.rx(pv1[i], i)
        qc.rx(pv2[i], i)
    qc.measure_all()
    return qc, pv1, pv2

# Cost function
def cost_function(parameter, qc, pv2):
    """
    Cost function: compute a cost based on the quantum circuit
    """
    qc = qc.assign_parameters({pv2: [i for i in parameter]})
    qc.measure_all()
    return get_cost(qc, 1000)
    

# Optimization
def optimize(cost_function):
    """
    classical optimizer to iteratively update the parameters
    """
    qc, pv1, pv2 = param_circuit()
    x0 = np.random.random(5)
    res = minimize(cost_function, x0, (qc, pv2), method='COBYLA')
    print("Random angles of first rotation :", pv1)
    print("optimized angle :", res.x)
    return res

def optimized_circuit(qc, res):
    qc_optimized = qc.assign_parameters({"theta["+str(i)+"]":res.x[i] for i in range(5)})
    counts = runSample(qc_optimized, 4000)
    return counts

# Print the circuit
qc, pv1, pv2 = param_circuit()
print("--- Single parameter circuit ---")
print(qc)

# Optimization iteration - step 2
print("--- Running optimization ---")
res = optimize(cost_function)

# Optimization iteration - step 3
print("\n--- Optimized circuit result ---")
counts = optimized_circuit(qc, res)
print(counts)