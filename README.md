[Data_Mart_2__Students_Earning_At_Least_50__Merit_Scholarship.csv](https://github.com/user-attachments/files/17853599/Data_Mart_2__Students_Earning_At_Least_50__Merit_Scholarship.csv)[Data_Mart_1__Students_Graduating_in_2024_with_GPA_between_3_3_and_3_6.csv](https://github.com/user-attachments/files/17853596/Data_Mart_1__Students_Graduating_in_2024_with_GPA_between_3_3_and_3_6.csv)![output (1)](https://github.com/user-attachments/assets/c7935576-c86f-4c1c-ab68-002962ab7b65)# USC Student Personality Insights and Data Exploration

## Description
This project analyzes a student survey dataset from USC, exploring relationships between personality types, academic performance, social experiences, and other demographic variables. The dataset is processed, cleaned, and visualized to uncover meaningful insights and correlations.

## Key Features
1. **Data Cleaning**:  
   - Renamed ambiguous columns for clarity.
   - Removed null columns and duplicate rows.
   - Focused on a subset of variables for meaningful analysis.

2. **Data Exploration**:  
   - Categorized personality types into Feeler (F) and Thinker (T) groups.
   - Generated visualizations for demographic and social experience trends.

3. **Insights**:  
   - Correlation analysis between age and GPA.
   - Analysis of social experiences by personality type.

4. **Data Marts**:  
   - **Data Mart 1**: Students graduating in 2024 with GPAs between 3.3 and 3.6.
   [Uploading Data_Mart_1__Studen,Personality_Type,Grad_Year,GPA,Sex,Overall_USC_Exp,Merit_Scholarship_Percent,Age,USC_Social_Exp,FT_Group
3,ENFJ-A,2024,3.56,Male,4,0%,22,4,F
5,ESTJ-A,2024,3.47,Female,5,0%,21,5,T
13,INTP-A,2024,3.44,Male,4,0%,22,4,T
14,ESTJ-A,2024,3.4,Female,5,0%,21,5,T
15,ESFJ-A,2024,3.59,Male,4,0%,21,4,F
22,INTJ-T,2024,3.54,Male,5,100%,21,5,T
23,ENTJ-T,2024,3.6,Male,4,0%,22,5,T
25,ISFJ-T,2024,3.58,Female,4,0%,21,3,F
29,ESFP-A,2024,3.6,Male,4,0%,21,5,F
30,ISFJ-T,2024,3.55,Female,5,0%,21,4,F
32,ENFJ-T,2024,3.4,Female,4,75%,21,3,F
39,ESFJ-A,2024,3.47,Male,5,0%,21,5,F
42,ESTP-T,2024,3.6,Male,4,0%,21,4,T
46,ENFP-A,2024,3.42,Female,4,0%,21,5,F
53,INFP-A,2024,3.48,Male,4,0%,21,3,F
61,ESTJ-T,2024,3.3,Female,5,25%,21,5,T
66,ENTP-T,2024,3.51,Female,4,0%,20,4,T
71,ENFJ-T,2024,3.5,Male,3,0%,22,3,F
73,ESFP-A,2024,3.5,Male,4,0%,22,4,F
ts_Graduating_in_2024_with_GPA_between_3_3_and_3_6.csv…]()

   - **Data Mart 2**: Students receiving at least 50% merit scholarships.
   [Uploading Data_Mart_2__Students_Earning_At_Least_50_,Personality_Type,Grad_Year,GPA,Sex,Overall_USC_Exp,Merit_Scholarship_Percent,Age,USC_Social_Exp,FT_Group
6,ISTJ-T,2025,3.93,Female,4,50%,21,3,T
10,ISFJ-A,2024,3.95,Male,4,50%,21,4,F
11,ISTJ-T,2024,3.78,Male,3,50%,21,3,T
16,ESFJ-A,2024,3.96,Female,5,75%,22,4,F
18,ESTP-A,2024,3.2,Male,3,100%,21,3,T
19,INFJ-A,2024,3.78,Female,5,75%,21,4,F
22,INTJ-T,2024,3.54,Male,5,100%,21,5,T
24,ISFP-T,2024,3.77,Male,4,50%,21,4,F
32,ENFJ-T,2024,3.4,Female,4,75%,21,3,F
38,INFJ-T,2024,3.89,Female,5,50%,21,5,F
40,INTJ-A,2024,3.81,Male,5,50%,21,5,T
43,ENTJ-A,2024,4.0,Male,5,50%,22,4,T
45,ENFJ-T,2024,3.99,Male,5,50%,21,5,F
47,ENFP-A,2024,3.84,Female,4,75%,21,3,F
49,ESFJ-A,2024,3.78,Male,4,100%,21,4,F
70,INFP-T,2024,3.7,Male,5,75%,27,4,F
72,INFJ-T,2023,3.9,Female,2,100%,22,1,F
_Merit_Scholarship.csv…]()

5. **Visualizations**:  
   - Pie charts displaying sex distribution by personality group.'
   ![output (1)](https://github.com/user-attachments/assets/95372e18-1ee1-48fd-8578-e5107ad6c1e7)
   - Horizontal bar chart comparing average social experience ratings.
   ![output (2)](https://github.com/user-attachments/assets/7002c2b4-7267-4a5f-808f-210154945ffc)


## Dataset
- **Source**: USC Student Survey Data (uploaded as `F2023_StudentSurvey.v2.csv`).
- **Key Variables**:
  - `Personality_Type`: Results from the 16 Personality Type test.
  - `Grad_Year`: Graduation year of the student.
  - `GPA`: Academic performance.
  - `Sex`: Gender identification.
  - `USC_Social_Exp`: Rating of USC's social experience.

## Requirements
- Python 3.x
- Required Libraries:  
  ```bash
  pandas
  numpy
  matplotlib

## Usage

### Data Cleaning
- Drops unnecessary columns and duplicates.
- Filters relevant variables for analysis.

### Visualization
- Provides demographic breakdowns and comparisons.

### Data Analysis
- Calculates correlations between age and GPA.
- Creates subsets (data marts) for specific student groups.

### Output
- Interactive data tables (Data Marts).
- Charts showing trends and distributions.

## Example Insights
- The average USC social experience rating differs significantly between Feelers and Thinkers.
- Students with higher merit scholarships may display distinct academic and personality traits.

## Future Improvements
- Expand to include additional demographic and academic variables.
- Enhance the analysis with machine learning models for predictive insights.
- Integrate the project into an interactive dashboard for real-time data exploration.
