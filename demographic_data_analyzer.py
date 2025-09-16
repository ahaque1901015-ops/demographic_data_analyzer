import pandas as pd

def calculate_demographics(print_data=True):
    # Read data from CSV file
    df = pd.read_csv("adult.data.csv")  # make sure your CSV file is named correctly

    # 1. How many people of each race are represented in this dataset? (race column)
    race_count = df['race'].value_counts()

    # 2. What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. What is the percentage of people who have a Bachelor's degree?
    total_people = df.shape[0]
    bachelors_count = df[df['education'] == 'Bachelors'].shape[0]
    percentage_bachelors = round((bachelors_count / total_people) * 100, 1)

    # 4. What percentage of people with advanced education make more than 50K?
    advanced_education = ['Bachelors', 'Masters', 'Doctorate']
    higher_edu = df[df['education'].isin(advanced_education)]
    higher_edu_rich = higher_edu[higher_edu['salary'] == '>50K'].shape[0]
    percentage_higher_edu_rich = round((higher_edu_rich / higher_edu.shape[0]) * 100, 1)

    # 5. What percentage of people without advanced education make more than 50K?
    lower_edu = df[~df['education'].isin(advanced_education)]
    lower_edu_rich = lower_edu[lower_edu['salary'] == '>50K'].shape[0]
    percentage_lower_edu_rich = round((lower_edu_rich / lower_edu.shape[0]) * 100, 1)

    # 6. What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()

    # 7. What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_min_workers = min_workers[min_workers['salary'] == '>50K'].shape[0]
    rich_percentage = round((rich_min_workers / min_workers.shape[0]) * 100, 1)

    # 8. What country has the highest percentage of people that earn >50K?
    country_group = df.groupby('native-country')
    country_rich_percentage = ((country_group['salary'].apply(lambda x: (x == '>50K').sum()) /
                               country_group['salary'].count()) * 100)
    highest_earning_country = country_rich_percentage.idxmax()
    highest_earning_country_percentage = round(country_rich_percentage.max(), 1)

    # 9. Identify the most popular occupation for those who earn >50K in India.
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_rich['occupation'].value_counts().idxmax()

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education earning >50K: {percentage_higher_edu_rich}%")
        print(f"Percentage without higher education earning >50K: {percentage_lower_edu_rich}%")
        print("Minimum hours per week:", min_work_hours)
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupation in India for those earning >50K:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'percentage_higher_edu_rich': percentage_higher_edu_rich,
        'percentage_lower_edu_rich': percentage_lower_edu_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
