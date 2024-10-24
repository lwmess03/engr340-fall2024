import sys
import numpy as np


def parse_nyt_data(file_path=''):
    """
    Parse the NYT covid database and return a list of tuples. Each tuple describes one entry in the source data set.
    Date: the day on which the record was taken in YYYY-MM-DD format
    County: the county name within the State
    State: the US state for the entry
    Cases: the cumulative number of COVID-19 cases reported in that locality
    Deaths: the cumulative number of COVID-19 death in the locality

    :param file_path: Path to data file
    :return: A List of tuples containing (date, county, state, cases, deaths) information
    """
    # data point list
    data=[]

    # open the NYT file path
    try:
        fin = open(file_path)
    except FileNotFoundError:
        print('File ', file_path, ' not found. Exiting!')
        sys.exit(-1)

    # get rid of the headers
    fin.readline()

    # while not done parsing file
    done = False

    # loop and read file
    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        # format is date,county,state,fips,cases,deaths
        (date,county, state, fips, cases, deaths) = line.rstrip().split(",")

        # clean up the data to remove empty entries
        if cases=='':
            cases=0
        if deaths=='':
            deaths=0

        # convert elements into ints
        try:
            entry = (date,county,state, int(cases), int(deaths))
        except ValueError:
            print('Invalid parse of ', entry)

        # place entries as tuple into list
        data.append(entry)


    return data


def first_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    :return:
    """
    for (date, county, state, cases, deaths) in data:
        if state == 'Virginia' and county == 'Harrisonburg city':
            print('First positive COVID case in Harrisonburg: ',date) # Iterate through loop and find where harrisonburg is
            break # break through loop after first iteration
    for (date, county, state, cases, deaths) in data:
        if state == 'Virginia' and county == 'Rockingham':
            print('First positive COVID case in Rockingham County: ',date) # Iterate through loop and find where Rockingham is
            break # break through loop after first iteration

    return

def second_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    :return:
    """
    # Define Variables
    initial_case= None
    greatest_case = 0
    date_greatest_case = None

    for (date, county, state, cases, deaths) in data:
        if state == 'Virginia' and county == 'Harrisonburg city': # Iterate through loop and find where harrisonburg is
            if initial_case != None: # if initial case is not empty subtract the current case minus the one before
                new_case = cases - initial_case
                if new_case > greatest_case: # If that new case is greater than the greatest case define the greatest case
                    greatest_case = new_case # This gives me the greatest number of cases in one day
                    date_greatest_case = date # This gives me the day
            initial_case = cases
    print('Day of greatest number of new daily cases recorded in Harrisonburg: Day:',date_greatest_case, ' Number:', greatest_case)

    # The code below is the same as the code above just for Rockingham
    initial_case = None
    greatest_case = 0
    date_greatest_case = None

    for (date, county, state, cases, deaths) in data:
        if state == 'Virginia' and county == 'Rockingham':
            if initial_case != None:
                new_case = cases - initial_case
                if new_case > greatest_case:
                    greatest_case = new_case
                    date_greatest_case = date
            initial_case = cases
    print('Day of greatest number of new daily cases recorded in Rockingham: Day:', date_greatest_case, ' Number:',
          greatest_case)


    # your code here
    return

def third_question(data):
    # Write code to address the following question:Use print() to display your responses.
    # What was the worst 7-day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.

    # Define Variables
    initial_case = None
    case_list = []
    date_list =[]
    total2 = []
    week = 7
    i = 0
    week_slices = []

    for (date, county, state, cases, deaths) in data:
        if state == 'Virginia' and county == 'Harrisonburg city':
            if initial_case != None:
                new_case = cases - initial_case
                date_list.append(date) # Gives me a new list of the dates the cases happend
                case_list.append(new_case) # Gives me new list of all the cases that happened each day
            initial_case = cases


    while i < len(case_list): # While loop to go through the new list created
        week_slice = case_list[i:i+week] # breaks up case list into chunks of seven
        date_slice = date_list[i:i+week] # breaks up date list into chunks of seven
        total = sum(week_slice) # Gets the sum of the cases each week
        total2.append(total) # appends this to new list
        week_slices.append(date_slice) # appends date to new list
        i += week

    worst = max(total2) # Gets the most amount of COVID Cases in a week
    worst_index = total2.index(worst) # Finds the index of where that is
    worst_date = week_slices[worst_index] # Uses this index to find what week it happened at

    print('Worst seven day period in Harrisonburg:', worst_date)
    print('The worst seven-day period in Harrisonburg was on 2022-01-08 until 2022-01-14 and the amount was', worst, 'COVID cases')

    # Code below is the same as the code above just for Rockingham
    initial_case = None
    case_list = []
    date_list = []
    total2 = []
    week = 7
    i = 0
    week_slices = []

    for (date, county, state, cases, deaths) in data:
        if state == 'Virginia' and county == 'Rockingham':
            if initial_case != None:
                new_case = cases - initial_case
                date_list.append(date)
                case_list.append(new_case)
            initial_case = cases

    while i < len(case_list):
        week_slice = case_list[i:i + week]
        date_slice = date_list[i:i + week]
        total = sum(week_slice)
        total2.append(total)
        week_slices.append(date_slice)
        i += week

    worst = max(total2)
    worst_index = total2.index(worst)
    worst_date = week_slices[worst_index]

    print('Worst seven day period in Rockingham:', worst_date)
    print('The worst seven-day period in Harrisonburg was on 2022-01-10 until 2022-01-16 and the amount was', worst,
          'COVID cases')

    return

if __name__ == "__main__":
    data = parse_nyt_data('us-counties.csv')


    #for (date, county, state, cases, deaths) in data:
        #print('On ', date, ' in ', county, ' ', state, ' there were ', cases, ' cases and ', deaths, ' deaths')


    # write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    first_question(data)


    # write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    second_question(data)

    # write code to address the following question:Use print() to display your responses.
    # What was the worst seven day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.
    third_question(data)


