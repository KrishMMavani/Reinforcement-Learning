# # import gymnasium as gym
# # import json
# # import random
# # from gymnasium import spaces
# # import numpy as np

# # class WebsiteEnv(gym.Env):
# #     """Custom Environment for Website User Interaction"""
# #     metadata = {'render.modes': ['human']}

# #     def __init__(self):
# #         super(WebsiteEnv, self).__init__()

# #         # Actions: Change font size, color, background color
# #         self.action_space = spaces.Discrete(3)  # 3 actions: Font size, Font color, Background color

# #         # Observations: Font size, Font color, Background color, Timestamp (5 features)
# #         self.observation_space = spaces.Box(low=0, high=1, shape=(5,), dtype=np.float32)

# #         # Initial state, random values for the UI features
# #         self.state = np.array([0.5, 0.5, 0.5, 0.5, 0.5])  # Placeholder features
# #         self.user_engagement = 0

# #     def reset(self, seed=None, options=None):
# #         # Set the seed for reproducibility
# #         super().reset(seed=seed)
# #         np.random.seed(seed)
        
# #         # Reset state to random feature values between 0 and 1
# #         self.state = np.array([random.uniform(0, 1) for _ in range(5)])
# #         self.user_engagement = 0
        
# #         # Return the initial state and additional info
# #         return self.state, {}

# #     def step(self, action):
# #         # Apply action: Modify UI feature based on action (0: Font size, 1: Font color, 2: Background color)
# #         if action == 0:  # Change font size
# #             self.state[0] += random.uniform(-0.1, 0.1)
# #         elif action == 1:  # Change font color
# #             self.state[1] = random.uniform(0, 1)
# #         elif action == 2:  # Change background color
# #             self.state[2] = random.uniform(0, 1)

# #         # Ensure feature values stay within bounds [0, 1]
# #         self.state = np.clip(self.state, 0, 1)

# #         # Simulate user engagement score (reward based on how balanced the UI is)
# #         engagement = self.calculate_engagement()

# #         # Reward is based on simulated engagement
# #         reward = engagement

# #         # Done condition: Engagement above 0.8
# #         done = engagement > 0.8

# #         return self.state, reward, done, {}, {}

# #     def calculate_engagement(self):
# #         # The closer the UI features are to 0.5, the better the user engagement (simplified for prototype)
# #         return 1 - np.mean(np.abs(self.state - 0.5))

# #     def render(self, mode='human'):
# #         print(f"Current State: {self.state}, Engagement: {self.calculate_engagement()}")


# import gymnasium as gym
# import json
# import random
# from gymnasium import spaces
# import numpy as np

# class WebsiteEnv(gym.Env):
#     """Custom Environment for Website User Interaction"""
#     metadata = {'render.modes': ['human']}

#     def __init__(self, json_file = 'D:\\RL_Demo\\Data\\sample.json'):
#         super(WebsiteEnv, self).__init__()

#         # Actions: Change font size, color, background color
#         self.action_space = spaces.Discrete(3)  # 3 actions: Font size, Font color, Background color

#         # Observations: Font size, Font color, Background color, Timestamp (5 features)
#         self.observation_space = spaces.Box(low=0, high=1, shape=(5,), dtype=np.float32)

#         # State will be loaded from the JSON file
#         self.state = None  # Placeholder for the state that will be loaded
#         self.user_engagement = 0

#         # Load JSON data for the environment
#         self.json_file = json_file

#     def reset(self, seed=None, options=None):
#         # Set the seed for reproducibility
#         super().reset(seed=seed)
#         np.random.seed(seed)

#         # Load state from JSON data
#         self.state = self.load_state_from_json()

#         self.user_engagement = 0

#         # Return the initial state and additional info
#         return self.state, {}

#     def step(self, action):
#         # Apply action: Modify UI feature based on action (0: Font size, 1: Font color, 2: Background color)
#         if action == 0:  # Change font size
#             self.state[0] += random.uniform(-0.1, 0.1)
#         elif action == 1:  # Change font color
#             self.state[1] = random.uniform(0, 1)
#         elif action == 2:  # Change background color
#             self.state[2] = random.uniform(0, 1)

