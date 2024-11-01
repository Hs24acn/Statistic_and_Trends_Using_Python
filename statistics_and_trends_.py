# Importing Libraries

import pandas as pd
import matplotlib.pyplot as plt


def plot_wind_energy_comparison(countries, start_year=None, end_year=None):
    """
    Plots a line chart comparing electricity production from wind energy between three specified countries
    over a given period.

    Parameters:
    countries (list): List of three country names to compare.
    start_year (int, optional): The start year for the plot (inclusive).
    end_year (int, optional): The end year for the plot (inclusive).

    Returns:
    None
    """
    # Filter data for the specified countries
    country_data = data[data['Entity'].isin(countries)]

    # Filter by the specified year range, if provided
    if start_year and end_year:
        country_data = country_data[(country_data['Year'] >= start_year) & (
            country_data['Year'] <= end_year)]

    # Plotting
    plt.figure(figsize=(12, 8))
    for country in countries:
        country_wind_data = country_data[country_data['Entity'] == country]
        plt.plot(
            country_wind_data['Year'],
            country_wind_data['Electricity from wind - TWh'],
            marker='o',
            label=country)

    # Graph styling
    plt.title('Electricity Production from Wind Energy Comparison')
    plt.xlabel('Year')
    plt.ylabel('Electricity from Wind (TWh)')
    plt.legend(title='Country')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Define the function to create the bar chart


def plot_renewable_energy_usa_2015(filtered_data):
    """
    Plots a bar chart showing the renewable energy consumption by source for a filtered dataset (USA, 2015).

    Parameters:
    filtered_data (DataFrame): Filtered DataFrame for the USA in 2015

    Returns:
    None
    """
    # Define renewable energy sources
    energy_sources = [
        'Electricity from wind - TWh',
        'Electricity from hydro - TWh',
        'Electricity from solar - TWh',
        'Other renewables including bioenergy - TWh']

    # Extract values for each energy source
    energy_values = filtered_data[energy_sources].values.flatten()

    # Define colors for each bar
    colors = ['skyblue', 'lightgreen', 'salmon', 'gold']

    # Plotting
    plt.figure(figsize=(10, 6))
    bars = plt.bar(energy_sources, energy_values, color=colors)
    plt.title('Renewable Energy Consumption in USA (2015)')
    plt.xlabel('Energy Source')
    plt.ylabel('Electricity (TWh)')
    plt.xticks(rotation=45)

    # Display the values on top of each bar
    for bar, value in zip(bars, energy_values):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5,
                 f'{value:.2f}', ha='center', va='bottom')

    plt.tight_layout()
    plt.show()


def plot_country_comparison_boxplot(countries, start_year, end_year):
    """
    Plots a box plot showing the distribution of renewable energy sources across specified countries
    for a given decade.

    Parameters:
    countries (list): List of country names to include in the comparison.
    start_year (int): The start year of the decade range.
    end_year (int): The end year of the decade range.

    Returns:
    None
    """
    # Filter data for the specified countries and decade range
    decade_data = data[(data['Entity'].isin(countries)) &
                       (data['Year'] >= start_year) &
                       (data['Year'] <= end_year)]

    # Define renewable energy sources
    energy_sources = [
        'Electricity from wind - TWh',
        'Electricity from hydro - TWh',
        'Electricity from solar - TWh',
        'Other renewables including bioenergy - TWh']

    # Set up the plot
    plt.figure(figsize=(15, 10))

    # Plot each energy source as a subplot
    for i, source in enumerate(energy_sources, 1):
        plt.subplot(2, 2, i)

        # Prepare data for box plot
        country_data = [decade_data[decade_data['Entity'] ==
                                    country][source].dropna() for country in countries]

        # Create box plot
        plt.boxplot(country_data, labels=countries, patch_artist=True)
        plt.title(
            f'Distribution of {source} among Countries ({start_year}-{end_year})')
        plt.xlabel('Country')
        plt.ylabel('Electricity (TWh)')

    plt.tight_layout()
    plt.show()

# Importing the Dataset"""


data = pd.read_csv('/content/drive/MyDrive/Datasets/modern-renewable-prod.csv')

data.head()
# Display the updated DataFrame structure


# Drop the 'Code' column from the dataset
data = data.drop(columns=['Code'])
data.head()

# Comparing three countries
plot_wind_energy_comparison(
    ['China', 'United States', 'India'], start_year=2000, end_year=2020)


# Filter data for USA in the year 2015
usa_data_2015 = data[(data['Entity'] == 'United States')
                     & (data['Year'] == 2015)]
# Call the function with the filtered data
plot_renewable_energy_usa_2015(usa_data_2015)


# comparing renewable energy sources from 2010 to 2020 for selected countries
plot_country_comparison_boxplot(
    ['United States', 'China', 'India', 'Germany', 'Brazil'], 2010, 2020)
