import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv'}



def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """


    print(f"'hi ! my name is \'bello\' and i'm here to help you to explore US bikeshare DATA\n")



    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # CITY INPUT
    city = str(input("what's the city you wanna explore it ? pls enter city name(chicago, new york city, washington)\n >>>")).lower()
    while city not in CITY_DATA.keys():
        print("that\'s not what I wanna see please enter the right city name, you can just copy it from the next msg\n")

        city = str(
            input(
                "what\'s the city you wanna explore it ? pls enter city name(chicago, new york city or washington)\n: "
            )).lower()




    # get user input for month (all, january, february, ... , june)
    # MONTH INPUT
    months_list = ["all", "january", "february", "march", "april", "may", "june"]
    month = str(
        input("what\'s the month you wanna explore it ? , (all, january, february, march, april, may, june)\n>>>")).lower()
    while month not in months_list:
        print("that\'s not what I wanna see please enter the right month name, you can just copy it from the next msg\n")

        month = str(input(
            "what\'s the month you wanna explore it ? , (all, january, february, march, april, may, june)\n>>>")).lower()
    # get user input for day of week (all, monday, tuesday, ... sunday)
    #DAY INPUT
    days_list = ["all", "saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday"]
    day = str(
        input(
            "what\'s the day you wanna explore it ? , (all, saturday, sunday, monday, tuesday, wednesday, thursday, friday)\n>>>"
        )).lower()
    while True:
        if day in days_list:
            break
        else:
            print("that\'s not what I wanna see please enter the right day name, you can just copy it from the next msg\n")
            day = str(
                input(
                    "what\'s the day you wanna explore it ? , (all, saturday, sunday, monday, tuesday, wednesday, thursday, friday)\n>>>"
                )).lower()
    print('-*-'*20)
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
    #read files and change dtype for start time column to date dime to get month, day, start hour
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time']= pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()
    df['start hour']= df['Start Time'].dt.hour
    #check for if we want all or specific month to filter it
    if month != "all":
        months_list = ["january", "february", "march", "april", "may", "june"]
        month = months_list.index(month)+1
        df = df[df['month'] == month]
    # check for if we want all or specific day to filter it as bool value
    if day != 'all':
        df = df[df['day'] == day.title()]

    return df


def time_stats(df,month,day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    time.sleep(1)

    start_time = time.time()

    # display the most common month

    common_m = df['month'].mode()[0]
    if month =="all":
        print(f'\nthe most common month is : {common_m}')



    # display the most common day of week
    common_d = df['day'].mode()[0]
    if day == "all":
        print(f'\nthe most common day is : {common_d}')


    # display the most common start hour
    common_h = df['start hour'].mode()[0]
    print(f'\nthe most common hour is : {common_h}\n')


    print("\nThis took like %s seconds." % (time.time() - start_time).__round__())
    print('-*-' * 20)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    time.sleep(1)
    start_time = time.time()

    # display most commonly used start station
    common_S = df['Start Station'].mode()[0]
    print(f'\nmost commonly used start station is     >>>     {common_S}')




    # display most commonly used end station
    common_eS = df['End Station'].mode()[0]
    print(f'\nmost commonly used end station is     >>>      {common_eS}')



    # display most frequent combination of start station and end station trip
    #we will make new df to concatenate start and end stations let's call it umm
    df["track"] = df['Start Station']+","+df['End Station']
    common_f = df['track'].mode()[0]
    print(f'\nmost frequent combination of start station and end station is      >>>     {common_f}')




    print("\nThis took like %s seconds." % (time.time() - start_time).__round__())
    print('-*-' * 20)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    time.sleep(1)

    start_time = time.time()

    # display total travel time
    ttt = df['Trip Duration'].sum()
    print(f"\ntotal travel time: {ttt}")


    # display mean travel time
    mtt = df['Trip Duration'].mean()
    print(f"\naverage travel time: {mtt}")



    print("\nThis took like %s seconds." % (time.time() - start_time).__round__())
    print('-*-' * 20)



def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    time.sleep(2)

    start_time = time.time()

    # Display counts of user types
    cou = df['User Type'].value_counts().to_frame()
    print(f"\ncounts of user types:\n{cou}\n")


    # Display counts of gender
    #not all of the data we received have gender column so we need to filter it
    if city != 'washington':
        cog = df['Gender'].value_counts().to_frame()
        print(f"\ncounts of gender:\n{cog}\n")



    # Display earliest, most recent, and most common year of birth
        #earliest
        e_year = df['Birth Year'].min()
        print(f"\nearliest year of birth: {int(e_year)}")


        #most recent
        r_year = df['Birth Year'].max()
        print(f"\nrecent birth year: {int(r_year)}")


        #most common
        mc_year = df['Birth Year'].mode()[0]
        print(f"\nmost common year of birth: {int(mc_year)}\n")

    else:
        print('this type of data not available for this city\n')


    print("\nThis took like %s seconds." % (time.time() - start_time).__round__())
    print('-*-' * 20)


def display_data(city):
    """
    Here I ran into a problem cuz if user wanna input entry and filter it by day for example this function will display 5 row
    from only filtred data so it's will not display raw data that's why i would Reset df variable
    """
    df = pd.read_csv(CITY_DATA[city])

    #to prompt the user if they want to see 5 lines of raw data,
    #Display that data if the answer is 'yes'
    print("\nok!, for now  you saw some statistical operations on data and also RAW data available to check if you want \n")


    i = 0
    user_input = input('if you like to display 5 rows of raw data ?, (yes or no)\n').lower()
    if user_input not in ["yes", "no"]:
        print("\ninvalid input\n")

        user_input = input('if you like to display 5 rows of raw data ?, (yes or no)\n').lower()

    #here we show 5 rows for ech time
    elif user_input != "yes":
        print("thanks!")

    else:
        while i+5 < df.shape[0]:
            print("\n")
            print(df.iloc[i:i+5])
            i += 5
            user_input = input('if you like to display more 5 rows of raw data ?, (yes or no)\n').lower()
            if user_input != "yes":
                print("thanks!")
                break




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(city)

        restart = input("\n! that's all,Would you like to restart? Enter yes or no.\n")
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
