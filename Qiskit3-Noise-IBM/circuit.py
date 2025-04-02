from qiskit import QuantumCircuit

def circuit_1():
    qc1 = QuantumCircuit(2)
    qc1.h(0)
    qc1.cx(0,1)
    return qc1