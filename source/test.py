from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from encoder import shor_encoding
from channel_sim import quantum_pauli_channel, quantum_depolarizing_channel
from correction_and_recovery import shor_correction, decode_no_correction
import numpy as np
from qiskit.providers.basic_provider import BasicSimulator, BasicProviderJob
from qiskit.quantum_info import DensityMatrix, partial_trace
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, depolarizing_error, amplitude_damping_error

q_in = QuantumRegister(1, 'q_in')
prep = QuantumCircuit(q_in)
c = ClassicalRegister(1, 'c')

alpha = 0
beta = 1

# prepari lo stato iniziale
prep.initialize([alpha, beta], q_in[0])

encoded, encoding_circuit = shor_encoding(prep)
after_channel = quantum_depolarizing_channel(encoded)
#after_channel = quantum_pauli_channel(encoded)
#full_circuit = decode_no_correction(after_channel,encoding_circuit)

full_circuit = shor_correction(after_channel)

#print(after_channel.draw())
full_circuit.draw(output='mpl', filename="test.png")





#simulator = BasicSimulator()
#transpiled_circuit = transpile(correction_circuit, simulator)


#results = simulator.run(transpiled_circuit, shots=1024)

#print(results.result().get_counts())

noise_model = NoiseModel()
#error = depolarizing_error(0.01, 1)
error = amplitude_damping_error(0.15)
noise_model.add_all_qubit_quantum_error(error, instructions=['delay'])


sim = AerSimulator(noise_model=noise_model)
#sim = AerSimulator()
transpiled_circuit = transpile(full_circuit, sim)
result = sim.run(transpiled_circuit, shots=1000).result()

print(result.get_counts())