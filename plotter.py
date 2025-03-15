import matplotlib.pyplot as plt
from IPython import display

plt.ion()

def plot(scores, mean_scores, record_scores):
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    plt.title('Training...')
    plt.xlabel('Number of Games')
    plt.ylabel('Score')

    # Plot each list
    plt.plot(scores, label='Score')
    plt.plot(mean_scores, label='Mean Score')
    plt.plot(record_scores, label='Max Record')

    plt.legend()
    
    # Just a safety check so we don't crash with an empty list
    if len(scores) > 0:
        plt.ylim(ymin=0)
        plt.text(len(scores)-1, scores[-1], str(scores[-1]))
        plt.text(len(mean_scores)-1, mean_scores[-1], str(mean_scores[-1]))
        plt.text(len(record_scores)-1, record_scores[-1], str(record_scores[-1]))

    plt.show(block=False)
    plt.pause(.1)