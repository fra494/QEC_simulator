from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister


def shor_encoding(input_circuit):

    q = input_circuit.qubits

    # gate
    input_circuit.cx(q[0], q[3])
    input_circuit.cx(q[0], q[6])
    input_circuit.h(q[0])
    input_circuit.h(q[6])
    input_circuit.h(q[3])

    input_circuit.cx(q[0], q[1])
    input_circuit.cx(q[6], q[7])
    input_circuit.cx(q[3], q[4])

    input_circuit.cx(q[0], q[2])
    input_circuit.cx(q[6], q[8])
    input_circuit.cx(q[3], q[5])

    input_circuit.barrier()




