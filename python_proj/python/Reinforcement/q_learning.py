import numpy as np

# Define the Q-learning function
def q_learning(env, num_episodes=1000, alpha=0.1, gamma=0.9, epsilon=0.1):
    # Initialize Q-table with zeros
    Q = np.zeros((env.n_states, env.n_actions))

    for episode in range(num_episodes):
        state = env.reset()
        done = False

        while not done:
            # Exploration-exploitation trade-off
            if np.random.rand() < epsilon:
                action = np.random.choice(env.n_actions)
            else:
                action = np.argmax(Q[state, :])

            next_state, reward, done = env.step(action)

            # Q-learning update rule
            Q[state, action] = (1 - alpha) * Q[state, action] + \
                               alpha * (reward + gamma * np.max(Q[next_state, :]))

            state = next_state

    return Q

# Define a simple grid-world environment
class GridWorld:
    def __init__(self):
        self.n_states = 16
        self.n_actions = 4
        self.transition_probs = np.array([
            [1, 5, 0, 4], [2, 6, 1, 5], [3, 7, 2, 6],
            [3, 8, 3, 7], [5, 9, 4, 8], [6, 10, 5, 9],
            [7, 11, 6, 10], [7, 12, 7, 11], [9, 13, 8, 12],
            [10, 14, 9, 13], [11, 15, 10, 14], [11, 15, 11, 15],
            [13, 13, 12, 12], [14, 14, 13, 13], [15, 15, 14, 14], [15, 15, 15, 15]
        ])
        self.rewards = np.array([-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 10])

    def reset(self):
        return 0

    def step(self, action):
        next_state = self.transition_probs[action, self.state]
        reward = self.rewards[next_state]
        self.state = next_state
        done = (next_state == 15)
        return next_state, reward, done

# Run Q-learning on the grid-world environment
grid_world = GridWorld()
learned_Q = q_learning(grid_world)

# Display the learned Q-values
print("Learned Q-values:")
print(learned_Q)
