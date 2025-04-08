from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_ibm_runtime import SamplerV2 as Sampler
from qiskit_aer import AerSimulator
from fidelity import fidelity_adjoint_circuit, fidelity_SwapTest_circuit
import numpy as np

sim = AerSimulator()
pm = generate_preset_pass_manager(backend=sim, optimization_level=1)

## Similarity adjoint matrix

def similarity_adjoint(nb_qubits, nb_feature, X, backend, pass_manager):
    n = len(X)

    circ = fidelity_adjoint_circuit(nb_qubits, nb_feature)
    circ_list = []
    for i in range(len(X)):
        for j in range(len(X)):
            # We keep only upper values
            if i > j:
                circ_iter = circ.copy()
                circ_iter = circ_iter.assign_parameters({"input1["+str(k)+"]":X[i][k] for k in range(nb_feature)})
                circ_iter = circ_iter.assign_parameters({"input2["+str(k)+"]":X[j][k] for k in range(nb_feature)})
                circ_list.append(circ_iter)

    circ_list = [pass_manager.run(i) for i in circ_list]
    sampler = Sampler(backend)
    job = sampler.run(circ_list)
    result = job.result()

    index = 0
    res = np.eye(n) # similarity matrix to be completed
    for i in range(len(X)):
        for j in range(len(X)):
            # We fill only upper values
            if i > j:
                bitstring = result[index].data.meas.get_bitstrings()
                nb_shots = result[index].metadata["shots"]
                fidelity = bitstring.count('0'*nb_qubits)/nb_shots
                res[i,j] = fidelity
                res[j,i] = fidelity
                index += 1

    return res

## Similarity swap test matrix

def similarity_swap(nb_qubits, nb_feature, X, backend, pass_manager):
    n = len(X)

    circ = fidelity_SwapTest_circuit(nb_qubits, nb_feature)
    circ_list = []
    for i in range(len(X)):
        for j in range(len(X)):
            # We keep only upper values
            if i > j:
                circ_iter = circ.copy()
                circ_iter = circ_iter.assign_parameters({"input1["+str(k)+"]":X[i][k] for k in range(nb_feature)})
                circ_iter = circ_iter.assign_parameters({"input2["+str(k)+"]":X[j][k] for k in range(nb_feature)})
                circ_list.append(circ_iter)

    circ_list = [pass_manager.run(i) for i in circ_list]

    sampler = Sampler(backend)
    job = sampler.run(circ_list)
    result = job.result()

    res = np.eye(n) # similarity matrix to be completed
    for i in range(len(X)):
        for j in range(len(X)):
            # We fill only upper values
            if i > j:
                bitstring = result[i+j-1].data.c.get_bitstrings()
                nb_shots = result[i+j-1].metadata["shots"]
                fidelity = bitstring.count('0')/nb_shots
                res[i,j] = fidelity
                res[j,i] = fidelity

    return res

## Examples

similarity_adjoint(2, 1, [[0.2, 1], [0.8, 1.2], [1.4, 1.6], [0.7, 0.9]], sim, pm)
similarity_swap(2, 1, [[0.2], [0.8], [1.4]], sim, pm)