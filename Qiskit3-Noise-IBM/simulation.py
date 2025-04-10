from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator
from qiskit_ibm_runtime.fake_provider import FakeAthensV2
from circuit import circuit
from utils import runSample

# Circuit selection
qc = circuit()

# Perfect simualtion
simulator = AerSimulator()
counts_perfect = runSample(qc, 4000, simulator)
print("--- Perfect simulation results ---")
print(counts_perfect)
plot_histogram(counts_perfect)

# Noisy simulation
device_backend = FakeAthensV2()
sim_noisy = AerSimulator.from_backend(device_backend)
counts_noisy = runSample(qc, 4000, sim_noisy)
print("--- Noisy simulation results ---")
print(counts_noisy)
plot_histogram(counts_noisy)