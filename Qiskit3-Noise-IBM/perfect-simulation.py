from qiskit import transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from circuit import circuit_1

simulator = AerSimulator()

qc = circuit_1()
circ = transpile(qc, simulator)

result = simulator.run(circ, shots=4000).result()
print(result)
counts = result.get_counts(circ)
print(counts)
plot_histogram(counts)