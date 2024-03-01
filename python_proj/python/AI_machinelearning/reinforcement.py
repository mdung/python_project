import numpy as np

# Define the environment (2D grid)
n_rows, n_cols = 3, 4
n_actions = 4  # Up, Down, Left, Right

# Define the Q-table and initialize with zeros
Q = np.zeros((n_rows * n_cols, n_actions))

# Define the reward matrix (negative values for invalid moves)
rewards = np.array([
    [-1, -1, -1, -1],
    [-1, -1, -1, -1],
    [-1, -1, -1, -1],
])

# Define the transition model (next state for each action)
transitions = np.array([
    [1, 4, 0, 0],  # From state 0 (top-left): Down, Right, Up, Left
    [2, 5, 0, 1],  # From state 1: Down, Right, Up, Left
    [2, 6, 1, 2],  # From state 2: Down, Right, Up, Left
    [3, 7, 2, 3],  # From state 3: Down, Right, Up, Left
    [5, 8, 4, 0],  # From state 4: Down, Right, Up, Left
    [6, 9, 4, 1],  # From state 5: Down, Right, Up, Left
    [7, 10, 5, 2],  # From state 6: Down, Right, Up, Left
    [7, 11, 6, 3],  # From state 7: Down, Right, Up, Left
    [9, 11, 8, 4],  # From state 8: Down, Right, Up, Left
    [10, 11, 8, 5],  # From state 9: Down, Right, Up, Left
    [11, 11, 9, 6],  # From state 10: Down, Right, Up, Left
    [11, 11, 10, 7],  # From state 11: Down, Right, Up, Left
])

# Define hyperparameters
gamma = 0.8  # Discount factor
alpha = 0.1  # Learning rate
epsilon = 0.1  # Exploration-exploitation trade-off

# Q-learning algorithm
def q_learning(state, n_episodes=1000):
    for _ in range(n_episodes):
        current_state = state
        while current_state != 11:  # Goal state
            # Exploration-exploitation trade-off
            if np.random.rand() < epsilon:
                action = np.random.randint(0, n_actions)
            else:
                action = np.argmax(Q[current_state, :])

            next_state = transitions[current_state, action]
            reward = rewards[current_state // n_cols, current_state % n_cols]

            # Update Q-value using the Q-learning update rule
            Q[current_state, action] = (1 - alpha) * Q[current_state, action] + \
                                       alpha * (reward + gamma * np.max(Q[next_state, :]))

            current_state = next_state

# Run Q-learning algorithm
q_learning(state=0)

# Display the learned Q-values
print("Learned Q-values:")
print(Q)

# Choose the optimal path from the starting state
current_state = 0
optimal_path = [current_state]
while current_state != 11:
    action = np.argmax(Q[current_state, :])
    current_state = transitions[current_state, action]
    optimal_path.append(current_state)

# Display the optimal path
print("Optimal Path:")
print(optimal_path)