#         # Ensure feature values stay within bounds [0, 1]
#         self.state = np.clip(self.state, 0, 1)

#         # Simulate user engagement score (reward based on how balanced the UI is)
#         engagement = self.calculate_engagement()

#         # Reward is based on simulated engagement
#         reward = engagement

#         # Done condition: Engagement above 0.8
#         done = engagement > 0.8

#         return self.state, reward, done, {}, {}

#     def calculate_engagement(self):
#         # The closer the UI features are to 0.5, the better the user engagement (simplified for prototype)
#         return 1 - np.mean(np.abs(self.state - 0.5))

#     def load_state_from_json(self):
#         """Load the initial state from the provided JSON file."""
#         with open(self.json_file, 'r') as file:
#             data = json.load(file)
        
#         # Assuming the JSON file contains the following keys
#         font_size = data.get('fontSize', 0.5)  # Default to 0.5 if missing
#         font_color = data.get('fontColor', 0.5)
#         background_color = data.get('backgroundColor', 0.5)
#         timestamp = data.get('timestamp', 0.5)
#         additional_feature = data.get('otherFeature', 0.5)  # Optional 5th feature
        
#         # Return the state as a numpy array
#         return np.array([font_size, font_color, background_color, timestamp, additional_feature])

#     def render(self, mode='human'):
#         print(f"Current State: {self.state}, Engagement: {self.calculate_engagement()}")



# import numpy as np
# import gymnasium as gym
# import json
# import os

# class ColorEnv(gym.Env):
#     def __init__(self, json_folder = './filtered_recordings'):
#         super(ColorEnv, self).__init__()
#         self.json_folder = json_folder
#         self.files = os.listdir(json_folder)
#         self.current_file_index = 0
        
#         # Action space: 3 continuous actions to modify color components
#         self.action_space = gym.spaces.Box(low=0, high=1, shape=(3,), dtype=np.float32)
        
#         # Observation space: 3 continuous observations for normalized color values
#         self.observation_space = gym.spaces.Box(low=0, high=1, shape=(3,), dtype=np.float32)
        
#         # Load the first JSON file
#         self.seed()

#     def load_json(self, file_index):
#         filepath = os.path.join(self.json_folder, self.files[file_index])
#         with open(filepath, 'r') as f:
#             data = json.load(f)
        
#         # If data is a list, select the first item or the desired index
#         if isinstance(data, list):
#             data = data[0]  # Adjust this if needed

#         return np.array([
#             data.get("button_color", 0),
#             data.get("navbar_color", 0),
#             data.get("background_color", 0)
#         ]) / 255.0

#     def reset(self, seed=None, options=None):
#         # Accept the seed and use it to seed the environment if needed
#         if seed is not None:
#             self.seed(seed)
        
#         self.current_file_index = (self.current_file_index + 1) % len(self.files)
#         self.state = self.load_json(self.current_file_index)
#         return self.state, {}

#     def step(self, action):
#         # Apply action to modify the color values
#         self.state = np.clip(self.state + action, 0, 1)
        
#         # Encourage the model to choose balanced values (centered around 0.5)
#         reward = -np.sum(np.square(self.state - 0.5))  # Penalize large deviations from 0.5
        
#         # Small reward for each step, penalty for extreme actions
#         reward += 1.0 - np.mean(np.abs(action))  # Encourage smaller actions

#         terminated = False  # Modify if there's a natural termination condition
#         truncated = False  # Modify if there's a time-based episode length
        
#         info = {}
#         return self.state, reward, terminated, truncated, info

#     def seed(self, seed=None):
#         np.random.seed(seed)

# environment.py
import numpy as np
import gymnasium as gym
import json
import os

