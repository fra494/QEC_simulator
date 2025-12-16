from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from encoder import shor_encoding
from channel_sim import quantum_channel
from correction_and_recovery import shor_correction
import numpy as np
from qiskit.providers.basic_provider import BasicSimulator, BasicProviderJob
from qiskit.quantum_info import DensityMatrix, partial_trace

q_in = QuantumRegister(1, 'q_in')
prep = QuantumCircuit(q_in)
c = ClassicalRegister(1, 'c')

alpha = 0
beta = 1

# prepari lo stato iniziale
prep.initialize([alpha, beta], q_in[0])

encoded = shor_encoding(prep)
after_channel = quantum_channel(encoded)
correction_circuit = shor_correction(after_channel)

#print(after_channel.draw())
print(correction_circuit.draw())





simulator = BasicSimulator()
transpiled_circuit = transpile(correction_circuit, simulator)


results = simulator.run(transpiled_circuit, shots=1024)

print(results.result().get_counts())


