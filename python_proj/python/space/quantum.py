from qiskit import Aer, QuantumCircuit, transpile, assemble, execute
from qiskit.visualization import plot_histogram, plot_bloch_multivector
from qiskit.extensions import Initialize

# Function to create the quantum teleportation circuit
def create_teleportation_circuit():
    qc = QuantumCircuit(3, 3)

    # Create an entangled pair of qubits (Bell pair)
    qc.h(1)
    qc.cx(1, 2)

    # Prepare the state to be teleported
    initial_state = [0, 1]
    qc.initialize(initial_state, 0)

    # Bell measurement
    qc.cx(0, 1)
    qc.h(0)
    qc.measure([0, 1], [0, 1])

    # Correction based on measurement results
    qc.cx(1, 2)
    qc.cz(0, 2)

    # Measure the result
    qc.measure(2, 2)

    return qc

# Simulate the quantum teleportation circuit
def simulate_teleportation_circuit(qc):
    backend = Aer.get_backend('qasm_simulator')
    transpiled_qc = transpile(qc, backend)
    qobj = assemble(transpiled_qc)
    result = execute(qc, backend, shots=1024).result()
    counts = result.get_counts()
    return counts

# Create and simulate the quantum teleportation circuit
teleportation_circuit = create_teleportation_circuit()
result_counts = simulate_teleportation_circuit(teleportation_circuit)

# Display the results
print("Results:", result_counts)
plot_histogram(result_counts)

# Visualize the final state using Bloch vectors
final_state = execute(teleportation_circuit, Aer.get_backend('statevector_simulator')).result().get_statevector()
plot_bloch_multivector(final_state)

