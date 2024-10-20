# # from stable_baselines3 import PPO
# # from website_env import WebsiteEnv

# # # Create the environment
# # env = WebsiteEnv()

# # # Create PPO model with the environment
# # model = PPO("MlpPolicy", env, verbose=1)

# # # Train the model
# # model.learn(total_timesteps=10000)

# # # Save the trained model
# # model.save("saved_models/ppo_website_env")

# # # You can reload the model later
# # # model = PPO.load("saved_models/ppo_website_env")


# import gymnasium as gym
# from stable_baselines3 import PPO
# from environment import ColorEnv

# # Create environment
# env = ColorEnv(json_folder="./filtered_recordings")

# # Initialize PPO model
# model = PPO("MlpPolicy", env, verbose=1)

# # Train the model
# model.learn(total_timesteps=10000)

# # Save the trained model
# model.save("saved_model/ppo_model")
# print("Model saved!")


# import gymnasium as gym
# from stable_baselines3 import PPO
# from environment import ColorEnv

# # Create environment
# env = ColorEnv(json_folder="./filtered_recordings")

# # Initialize PPO model
# model = PPO("MlpPolicy", env, verbose=1)

# # Train the model
# model.learn(total_timesteps=100000)

# # Save the trained model
# model.save("saved_model/ppo_model")
# print("Model saved!")

# train.py
import gymnasium as gym
from stable_baselines3 import PPO
from environment import ColorEnv

# Create environment
env = ColorEnv(json_folder="./filtered_recordings")

# Initialize PPO model
model = PPO("MlpPolicy", env, verbose=1)

# Train the model
model.learn(total_timesteps=100000)

# Save the trained model
model.save("saved_model/ppo_model")
print("Model saved!")
