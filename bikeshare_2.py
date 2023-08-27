import time
import pandas as pd
import numpy as np

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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("\nWhich city you would like to analyze? You can choose from Chicago, New York City or Washington: ")
    city = city.lower()
    while True:
        if city in {'chicago', 'new york city', 'washington'}:
            break
        else:
            print("\nPlease choose only one from available cities: Chicago, New York City or Washington.")
            city = input("\nWhich city you would like to analyze? You can choose from Chicago, New York City or Washington: ")
            city = city.lower()
            continue
    
    # TO DO: get user input for month (all, january, february, ... , june)
    
    month  = input("\nWhich month you would like to analyze? You can choose from: all, January, February, March, April, May, June: ")
    month = month.lower()
    while True: 
        if month in {'all', 'january', 'february', 'march', 'april', 'may', 'june'}:
            break
        else:
            print("\nPlease choose only one from available months: all, January, February, March, April, May, June.")
            month = input("\nWhich month you would like to analyze? You can choose from: all, January, February, March, April, May, June: ")
            month = month.lower()
            continue
                
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    day = input("\nWhich day of week you would like to analyze? You can choose from: all, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday: ")
    day = day.lower()
    while True:
        if day in {'all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'}:
            break
        else:
            print("\nPlease choose only one from available days of week: all, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday.")
            day = input("\nWhich day of week you would like to analyze? You can choose from: all, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday: ")
            day = day.lower()
            continue
            
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
        df = df[df['Start Time'].dt.month == month]
    if day != 'all':
        df = df[df['Start Time'].dt.day_name() == day.title()]       
        
    return df

def time_stats(df):
    
    """Displays statistics on the most frequent times of travel."""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print("\nMost popular month: ", popular_month)
    
    # TO DO: display the most common day of week
    
    df['day_of_week'] = df['Start Time'].dt.day_name()
    popular_day = df['day_of_week'].mode()[0]
    print("\nMost popular day: ", popular_day)
    
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("\nMost popular hour: ", popular_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    
    """Displays statistics on the most popular stations and trip."""
    
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("\nMost popular start station: ", popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("\nMost popular end station: ", popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['start_end'] = df['Start Station'] + " - " + df['End Station']
    popular_combination_station = df['start_end'].mode()[0]
    print("\nMost popular station trip: ", popular_combination_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time']=pd.to_datetime(df['End Time'])
    df['delta']=df['End Time']-df['Start Time']
    
    # TO DO: display total travel time
    
    total_travel_time=pd.to_timedelta(df['delta'], unit='m').sum()
    print("\nTotal travel time: ", total_travel_time)
    # TO DO: display mean travel time

    mean_travel_time=pd.to_timedelta(df['delta'], unit='m').mean()
    print("\nMean travel time: ", mean_travel_time)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # TO DO: Display counts of user types
    
    user_types = df['User Type'].value_counts()
    print("\nCounts of user types: ", user_types)
    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print("\nCounts of gender: ", gender)
    except KeyError:
        print("\nThere is no gender statement.")
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_BD = df['Birth Year'].min()
        print("\nEarliest Birth Year: ", earliest_BD)
        recent_BD = df['Birth Year'].max()
        print("\nRecent Birth Year: ", recent_BD)
        common_BD = df['Birth Year'].mode()[0]
        print("\nMost common Birth Year: ", common_BD)
    except KeyError:
        print("\nThere is no Birth Year statement.")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        raw_data = input("\nWould you like to see individual trip data? Type yes or no.\n")
        while True:
            if raw_data.lower() in {'yes', 'no'}:
                break
            else:
                print("\nPlease choose only one from available options: yes or no")
                raw_data = input("\nWould you like to see individual trip data? Type yes or no.\n")
                raw_data = raw_data.lower()
                continue
        x = 0
        while True:
            if raw_data.lower() != 'yes':
                break
            else:
                print(df.iloc[x:x+5])
                x += 5
                raw_data = input('\nWould you like to see individual trip data? Type yes or no.\n')
                continue
        restart = input("\nWould you like to restart? Enter yes or no.\n")
        while True:
            if restart.lower() in {'yes', 'no'}:
                break
            else:
                print("\nPlease choose only one from available options: yes or no")
                restart = input("\nWould you like to restart? Enter yes or no.\n")
                restart = restart.lower()
                continue
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
