from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from utils import runStateVector

## Exercice 3 

# 1 - Implement a C-C-C-X
# 2 - Idem using only 2-qubit gates
# Note: A Toffoli gate can be decomposed into controlled-S gates
# Knowing that, use controlled-S gates .cs() to implementx.
# Print the resulting circuit, and check that it indeed works.

def toffoli_gate():
    """
    This function implement a Toffoli gate
    using only CS gates and CX
    """
    qc = QuantumCircuit(3)
    # Hadamard
    qc.h(2)
    # CCZ implementation
    qc.cs(1,2)
    qc.cx(0,1)
    qc.cs(1,2)
    qc.cx(0,1)
    qc.cs(0,2)
    # Hadamard
    qc.h(2)
    return qc

def bogus_v2():
    """
    This function implement a CCCX
    only with the previous toffoli function
    """
    q = QuantumRegister(5, name="q1")
    c = ClassicalRegister(5)
    qc = QuantumCircuit(q, c)

    toffoli = toffoli_gate()
    qc = qc.compose(toffoli, qubits=[0, 1, 4])
    qc = qc.compose(toffoli, qubits=[2, 4, 3])
    qc = qc.compose(toffoli, qubits=[0, 1, 4])
    return qc

def init_state():
    """
    This function initialize the qubits to |11110>
    to test the CCCX (Bogus) function
    """
    qc = QuantumCircuit(5)
    # Initialize first 3 qubits to one
    for i in range(4):
        qc.initialize(1, i)
    return qc

qc = bogus_v2()
init = init_state()
qc = init.compose(qc)
print("\nThe Bogus v2 circuit is:")
print(qc)
print("\nThe input statevector is:")
runStateVector(init)
print("\nThe output statevector is:")
runStateVector(qc)
