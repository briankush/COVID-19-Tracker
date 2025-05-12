# COVID-19 Data Analysis and Visualization

## Project Description
This project analyzes and visualizes COVID-19 data for selected countries (United States, India, and Kenya) using publicly available datasets. It provides insights into the progression of the pandemic through various plots and a choropleth map.

## Objectives
- Load and clean COVID-19 data from a CSV file.
- Explore key metrics such as total cases, deaths, and vaccinations.
- Visualize trends over time for selected countries.
- Create a choropleth map to compare cases per million across countries.
- Provide an interactive and informative way to understand COVID-19 impact.

## Tools and Libraries Used
- Python 3
- pandas
- seaborn
- matplotlib
- plotly.express

## How to Run/View the Project
1. Ensure you have Python 3 installed.
2. Install the required libraries if not already installed:
   ```
   pip install pandas seaborn matplotlib plotly
   ```
3. Place the dataset file `owid-covid-data.csv` in the same directory as `main.py`.
4. Run the script from the command line:
   ```
   python main.py
   ```
5. The script will load the data, perform analysis, and display various plots and a choropleth map.

## Insights and Reflections
This project demonstrates how data cleaning and visualization can provide meaningful insights into the COVID-19 pandemic. The use of multiple visualization libraries allows for both static and interactive representations, enhancing understanding of the data. Future improvements could include expanding the list of countries, adding more metrics, and improving the interactivity of the visualizations.
