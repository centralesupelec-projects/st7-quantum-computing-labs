from qiskit import QuantumCircuit
from qiskit.circuit import ParameterVector

# Encode classical data in quantum format - Embedding or feature map !!

def embbeding_circuit(nb_qubits, nb_feature, name="input"):
    """
        nb_qubits : nomber of qubits in the circuit
        nb_feature : nb_feature of data
        This function return the circuit of embedding
    """
    qc = QuantumCircuit(nb_qubits)
    x = ParameterVector(name, nb_feature)
    for i in range(nb_qubits):
        qc.h(i)
        qc.rz(x[i % nb_feature], i)
    return qc

## Draw example circuit

embbeding_circuit(3,2).draw()