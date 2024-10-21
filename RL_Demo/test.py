# # import time
# # import json
# # from stable_baselines3 import PPO
# # from website_env import WebsiteEnv

# # # Load the trained PPO model
# # model = PPO.load("saved_models/ppo_website_env")

# # # Create the environment
# # env = WebsiteEnv()

# # # Reset the environment to get the initial observation
# # obs, _ = env.reset()

# # # Run for a few steps to simulate real-time changes
# # for step in range(100):  # Simulate 100 steps, change time as needed
# #     action, _states = model.predict(obs)
# #     obs, rewards, done, info, _ = env.step(action)

# #     # Save the current state (modified by RL agent) to a JSON file every 10 seconds
# #     ui_data = {
# #         "fontSize": obs[0],
# #         "fontColor": obs[1],
# #         "backgroundColor": obs[2],
# #         "timestamp": time.time()
# #     }

# #     with open(f"data/rl_modified_ui_step_{step}.json", 'w') as outfile:
# #         json.dump(ui_data, outfile, indent=4)

# #     # Sleep for 10 seconds to simulate real-time updates
# #     time.sleep(10)

# #     # Reset the environment if done
# #     if done:
# #         obs, _ = env.reset()

# # import time
# # import json
# # from stable_baselines3 import PPO
# # from website_env import WebsiteEnv

# # # Function to convert float value to a pixel font size
# # def convert_to_font_size(value):
# #     # Convert value between 0 and 1 to a range of 12px to 32px
# #     min_font_size = 12
# #     max_font_size = 32
# #     return int(min_font_size + (max_font_size - min_font_size) * value)

# # # Function to convert float value to a hex color code
# # def convert_to_color(value):
# #     # Convert value between 0 and 1 to a range of 0 to 255, then to hex
# #     color_int = int(value * 255)
# #     return f"#{color_int:02x}{color_int:02x}{color_int:02x}"  # Grayscale for simplicity

# # # Load the trained PPO model
# # model = PPO.load("saved_models/ppo_website_env")

# # # Create the environment
# # env = WebsiteEnv()

# # # Reset the environment to get the initial observation
# # obs, _ = env.reset()

# # # Run for a few steps to simulate real-time changes
# # for step in range(100):  # Simulate 100 steps, change time as needed
# #     action, _states = model.predict(obs)
# #     obs, rewards, done, info, _ = env.step(action)

# #     # Convert the values to actual font size and colors
# #     font_size = convert_to_font_size(obs[0])
# #     font_color = convert_to_color(obs[1])
# #     background_color = convert_to_color(obs[2])

# #     # Save the current state (modified by RL agent) to a JSON file every 10 seconds
# #     ui_data = {
# #         "fontSize": f"{font_size}px",  # Font size in pixels
# #         "fontColor": font_color,       # Font color in hex
# #         "backgroundColor": background_color,  # Background color in hex
# #         "timestamp": time.time()
# #     }

# #     # Write to a JSON file
# #     with open(f"data/rl_modified_ui_step_{step}.json", 'w') as outfile:
# #         json.dump(ui_data, outfile, indent=4)

# #     # Sleep for 10 seconds to simulate real-time updates
# #     time.sleep(10)

# #     # Reset the environment if done
# #     if done:
# #         obs, _ = env.reset()

# import time
# import json
# from stable_baselines3 import PPO
# from website_env import WebsiteEnv

# # Function to convert float value to a pixel font size
# def convert_to_font_size(value):
#     # Convert value between 0 and 1 to a range of 12px to 32px
#     min_font_size = 12
#     max_font_size = 32
#     return int(min_font_size + (max_font_size - min_font_size) * value)

# # Function to convert float value to a hex color code
# def convert_to_color(value):
#     # Convert value between 0 and 1 to a range of 0 to 255, then to hex
#     color_int = int(value * 255)
#     return f"#{color_int:02x}{color_int:02x}{color_int:02x}"  # Grayscale for simplicity

# # Load the trained PPO model
# model = PPO.load("saved_models/ppo_website_env")

# # Create the environment with the real data
# json_file_path = 'data/sample.json'
# env = WebsiteEnv(json_file=json_file_path)

# # Reset the environment to get the initial observation
# obs, _ = env.reset()

# # Run for a few steps to simulate real-time changes
# for step in range(100):  # Simulate 100 steps, change time as needed
#     action, _states = model.predict(obs)
#     obs, rewards, done, info, _ = env.step(action)

