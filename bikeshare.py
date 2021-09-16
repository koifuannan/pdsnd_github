import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#city_dict ={'Chicago' : 1, 'New York City' : 2 , 'Washington:' :3 }
month_list = ['january', 'february', 'march', 'april', 'may', 'june','all']
day_list = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday' , 'friday', 'saturday' , 'all']


def get_filters():

    city =""
    month =""
    day =""

    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while city not in CITY_DATA.keys():
        try:
            city = input("Enter Chicago, New York City or Washington to make a choice: ").lower()

            if (city not in CITY_DATA.keys()):
                print("Wrong choice. Choose from menu provided!\n")
        except exception as ex:
            print(ex)


    # TO DO: get user input for month (all, january, february, ... , june)
    while month not in month_list:
        try:
            month = input("Enter the month for the analysis in full. From January to June only or all for all the months: ").lower()

            if (month not in month_list):
                print("Allowed entries are: January, Frebruary, March, April, May, June, All only")
        except exception as e:
            print(e)


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while day not in day_list:
        try:
            print("\nEnter the day you want the anlysis made. Options are")
            print(*day_list, sep = ", ")
            day = input().lower()

            if (day not in day_list):
                print("Allowed entries are the numeric corresponding to the days\n", day_list )
        except exception as de:
            print(de)

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #load the file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    """
    use if statements to filter the data as required
    to be able to do that, first extract the month and day of the week from the Start Time and End Time to create new cloumns

    """
    #first convert the start time column to datetime before the extraction
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #df['End Time'] = pd.to_datetime(df['End Time'])

    #next is the extraction to create new columns
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    #now the filtering starts, first by month
    if (month != 'all'):
        df = df[df['month'] == month.title()]


    #then by day of the week
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):

    print(df)

    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()



    # TO DO: display most commonly used start station
    common_travel_month = df['month'].mode()[0]

    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]

    print("*************************************************")
    print("Frequent Month of Travel => {}".format(common_travel_month))
    print("Frequent Day of Travel => {}".format(common_day_of_week))
    print("Frequent Hour of Travel => {}\n".format(common_hour))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]


    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]


    # TO DO: display most frequent combination of start station and end station trip
    """
    To get the frequent start station and station, would mean that we treat the start station and end station as one and
    find the mode. Thus, we can concatenate these two columns into one and find the mode using the new column
    """
    start_end_station = df['Start Station'] + ' ' +  df['End Station']
    frequent_start_end_station = start_end_station.mode()[0]

    print("*************************************************")
    print("Frequently used Start Station for Travel => {}".format(common_start_station))
    print("Frequently used End Station for Travel => {}".format(common_end_station))
    print("Frequently used Start and End Station Combination for Travel => {}\n".format(frequent_start_end_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    """
    First we have to calculate the time difference and then find the sum of all the time difference
    """
    total_travel_time = (pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).sum()

    # TO DO: display mean travel time
    mean_travel_time = (pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).mean()

    print("*************************************************")
    print("Total Travel Time => {}".format(total_travel_time))
    print("Mean Travel Time => {}".format(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_types = df['User Type'].value_counts()

    for index, value in count_user_types.items():
        print("There are {} : {} \n".format(value,index))

    # TO DO: Display counts of gender
    count_gender = df['Gender'].value_counts()

    for index, value in count_gender.items():
        print("There are {} : {} \n".format(value,index))

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_birth_year = df['Birth Year'].min()
    recent_birth_year = df['Birth Year'].max()
    common_birth_year = df['Birth Year'].mode()[0]

    print("*************************************************")
    print("Earliest Birth Year => {}".format(earliest_birth_year))
    print("Recent Birth Year Year => {}".format(recent_birth_year))
    print("The most common Birth Year => {}".format(common_birth_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def show_raw_data(df):

    #print(df.head())
    r_count = 0
    value =""

    while True:
        if (r_count==0):
            value = "first"
        else:
            value ="next"

        r_data = input('\nView the ' + value + ' five row of raw data? Enter yes or no.\n')
        if r_data.lower() != 'yes':
            return
        r_count += 5

        dfDict  = df.iloc[r_count: r_count+5].to_dict('index')
        for key, value in dfDict.items():
            print(key, ':', value)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
