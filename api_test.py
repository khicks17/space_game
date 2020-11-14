import moonphase_client

API = '55417ad6908c4d9484a153318201211'
location = 'Annapolis'

my_client = moonphase_client.WeatherClient(API)
current_moonphase = my_client.get_moonphase(location)
print(current_moonphase)

if current_moonphase == 'New Moon':
    print('yes its a New Moon')

if current_moonphase == 'Waxing Crescent':
    print('yes its a waxing crescent')

if current_moonphase == 'First Quarter':
    print('yes its a first quarter')

if current_moonphase == 'Waxing Gibbous':
    print('yes its a waxing gibbous')

if current_moonphase == 'Full Moon':
    print('yes its a full moon')

if current_moonphase == 'Waning Gibbous':
    print('yes its a waning gibbous')

if current_moonphase == 'Last Quarter':
    print('yes its a last quarter')

if current_moonphase == 'Waning Crescent':
    print('yes its a waning crescent')