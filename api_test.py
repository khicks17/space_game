import moonphase_client

API = '55417ad6908c4d9484a153318201211'
location = 'Annapolis'

my_client = moonphase_client.WeatherClient(API)
current_moonphase = my_client.get_moonphase(location)
print('%d' % current_moonphase)