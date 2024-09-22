"""
File:    metro_lines.py
Author:  Abby Joseph
Date:    5/17/2022
Section: 31
E-mail:  abbyj1@umbc.edu
Description:
    This program allows the user to build a metro system with trains, lines, and stations, and
    plan trips from one stations to another.
"""
EXIT_STRING = 'exit'
STATION_NAME = 2
FIRST_STATION = 2
SECOND_STATION = 3
LINE_NAME = 4
TRAIN_ID = 2
LINE = 3
STARTING_STATION = 4
STATION = 3
TRAIN = 3
FIVE_WORDS = 5


def create_station(station_name):
    """
    A function to add a station to the system
    :param station_name: The name for the new station
    :return: None
    """
    if station_name not in metro_dict['stations']:
        # Adds the stations name to a list of all of the stations
        metro_dict['stations'].append(station_name)

    if station_name not in locations:
        locations[station_name] = {'lines': {}, 'visited': False}


def connect_stations(first_station, second_station, line_name):
    """
    A function to connect two stations on a line
    :param first_station: The name of the first station
    :param second_station: The name of the second station
    :param line_name: The name of the line they are connected on
    :return: None
    """
    if first_station in metro_dict['stations'] and second_station in metro_dict['stations']:
        if line_name not in metro_dict['lines']:
            metro_dict['lines'][line_name] = {first_station: [second_station], second_station:
                                              [first_station]}
        else:
            if first_station in metro_dict['lines'][line_name] and second_station not in metro_dict['lines'][line_name][first_station]:
                metro_dict['lines'][line_name].get(first_station).append(second_station)
            elif second_station in metro_dict['lines'][line_name][first_station]:
                print(f'Stations {first_station} and {second_station} are already connected through the {line_name} line. ')
            else:
                metro_dict['lines'][line_name][first_station] = [second_station]
            if second_station in metro_dict['lines'][line_name] and first_station not in metro_dict['lines'][line_name][second_station]:
                metro_dict['lines'][line_name].get(second_station).append(first_station)
            else:
                metro_dict['lines'][line_name][second_station] = [first_station]

        if line_name not in locations[first_station] and line_name not in locations[second_station]:
            locations[first_station]['lines'][second_station] = line_name
            locations[second_station]['lines'][first_station] = line_name
        else:
            locations[first_station]['lines'][second_station] += line_name
            locations[second_station]['lines'][first_station] += line_name
    else:
        # Displays the unrecognized station to the user
        if first_station not in metro_dict['stations']:
            print(f'Unrecognized station: {first_station}.')
        if second_station not in metro_dict['stations']:
            print(f'Unrecognized station: {second_station}.')


def plan_trip(start_station, end_station):
    """
    A function to plan what trains and lines to ride on to get from one station to another
    :param start_station: The name of the starting station
    :param end_station: The name of the ending station
    :return: A 2D List of stations and lines in the order to ride them
    """
    if start_station in metro_dict['stations'] and end_station in metro_dict['stations']:
        if start_station == end_station:
            return [end_station]

        # Marks the current station as having been visited
        locations[start_station]['visited'] = True

        for next_station in locations[start_station]['lines']:
            if not locations[next_station]['visited']:
                trip_plan = plan_trip(next_station, end_station)
                if trip_plan:
                    return [[start_station, locations[start_station]['lines'][next_station]]] + \
                           trip_plan
        return []


def create_train(train_id, line_name, starting_pos):
    """
    A function the add a train to the system
    :param train_id: The name of the new train
    :param line_name: The line the train will ride on
    :param starting_pos: The station the train will start at
    :return: None
    """
    if train_id not in metro_dict['trains']:
        # Adds the train's information to the metro system
        metro_dict['trains'][train_id] = [line_name, starting_pos]


def display_stations():
    """
    A function to display all the stations in the metro system
    :return: None
    """
    for station in metro_dict['stations']:
        # Prints each station
        print('\t' + station)


def display_trains():
    """
    A function to display all the trains in the metro system
    :return: None
    """
    for train in metro_dict['trains']:
        print(f'*** Information for Train {train} ***')
        print('\tLine:', metro_dict['trains'][train][0])
        # Prints the current position of each train
        print('\tCurrent position:', metro_dict['trains'][train][1])


