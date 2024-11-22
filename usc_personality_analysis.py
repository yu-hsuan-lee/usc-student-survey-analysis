# PYTHON MODULES
# import user-installed modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# pandas options
pd.set_option('display.max_rows', 100)

# use !wget -nc 'github path' to pull the happiness data

#load data from github
!wget "https://raw.githubusercontent.com/emilyyyyyleeeee/ITP487_FinalExam/main/F2023_StudentSurvey.v2.csv"

student_survey_log = pd.read_csv('F2023_StudentSurvey.v2.csv')

# Create a copy of the original data
student_survey_df = student_survey_log.copy()

# Rename the first column
student_survey_df.rename(columns={'16 Personality Type Results': 'Personality_Type'}, inplace=True)

# Remove null columns
student_survey_df = student_survey_df.dropna(axis=1, how='all')

# Remove duplicates
student_survey_df = student_survey_df.drop_duplicates()

# Isolate the specified variables
variables_of_interest = ['Personality_Type', 'Grad_Year', 'GPA', 'Sex', 'Overall_USC_Exp',
                         'Merit_Scholarship_Percent', 'Age', 'USC_Social_Exp']
student_survey_df = student_survey_df[variables_of_interest]

# Create a new column for F/T based on Personality_Type
student_survey_df['FT_Group'] = student_survey_df['Personality_Type'].apply(lambda x: 'F' if 'F' in x else 'T')

# Display the cleaned and processed data
student_survey_df.head()

import matplotlib.pyplot as plt

# Preparing data for pie charts
sex_breakdown_f = student_survey_df[student_survey_df['FT_Group'] == 'F']['Sex'].value_counts()
sex_breakdown_t = student_survey_df[student_survey_df['FT_Group'] == 'T']['Sex'].value_counts()

# Pie chart for F group
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.pie(sex_breakdown_f, labels=sex_breakdown_f.index, autopct='%1.1f%%', startangle=140)
plt.title('Sex Breakdown for Feeler Group')

# Pie chart for T group
plt.subplot(1, 2, 2)
plt.pie(sex_breakdown_t, labels=sex_breakdown_t.index, autopct='%1.1f%%', startangle=140)
plt.title('Sex Breakdown for Thinker Group')

# Show the pie charts
plt.tight_layout()
plt.show()

# Preparing data for the horizontal bar chart
usc_social_exp_avg = student_survey_df.groupby('FT_Group')['USC_Social_Exp'].mean()

# Creating a horizontal bar chart
plt.figure(figsize=(10, 6))
usc_social_exp_avg.plot(kind='barh', color=['blue', 'green'])

plt.title('Average USC Social Experience Rating by Personality Group')
plt.xlabel('Average Rating')
plt.ylabel('Personality Group')
plt.xticks(range(0, 6))  # Assuming the ratings are on a scale of 1-5
plt.grid(axis='x')

# Show the bar chart
plt.show()

# Extracting only the columns of interest (Age and GPA) for analysis
df_analysis = student_survey_df[['Age', 'GPA']]

# Calculating the Pearson correlation
correlation_result = df_analysis.corr(method='pearson')
display(correlation_result)

# Creating Data Mart 1: Students graduating in 2024 with GPA between 3.3 and 3.6 (inclusive)
data_mart_1 = student_survey_df[(student_survey_df['Grad_Year'] == 2024) &
                                (student_survey_df['GPA'] >= 3.3) &
                                (student_survey_df['GPA'] <= 3.6)]

data_mart_1_head = data_mart_1.head()
print("Data Mart 1: Students Graduating in 2024 with GPA between 3.3 and 3.6")
display(data_mart_1_head)

#Data Mart 2: Students who earn at least 50% merit scholarship
data_mart_2 = student_survey_df[student_survey_df['Merit_Scholarship_Percent'] >= 0.50]

data_mart_2_head = data_mart_2.head()
print("\nData Mart 2: Students Earning At Least 50% Merit Scholarship")
display(data_mart_2_head)
