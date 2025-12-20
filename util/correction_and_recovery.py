from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister

def shor_correction(input_circuit):

    c = ClassicalRegister(1, 'c')

    q = input_circuit.qubits
    input_circuit.add_register(c)

    # gates
    input_circuit.cx(q[3], q[4])
    input_circuit.cx(q[6], q[7])
    input_circuit.cx(q[0], q[1])
    input_circuit.cx(q[3], q[5])
    input_circuit.cx(q[6], q[8])
    input_circuit.cx(q[0], q[2])

    input_circuit.ccx(q[4], q[5], q[3])
    input_circuit.ccx(q[7], q[8], q[6])
    input_circuit.ccx(q[1], q[2], q[0])

    input_circuit.h(q[3])
    input_circuit.h(q[6])
    input_circuit.h(q[0])

    input_circuit.cx(q[0], q[3])
    input_circuit.cx(q[0], q[6])

    input_circuit.ccx(q[3], q[6], q[0])

    input_circuit.barrier()

    input_circuit.measure([0], [0])



def decode_no_correction(input_circuit):

    c = ClassicalRegister(1, 'c')

    q = input_circuit.qubits
    input_circuit.add_register(c)

    #gates

    input_circuit.cx(q[0], q[2])
    input_circuit.cx(q[0], q[1])
    input_circuit.h(q[0])

    input_circuit.cx(q[3], q[5])
    input_circuit.cx(q[3], q[4])
    input_circuit.h(q[3])

    input_circuit.cx(q[6], q[8])
    input_circuit.cx(q[6], q[7])
    input_circuit.h(q[6])

    input_circuit.cx(q[0], q[6])
    input_circuit.cx(q[0], q[3])

    input_circuit.measure([0], [0])
