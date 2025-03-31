from qiskit import *
from utils import runStateVector

def exampleDraw():
    q = QuantumRegister(2, name="x")    # Allocating 2 qubits
    c = ClassicalRegister(2, name="y")  # Allocating 2 bits

    # We build a quantum circuit with both registers.
    # By default, everything is initialized to 0 and to |0>
    qc = QuantumCircuit(q,c)

    qc.h(q[0])        # Applying Hadamard on qubit 0:
    qc.x(q[0])        # Applying X on qubit 0:
    qc.z(q[0])        # Applying z on qubit 0:
    qc.cx(q[0],q[1])  # Applying CNOT on qubits 0 and 1:
    qc.measure(q, c)  # Mesure of all of register q, storing results in c.
                      # This is still part of the circuit !
    print(qc)         # print the circuit in ASCII form

exampleDraw()

def exampleStateVector():
    q1 = QuantumRegister(3, name="q1")
    q2 = QuantumRegister(1, name="q2")
    qc = QuantumCircuit(q1,q2)
    
    qc.x(q1[0])
    qc.x(q1[1])
    qc.h(q2[0])
    qc.cx(q2[0],q1[2])

    print(qc)
    runStateVector(qc)

exampleStateVector()

def exampleSample():
    q = QuantumRegister(3, name="q1")
    c = ClassicalRegister(3)
    qc = QuantumCircuit(q,c)
    
    qc.x(q[0])
    qc.h(q[1])
    qc.cx(q[1],q[2])


    qc.measure(q,c)

    print(qc)
    return runSample(qc,1000)

print(exampleSample())