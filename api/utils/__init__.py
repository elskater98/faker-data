from datetime import datetime, timedelta

import numpy as np
import pandas as pd

from api.utils.faker_singleton import SingletonFaker

s = SingletonFaker()


def simulate_day_temperature(start_date, days, interval=5, base_temp=20, daily_variation=10, trend_increase=0.05,
                             ):
    """
    Simulate temperatures for each second in a number of days, with an overall increasing trend.

    Parameters:
    - start_date: str, starting date in the format 'YYYY-MM-DD HH:MM:SS'
    - days: int, number of days to simulate
    - interval: int, time interval between measurements in seconds
    - base_temp: float, base temperature around which daily variations occur
    - daily_variation: float, amplitude of daily temperature variation
    - trend_increase: float, daily temperature increase
    - noise_level: float, standard deviation of the noise

    Returns:
    - temperatures: list of float, generated temperatures
    - times: list of str, corresponding timestamps in 'YYYY-MM-DD HH:MM:SS' format
    """
    total_seconds = days * 24 * 60 * 60  # Total time in seconds
    measurements = total_seconds // interval  # Number of measurements

    # Generate time points
    if isinstance(start_date, str):
        start_datetime = datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S')
    else:
        start_datetime = start_date

    times = [start_datetime + timedelta(seconds=i * interval) for i in range(measurements)]

    # Daily temperature variation (sinusoidal)
    daily_variation_pattern = daily_variation * np.sin(2 * np.pi * np.arange(measurements) / (24 * 60 * 60 / interval))

    # Overall increasing trend
    trend = base_temp + trend_increase * (np.arange(measurements) / (24 * 60 * 60 / interval))

    # Combined temperature
    temperatures = trend + daily_variation_pattern

    # Format times to 'YYYY-MM-DD HH:MM:SS'
    formatted_times = [time.strftime('%Y-%m-%d %H:%M:%S') for time in times]

    return pd.DataFrame({'collected_dt': formatted_times, 'temperature': temperatures})


def simulate_energy_consumption(start_date, days, interval=3600, day_consumption=8, night_consumption=3):
    """
    Simulate energy consumption over multiple days, with higher consumption during the day and lower consumption at night.

    Parameters:
    - start_date: str, starting date in the format 'YYYY-MM-DD HH:MM:SS'
    - days: int, number of days to simulate
    - interval: int, time interval between measurements in seconds
    - day_consumption: float, average energy consumption during the day
    - night_consumption: float, average energy consumption at night
    - noise_level: float, standard deviation of the noise

    Returns:
    - df: pd.DataFrame, DataFrame with datetime and corresponding energy consumption values
    """
    total_seconds = days * 24 * 60 * 60  # Total time in seconds
    measurements = total_seconds // interval  # Number of measurements
    start_datetime = pd.to_datetime(start_date)
    times = pd.date_range(start=start_datetime, periods=measurements, freq=f'{interval}s')

    # Daytime energy consumption (higher values)
    day_consumption_pattern = day_consumption * (
            np.sin(2 * np.pi * np.arange(measurements) / (24 * 60 * 60 / interval)) + 1)

    # Nighttime energy consumption (lower values)
    night_consumption_pattern = night_consumption * (
            np.cos(2 * np.pi * np.arange(measurements) / (24 * 60 * 60 / interval)) + 1)

    # Combined energy consumption with noise
    consumption = day_consumption_pattern + night_consumption_pattern

    # Create DataFrame
    df = pd.DataFrame({'collected_dt': times, 'energy_consumption': consumption})

    return df


def add_noise(df, column_name, noise_level=2):
    """
    Add random noise to the specified column of a DataFrame.

    Parameters:
    - df: pd.DataFrame, input DataFrame
    - column_name: str, name of the column to which noise will be added
    - noise_level: float, standard deviation of the noise to be added

    Returns:
    - df_noisy: pd.DataFrame, DataFrame with noise added to the specified column
    """
    df_noisy = df.copy()
    noise = np.random.normal(0, noise_level, len(df))
    df_noisy[column_name] += noise
    return df_noisy


def add_random_nulls(df, column_name, null_probability=0.01):
    """
    Add random null values to the specified column of a DataFrame.

    Parameters:
    - df: pd.DataFrame, input DataFrame
    - column_name: str, name of the column to which null values will be added
    - null_probability: float, probability of a value being set to null

    Returns:
    - df_with_nulls: pd.DataFrame, DataFrame with null values added to the specified column
    """
    df_with_nulls = df.copy()
    mask = np.random.rand(len(df)) < null_probability
    df_with_nulls.loc[mask, column_name] = np.nan
    return df_with_nulls



def check_provider():pass

def get_provider_value(s: SingletonFaker, value, extra_params):
    # TODO: VALIDATE PROVIDERS USING
    # if hasattr(s.faker, value):
    fn = getattr(s.faker, value)
    return fn(**extra_params) if extra_params else fn()
    # else:
    #     return None
        # raise NotImplemented(f"Provider value not implemented {value}")


def generate_custom_value(fields: dict):
    record = {}
    for k, v in fields.items():
        record.update({k: get_provider_value(s=s, value=v.get('method'), extra_params=v.get('extra_params'))})
    return record
