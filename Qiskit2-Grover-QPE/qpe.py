from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit.library import UnitaryGate, QFT
from qiskit.quantum_info import Operator
from utils import runSample
from math import pi
import numpy as np

## QPE Algorithm ##
# Quantum Phase Estimation - We use a Unitary matrix U,
# an eigenvector Phi with e^(2i*pi*omega) eigenvalues.
# The QPE Algorithm let us determine omega in binary form with
# a requested precision.

# Unitary gate definition
U = UnitaryGate(
    Operator([[1,0,0,0],
              [0,1,0,0],
              [0,0,1,0],
              [0,0,0,np.exp(pi*2j*(6/8))]]
    ), 
    label="U"
)

def QPE(size_eig = 3, size_phi = 2, Unitary = U):
    """
    QPE circuit
    size_eig: Size of eigenvalue - bit precision
    size_phi: Size of eigenvector - linked to the size of U (2^size_phi)
    Unitary: Unitary matrix gate for the QPE - UnitaryGate
    """
    # Registers definition - total qubits = size_eig + size_phi
    eig = QuantumRegister(size_eig, name="eig")
    phi = QuantumRegister(size_phi, name="phi")
    ceig = ClassicalRegister(size_eig, name="ceig")
    qc = QuantumCircuit(eig,phi,ceig)

    # Pick two random eigenvectors
    qc.initialize([0,0,0,1], list(range(size_eig, size_eig+size_phi)))

    # Hadamard gates for eigenvalues part
    for i in range(size_eig):
        qc.h(eig[i])

    # Controlled U gates
    CU_list = []
    for i in range(1, size_eig+1):
        CU = Unitary.power(i).control()
        CU_list.append(CU)

    for i in range(size_eig)[::-1]:
        qc.append(CU_list[i], [list(eig)[i]] + list(phi))

    # Inverse Fourier Transoform at the end
    inverse_QFT = QFT(size_eig).inverse()
    qc.append(inverse_QFT, eig)
    qc.measure(eig,ceig)
    return qc

# Print the circuit
qc = QPE()
print("-- QPE circuit --- \n")
print(qc)

# Run the circuit with 3 bits precision
s = runSample(qc, 1000)
print("-- Running QPE circuit | Precision 3 bits ---")
print("results: ", s)
# Note: We can see that the most frequent state is |110>,
# which correspond to 6/8 = 3/4.
# We can conclude that w = e^(2i*pi*3/4), as expected.

# Run the circuit with 4 bits precision
qc = QPE(4)
s = runSample(qc, 1000)
print("\n-- Running QPE circuit | Precision 4 bits ---")
print("results: ", s)

# Run the circuit with 5 bits precision
qc = QPE(5)
s = runSample(qc, 1000)
print("\n-- Running QPE circuit | Precision 5 bits ---")
print("results: ", s)