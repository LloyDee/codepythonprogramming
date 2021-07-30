import phonenumbers, speedtest
from phonenumbers import carrier, geocoder, timezone



phone_number = phonenumbers.parse('+19562122242')
print("Country State: {}".format(geocoder.description_for_number(phone_number,'en')))
print("Name: {}".format(carrier.name_for_number(phone_number,'en')))
print("Time Zone: {}".format(timezone.time_zones_for_number(phone_number)))

st = speedtest.Speedtest()

print("Download speed is {:.2f} Mbps".format(st.download()/1000000))
print("Upload speed is {:.2f} Mbps".format(st.upload()/1000000))

