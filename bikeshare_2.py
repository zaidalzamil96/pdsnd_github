import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months_list = [ "All",
                    "January",
                    "February",
                    "March",
                    "April",
                    "May",
                    "June"]

days_list = ["all", "monday",
                "tuesday",
                "wednesday",
                "thursday",
                "friday",
                "saturday",
                "sunday"]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hey! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = input("Enter city name (chicago, new york city, washington): ").lower()
    while city not in CITY_DATA:
        city = input("Enter city name (chicago, new york city, washington): ").lower()




    # get user input for month (all, january, february, ... , june)
    month = input("Enter month (all, january, february, ... , june): ").title()
    while month not in months_list:
        month = input("Enter month (all, january, february, ... , june): ").title()




    # get user input for day of week (all, monday, tuesday, ... sunday)


    day = input("Enter day of week (all, monday, tuesday, ... sunday): ").lower()
    while day not in days_list:
        day = input("Enter day of week (all, monday, tuesday, ... sunday): ").lower()




    print('-'*35)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specific city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])
    df["Start Time"] = pd.to_datetime(df["Start Time"])

    month = months_list.index(month)

    if month != 0:
        condition = df["Start Time"].dt.month == month
        df = df[condition]


    day = days_list.index(day) - 1  # to make monday=0, all=-1

    if day != -1:   # day not equal 'all'
        condition = df["Start Time"].dt.dayofweek == day
        df = df[condition]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    month_num = df["Start Time"].dt.month.mode()[0]
    month = months_list[month_num]
    print("the most common month is:", month)


    # display the most common day of week
    day_num = df["Start Time"].dt.dayofweek.mode()[0]
    day = days_list[day_num + 1]
    print("the most common day of week is:", day)


    # display the most common start hour
    hour = df["Start Time"].dt.hour.mode()[0]
    print("the most common start hour is:", hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_st = df["Start Station"].mode()[0]
    print("most commonly used start station:", start_st)


    # display most commonly used end station
    end_st = df["End Station"].mode()[0]
    print("most commonly used end station:", end_st)


    # display most frequent combination of start station and end station trip
    start_st, end_st = df[["Start Station", "End Station"]].mode().iloc[0,:]
    print("most frequent combination of start station and end station trip is:", start_st, "and", end_st)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df["Trip Duration"].sum()
    print("total travel time:", total_time)


    # display mean travel time
    avg_time = df["Trip Duration"].mean()
    print("mean travel time:", avg_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    counts = df["User Type"].value_counts()
    print("counts of user types:")
    print(counts, "\n")


    # Display counts of gender
    if "Gender" in df.columns:
        counts = df["Gender"].value_counts()
        print("counts of gender:")
        print(counts, "\n")


    # Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        earliest = df["Birth Year"].min()
        recent = df["Birth Year"].max()
        common = df["Birth Year"].mode()[0]
        print("earliest:", earliest)
        print("most recent:", recent)
        print("most common:", common)

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

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
