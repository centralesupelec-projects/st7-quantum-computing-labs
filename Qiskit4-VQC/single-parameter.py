from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
import numpy as np

qc1 = QuantumCircuit(1)

qc1.rx(np.pi/2, 0)
qc1.rz(np.pi/2, 0)

state = Statevector(qc1)
plot_bloch_multivector(state)

## Single Parameter

from qiskit.circuit import Parameter

qc2 = QuantumCircuit(1)

# create the parameter
phi = Parameter('phi')
 
# parameterize the rotation
qc2.rx(phi, 0)

qc2.draw()

qc3 = qc2.assign_parameters({phi: np.pi})
qc3.draw()