#     # Convert the values to actual font size and colors
#     font_size = convert_to_font_size(obs[0])
#     font_color = convert_to_color(obs[1])
#     background_color = convert_to_color(obs[2])

#     # Save the current state (modified by RL agent) to a JSON file every 10 seconds
#     ui_data = {
#         "fontSize": f"{font_size}px",  # Font size in pixels
#         "fontColor": font_color,       # Font color in hex
#         "backgroundColor": background_color,  # Background color in hex
#         "timestamp": time.time()
#     }

#     # Write to a JSON file
#     with open(f"data/rl_modified_ui_step_{step}.json", 'w') as outfile:
#         json.dump(ui_data, outfile, indent=4)

#     # Sleep for 10 seconds to simulate real-time updates
#     time.sleep(10)

#     # Reset the environment if done
#     if done:
#         obs, _ = env.reset()


# import time
# import json
# import os
# import numpy as np
# from stable_baselines3 import PPO
# from environment import ColorEnv

# # Load the environment and the model
# env = ColorEnv(json_folder="filtered_recordings")
# model = PPO.load("saved_model/ppo_model")

# # Reset the environment
# obs, _ = env.reset()  # Discard the `info` part and keep only `obs`

# # Run the agent for 10 seconds and generate new JSON files
# # Run the agent for 10 seconds and generate new JSON files
# start_time = time.time()
# new_json_folder = "new_files"
# os.makedirs(new_json_folder, exist_ok=True)

# while time.time() - start_time < 10:
#     action, _states = model.predict(obs)
    
#     # Update to unpack all 5 values returned by env.step()
#     obs, reward, terminated, truncated, info = env.step(action)
    
#     # Generate a new JSON file
#     output_data = {
#         "button_color": int(obs[0] * 255),
#         "navbar_color": int(obs[1] * 255),
#         "background_color": int(obs[2] * 255)
#     }
    
#     filename = f"{int(time.time())}.json"
#     with open(os.path.join(new_json_folder, filename), 'w') as f:
#         json.dump(output_data, f)
#     print(f"Generated {filename}")

#     # Break loop if the episode ends
#     if terminated or truncated:
#         obs, _ = env.reset()  # Reset environment

# print("Testing complete!")


import time
import json
import os
from stable_baselines3 import PPO
from environment import ColorEnv

# Load the environment and the model
env = ColorEnv(json_folder="filtered_recordings")
model = PPO.load("saved_model/ppo_model")

# Reset the environment
obs, _ = env.reset()

# Directory to save new JSON files
new_json_folder = "new_files"
os.makedirs(new_json_folder, exist_ok=True)

# Set the total time to run the agent (in seconds)
total_run_time = 60  # Run for a total of 60 seconds as an example
file_interval = 10  # Generate a new JSON file every 10 seconds

start_time = time.time()
last_file_time = start_time

# Initialize termination flags
terminated = False
truncated = False

# Function to convert RGB values to rgb(x, y, z) format
def to_rgb_format(r, g, b):
    return f"rgb({int(r)}, {int(g)}, {int(b)})"

# Run the agent and generate new JSON files at 10-second intervals
while time.time() - start_time < total_run_time:
    # Generate a new JSON file every 10 seconds
    current_time = time.time()
    if current_time - last_file_time >= file_interval:
        # Predict the next action using the model
        action, _states = model.predict(obs)
        obs, reward, terminated, truncated, info = env.step(action)

        # Convert the normalized RGB values to actual 255-scale RGB and then to `rgb(x, y, z)` format
        button_rgb = to_rgb_format(obs[0] * 255, obs[1] * 255, obs[2] * 255)
        navbar_rgb = to_rgb_format(obs[3] * 255, obs[4] * 255, obs[5] * 255)
        background_rgb = to_rgb_format(obs[6] * 255, obs[7] * 255, obs[8] * 255)

        # Create the output data in RGB format
        output_data = {
            "button_color": button_rgb,
            "navbar_color": navbar_rgb,
            "background_color": background_rgb
        }

        # Save the output data to a new JSON file with a timestamp
        filename = f"{int(current_time)}_colors.json"
        with open(os.path.join(new_json_folder, filename), 'w') as f:
            json.dump(output_data, f)

        print(f"Generated {filename}")

        # Update the time of the last file creation
        last_file_time = current_time

    # Reset the environment if the episode ends (terminated or truncated)
    if terminated or truncated:
        obs, _ = env.reset()
        terminated = False  # Reset flags after resetting the environment
        truncated = False

print("Testing complete!")
