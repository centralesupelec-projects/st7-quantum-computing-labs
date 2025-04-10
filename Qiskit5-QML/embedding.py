from qiskit import QuantumCircuit
from qiskit.circuit import ParameterVector

## QML - Quantum Machine learning ##
# Step 1 - Quantum embedding: encode classical data into the quantum circuit, with variational circuits / quantum maps.
# Step 2 - Fidelity computation: compute the distance (fidelity / overlap) between two quantum states, with a kernel function.
# Step 3 - Similarity Matrix: we compute a matrix to get distance / fidelity between all states in input.
# Step 4 - QML Clustering: we use the previously defined similarity matrix to solve a classical clustering problem

# Step 1 - Quantum embedding

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

if __name__ == "__main__":
    # Print the circuit
    qc = embbeding_circuit(3,2)
    print("The embedding circuit:")
    print(qc)