import tensorflow as tf
import numpy as np
import gym

# Actor-Critic Network
class ActorCriticNetwork(tf.keras.Model):
    def __init__(self, n_actions):
        super(ActorCriticNetwork, self).__init__()
        self.dense_shared = tf.keras.layers.Dense(128, activation='relu')
        self.dense_policy = tf.keras.layers.Dense(n_actions, activation='softmax')
        self.dense_value = tf.keras.layers.Dense(1, activation='linear')

    def call(self, state):
        x = self.dense_shared(state)
        policy = self.dense_policy(x)
        value = self.dense_value(x)
        return policy, value

# Actor-Critic Agent
class ActorCriticAgent:
    def __init__(self, n_actions, gamma=0.99, actor_lr=0.001, critic_lr=0.001):
        self.n_actions = n_actions
        self.gamma = gamma
        self.actor_lr = actor_lr
        self.critic_lr = critic_lr

        self.actor_critic_network = ActorCriticNetwork(n_actions)
        self.actor_optimizer = tf.keras.optimizers.Adam(learning_rate=actor_lr)
        self.critic_optimizer = tf.keras.optimizers.Adam(learning_rate=critic_lr)

    def select_action(self, state):
        state = tf.convert_to_tensor([state], dtype=tf.float32)
        policy, _ = self.actor_critic_network(state)
        action = np.random.choice(self.n_actions, p=np.squeeze(policy))
        return action

    def train(self, states, actions, rewards, next_states, dones):
        states = tf.convert_to_tensor(states, dtype=tf.float32)
        actions = tf.convert_to_tensor(actions, dtype=tf.int32)
        rewards = tf.convert_to_tensor(rewards, dtype=tf.float32)
        next_states = tf.convert_to_tensor(next_states, dtype=tf.float32)
        dones = tf.convert_to_tensor(dones, dtype=tf.float32)

        with tf.GradientTape(persistent=True) as tape:
            policy, value = self.actor_critic_network(states)
            next_policy, next_value = self.actor_critic_network(next_states)

            advantages = rewards + self.gamma * (1 - dones) * next_value.numpy() - value.numpy()
            actor_loss = -tf.reduce_sum(tf.math.log(tf.reduce_sum(policy * tf.one_hot(actions, self.n_actions), axis=1)) * advantages)
            critic_loss = tf.reduce_sum(tf.square(advantages))

        actor_gradients = tape.gradient(actor_loss, self.actor_critic_network.trainable_variables)
        critic_gradients = tape.gradient(critic_loss, self.actor_critic_network.trainable_variables)

        self.actor_optimizer.apply_gradients(zip(actor_gradients, self.actor_critic_network.trainable_variables))
        self.critic_optimizer.apply_gradients(zip(critic_gradients, self.actor_critic_network.trainable_variables))

# Training the Actor-Critic Agent on CartPole
def train_actor_critic_agent(env, agent, num_episodes=1000):
    for episode in range(num_episodes):
        states, actions, rewards, next_states, dones = [], [], [], [], []
        state = env.reset()
        done = False

        while not done:
            action = agent.select_action(state)
            next_state, reward, done, _ = env.step(action)

            states.append(state)
            actions.append(action)
            rewards.append(reward)
            next_states.append(next_state)
            dones.append(done)

            state = next_state

        agent.train(states, actions, rewards, next_states, dones)

# Evaluate the trained agent on CartPole
def evaluate_actor_critic_agent(env, agent, num_episodes=10):
    total_rewards = []
    for _ in range(num_episodes):
        state = env.reset()
        total_reward = 0
        done = False

        while not done:
            action = agent.select_action(state)
            state, reward, done, _ = env.step(action)
            total_reward += reward

        total_rewards.append(total_reward)

    average_reward = np.mean(total_rewards)
    return average_reward

# Create CartPole environment
env = gym.make('CartPole-v1')
n_actions = env.action_space.n
state_size = env.observation_space.shape[0]

# Create Actor-Critic agent and train
actor_critic_agent = ActorCriticAgent(n_actions=n_actions)
train_actor_critic_agent(env, actor_critic_agent)

# Evaluate the trained agent
avg_reward = evaluate_actor_critic_agent(env, actor_critic_agent)
print(f"Average Reward over 10 episodes: {avg_reward}")

env.close()
