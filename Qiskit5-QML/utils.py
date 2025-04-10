from qiskit import transpile
from qiskit_aer import AerSimulator
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_ibm_runtime import SamplerV2 as Sampler

def get_fidelity_adjoint(qc, howmany):
    simulator = AerSimulator()
    circ = transpile(qc, simulator)
    result = simulator.run(circ, shots=howmany).result()
    fidelity = result.get_counts(circ)['000']/howmany
    return fidelity

def get_fidelity_swaptest(qc, howmany):
    simulator = AerSimulator()
    circ = transpile(qc, simulator)
    result = simulator.run(circ, shots=howmany).result()
    fidelity = result.get_counts(circ)['0']/howmany
    return fidelity

def runCircuits(circ_list):
    simulator = AerSimulator()
    pass_manager = generate_preset_pass_manager(backend=simulator, optimization_level=1)
    circ_list = [pass_manager.run(i) for i in circ_list]
    sampler = Sampler(simulator)
    job = sampler.run(circ_list)
    result = job.result()
    return result