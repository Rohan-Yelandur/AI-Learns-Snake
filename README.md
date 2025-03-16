# AI-Learns-Snake

Train and deploy an agent to play the classic snake game!
Uses reinforcement learning to train the model.

## Setup
To install the necessary dependencies run the following in a terminal:
```bash
pip install -r requirements.txt
```

## How to Use
To train and save a new model run:
In 'ai_game.py' change the SPEED variable to adjust training speed.
```bash
python teach_agent.py
```

To test a previously trained model:
Change the MODEL_NAME variable in 'run_model.py' to change which saved model you run.
```bash
python run_model.py
```

To play snake yourself if you think you're better than AI:
Change the SPEED variable in 'human_game.py' to adjust how fast the snake moves.
```bash
python human_game.py
```