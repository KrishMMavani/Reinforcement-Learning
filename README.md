# RL_Model

## Overview
This project is a prototype model that utilizes RRWEB for tracking user interactions and applies Reinforcement Learning (RL) to optimize user engagement. The model captures frontend data using RRWEB, which is then processed by a reinforcement learning algorithm to dynamically modify UI features based on user behavior.

## Project Structure
- `train.py`: This script is used to train the reinforcement learning model.
- `test.py`: This script is used to evaluate the trained model and generate output based on user interactions.
- `saved_model/`: This directory stores the trained model, specifically `ppo_model.zip`.

## Installation
To run this project, make sure you have Python and the required libraries installed. You can install the necessary libraries using:

```bash
pip install -r requirements.txt
```

## Run the project
To run this project:
```
python app.py
```
```
python run_both.py
```

