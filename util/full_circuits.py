from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit.providers.basic_provider import BasicSimulator, BasicProviderJob
from qiskit.quantum_info import DensityMatrix, partial_trace
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, depolarizing_error, amplitude_damping_error, phase_damping_error

from util.encoder import shor_encoding
from util.channel_sim import quantum_pauli_channel, quantum_delay_channel_all_qb, quantum_delay_channel_one_qb, ideal_empty_channel
from util.correction_and_recovery import shor_correction, decode_no_correction

import numpy as np


def no_error(alpha, beta):

    q_in = QuantumRegister(1, 'q_in')
    prep = QuantumCircuit(q_in)
    c = ClassicalRegister(1, 'c')

    #COSTRUZIONE DEL CIRCUITO

    prep.initialize([alpha, beta], q_in[0])
    encoded, encoding_circuit = shor_encoding(prep)
    after_channel, channel_circuit = ideal_empty_channel(encoded)
    full_circuit, decoding_circuit = shor_correction(after_channel)
    full_circuit.draw(output='mpl', filename="./circuits_img/no_noise.png")

    #ESECUZIONE DEL CIRCUITO SU SIMULATORE

    sim = AerSimulator()
    transpiled_circuit = transpile(full_circuit, sim)
    result = sim.run(transpiled_circuit, shots=100).result()

    return result.get_counts()


def uniform_pauli_channel_error(alpha, beta, p):

    q_in = QuantumRegister(1, 'q_in')
    prep = QuantumCircuit(q_in)
    c = ClassicalRegister(1, 'c')

    #COSTRUZIONE DEL CIRCUITO

    prep.initialize([alpha, beta], q_in[0])
    encoded, encoding_circuit = shor_encoding(prep)
    after_channel, channel_circuit = quantum_pauli_channel(encoded)
    full_circuit, decoding_circuit = shor_correction(after_channel)
    full_circuit.draw(output='mpl', filename="./circuits_img/uniform_pauli_channel.png")

    #ESECUZIONE DEL CIRCUITO SU SIMULATORE

    sim = AerSimulator()
    transpiled_circuit = transpile(full_circuit, sim)
    result = sim.run(transpiled_circuit, shots=100).result()

    return result.get_counts()

def uniform_pauli_channel_error_nc(alpha, beta, p):

    q_in = QuantumRegister(1, 'q_in')
    prep = QuantumCircuit(q_in)
    c = ClassicalRegister(1, 'c')

    #COSTRUZIONE DEL CIRCUITO

    prep.initialize([alpha, beta], q_in[0])
    encoded, encoding_circuit = shor_encoding(prep)
    after_channel, channel_circuit = quantum_pauli_channel(encoded)
    full_circuit, decoding_circuit = decode_no_correction(after_channel, encoding_circuit)
    full_circuit.draw(output='mpl', filename="./circuits_img/uniform_pauli_channel_nc.png")

    #ESECUZIONE DEL CIRCUITO SU SIMULATORE

    sim = AerSimulator()
    transpiled_circuit = transpile(full_circuit, sim)
    result = sim.run(transpiled_circuit, shots=100).result()

    return result.get_counts()

def depolarizing_channel_error(alpha, beta, p):

    q_in = QuantumRegister(1, 'q_in')
    prep = QuantumCircuit(q_in)
    c = ClassicalRegister(1, 'c')

    #COSTRUZIONE DEL CIRCUITO

    prep.initialize([alpha, beta], q_in[0])
    encoded, encoding_circuit = shor_encoding(prep)
    after_channel, channel_circuit = quantum_delay_channel_all_qb(encoded)
    #after_channel, channel_circuit = quantum_delay_channel_one_qb(encoded)
    full_circuit, decoding_circuit = shor_correction(after_channel)
    full_circuit.draw(output='mpl', filename="./circuits_img/depolarizing_channel.png")

    #ESECUZIONE DEL CIRCUITO SU SIMULATORE

    noise_model = NoiseModel()
    error = depolarizing_error(p, 1)
    noise_model.add_all_qubit_quantum_error(error, instructions=['delay'])
    sim = AerSimulator(noise_model=noise_model)
    transpiled_circuit = transpile(full_circuit, sim)
    result = sim.run(transpiled_circuit, shots=100).result()

    return result.get_counts()


