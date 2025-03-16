import torch
import numpy as np
from ai_game import SnakeGameAI, Direction, Point
from model import Linear_QNet

def get_state(game):
    head = game.snake[0]
    point_l = Point(head.x - 20, head.y)
    point_r = Point(head.x + 20, head.y)
    point_u = Point(head.x, head.y - 20)
    point_d = Point(head.x, head.y + 20)

    dir_l = game.direction == Direction.LEFT
    dir_r = game.direction == Direction.RIGHT
    dir_u = game.direction == Direction.UP
    dir_d = game.direction == Direction.DOWN

    state = [
        # Danger straight
        (dir_r and game.is_collision(point_r)) or
        (dir_l and game.is_collision(point_l)) or
        (dir_u and game.is_collision(point_u)) or
        (dir_d and game.is_collision(point_d)),

        # Danger right
        (dir_u and game.is_collision(point_r)) or
        (dir_d and game.is_collision(point_l)) or
        (dir_l and game.is_collision(point_u)) or
        (dir_r and game.is_collision(point_d)),

        # Danger left
        (dir_d and game.is_collision(point_r)) or
        (dir_u and game.is_collision(point_l)) or
        (dir_r and game.is_collision(point_u)) or
        (dir_l and game.is_collision(point_d)),

        # Move direction
        dir_l,
        dir_r,
        dir_u,
        dir_d,

        # Food location
        game.food.x < head.x,  # food left
        game.food.x > head.x,  # food right
        game.food.y < head.y,  # food up
        game.food.y > head.y   # food down
    ]
    return np.array(state, dtype=int)

def get_action(model, state):
    """Use the loaded model to select the best action (no random exploration)."""
    state0 = torch.tensor(state, dtype=torch.float)
    prediction = model(state0)
    move = torch.argmax(prediction).item()
    final_move = [0, 0, 0]
    final_move[move] = 1
    return final_move

def run_model(model_file='model.pth'):
    """Load the saved model and run the game loop without training or plotting."""
    model = Linear_QNet(11, 256, 3)
    model.load(model_file)         # Adjust this if your load method requires a path
    game = SnakeGameAI()

    record = 0
    while True:
        state = get_state(game)
        action = get_action(model, state)
        reward, done, score = game.play_step(action)
        if done:
            # If the game ended, reset
            game.reset()
            if score > record:
                record = score
            print(f"Score: {score}, Record: {record}")

if __name__ == '__main__':
    # Replace 'my_saved_model.pth' with the exact file name you want to load
    run_model('model_20250315_184321.pth')