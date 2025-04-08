from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from utils import runStateVector, runSample

## Exercice 2 ##

# 1 - Implement the "bogus" circuit and double-check what we discussed
# You will need to generate an entangled state as above!
# 2. Now, implement the "correct" version and check that
# the ancilla wire is separated from the other registers.
# Note: In QisKit, Toffoli gates are .ccx()

def bogus():
    q = QuantumRegister(5, name="q1")
    c = ClassicalRegister(5)
    qc = QuantumCircuit(q, c)
    
    qc.ccx(q[0], q[1], q[4])
    qc.ccx(q[2], q[4], q[3])
    return qc

def bogus_corrected():
    q = QuantumRegister(5, name="q1")
    c = ClassicalRegister(5)
    qc = QuantumCircuit(q, c)
    
    qc.ccx(q[0], q[1], q[4])
    qc.ccx(q[2], q[4], q[3])
    qc.ccx(q[0], q[1], q[4])
    return qc

def entangled_input(n):
    qc = QuantumCircuit(n)
    
    qc.x(0)
    qc.h(0)
    for i in range(1, n-1):
        qc.cx(0, i)
    return qc

def post_circuit():
    qc = QuantumCircuit(5)
    for i in range(2, 0, -1):
        qc.cx(0, i)
    qc.h(0)
    qc.x(0)
    return qc

def complete_circuit(mode, measure=False):
    if mode == "cccx":
        q = QuantumRegister(5, name="q1")
        c = ClassicalRegister(5)
        qc0 = QuantumCircuit(q,c)
        qc0.mcx([0,1,2],3)
    elif mode == "bogus":
        qc0 = bogus()
    elif mode == "bogus-corrected":
        qc0 = bogus_corrected()
    else:
        raise ValueError("Mode should be cccx, bogus or bogus-corrected")
    input_state = entangled_input(5)
    qc0 = input_state.compose(qc0, qubits=[0, 1, 2, 3, 4])
    qc1 = post_circuit()
    complete = qc0.compose(qc1, qubits=[0, 1, 2, 3, 4])
    if measure:
        complete.measure([0,1,2,3], [0,1,2,3])
    return complete

# Case 1: basic state input : |0000>;
print("Basic state:")
circuit = bogus()
print(circuit)
runStateVector(circuit)

# Case 2: entangled state input
print("Entangled state:")
input_state = entangled_input(5)
combined = input_state.compose(circuit, qubits=[0, 1, 2, 3, 4])
print(combined)
runStateVector(input_state)
runStateVector(combined)

# Case 3: computation with measure: cccx vs BOGUS
print("\nSample measure with BOGUS:")
complete = complete_circuit(mode="bogus", measure=True)
print(complete)
runSample(complete, 1000)

print("\nSample measure with CCCX:")
complete = complete_circuit(mode="cccx", measure=True)
print(complete)
runSample(complete, 1000)

# Case 4: Bogus correction
print("\nSample measure with bogus corrected !:")
complete = complete_circuit(mode="bogus-corrected", measure=True)
print(complete)
runSample(complete, 1000)