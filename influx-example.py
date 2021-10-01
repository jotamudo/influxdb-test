#Import the stuff we need
#pip install influxdb 
from influxdb_client import InfluxDBClient, Point
from datetime import datetime
import pandas as pd


#Setup database
client = InfluxDBClient(url='localhost:8086', token='Zk3TVEXLNN_MLHaKyqM36mUPL7eaAkWcvRZOQVNH-jgM1usJwWWKG486xuWdejbOOlg22Snl7tJKwoQu2NNzBQ==', org='org')
# client.create_database('mydb')
# client.get_list_database()
# client.switch_database('mydb')


#Setup Payload
json_payload = []
data = {
    "measurement": "stocks",
    "tags": {
        "ticker": "TSLA" 
        },
    "time": datetime.now(),
    "fields": {
        'open': 688.37,
        'close': 667.93
    }
}
json_payload.append(data)
data = pd.read_csv('./flash_2019_2_24_1.csv')
write_client = client.write_api()
write_client.write('bucket', 'org', record=data, data_frame_measurement_name='data',
                   data_frame_tag_columns=['flash_id']
                   )

#Send our payload


# Select statement

