from embedding import embbeding_circuit
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

## Fidelity Adjoint circuit

def fidelity_adjoint_circuit(nb_qubits, nb_feature):
    """
        nb_qubits : nomber of qubits in the circuit
        nb_feature : nb_feature of data
        This function insert the data in the circuit for fidelity with adjoint method
    """
    qc1 = embbeding_circuit(nb_qubits, nb_feature, name="input1")
    qc2 = embbeding_circuit(nb_qubits, nb_feature, name="input2")
    qc2_inverse = qc2.inverse().to_gate()
    qc1.append(qc2_inverse, [i for i in range(nb_qubits)])
    qc1.measure_all()
    return qc1

fidelity_adjoint_circuit(3, 2).decompose().draw()

## Fidelity Swap test circuit

def fidelity_SwapTest_circuit(nb_qubits, nb_feature):
    """
        nb_qubits : nomber of qubits in the circuit
        nb_feature : nb_feature of data
        This function insert the data in the circuit for fidelity with Swap Test
    """
    qc = QuantumCircuit(2*nb_qubits + 1, 1)
    qc1 = embbeding_circuit(nb_qubits, nb_feature, name="input1")
    qc2 = embbeding_circuit(nb_qubits, nb_feature, name="input2")
    qc = qc.compose(qc1, qubits=[i for i in range(1, nb_qubits+1)])
    qc = qc.compose(qc2, qubits=[i for i in range(nb_qubits+1, 2*nb_qubits+1)])
    # SwapTest
    qc.h(0)
    for i in range(1, nb_qubits+1):
        qc.cswap(0, i, i + nb_qubits)
    qc.h(0)

    qc.measure(0,0)
    return qc

fidelity_SwapTest_circuit(3, 2).draw()

## Fidelity calculus

nb_shots = 1024 #1024 by default
sim = AerSimulator(shots=nb_shots)
p1, p2 = [0.2,0.2], [0.8,0.8] # Example vectors

# With adjoint circuit
circ = fidelity_adjoint_circuit(3, 2)
circ = circ.assign_parameters({"input1["+str(i)+"]":p1[i] for i in range(2)})
circ = circ.assign_parameters({"input2["+str(i)+"]":p2[i] for i in range(2)})
circ = transpile(circ, sim)
# Calcul fidelity
result = sim.run(circ).result()
fidelity = result.get_counts(circ)['000']/nb_shots
print(fidelity)

# With swap test circuits
circ = fidelity_SwapTest_circuit(3, 2)
circ = circ.assign_parameters({"input1["+str(i)+"]":p1[i] for i in range(2)})
circ = circ.assign_parameters({"input2["+str(i)+"]":p2[i] for i in range(2)})
circ = transpile(circ, sim)
# Calcul fidelity
result = sim.run(circ).result()
fidelity = result.get_counts(circ)['0']/nb_shots
print(fidelity)