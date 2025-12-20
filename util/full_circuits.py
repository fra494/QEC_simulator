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

    q = QuantumRegister(9, 'q')
    qc = QuantumCircuit(q)

    #COSTRUZIONE DEL CIRCUITO

    qc.initialize([alpha, beta], q[0])
    shor_encoding(qc)
    ideal_empty_channel(qc)
    shor_correction(qc)

    qc.draw(output='mpl', filename="./circuits_img/no_noise.png")

    #ESECUZIONE DEL CIRCUITO SU SIMULATORE

    sim = AerSimulator()
    transpiled_circuit = transpile(qc, sim)
    result = sim.run(transpiled_circuit, shots=100).result()

    return result.get_counts()


def uniform_pauli_channel_error(alpha, beta, p):

    q = QuantumRegister(9, 'q')
    qc = QuantumCircuit(q)

    #COSTRUZIONE DEL CIRCUITO

    qc.initialize([alpha, beta], q[0])
    shor_encoding(qc)
    quantum_pauli_channel(qc, p)
    shor_correction(qc)

    qc.draw(output='mpl', filename="./circuits_img/uniform_pauli_channel.png")

    #ESECUZIONE DEL CIRCUITO SU SIMULATORE

    sim = AerSimulator()
    transpiled_circuit = transpile(qc, sim)
    result = sim.run(transpiled_circuit, shots=100).result()

    return result.get_counts()


def uniform_pauli_channel_error_nc(alpha, beta, p):

    q = QuantumRegister(9, 'q')
    qc = QuantumCircuit(q)

    #COSTRUZIONE DEL CIRCUITO

    qc.initialize([alpha, beta], q[0])
    shor_encoding(qc)
    quantum_pauli_channel(qc, p)
    decode_no_correction(qc)

    qc.draw(output='mpl', filename="./circuits_img/uniform_pauli_channel_nc.png")

    #ESECUZIONE DEL CIRCUITO SU SIMULATORE

    sim = AerSimulator()
    transpiled_circuit = transpile(qc, sim)
    result = sim.run(transpiled_circuit, shots=100).result()

    return result.get_counts()

    

def depolarizing_channel_error(alpha, beta, p):

    q = QuantumRegister(9, 'q')
    qc = QuantumCircuit(q)

    #COSTRUZIONE DEL CIRCUITO

    qc.initialize([alpha, beta], q[0])
    shor_encoding(qc)
    #quantum_delay_channel_all_qb(qc)
    quantum_delay_channel_one_qb(qc)
    shor_correction(qc)

    qc.draw(output='mpl', filename="./circuits_img/depolarizing_channel.png")

    #ESECUZIONE DEL CIRCUITO SU SIMULATORE

    noise_model = NoiseModel()
    error = depolarizing_error(p, 1)
    noise_model.add_all_qubit_quantum_error(error, instructions=['delay'])
    sim = AerSimulator(noise_model=noise_model)
    transpiled_circuit = transpile(qc, sim)
    result = sim.run(transpiled_circuit, shots=100).result()

    return result.get_counts()



def depolarizing_channel_error_nc(alpha, beta, p):

    q = QuantumRegister(9, 'q')
    qc = QuantumCircuit(q)

    #COSTRUZIONE DEL CIRCUITO

    qc.initialize([alpha, beta], q[0])
    shor_encoding(qc)
    #quantum_delay_channel_all_qb(qc)
    quantum_delay_channel_one_qb(qc)
    decode_no_correction(qc)

    qc.draw(output='mpl', filename="./circuits_img/depolarizing_channel_nc.png")

    #ESECUZIONE DEL CIRCUITO SU SIMULATORE

    noise_model = NoiseModel()
    error = depolarizing_error(p, 1)
    noise_model.add_all_qubit_quantum_error(error, instructions=['delay'])
    sim = AerSimulator(noise_model=noise_model)
    transpiled_circuit = transpile(qc, sim)
    result = sim.run(transpiled_circuit, shots=100).result()

    return result.get_counts()



