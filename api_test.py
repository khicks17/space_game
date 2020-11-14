import socket
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

import moonphase_client

API = '55417ad6908c4d9484a153318201211'
location = 'Tokyo'

my_client = moonphase_client.WeatherClient(API)
current_moonphase = my_client.get_moonphase(location)
print(current_moonphase)
