from sense_hat import SenseHat
import time
import datetime
import csv

sense = SenseHat()
# Damn thing's bright as hell
sense.low_light = True

today_object = datetime.datetime.today()
todays_date = today_object.strftime('%Y_%m_%d')
current_time = today_object.strftime('%I:%M%p')
file_name = todays_date + '_data.csv'

def celsiusToFahrenheit(cels):
    fahr = (cels * 1.8) + 32
    return fahr

# Get temperature and convert to Fahrenheit
temp = sense.get_temperature()
temp = celsiusToFahrenheit(temp)
humidity = sense.get_humidity()
# Testing to see if the other ways to get temperature are more accurate
humidity_temp = sense.get_temperature_from_humidity()
humidity_temp = celsiusToFahrenheit(humidity_temp)
pressure_temp = sense.get_temperature_from_pressure()
pressure_temp = celsiusToFahrenheit(pressure_temp)

print (current_time + " " + '%.2f'%(temp) + "F " + '%.2f'%(humidity)+'%')
print("humidity temp is: " + str(humidity_temp))
print("pressure temp is: " + str(pressure_temp))


# This shows the proper way to write the csv so that it will open in excel/libreoffice in two columns
# 'a' refers to append mode
with open (file_name,'a',newline = '') as csvfile:
    my_writer = csv.writer(csvfile, delimiter = ',')
    #my_writer.writerow(['01:14','55.7'])
    #my_writer.writerow(['01:16','56.3'])

    