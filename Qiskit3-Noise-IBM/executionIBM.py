from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit.visualization import plot_histogram
from qiskit_ibm_runtime import SamplerV2 as Sampler
from circuit import circuit
from time import sleep
import matplotlib.pyplot as plt

service = QiskitRuntimeService(
    channel='ibm_quantum',
    instance='ibm-q/open/main',
    token='<token>'
    )

backend = service.least_busy(operational=True, simulator=False)

def runSample_IBM(backend, qc_list):
    pm = generate_preset_pass_manager(backend=backend, optimization_level=1)
    qc_optimized_list = [pm.run(qc) for qc in qc_list]
    sampler = Sampler(backend)
    job = sampler.run(qc_optimized_list)
    # Waiting for job to complete to get data
    print(f"Estimated time: {job.usage_estimation['quantum_seconds']:.3f}s")
    while not job.done():
        sleep(1)
    print(f"Job done !")
    print(f"Estimated time: {job.usage_estimation['quantum_seconds']:.3f}s | Real time: {job.usage()}s")
    # Get final data
    result = job.result()
    counts = result[0].data.meas.get_counts()
    return counts

if __name__ == "__main__":
    # Circuit selection
    qc = circuit()
    print("--- Running circuit on IBM hardware --- Waiting")
    counts = runSample_IBM(backend, [qc])
    print("\n--- Counts result ---")
    print(counts)
    plot_histogram(counts)
    plt.show()