def amplitude_damping_channel_error(alpha, beta, a):

    q = QuantumRegister(9, 'q')
    qc = QuantumCircuit(q)

    #COSTRUZIONE DEL CIRCUITO

    qc.initialize([alpha, beta], q[0])
    shor_encoding(qc)
    #quantum_delay_channel_all_qb(qc)
    quantum_delay_channel_one_qb(qc)
    shor_correction(qc)

    qc.draw(output='mpl', filename="./circuits_img/amplitude_damping_channel.png")

    #ESECUZIONE DEL CIRCUITO SU SIMULATORE

    noise_model = NoiseModel()
    error = amplitude_damping_error(a)
    noise_model.add_all_qubit_quantum_error(error, instructions=['delay'])
    sim = AerSimulator(noise_model=noise_model)
    transpiled_circuit = transpile(qc, sim)
    result = sim.run(transpiled_circuit, shots=100).result()

    return result.get_counts()



def amplitude_damping_channel_error_nc(alpha, beta, a):

    q = QuantumRegister(9, 'q')
    qc = QuantumCircuit(q)

    #COSTRUZIONE DEL CIRCUITO

    qc.initialize([alpha, beta], q[0])
    shor_encoding(qc)
    #quantum_delay_channel_all_qb(qc)
    quantum_delay_channel_one_qb(qc)
    decode_no_correction(qc)

    qc.draw(output='mpl', filename="./circuits_img/amplitude_damping_channel_nc.png")

    #ESECUZIONE DEL CIRCUITO SU SIMULATORE

    noise_model = NoiseModel()
    error = amplitude_damping_error(a)
    noise_model.add_all_qubit_quantum_error(error, instructions=['delay'])
    sim = AerSimulator(noise_model=noise_model)
    transpiled_circuit = transpile(qc, sim)
    result = sim.run(transpiled_circuit, shots=100).result()

    return result.get_counts()



def phase_damping_channel_error(alpha, beta, b):

    q = QuantumRegister(9, 'q')
    qc = QuantumCircuit(q)

    #COSTRUZIONE DEL CIRCUITO

    qc.initialize([alpha, beta], q[0])
    shor_encoding(qc)
    #quantum_delay_channel_all_qb(qc)
    quantum_delay_channel_one_qb(qc)
    shor_correction(qc)

    qc.draw(output='mpl', filename="./circuits_img/phase_damping_channel.png")

    #ESECUZIONE DEL CIRCUITO SU SIMULATORE

    noise_model = NoiseModel()
    error = phase_damping_error(b)
    noise_model.add_all_qubit_quantum_error(error, instructions=['delay'])
    sim = AerSimulator(noise_model=noise_model)
    transpiled_circuit = transpile(qc, sim)
    result = sim.run(transpiled_circuit, shots=100).result()

    return result.get_counts()




def phase_damping_channel_error_nc(alpha, beta, b):

    q = QuantumRegister(9, 'q')
    qc = QuantumCircuit(q)

    #COSTRUZIONE DEL CIRCUITO

    qc.initialize([alpha, beta], q[0])
    shor_encoding(qc)
    #quantum_delay_channel_all_qb(qc)
    quantum_delay_channel_one_qb(qc)
    decode_no_correction(qc)

    qc.draw(output='mpl', filename="./circuits_img/phase_damping_channel_nc.png")

    #ESECUZIONE DEL CIRCUITO SU SIMULATORE

    noise_model = NoiseModel()
    error = phase_damping_error(b)
    noise_model.add_all_qubit_quantum_error(error, instructions=['delay'])
    sim = AerSimulator(noise_model=noise_model)
    transpiled_circuit = transpile(qc, sim)
    result = sim.run(transpiled_circuit, shots=100).result()

    return result.get_counts()