# Assignment: Train RL agent to navigate road crossing with actions: right, left, right
import numpy as np
import random

# Environment setup
road_length = 5  # Positions: 0 (start) to 4 (goal - other side of road)
actions = ["left", "right"]
action_names = ["left", "right"]

# Q-table (state x action)
Q = np.zeros((road_length, len(actions)))

# Hyperparameters
episodes = 1000  # Training episodes
learning_rate = 0.8  # How fast the agent learns
gamma = 0.9  # Discount factor for future rewards
epsilon = 0.3  # Exploration rate (30% random actions)

# Training loop
print("Training the agent to cross the road...")
for episode in range(episodes):
    state = 0  # Start at position 0 (one side of road)
    
    while state != 4:  # Goal is position 4 (other side of road)
        # Epsilon-greedy action selection
        if random.uniform(0, 1) < epsilon:
            action = random.randint(0, 1)  # Explore (random action)
        else:
            action = np.argmax(Q[state])  # Exploit (best known action)
        
        # Take action and get new state
        if action == 0:  # Move left
            new_state = max(0, state - 1)
        else:  # Move right
            new_state = min(4, state + 1)
        
        # Reward structure for road crossing:
        # +10 for reaching the goal (other side)
        # -1 for each step to encourage efficiency
        # Additional penalty for going backwards
        if new_state == 4:
            reward = 10  # Successfully crossed the road
        elif new_state < state:
            reward = -2  # Penalty for moving backwards
        else:
            reward = -1  # Small penalty for each step
        
        # Q-learning update rule
        Q[state, action] = Q[state, action] + learning_rate * (
            reward + gamma * np.max(Q[new_state]) - Q[state, action]
        )
        
        # Move to new state
        state = new_state

# Display learned Q-table
print("\nLearned Q-table:")
print("State | Left Action | Right Action")
print("-" * 35)
for i in range(road_length):
    print(f"  {i}   |    {Q[i,0]:.2f}     |     {Q[i,1]:.2f}")

# Test the trained agent
print("\n" + "="*50)
print("TESTING: Agent attempting to cross the road")
print("="*50)

state = 0
steps = 0
path = []
positions = [0]  # Track positions for visualization

print(f"Starting position: {state} (one side of road)")
print("Goal: Reach position 4 (other side of road)")
print("\nAgent's path to cross the road:")

while state != 4 and steps < 10:  # Safety limit
    action = np.argmax(Q[state])  # Choose best action
    action_name = action_names[action]
    
    # Execute action
    if action == 0:  # left
        new_state = max(0, state - 1)
    else:  # right
        new_state = min(4, state + 1)
    
    steps += 1
    path.append(action_name)
    positions.append(new_state)
    
    print(f"Step {steps}: Move {action_name} → Position {new_state}")
    state = new_state

# Results
print(f"\nFinal path taken: {' → '.join(path)}")
print(f"Position sequence: {' → '.join(map(str, positions))}")

if state == 4:
    print(f"SUCCESS! Goal reached in {steps} steps!")
    print("The agent successfully learned to cross the road!")
else:
    print("Failed to reach goal within step limit")

# Analyze the optimal policy
print(f"\nLearned Policy (best action for each state):")
for i in range(road_length-1):  # Don't include goal state
    best_action = np.argmax(Q[i])
    print(f"State {i}: {action_names[best_action]}")