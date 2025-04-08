from qiskit import ClassicalRegister, QuantumRegister, QuantumCircuit
from utils import runStateVector, runSample

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
    qc.measure(q, c)  # Mesure of all of register q, storing results in c (part of the circuit)
    return qc

def exampleStateVector():
    q1 = QuantumRegister(3, name="q1")
    q2 = QuantumRegister(1, name="q2")
    qc = QuantumCircuit(q1,q2)
    
    qc.x(q1[0])
    qc.x(q1[1])
    qc.h(q2[0])
    qc.cx(q2[0],q1[2])
    return qc

def exampleSample():
    q = QuantumRegister(3, name="q1")
    c = ClassicalRegister(3)
    qc = QuantumCircuit(q,c)
    
    qc.x(q[0])
    qc.h(q[1])
    qc.cx(q[1],q[2])
    qc.measure(q,c)
    return qc

## Draw and run circuits

# print the circuit in ASCII form
print("--- Circuit 1 - Draw ---\n")
qc1 = exampleDraw()
print(qc1)

# Compute the output state vector
print("\n--- Circuit 2 - Compute state vector ---\n")
qc2 = exampleStateVector()
print(qc2)
print("\nThe state vector is: \n")
runStateVector(qc2)

# Run the circuit with a simulator
# Need measure to get a result, else it will raise a QiskitError
NB_SHOTS = 1000 # Number of executions of the circuit
print("\n--- Circuit 3 - Simulation of measures ---\n")
qc3 = exampleSample()
print(qc3)
print("\nThe result of measures is (number of measures): \n")
# We get a dictionnary with the amount of measures for each state (sample)
runSample(qc3,NB_SHOTS)