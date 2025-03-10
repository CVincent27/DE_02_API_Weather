from datetime import datetime, timedelta
import pandas as pd


def weather_data_cleaning():
    df = pd.read_csv("data_csv/weather_data.csv")
    sunrise_times = []
    sunset_times = []
    timezones = []

    for col in df.itertuples(index=False):
        sunrise_utc = col.sunrise
        sunset_utc = col.sunset
        timezone_shift = col.timezone
        timezones.append(timezone_shift // 3600)

        # Transfo UTC en heure locale
        sunrise_utc = datetime.fromtimestamp(sunrise_utc)
        sunset_utc = datetime.fromtimestamp(sunset_utc)

        # decal horaire
        sunrise_local = sunrise_utc + timedelta(seconds=timezone_shift)
        sunset_local = sunset_utc + timedelta(seconds=timezone_shift)

        sunrise_times.append(sunrise_local.strftime('%H:%M'))
        sunset_times.append(sunset_local.strftime('%H:%M'))

    df['utc'] = timezones
    df['sunrise_time'] = sunrise_times
    df['sunset_time'] = sunset_times
    df.to_csv("data_csv/weather_data.csv", index=False)

if __name__ == "__main__":
    weather_data_cleaning()