"""
import soil_tempatures
import soil_moisture_measurment
import time
import psycopg2
import datetime
import ambient_sensor
import water_plant
#import GPIO

tom_plant_1_moist = 0
tom_plant_0_moist = 0

def get_soil_temp_tom_0():
    return soil_tempatures.get_tempature_tomato_zero()

def get_soil_temp_tom_1():
    return soil_tempatures.get_tempature_tomato_one()

def get_soil_moisture_tom0():
    '''returns the soil moisture' of tomato plant 0'''
    return soil_moisture_measurment.get_values(4, 1)

def get_soil_moisture_tom1():
    '''returns the soil moisture' of tomato plant 1'''
    return soil_moisture_measurment.get_values(4, 0)

def water_if_needed(plant_reading, plant_num):
    '''waters which ever plant needs water takes readings from moisture sensors'''
    if (plant_reading <= 1100):
        #print ("return 1 and value of plant reading: ", plant_reading)
        water_plant.water(plant_num)
        return 1 #function that will water the plant
    else:
        #print ("return 0 and value of plant reading: ", plant_reading)
        return 0

def get_ambient_r_data():
    '''Gets the ambient sensor from BME200 sensor located in box'''
    print (ambient_sensor.get_temp())
    print (ambient_sensor.get_humidity())
    print (ambient_sensor.get_pressure())

def submit_to_database():
    '''add all the relivant data into the database'''
    con = psycopg2.connect(dbname="Tomato_Growth", user="tomatopi", password="68Uk%&*SLiaUSb0tLu", host="db.cooper.coop")
    now = datetime.datetime.now()
    cur = con.cursor()

    #cur.execute( """#INSERT INTO tomato_plant_sensors_values (date, soil_tempature_tom0,
     #ambient_humidity,ambient_tempature,
     #watered_stat_tom1,watered_stat_tom0,
    #  soil_tempature_tom1,ambient_pressure) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);""", (now.strftime("%Y-%m-%d %H:%M:%S"),get_soil_temp_tom_0(),ambient_sensor.get_humidity(),ambient_sensor.get_temp(),water_if_needed(get_soil_moisture_tom1(),1),water_if_needed(get_soil_moisture_tom0(),0),get_soil_moisture_tom1(),get_soil_moisture_tom0(),get_soil_temp_tom_1(),ambient_sensor.get_pressure()))
    #con.commit()
    #con.close()

#submit_to_database()

#while(True):
#   submit_to_database()
#  time.sleep(600)
"""