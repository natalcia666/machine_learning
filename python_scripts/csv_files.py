import pandas as pd
src_file=pd.read_csv('/home/nblaszczuk/natalia/machine_learning/python_scripts/metero_test_file.csv')
df=pd.read_csv('/home/nblaszczuk/natalia/machine_learning/python_scripts/metero_test_file.csv')

df[['date', 'hours']] = df['time'].str.split(' ', expand=True) #dzieli time na czas i dzien)
del df['time']

temp_data=df
hours = [f'{h}:00' for h in range(24)]

temp_data = temp_data.pivot(
    index='date',
    columns='hours',
    values='temperature'
)

temp_data = temp_data.reindex(columns=hours)

daily_mean = df.groupby('date')[
    [
        'relative_humidity_2m',
        'cloud_cover',
        'wind_speed_10m',
        'wind_direction_10m',
        'pressure_msl'
    ]
].mean()
daily_sum = df.groupby('date')[
    [
        'precipitation'
    ]
].sum()

daily_mean=daily_mean.join(daily_sum)
result = temp_data.join(daily_mean)

result = result.reset_index()
result.to_csv('weather_data.csv', index=False)