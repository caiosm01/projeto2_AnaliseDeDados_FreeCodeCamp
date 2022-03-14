import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = pd.Series(df.race.value_counts())

    # What is the average age of men?
    df2 = df[['sex', 'age']].loc[df[['sex', 'age']]['sex'] == 'Male']
    average_age_men = round(df2.age.mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df.education.value_counts()[2] / df.education.value_counts().sum()) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    df3 = df[['education', 'salary']].loc[(df[['education', 'salary']]['education'] == 'Bachelors') | (df[['education', 'salary']]['education'] == 'Masters') | (df[['education', 'salary']]['education'] == 'Doctorate')]

    df4 = df[['education', 'salary']].loc[(df[['education', 'salary']]['education'] != 'Bachelors') & (df[['education', 'salary']]['education'] != 'Masters') & (df[['education', 'salary']]['education'] != 'Doctorate')]

    higher_education = len(df3)

    lower_education = len(df4)

    # percentage with salary >50K
    higher = df3.loc[df3['salary'] == '>50K']
    lower = df4.loc[df4['salary'] == '>50K']
  
    higher_education_rich = round(100 * len(higher)/ higher_education, 1)
                                        
    lower_education_rich = round(100 * len(lower) / lower_education, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    df5 = df[['hours-per-week', 'salary']].loc[df[['hours-per-week', 'salary']]['hours-per-week'] == min_work_hours]
  
    num_min_workers = len(df5)

    rich_percentage = round(100 * len(df5.loc[df5['salary'] == '>50K']) / num_min_workers, 1)

    # What country has the highest percentage of people that earn >50K?
    df6 = df[['native-country', 'salary']]
    df7 = df[['native-country', 'salary']].loc[df[['native-country', 'salary']]['salary'] == '>50K']

    countrys = df7['native-country'].unique()
    
    bigger = 0
    earning_country = ''
  
    for country in countrys:
      percent = round(100 * (df7['native-country'].value_counts()[country]) / (df6['native-country'].value_counts()[country]), 1)
      if percent >= bigger:
        bigger = percent
        earning_country = country
      
    highest_earning_country = earning_country
    highest_earning_country_percentage = bigger

    # Identify the most popular occupation for those who earn >50K in India.
    df8 = df[['occupation', 'native-country', 'salary']].loc[(df[['occupation', 'native-country', 'salary']]['salary'] == '>50K') & (df[['occupation', 'native-country', 'salary']]['native-country'] == 'India')]

    top_IN_occupation = df8['occupation'].value_counts().index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