class ColorEnv(gym.Env):
    def __init__(self, json_folder='./filtered_recordings'):
        super(ColorEnv, self).__init__()
        self.json_folder = json_folder
        self.files = os.listdir(json_folder)
        self.current_file_index = 0

        # Adjust observation space: 3 elements (button, navbar, background) × 3 color channels (RGB)
        self.observation_space = gym.spaces.Box(low=0, high=1, shape=(9,), dtype=np.float32)

        # Adjust action space to modify all 9 color values (3 elements × 3 color channels)
        self.action_space = gym.spaces.Box(low=-0.05, high=0.05, shape=(9,), dtype=np.float32)

        # Historical engagement data (for reward calculation)
        self.engagement_data = {}

        # Load initial JSON
        self.seed()

    def load_json(self, file_index):
        """Load and parse a JSON file and extract color information."""
        filepath = os.path.join(self.json_folder, self.files[file_index])
        with open(filepath, 'r') as f:
            data = json.load(f)

        # Ensure 'data' is a dictionary, if not, handle as list
        if isinstance(data, list):
            data = data[0]  # Assuming first item in list is relevant
        
        # Safeguard for missing or incorrect structure
        elements = data.get('data', {}).get('elements', [])
        button_color = [0, 0, 0]
        navbar_color = [0, 0, 0]
        background_color = [0, 0, 0]
        
        # Extract color information if elements are available
        for element in elements:
            style = element.get('attributes', {}).get('style', {})
            if element['type'] == 'button':
                button_color = self.extract_rgb(style.get('background-color', 'rgb(0,0,0)'))
            elif element['type'] == 'navbar':
                navbar_color = self.extract_rgb(style.get('background-color', 'rgb(0,0,0)'))
            elif element['type'] == 'background':
                background_color = self.extract_rgb(style.get('background-color', 'rgb(0,0,0)'))

        # Normalize to [0, 1] and return as a flat array
        return np.array(button_color + navbar_color + background_color) / 255.0
    
    def extract_rgb(self, color_str):
        """Extract RGB values from 'rgb(x,x,x)' or 'rgba(x,x,x,x)' string."""
        # Remove 'rgb(' or 'rgba(' and the closing ')'
        color_str = color_str.replace('rgba(', '').replace('rgb(', '').replace(')', '')
        
        # Split the color values by commas and take the first 3 values (R, G, B)
        rgb_values = color_str.split(',')[:3]  # Ignore alpha channel if present
        
        return [int(x.strip()) for x in rgb_values]

    def load_engagement_data(self, file_index):
        """Load historical engagement data for reward calculation (dummy implementation)."""
        return {
            'user_clicks': np.random.rand(),      # Random for now, but should be actual data
            'scroll_depth': np.random.rand(),     # Random for now, but should be actual data
            'bounce_rate': np.random.rand()       # Random for now, but should be actual data
        }

    def reset(self, seed=None, options=None):
        """Reset the environment to a new state."""
        if seed is not None:
            self.seed(seed)

        self.current_file_index = (self.current_file_index + 1) % len(self.files)
        self.state = self.load_json(self.current_file_index)
        self.engagement_data = self.load_engagement_data(self.current_file_index)
        return self.state, {}

    def step(self, action):
        """Take an action in the environment and return the new state, reward, and done flags."""
        # Apply action to the current state (9 values for 3 elements with 3 color channels each) and clip to [0, 1]
        self.state = np.clip(self.state + action, 0, 1)

        # Compute reward: Balance action size with deviation from optimal state (centered around 0.5)
        button_weight = 1.0
        navbar_weight = 1.5
        background_weight = 0.8

        # Reward based on proximity to balanced color and engagement data
        button_reward = button_weight * np.sum(np.square(self.state[0:3] - 0.5))
        navbar_reward = navbar_weight * np.sum(np.square(self.state[3:6] - 0.5))
        background_reward = background_weight * np.sum(np.square(self.state[6:9] - 0.5))

        # Sum the rewards for each component
        reward = -(button_reward + navbar_reward + background_reward)

        # Incorporate engagement metrics (user clicks, scroll depth, and bounce rate)
        engagement_bonus = (self.engagement_data['user_clicks'] * 0.5 +
                            self.engagement_data['scroll_depth'] * 0.3 -
                            self.engagement_data['bounce_rate'] * 0.2)
        reward += engagement_bonus

        # Reward for smaller actions (encourages fine-tuning)
        reward += 1.0 - np.mean(np.abs(action))

        # Episode termination condition (small actions)
        terminated = np.all(np.abs(action) < 0.01)
        truncated = False

        # Ensure reward is a scalar (convert to float if necessary)
        return self.state, float(reward), terminated, truncated, {}

    def seed(self, seed=None):
        """Set the random seed for the environment."""
        np.random.seed(seed)