from qiskit.circuit import ParameterVector
from qiskit import QuantumCircuit
import numpy as np

## VQC - Variational Quantum Computing ##
# Step 1 - parameterized quantum circuit, or ansatz.
# Step 2 - Use a classical optimizer to iteratively update the parameters
# with the goal of minimizing a cost function
# Step 3 - Use the approximate solution with classical post-processing
# to solve the eigenvalue or optimization problem

# Step 1 - Single Parameter

from qiskit.circuit import Parameter

def circuit1():
    qc = QuantumCircuit(1)
    # create the parameter
    phi = Parameter('phi')
    # parameterize the rotation
    qc.rx(phi, 0)
    return qc, phi

# Print the circuit
qc, phi = circuit1()
print("--- Single parameter circuit ---")
print(qc)

# Circuit with parameter assigned
qc_assigned = qc.assign_parameters({phi: np.pi})
print("\n--- Single parameter circuit assigned ---")
print(qc_assigned)

# Step 1 - Multiple Parameter

def circuit2():
    qc = QuantumCircuit(5)
    pv = ParameterVector("theta", 5)

    # Rotate qubit i by the angle RX of the i_th parameter theta
    for i in range(5):
        qc.rx(pv[i], i)
    return qc, pv

# Print the circuit
qc, pv = circuit2()
print("\n--- Multiple parameter circuit ---")
print(qc)

# Circuit with parameter assigned
qc_param = qc.assign_parameters({pv: [np.pi, np.pi/2, np.pi, np.pi, np.pi]})
print("\n--- Multiple parameter circuit assigned ---")
print(qc_param)