import tensorflow as tf
import numpy as np
import gym

# Define the Deep Q-Network (DQN) model
class DQN(tf.keras.Model):
    def __init__(self, n_actions):
        super(DQN, self).__init__()
        self.dense1 = tf.keras.layers.Dense(64, activation='relu')
        self.dense2 = tf.keras.layers.Dense(64, activation='relu')
        self.output_layer = tf.keras.layers.Dense(n_actions, activation='linear')

    def call(self, state):
        x = self.dense1(state)
        x = self.dense2(x)
        return self.output_layer(x)

# Define the replay buffer
class ReplayBuffer:
    def __init__(self, buffer_size):
        self.buffer_size = buffer_size
        self.buffer = []

    def add_experience(self, experience):
        self.buffer.append(experience)
        if len(self.buffer) > self.buffer_size:
            self.buffer.pop(0)

    def sample_batch(self, batch_size):
        indices = np.random.choice(len(self.buffer), batch_size, replace=False)
        return [self.buffer[i] for i in indices]

# Define the Deep Q-Learning agent
class DQNAgent:
    def __init__(self, n_actions, epsilon=1.0, epsilon_decay=0.995, min_epsilon=0.01, gamma=0.99):
        self.n_actions = n_actions
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.min_epsilon = min_epsilon
        self.gamma = gamma
        self.model = DQN(n_actions)
        self.target_model = DQN(n_actions)
        self.target_model.set_weights(self.model.get_weights())
        self.optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
        self.replay_buffer = ReplayBuffer(buffer_size=10000)

    def select_action(self, state):
        if np.random.rand() < self.epsilon:
            return np.random.choice(self.n_actions)
        else:
            q_values = self.model.predict(state[np.newaxis, :])
            return np.argmax(q_values)

    def train(self, batch_size=32):
        if len(self.replay_buffer.buffer) < batch_size:
            return

        experiences = self.replay_buffer.sample_batch(batch_size)
        states, actions, rewards, next_states, dones = zip(*experiences)

        states = np.vstack(states)
        next_states = np.vstack(next_states)

        q_values = self.model(states)
        next_q_values = self.target_model(next_states)

        targets = q_values.numpy()
        for i in range(batch_size):
            targets[i, actions[i]] = rewards[i] + (1 - dones[i]) * self.gamma * np.max(next_q_values[i])

        with tf.GradientTape() as tape:
            q_values = self.model(states)
            loss = tf.reduce_mean(tf.square(targets - q_values))

        gradients = tape.gradient(loss, self.model.trainable_variables)
        self.optimizer.apply_gradients(zip(gradients, self.model.trainable_variables))

    def update_target_network(self):
        self.target_model.set_weights(self.model.get_weights())

# Train the DQN agent on the CartPole environment
env = gym.make('CartPole-v1')
n_actions = env.action_space.n
state_size = env.observation_space.shape[0]

agent = DQNAgent(n_actions=n_actions)

num_episodes = 500
for episode in range(num_episodes):
    state = env.reset()
    total_reward = 0

    while True:
        action = agent.select_action(state)
        next_state, reward, done, _ = env.step(action)

        agent.replay_buffer.add_experience((state, action, reward, next_state, done))
        agent.train()

        state = next_state
        total_reward += reward

        if done:
            agent.update_target_network()
            break

    # Decay epsilon for exploration-exploitation trade-off
    agent.epsilon = max(agent.epsilon * agent.epsilon_decay, agent.min_epsilon)

    print(f"Episode {episode + 1}, Total Reward: {total_reward}")

# Evaluate the trained agent
total_rewards = []
for _ in range(10):
    state = env.reset()
    total_reward = 0

    while True:
        action = agent.select_action(state)
        next_state, reward, done, _ = env.step(action)

        state = next_state
        total_reward += reward

        if done:
            break

    total_rewards.append(total_reward)

average_reward = np.mean(total_rewards)
print(f"Average Reward over 10 episodes: {average_reward}")

env.close()