def depolarizing_channel_error_nc(alpha, beta, p):

    q_in = QuantumRegister(1, 'q_in')
    prep = QuantumCircuit(q_in)
    c = ClassicalRegister(1, 'c')

    #COSTRUZIONE DEL CIRCUITO

    prep.initialize([alpha, beta], q_in[0])
    encoded, encoding_circuit = shor_encoding(prep)
    after_channel, channel_circuit = quantum_delay_channel_all_qb(encoded)
    #after_channel, channel_circuit = quantum_delay_channel_one_qb(encoded)
    full_circuit, decoding_circuit = decode_no_correction(after_channel, encoding_circuit)
    full_circuit.draw(output='mpl', filename="./circuits_img/depolarizing_channel_nc.png")

    #ESECUZIONE DEL CIRCUITO SU SIMULATORE

    noise_model = NoiseModel()
    error = depolarizing_error(p, 1)
    noise_model.add_all_qubit_quantum_error(error, instructions=['delay'])
    sim = AerSimulator(noise_model=noise_model)
    transpiled_circuit = transpile(full_circuit, sim)
    result = sim.run(transpiled_circuit, shots=100).result()

    return result.get_counts()


def amplitude_damping_channel_error(alpha, beta, a):

    q_in = QuantumRegister(1, 'q_in')
    prep = QuantumCircuit(q_in)
    c = ClassicalRegister(1, 'c')

    #COSTRUZIONE DEL CIRCUITO

    prep.initialize([alpha, beta], q_in[0])
    encoded, encoding_circuit = shor_encoding(prep)
    #after_channel, channel_circuit = quantum_delay_channel_all_qb(encoded)
    after_channel, channel_circuit = quantum_delay_channel_one_qb(encoded)
    full_circuit, decoding_circuit = shor_correction(after_channel)
    full_circuit.draw(output='mpl', filename="./circuits_img/amplitude_damping_channel.png")

    #ESECUZIONE DEL CIRCUITO SU SIMULATORE

    noise_model = NoiseModel()
    error = amplitude_damping_error(a, 1)
    noise_model.add_all_qubit_quantum_error(error, instructions=['delay'])
    sim = AerSimulator(noise_model=noise_model)
    transpiled_circuit = transpile(full_circuit, sim)
    result = sim.run(transpiled_circuit, shots=100).result()

    return result.get_counts()

def amplitude_damping_channel_error_nc(alpha, beta, a):

    q_in = QuantumRegister(1, 'q_in')
    prep = QuantumCircuit(q_in)
    c = ClassicalRegister(1, 'c')

    #COSTRUZIONE DEL CIRCUITO

    prep.initialize([alpha, beta], q_in[0])
    encoded, encoding_circuit = shor_encoding(prep)
    #after_channel, channel_circuit = quantum_delay_channel_all_qb(encoded)
    after_channel, channel_circuit = quantum_delay_channel_one_qb(encoded)
    full_circuit, decoding_circuit = decode_no_correction(after_channel, encoding_circuit)
    full_circuit.draw(output='mpl', filename="./circuits_img/amplitude_damping_channel_nc.png")

    #ESECUZIONE DEL CIRCUITO SU SIMULATORE

    noise_model = NoiseModel()
    error = amplitude_damping_error(a, 1)
    noise_model.add_all_qubit_quantum_error(error, instructions=['delay'])
    sim = AerSimulator(noise_model=noise_model)
    transpiled_circuit = transpile(full_circuit, sim)
    result = sim.run(transpiled_circuit, shots=100).result()

    return result.get_counts()

def phase_damping_channel_error(alpha, beta, b):

    q_in = QuantumRegister(1, 'q_in')
    prep = QuantumCircuit(q_in)
    c = ClassicalRegister(1, 'c')

    #COSTRUZIONE DEL CIRCUITO

    prep.initialize([alpha, beta], q_in[0])
    encoded, encoding_circuit = shor_encoding(prep)
    after_channel, channel_circuit = quantum_delay_channel_all_qb(encoded)
    #after_channel, channel_circuit = quantum_delay_channel_one_qb(encoded)
    full_circuit, decoding_circuit = shor_correction(after_channel)
    full_circuit.draw(output='mpl', filename="./circuits_img/phase_damping_channel.png")

    #ESECUZIONE DEL CIRCUITO SU SIMULATORE

    noise_model = NoiseModel()
    error = phase_damping_error(b)
    noise_model.add_all_qubit_quantum_error(error, instructions=['delay'])
    sim = AerSimulator(noise_model=noise_model)
    transpiled_circuit = transpile(full_circuit, sim)
    result = sim.run(transpiled_circuit, shots=100).result()

    return result.get_counts()