from meteostat import Point, Hourly
from datetime import datetime

# JFK Airport
location = Point(40.6413, -73.7781)

# Convert ISO string to timezone-naive datetime
utc_time = datetime.fromisoformat("2025-08-01 14:00:00+00:00").replace(tzinfo=None)

# Round to exact hour
utc_hour = utc_time.replace(minute=0, second=0, microsecond=0)
print(utc_hour.hour)
# Fetch weather
df = Hourly(location, utc_hour, utc_hour).fetch()
row = df.iloc[0]  # First (and only) row for the hour
value = {
        "temp": row["temp"],
        "rhum": row["rhum"],
        "prcp": row["prcp"],
        "wspd": row["wspd"],
        "coco": row["coco"]
    }
value = {k: float(v) for k, v in value.items()}
print(value)