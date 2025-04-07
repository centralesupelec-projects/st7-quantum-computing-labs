from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
from qiskit.circuit import ParameterVector
import numpy as np

## Multiple Parameter

qc4 = QuantumCircuit(5)

pv = ParameterVector("theta", 5)

# Rotate qubit i by the angle RX of the i_th parameter theta
for i in range(5):
    qc4.rx(pv[i], i)

qc4.draw()
qc4_param = qc4.assign_parameters({pv: [np.pi, np.pi/2, np.pi, np.pi, np.pi]})
qc4_param.draw()