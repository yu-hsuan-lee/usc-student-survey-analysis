# USC Student Personality Insights and Data Exploration

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
   <img width="828" alt="Screenshot 2024-11-21 at 4 26 33 PM" src="https://github.com/user-attachments/assets/06e47e25-da35-4d97-acb1-0a3266aa60ab">

   - **Data Mart 2**: Students receiving at least 50% merit scholarships.
   <img width="810" alt="Screenshot 2024-11-21 at 4 27 08 PM" src="https://github.com/user-attachments/assets/42bdff0a-d071-42d8-8f26-a3081b067ee4">

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
