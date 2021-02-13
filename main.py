import pickle
import matplotlib.pyplot as plt

from process_raw_data import get_kills_data, get_cheaters_data
from cheater_motifs import identify_cheater_observers, count_new_cheaters
from shuffle import randomise, save_randomised_data

def load_data(cheaters, num_randomisations = 10):
    """
    Loads the pickled data from the local directory. Defaults to reading 10 pickled files.

    Takes in cheaters (a dictionary). Returns a list of the number of randomised observer-cheater motifs.
    """

    random_num_new_cheaters_list = []

    for i in range(num_randomisations):

        file_name = 'shuffled_data_' + str(i + 1)

        # Unpickle saved Python object
        with open (file_name, 'rb') as fr:

            kills = pickle.load(fr)

        observers, killed_by_cheaters, cheater_indices = identify_cheater_observers(kills, cheaters)

        random_num_new_cheaters = count_new_cheaters(cheaters, observers, killed_by_cheaters)

        random_num_new_cheaters_list.append(random_num_new_cheaters)

    return random_num_new_cheaters_list


def plot_motifs(actual_num_new_cheaters, random_num_new_cheaters_list):
    """
    Plots the number of observer-cheater motifs in the actual and randomised data.

    Takes in an integer representing the number of observer-cheater motifs in the actual data,
    and a list of integers representing the number of observer-cheater motifs in the randomised data.
    """

    plt.hist(random_num_new_cheaters_list, bins = len(random_num_new_cheaters_list),
             edgecolor = 'black', label = 'Randomised')
    plt.vlines(actual_num_new_cheaters, 0, 4, colors = 'red', label = 'Actual')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    plt.xlabel('Number of New Cheaters')
    plt.ylabel('Count')
    plt.title('Actual vs. Randomised Number of Observer-Cheater Motifs')
    plt.grid(True)
    plt.show()


def main():

    kills = get_kills_data('kills.txt')

    cheaters = get_cheaters_data('cheaters.txt')

    actual_observers, actual_killed_by_cheaters, cheater_indices = \
    identify_cheater_observers(kills, cheaters)

    actual_num_new_cheaters = \
    count_new_cheaters(cheaters, actual_observers, actual_killed_by_cheaters)

    save_randomised_data(kills, cheater_indices)

    random_num_new_cheaters_list = load_data(cheaters)

    plot_motifs(actual_num_new_cheaters, random_num_new_cheaters_list)


if __name__ == '__main__':
    main()
