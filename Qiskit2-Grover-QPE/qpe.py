from qiskit.circuit.library import UnitaryGate
from qiskit.quantum_info import Operator
from math import pi
import numpy as np
from utils import *

U = UnitaryGate(
    Operator([[1,0,0,0],
              [0,1,0,0],
              [0,0,1,0],
              [0,0,0,np.exp(pi*2j*(6/8))]]), label="U")

from qiskit.circuit.library import QFT

size_eig = 3
size_phi = 2

eig = QuantumRegister(size_eig, name="eig")
phi = QuantumRegister(size_phi, name="phi")
ceig = ClassicalRegister(size_eig, name="ceig")
qc = QuantumCircuit(eig,phi,ceig)

# To fill in
# C-U, C-U^2, C-U^4

# Pick two random eigenvectors
qc.initialize([0,0,0,1], list(range(size_eig, size_eig+size_phi)))

for i in range(size_eig):
    qc.h(eig[i])

CU_list = []
for i in range(1, size_eig+1):
    CU = U.power(i).control()
    CU_list.append(CU)

for i in range(size_eig)[::-1]:
    qc.append(CU_list[i], [list(eig)[i]] + list(phi))

inverse_QFT = QFT(size_eig).inverse()

qc.append(inverse_QFT, eig)

qc.measure(eig,ceig)

qc.draw()

# First, make sure that the drawing is OK.

# Then run the backend !

runSample(qc, 1000)

