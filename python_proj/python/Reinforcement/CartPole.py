import numpy as np
import tensorflow as tf
import gym

# Define the CartPole environment
env = gym.make('CartPole-v1')

# Define the Q-network
model = tf.keras.Sequential([
    tf.keras.layers.Dense(24, activation='relu', input_shape=(env.observation_space.shape[0],)),
    tf.keras.layers.Dense(24, activation='relu'),
    tf.keras.layers.Dense(env.action_space.n, activation='linear')
])

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
              loss='mse')

# Parameters
gamma = 0.99  # discount factor
epsilon = 1.0  # exploration-exploitation trade-off
epsilon_decay = 0.995
epsilon_min = 0.01
batch_size = 64
memory = []

# Training the agent
for episode in range(1000):  # You may need more episodes for better convergence
    state = env.reset()
    state = np.reshape(state, [1, env.observation_space.shape[0]])

    total_reward = 0

    while True:
        # Choose action using epsilon-greedy strategy
        if np.random.rand() <= epsilon:
            action = env.action_space.sample()
        else:
            q_values = model.predict(state)
            action = np.argmax(q_values[0])

        # Take the chosen action and observe the next state and reward
        next_state, reward, done, _ = env.step(action)
        next_state = np.reshape(next_state, [1, env.observation_space.shape[0]])

        # Store the experience in memory
        memory.append((state, action, reward, next_state, done))

        state = next_state
        total_reward += reward

        if done:
            break

    # Train the model using experience replay
    if len(memory) >= batch_size:
        batch = np.random.choice(memory, batch_size, replace=False)
        for state, action, reward, next_state, done in batch:
            target = reward
            if not done:
                target = reward + gamma * np.max(model.predict(next_state)[0])

            target_f = model.predict(state)
            target_f[0][action] = target

            model.fit(state, target_f, epochs=1, verbose=0)

    # Decay epsilon
    if epsilon > epsilon_min:
        epsilon *= epsilon_decay

    print(f"Episode: {episode + 1}, Total Reward: {total_reward}")

# Test the trained agent
total_reward = 0
state = env.reset()
state = np.reshape(state, [1, env.observation_space.shape[0]])

while True:
    action = np.argmax(model.predict(state)[0])
    next_state, reward, done, _ = env.step(action)
    next_state = np.reshape(next_state, [1, env.observation_space.shape[0]])
    state = next_state
    total_reward += reward

    env.render()

    if done:
        break

print(f"Test Total Reward: {total_reward}")

env.close()
