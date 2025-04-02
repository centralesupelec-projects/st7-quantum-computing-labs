from qiskit import transpile
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator
from qiskit_ibm_runtime.fake_provider import FakeAthensV2
from circuit import circuit_1

device_backend = FakeAthensV2()
simulator = AerSimulator()
sim_noisy = AerSimulator.from_backend(device_backend)

qc = circuit_1()
circ = transpile(qc, sim_noisy)

result = sim_noisy.run(circ, shots=4000).result()
print(result)
counts = result.get_counts(circ)
plot_histogram(counts)