import gym
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv2D
from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint
from rl.agents.dqn import DQNAgent
from rl.policy import EpsGreedyQPolicy
from rl.memory import SequentialMemory

# Environment setup
ENV_NAME = 'Breakout-v0'
env = gym.make(ENV_NAME)
np.random.seed(123)
env.seed(123)
nb_actions = env.action_space.n

# Building the model
def build_model(input_shape, nb_actions):
    model = Sequential()
    model.add(Conv2D(32, (8, 8), strides=4, activation='relu', input_shape=input_shape))
    model.add(Conv2D(64, (4, 4), strides=2, activation='relu'))
    model.add(Conv2D(64, (3, 3), strides=1, activation='relu'))
    model.add(Flatten())
    model.add(Dense(512, activation='relu'))
    model.add(Dense(nb_actions, activation='linear'))
    return model

# Define input shape (assuming the default Gym Breakout observation is RGB frames)
input_shape = (1,) + env.observation_space.shape
model = build_model(input_shape, nb_actions)
print(model.summary())

# Configuring the agent
memory = SequentialMemory(limit=1000000, window_length=1)
policy = EpsGreedyQPolicy()
dqn = DQNAgent(model=model, nb_actions=nb_actions, memory=memory, policy=policy,
               nb_steps_warmup=1000, gamma=0.99, target_model_update=1000)
dqn.compile(Adam(learning_rate=0.00025), metrics=['mae'])

# Training the agent
checkpoint = ModelCheckpoint('policy.h5', monitor='episode_reward', save_best_only=True, mode='max')
dqn.fit(env, nb_steps=50000, visualize=False, verbose=2, callbacks=[checkpoint])

# Saving the policy
model.save('policy.h5')

# Test the trained agent
dqn.test(env, nb_episodes=10, visualize=True)
