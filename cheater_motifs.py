from datetime import datetime, timedelta

def identify_cheater_observers(kills, cheaters):
    """
    Identifies the players who observed cheating.

    Takes in kills (a list of lists) and cheaters (a dictionary).

    Returns a dictionary of players who observed a cheater kill 3 people,
    a dictionary of players who were killed by a cheater,
    and the indices of the cheaters in the kills list.
    """

    # Stores players killed in a given match before a cheater kills 3 people
    # {killer : [player_killed, attack_time]}
    nodes = {}

    # Stores observers who observed a cheater kill 3 players
    # {observer: attack_time}
    observers = {}

    # Stores observers who were killed by cheaters
    # {player_killed: attack_time}
    killed_by_cheaters = {}

    # List of indices of cheaters in kills[]
    cheater_indices = []

    # Initial match id
    previous_match_id = kills[0][0]

    cheater_found = False

    index = 0

    # Iterate through all kills
    for kill in kills:

        # Check if new match id to reset network
        if kill[0] != previous_match_id:

            # Add attack_times of players who were killed by cheaters
            # (i.e. Step 1 part b)
            if cheater_found == True:

                # Get the 3 kills of the cheater
                kill_1, kill_2, kill_3 = nodes[cheater_id]

                # Check if player_killed_id is already included
                # in killed_by_cheaters
                if kill_1[0] not in killed_by_cheaters:

                    # Assign attack_time to player_killed_id
                    killed_by_cheaters[kill_1[0]] = kill_1[1]

                # Check if player_killed_id is already included
                # in killed_by_cheaters
                if kill_2[0] not in killed_by_cheaters:

                    # Assign attack_time to player_killed_id
                    killed_by_cheaters[kill_2[0]] = kill_2[1]

                # Check if player_killed_id is already included
                # in killed_by_cheaters
                if kill_3[0] not in killed_by_cheaters:

                    # Assign attack_time to player_killed_id
                    killed_by_cheaters[kill_3[0]] = kill_3[1]

            # Reset match network
            nodes = {}
            cheater_found = False


        # Add killer to network if not already there
        if kill[1] not in nodes:
            nodes[kill[1]] = []

        # Check if the killer is a cheater
        if cheater_found == False:

            # Check if killer has 3 or more kills and is a cheater
            if len(nodes[kill[1]]) == 3 and kill[1] in cheaters:

                cheater_found = True

                # Get id of cheater
                cheater_id = kill[1]

                # Get index of cheater
                cheater_indices.append(index)

        # Add observers who observed 3 kills to observers dictionary
        if cheater_found == True:

            if (kill[1] not in observers) and (kill[1] != cheater_id):

                # Assign attack_time to killer who observed cheating
                observers[kill[1]] = kill[3]

            if (kill[2] not in observers) and (kill[2] != cheater_id):

                # Assign attack_time to player killed who observed cheating
                observers[kill[2]] = kill[3]

        else:
            # Add attack_time of kill to list of killed players
            nodes[kill[1]].append([kill[2], kill[3]])

        # Get match id
        previous_match_id = kill[0]
        index += 1

    return observers, killed_by_cheaters, cheater_indices


def count_new_cheaters(cheaters, observers, killed_by_cheaters):
    """
    Counts the number of observer-cheater motifs.

    Takes in a dictionary of cheaters, a dictionary of observers of cheaters
    killing 3 people, and a dictionary of players killed by cheaters.

    Returns the number of observers who cheated within 5 days.
    """

    num_new_cheaters = 0

    # Iterates through cheaters dictionary
    for cheater in cheaters:

        if cheater in observers:

            # Calculate time difference between observing cheating
            # and actually cheating
            delta = (cheaters[cheater][0]) - (observers[cheater])

            # Check if the time difference is between 0 and 5 days
            if (timedelta(days = 0) <= delta <= timedelta(days = 5)):

                num_new_cheaters += 1

        elif cheater in killed_by_cheaters:

            # Calculate time difference between observing cheating
            # and actually cheating
            delta = (cheaters[cheater][0]) - (killed_by_cheaters[cheater])

            # Check if the time difference is between 0 and 5 days
            if (timedelta(days = 0) <= delta <= timedelta(days = 5)):

                num_new_cheaters += 1

    return num_new_cheaters
