import time
import datetime as dt
import pandas as pd
import numpy as np

#Get city data to dictionaries
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

# get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input("Enter one of the 3 city names; chicago, new york city or washigton: ")
            print("\n", "="*30)
            if city == 'chicago':
                print("You've chose to review chicago")
            elif city == 'new york city':
                print("You've chose to review New York City")
            elif city == 'washington':
                print("You've chose to review Washington, DC")
            elif city == 'all':
                print("You've chose to review all 3 cities")
            else:
                print("Opps! ):\n Sorry! You have entered the wrong city")
                continue
            break
            print("="*30)
        except:
            print("):\n Please, input a valid city or verify your input characters!\n):")

# get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input("Enter either one of the first semester month (january-june) or type 'all' to get into aquire all the 6 months: ")
            months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
            if month not in months:
                print("What you've entered is invalid, remember (january-june) or 'all'!")
            break
        except:
            print("):\n Please, enter a valid month index")

# get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input("Enter one day of the week or enter 'all' to aquire all days at once: ")
            days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
            if day not in days:
                print("Please, this is not a valid day!")
            break
        except:
            print("Sorry! That was not a valid week we sugest to enter!")

    print('-'*40)
    print('|'*30, '\n')
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
    if city == 'all':
        df = pd.concat(map(pd.read_csv, ["chicago.csv", "new_york_city.csv", "washington.csv"]), ignore_index = True, sort = False)
        print("Loading all cities")
    else:
        df = pd.read_csv(CITY_DATA[city])
    #Converting star time colum into a date time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    #Let's filter months if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    #Let's filter the days if applcable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[ df['day_of_week'] == day.title()]
    return df

def raw_data(df):
    """
    Displays 5 rows of data based on user input
    Args:
        df - panda dataframe returned from filtering by city month and/or day
        declare - yes or no based on user decision
    """
    declare = str(input("Do you want to view rows of the raw data? 'yes' or 'no': ").lower())

    while True:
        if declare == 'yes':
            print(df.head(5))
            break
        else:
            print('Thank you')
            break
    print('-'*40)
    print('|'*30, '\n')

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_commo_month = df['month'].mode()[0]
    print("The most common month is", most_commo_month)
    # display the most common day of week
    most_commo_day = df['day_of_week'].mode()[0]
    print("The most common day of the weeek is ", most_commo_day)
    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_commo_hour = df['hour'].mode()[0]
    print("The most common hour is ", most_commo_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    mst_com_str_station = df['Start Station'].mode()[0]
    print("The most common start station is ", mst_com_str_station)

    # display most commonly used end station
    mst_com_end_station = df['End Station'].mode()[0]
    print("The most end station is", mst_com_end_station)
    # display most frequent combination of start station and end station trip
    mst_frequent_str_and_end_station = (df['Start Station'] + '-' + df['End Station']).mode()[0]
    print("The most frequent start to end station is ", mst_frequent_str_and_end_station)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    t_hours = total_travel_time
    t_minutes = t_hours // 60
    t_seconds = t_minutes // 60
    print("The total time they traveled is {} hours {} minutes and {} seconds".format(t_hours, t_minutes, t_seconds))
    #print("The number of time they traveled is ", total_travel_time, " hours")

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    mn_hours = mean_travel_time
    mn_minutes = mn_hours // 60
    mn_seconds = mn_minutes // 60
    print("The average time they traveled is {} hours {} minutes {} seconds".format(mn_hours, mn_minutes, mn_seconds))
    #print("The average hours they traveled is ", mean_travel_time, " hours")

    print("Travel time for each user type:\n")
    # display the total trip duration for each user type
    user_type_trip = df.groupby(['User Type']).sum()['Trip Duration']
    for i, u_trip in enumerate(user_type_trip):
        print("  {}: {} seconds".format(user_type_trip.index[i], u_trip))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The user categories are as follow:\n", user_types)
    # Display counts of gender
    if city != 'washington':
        genders = df['Gender'].value_counts()
        print("The user genders are:\n", genders)
    # Display earliest, most recent, and most common year of birth
    if city != 'washington':
        earliest = df['Birth Year'].max()
        print("The earliest year of birth is ", earliest)
        recent = df['Birth Year'].min()
        print("The most recent year of birth is ", recent)
        common = df['Birth Year'].mode()[0]
        print("The most common year of birth is ", common)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def gen_description(df):
    """Display the general description of the selected data based on user input
    Args:
        df- panda dataframe returned from filtering by city, month and/or day
        chose - yes or no based on user decision
        """
    chose = str(input("Would you like to display the summary statistics of your selection? 'yes' or 'no': ").lower())
    while True:
        if chose == 'yes':
            print(df.describe())
            break
        else:
            print('Alright, thanks')
            break
    print('-'*40)
    print('_'*40, '\n')

def main():
    """
    This is the part where all the above defined funtions depend on.
    Args:
    raw_data(df)- refreshes the raw data fuction
    time_stats(df)- refreshes the time_stats fuction
    ... -
    """
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        gen_description(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
	main()
