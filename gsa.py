import random
import numpy as np
import time

# Create a simple prediction learning based environment
# Create a small field 5x5 
# Initialize the grid size
GRID_SIZE = 5

# Create the grid
grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Define position of reward inside the grid
grid[1][4] = 7

# Now let's create the agent (Agent R)
AGENT_R = 8

# How many thimes did agent find number 7
FOUND_COUNT = 0

# Initialize the agent's position
agent_position = (0, 0)

# Place the agent in the grid
grid[agent_position[0]][agent_position[1]] = AGENT_R

# Define the possible actions the agent can take
ACTIONS = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

# Function to move the agent
def move_agent(new_position):
    global agent_position, grid, FOUND_COUNT

    # Remove the agent from its current position
    grid[agent_position[0]][agent_position[1]] = 0

    # Check if the agent has reached the target
    if grid[new_position[0]][new_position[1]] == 7:
        print("I found number 7!")
        FOUND_COUNT += 1
        # Place the agent at a random position in the grid
        new_position = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))

    # Update the agent's position
    agent_position = new_position

    # Place the agent at the new position
    grid[agent_position[0]][agent_position[1]] = AGENT_R

# Function to predict the agent's next position // simulatin world model here
def predict_next_position(current_position, action):
    # Get the change in position from the action
    delta_position = ACTIONS[action]

    # Calculate the new position
    new_position = (current_position[0] + delta_position[0], current_position[1] + delta_position[1])

    # Make sure the new position is inside the grid
    new_position = (max(0, min(GRID_SIZE - 1, new_position[0])), max(0, min(GRID_SIZE - 1, new_position[1])))

    return new_position

# Function to compute the energy of a position // similar to reward function
def compute_energy(position):
    # Define the position of the reward
    objective_position = (1, 4)

    # Compute the distance from the position to the objective
    distance = abs(position[0] - objective_position[0]) + abs(position[1] - objective_position[1])

    # The energy is the distance
    energy = distance

    return energy

# Function to compute the energy of the predicted outcome
def compute_predicted_energy(current_position, action):
    # Predict the next position
    predicted_position = predict_next_position(current_position, action)

    # Compute the energy of the predicted position
    predicted_energy = compute_energy(predicted_position)

    return predicted_energy

# Agent suggest action
def suggest_action_sequence(current_position):
    # Initialize the best action and its energy
    best_action = None
    best_energy = float('inf')

    # Iterate over all possible actions
    for action in ACTIONS:
        # Compute the energy of the predicted outcome for this action
        predicted_energy = compute_predicted_energy(current_position, action)

        # If this action results in a lower energy, update the best action and its energy
        if predicted_energy < best_energy:
            best_action = action
            best_energy = predicted_energy

    # Return the best action
    return best_action

# Number of steps the agent will take
num_steps = 100

# Print the grid to visualize the agent's progress
print("Agent found number 7 ", FOUND_COUNT, "times.")
for row in grid:
    print(row)
print("\n")
# Wait for 2 seconds
time.sleep(2)

for _ in range(num_steps):
    # Get the best action for the agent to take
    action = suggest_action_sequence(agent_position)

    # Predict the agent's next position
    new_position = predict_next_position(agent_position, action)

    # Move the agent to the new position
    move_agent(new_position)

    # Print the grid to visualize the agent's progress
    print("Agent found number 7 ", FOUND_COUNT, "times.")
    for row in grid:
        print(row)
    print("\n")
    # Wait for 2 seconds
    time.sleep(2)