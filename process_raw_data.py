from datetime import datetime, timedelta

def get_kills_data(fname):
    """
    Reads in kills raw text file.

    Returns a formatted list of lists of kills.
    """

    assert type(fname) == str, "Argument is not a string"

    path = '../assignment-final-data/' + fname

    with open(path, 'r') as f:

        data = []

        for line in f.readlines():

            # kills.txt
            # match_id | killer_id | player_killed_id | attack_time

            # Split string on tab and remove leading/trailing white space
            match_id, killer_id, player_killed_id, attack_time = \
            line.strip().split('\t')

            # Add each entry to a list and convert datetime
            data.append([match_id, killer_id,
                         player_killed_id,
                         datetime.strptime(attack_time, "%Y-%m-%d %H:%M:%S.%f")])

        # Sort kills by match_id and by attack_time
        data = sorted(data, key = lambda x: (x[0], x[3]))

    # [[match_id, killer_id, player_killed_id, attack_time]]
    return data


def get_cheaters_data(fname):
    """
    Reads in cheaters raw text file.

    Returns a formatted dictionary of cheaters.
    """
    assert type(fname) == str, "Argument is not a string"

    path = '../assignment-final-data/' + fname

    with open(path, 'r') as f:

        data = {}

        for line in f.readlines():

            # cheaters.txt – contains cheaters who played
            # between March 1 and March 10, 2019
            # player_id | cheating_date | banned_date

            # Split string on tab and remove leading/trailing white space
            player_id, cheating_date, banned_date = line.strip().split('\t')

            # Add each cheater as a key and the cheating date / banned date
            # as dictionary values
            data[player_id] = []
            data[player_id].append(datetime.strptime(cheating_date, "%Y-%m-%d"))
            data[player_id].append(datetime.strptime(banned_date, "%Y-%m-%d"))

    # {cheater: [cheating_date, banned_date]}
    return data
