import time
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
              
# NEW COMMENT for project submission 3B.

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print('\nWhich city would you like to explore: Chicago, New York City, or Washington ?')
    while True:
        try:
            city = input('Enter name of a city:').lower()
            city = CITY_DATA[city]
            print('\nGreat! We now checking the data for ',city)
            break
        except KeyError:
                print('Sorry, we only have data for chicago, new york city and washington !')
                True

    # get user input for month (all, january, february, ... , june)
    print('\nWhich month between january to june would you like to explore ? \nOr do want to explore all months (please tip all) ?')

    while True:
        month = input('Enter month of the year: ').lower()
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
        if month in months:
            print('nGreat! we are checking data for', month)
            break
        else:
            print('Sorry, please enter all or months; january to june')

        # filter by month to create the new dataframe

    # get user input for day of week (all, monday, tuesday, ... sunday)
    print('\nWhich day of the week would you like to explore ?\nOr do want to explore all days ot the week (please tip all) ?')
    day = input('\nEnter day of the week: ').lower()


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
    df=pd.read_csv(city)

    df['Start Time']= pd.to_datetime(df['Start Time'], errors='coerce')

    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.day_name()

    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]


    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    common_month = df['month'].mode()[0]
    print('Most common month: ', common_month)

    # display the most common day of week

    common_day = df['day_of_week'].mode()[0]
    print('Most common day of week: ', common_day)

    # display the most common start hour

    common_start_hour = df['hour'].mode()[0]
    print('Most common start hour: ', common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print( 'Most common start Station: ', common_start_station)                                         #'Start Station', 'End Station

    # display most commonly used end station

    common_end_station = df['End Station'].mode()[0]
    print( 'Most common end Station: ', common_end_station)

    # display most frequent combination of start station and end station trip

    common_combination = df.groupby(['Start Station','End Station']).size().idxmax()
    print( 'Most common frequent combination of start station and end station: ', common_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    trip_duration = df['Trip Duration'].sum()
    print('Total trip duration: ', trip_duration)


    # display mean travel time

    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel time: ', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    user_types = df['User Type'].value_counts()
    print('Counts of User Type: ', user_types)

    # Display counts of gender

    if 'Gender' in df:
        gender_count = df['Gender'].value_counts()
        print('Total Gender count: ', gender_count)
    else:
        print('Gender information is not available for this city')


    # Display earliest, most recent, and most common year of birth

    if 'Birth Year' in df:
        common_birth_year=df['Birth Year'].mode()[0]
        print('Most common birth year: ', common_birth_year)
        birth_year_count = df['Birth Year'].value_counts(normalize = True).plot(kind='bar')  # birth_year_count = df['Birth Year'].value_counts(normalize = True).plot(kind='bar')
        plt.title('This histogramm shows the distribution of the birth years over all customers for selected time!')
        plt.ylabel('Count customers')
        plt.xlabel('Year of birth')
        plt.show()

        #print('This chart shows us the distribution of Birth years our customers',birth_year_count)
    else:
        print('Birth year information is not availabe for this city')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    #displaying answer if user want to view first five rows of data or not ---> NICHT TEIL DER AUFGABE !!!!

    while True:
        answer = input('\nWould you like to view data? Enter yes or no:\n').lower()
        if answer == 'yes':
            print('First five raw data\n', df.head())
            break
        elif answer == 'no':
            break
        else:
            True


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no:\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
