# Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Load the dataset
def load_data(file_path):
    """
    Load the COVID-19 dataset from a CSV file.
    """
    try:
        df = pd.read_csv(file_path)
        print("Data loaded successfully!")
        return df
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None

# Explore the dataset
def explore_data(df):
    """
    Perform basic exploration of the dataset.
    """
    print("Columns in the dataset:")
    print(df.columns)
    print("\nPreview of the data:")
    print(df.head())
    print("\nMissing values in each column:")
    print(df.isnull().sum())

# Clean the dataset
def clean_data(df):
    """
    Clean the dataset by filtering, handling missing values, and converting data types.
    """
    # Filter for countries of interest (example: USA, India, Kenya)
    countries_of_interest = ['United States', 'India', 'Kenya']
    df = df[df['location'].isin(countries_of_interest)]

    # Drop rows with missing critical values
    df = df.dropna(subset=['date', 'total_cases', 'total_deaths'])

    # Convert date column to datetime
    df['date'] = pd.to_datetime(df['date'])

    # Fill missing numeric values with interpolation
    df = df.fillna(method='ffill')

    # Calculate death rate
    df['death_rate'] = df['total_deaths'] / df['total_cases']

    # Calculate % vaccinated if population and total_vaccinations exist
    if 'total_vaccinations' in df.columns and 'population' in df.columns:
        df['percent_vaccinated'] = df['total_vaccinations'] / df['population'] * 100

    print("Data cleaned successfully!")
    return df

# Plot total cases over time
def plot_total_cases(df):
    """
    Plot total cases over time for selected countries.
    """
    plt.figure(figsize=(10, 6))
    for country in df['location'].unique():
        country_data = df[df['location'] == country]
        plt.plot(country_data['date'], country_data['total_cases'], label=country)

    plt.title("Total COVID-19 Cases Over Time")
    plt.xlabel("Date")
    plt.ylabel("Total Cases")
    plt.legend()
    plt.grid()
    plt.show()

# Plot total deaths over time
def plot_total_deaths(df):
    """
    Plot total deaths over time for selected countries.
    """
    plt.figure(figsize=(10, 6))
    for country in df['location'].unique():
        country_data = df[df['location'] == country]
        plt.plot(country_data['date'], country_data['total_deaths'], label=country)

    plt.title("Total COVID-19 Deaths Over Time")
    plt.xlabel("Date")
    plt.ylabel("Total Deaths")
    plt.legend()
    plt.grid()
    plt.show()

# Plot daily new cases
def plot_new_cases(df):
    """
    Plot daily new cases for selected countries.
    """
    plt.figure(figsize=(10, 6))
    for country in df['location'].unique():
        country_data = df[df['location'] == country]
        if 'new_cases' in country_data:
            plt.plot(country_data['date'], country_data['new_cases'], label=country)

    plt.title("Daily New COVID-19 Cases")
    plt.xlabel("Date")
    plt.ylabel("New Cases")
    plt.legend()
    plt.grid()
    plt.show()

# Plot vaccinations over time
def plot_vaccinations(df):
    """
    Plot total vaccinations over time for selected countries.
    """
    plt.figure(figsize=(10, 6))
    for country in df['location'].unique():
        country_data = df[df['location'] == country]
        if 'total_vaccinations' in country_data:
            plt.plot(country_data['date'], country_data['total_vaccinations'], label=country)

    plt.title("Total COVID-19 Vaccinations Over Time")
    plt.xlabel("Date")
    plt.ylabel("Total Vaccinations")
    plt.legend()
    plt.grid()
    plt.show()

# Generate Choropleth Map
def plot_choropleth(df):
    """
    Plot choropleth map of total cases using Plotly Express.
    """
    latest = df[df['date'] == df['date'].max()]
    map_data = latest.groupby('location').agg({
        'total_cases': 'max',
        'population': 'max'
    }).reset_index()
    map_data['cases_per_million'] = map_data['total_cases'] / (map_data['population'] / 1e6)

    iso_codes = {
        'United States': 'USA',
        'India': 'IND',
        'Kenya': 'KEN'
    }
    map_data['iso_code'] = map_data['location'].map(iso_codes)

    fig = px.choropleth(map_data,
                        locations="iso_code",
                        color="cases_per_million",
                        hover_name="location",
                        color_continuous_scale=px.colors.sequential.Plasma,
                        title="COVID-19 Cases per Million by Country")
    fig.show()

# Main function
if __name__ == "__main__":
    # File path to the dataset
    file_path = "owid-covid-data.csv"

    # Load the data
    data = load_data(file_path)

    if data is not None:
        # Explore the data
        explore_data(data)

        # Clean the data
        cleaned_data = clean_data(data)

        # Plot total cases over time
        plot_total_cases(cleaned_data)

        # Plot total deaths over time
        plot_total_deaths(cleaned_data)

        # Plot daily new cases
        plot_new_cases(cleaned_data)

        # Plot vaccination data
        plot_vaccinations(cleaned_data)

        # Plot choropleth map
        plot_choropleth(cleaned_data)