def get_station_info(station):
    """
    A function to display information about a station
    :param station: The station's name
    :return: None
    """
    print(f'*** Information for Station {station} ***')
    for line in metro_dict['lines']:
        if station in metro_dict['lines'][line]:
            for next_station in metro_dict['lines'][line][station]:
                # Prints the lines connected to the station and the next station on the line
                print(f'\t{line} Line - Next Station: ' + next_station)


def get_train_info(train):
    """
    A function to display information about a train
    :param train: The train's name
    :return: None
    """
    print(f'*** Information for Train {train} ***')
    print('\tLine: ' + metro_dict['trains'][train][0])
    # Prints the current position of the train
    print('\tCurrent Position: ' + metro_dict['trains'][train][1])


def display_path(path, start_station, end_station):
    """
    A function to display the planned trip
    :param path: The ordered 2D list of what stations and lines to ride
    :param start_station: The starting station's name
    :param end_station: The ending station's name
    :return: None
    """
    if path == []:
        print(f'It is not possible to reach {end_station} from {start_station}')
    elif path == None:
        if start_station not in metro_dict['stations']:
            print(f'Unrecognized station: {start_station}.')
        if end_station not in metro_dict['stations']:
            print(f'Unrecognized station: {end_station}.')
    else:
        print(f'Start on the {path[0][1]} line --> {path[0][0]} --> ', end='')
        for i in range(len(path)):
            if i == len(path) - 1:
                print(path[i])
            elif i > 0:
                if path[i][1] == path[i - 1][1]:
                    print(f'{path[i][0]} --> ', end='')
                else:
                    # Tells the user which line to move to next
                    print(
                        f'At {path[i][0]} transfer from the {path[i - 1][1]} '
                        f'line to the {path[i][1]}'
                        f' line. --> ', end='')


def reset_visited(locations_dict):
    """
    A function to reset locations marked visited
    :param locations_dict: A dictionary with stations, lines, and visited status
    :return: None
    """
    for station in locations_dict:
        # Sets each station to a False visited status
        locations_dict[station]['visited'] = False


def run_metro():
    """
    A function to run the metro system
    :return: None
    """
    action_in = input(f'[{system_name_in}] >>> ')
    while action_in.lower() != EXIT_STRING:
        # Checks if the user is asking to create a station
        if 'create station' in action_in.lower() or 'create stations' in action_in.lower():
            create_station(action_in.split()[STATION_NAME])
        elif 'connect stations' in action_in.lower() or 'connect station' in action_in.lower():
            if len(action_in.split()) == FIVE_WORDS:
                connect_stations(action_in.split()[FIRST_STATION],
                                 action_in.split()[SECOND_STATION], action_in.split()[LINE_NAME])
            else:
                print('Please include the stations you want to connect and the line name.')
        elif 'create train' in action_in.lower():
            create_train(action_in.split()[TRAIN_ID], action_in.split()[LINE],
                         action_in.split()[STARTING_STATION])
        elif 'plan trip' in action_in.lower():
            display_path(plan_trip(action_in.split()[FIRST_STATION],
                                   action_in.split()[SECOND_STATION]),
                         action_in.split()[FIRST_STATION], action_in.split()[SECOND_STATION])
            reset_visited(locations)
        elif 'display stations' in action_in.lower():
            display_stations()
        elif 'display trains' in action_in.lower():
            display_trains()
        elif 'get station info' in action_in.lower() or 'get stations info' in action_in.lower():
            if action_in.split()[STATION] in metro_dict['stations']:
                get_station_info(action_in.split()[STATION])
            else:
                print(f'Unable to find station: {action_in.split()[TRAIN]}')
        elif 'get train info' in action_in.lower() or 'get trains info' in action_in.lower():
            if action_in.split()[TRAIN] in metro_dict['trains']:
                get_train_info(action_in.split()[TRAIN])
            else:
                print(f'Unable to find train: {action_in.split()[TRAIN]}')
        else:
            print(f'Unknown command: {action_in}')

        action_in = input(f'[{system_name_in}] >>> ')


if __name__ == '__main__':
    metro_dict = {'stations': [], 'trains': {}, 'lines': {}}
    locations = {}
    # Asks the user what the metro system is called
    system_name_in = input('>>> ')
    run_metro()
