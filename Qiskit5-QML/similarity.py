from fidelity import fidelity_adjoint_circuit, fidelity_swaptest_circuit
from utils import runCircuits
import numpy as np

# Step 3 - Similarity Matrix

def similarity_matrix(nb_qubits, nb_feature, X, circ_type):
    """
    Compute the similarity matrix for input vector X
    nb_qubits: number of input qubits for the fidelity circuit = dimension of input vectors
    nb_features: number of dimensions in the embedding circuit (parameters for clustering)
    X: list of input vectors to compute the similarity on. This list can be of any length
    circ_type: "adjoint" or "swap". Type of fidelity circuit to use
    """
    n = len(X)
    circ_list = []
    # Select corresponding circuit
    if circ_type == "adjoint":
        circ = fidelity_adjoint_circuit(nb_qubits, nb_feature)
    elif circ_type == "swap":
        circ = fidelity_swaptest_circuit(nb_qubits, nb_feature)
    else:
        raise ValueError("circ_type should be adjoint or swap")
    
    # Compute the list of parametrized circuits
    for i in range(n):
        for j in range(n):
            if i > j: # We keep only upper values
                circ_iter = circ.copy()
                circ_iter = circ_iter.assign_parameters({"input1["+str(k)+"]":X[i][k] for k in range(nb_feature)})
                circ_iter = circ_iter.assign_parameters({"input2["+str(k)+"]":X[j][k] for k in range(nb_feature)})
                circ_list.append(circ_iter)

    # Compute the circuits
    result = runCircuits(circ_list)

    # Create the similarity matrix
    index = 0
    sim_matrix = np.eye(n)
    for i in range(n):
        for j in range(n):
            if i > j: # We fill only upper values
                if circ_type == "adjoint":
                    bitstring = result[index].data.meas.get_bitstrings()
                    nb_shots = result[index].metadata["shots"]
                    fidelity = bitstring.count('0'*nb_qubits)/nb_shots
                elif circ_type == "swap":
                    bitstring = result[index].data.c.get_bitstrings()
                    nb_shots = result[index].metadata["shots"]
                    fidelity = bitstring.count('0')/nb_shots
                sim_matrix[i,j] = fidelity
                sim_matrix[j,i] = fidelity
                index += 1

    return sim_matrix

if __name__ == "__main__":
    X_input_example = [[0.2, 1], [0.8, 1.2], [1.4, 1.6], [0.7, 0.9]]
    # Method 1: Similarity adjoint matrix
    matrix = similarity_matrix(2, 1, X_input_example, circ_type="adjoint")
    print("--- Similarity matrix with adjoint ---\n")
    print(matrix)

    # Method 2: Similarity swap test matrix
    matrix = similarity_matrix(2, 1, X_input_example, circ_type="swap")
    print("\n--- Similarity matrix with swap test ---\n")
    print(matrix)