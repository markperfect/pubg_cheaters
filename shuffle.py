import random
import pickle

def randomise(kills, cheater_indices):
    """
    Shuffles the order of kills within a game while keeping cheaters in-place.

    Takes in kills (a list of lists) and a list of cheater indices in kills.
    Returns a shuffled dataset.
    """

    # Get first match id
    previous_match_id = kills[0][0]

    # Lower bound index for slice
    old_match_index = 0

    # Upper bound index for slice
    new_match_index = 0

    # Index of cheater in cheater_indices
    cheater_index = 0

    # Shuffled dataset
    new_dataset = []

    index = 0

    for kill in kills:

        # Check if new match id or if index is at the end of the list
        if kill[0] != previous_match_id or index == len(kills):

            # Use current index as upper bound for slice
            new_match_index = index

            # Get slice of kills from 1 match
            kills_slice = kills[old_match_index:new_match_index]

            # Shuffle match
            shuffled_slice = random.sample(kills_slice, len(kills_slice))

            if cheater_index < len(cheater_indices):

                # Check if cheater_index is in the given match slice
                if ((new_match_index > cheater_indices[cheater_index]) and
                    (old_match_index < cheater_indices[cheater_index])):

                        # Get index of cheater in the sliced data
                        slice_cheater_index = cheater_indices[cheater_index] - old_match_index

                        # Get corresponding row of data for the cheater in the sliced data
                        slice_cheater_kill = kills_slice[slice_cheater_index]

                        # Get index of cheater in the shuffled data
                        shuffled_cheater_index = shuffled_slice.index(slice_cheater_kill)

                        # Get corresponding row of data for the cheater in the shuffled data
                        shuffled_cheater_kill = shuffled_slice[shuffled_cheater_index]

                        # Swap the cheater from the shuffled data into the original position
                        shuffled_slice[shuffled_cheater_index], shuffled_slice[slice_cheater_index] \
                        = shuffled_slice[slice_cheater_index], shuffled_slice[shuffled_cheater_index]

                        cheater_index += 1

            # Add to shuffled dataset
            new_dataset.extend(shuffled_slice)

            # Store existing index as lower bound for new slice
            old_match_index = index

        # Get match id
        previous_match_id = kill[0]

        index += 1

        # Increment index for final slice
        if index == (len(kills) - 1):

            index += 1

    return new_dataset


def save_randomised_data(kills, cheater_indices, num_randomisations = 10):
    """
    Randomises the data a specified number of times (default is 10).
    Saves the processed data to the local directory.

    Takes in kills (a list of lists) and a list of cheater indices in kills.
    """

    for i in range(num_randomisations):

        # Pickle shuffled dataset
        file_name = 'shuffled_data_' + str(i + 1)

        with open (file_name, 'wb') as fw:

            new_dataset = randomise(kills, cheater_indices)

            pickle.dump(new_dataset, fw)
