import gym
import numpy as np
from keras.models import load_model
from rl.agents.dqn import DQNAgent
from rl.policy import GreedyQPolicy
from rl.memory import SequentialMemory

# Environment setup
ENV_NAME = 'Breakout-v0'
env = gym.make(ENV_NAME)
np.random.seed(123)
env.seed(123)
nb_actions = env.action_space.n

# Load the trained model
model = load_model('policy.h5')

# Configure the agent for testing
memory = SequentialMemory(limit=1000000, window_length=1)  # Same configuration as training
policy = GreedyQPolicy()  # Use GreedyQPolicy for deterministic actions
dqn = DQNAgent(model=model, nb_actions=nb_actions, memory=memory, policy=policy,
               nb_steps_warmup=0, gamma=0.99, target_model_update=1)
dqn.compile(optimizer='adam', metrics=['mae'])

# Play the game
dqn.test(env, nb_episodes=5, visualize=True)
