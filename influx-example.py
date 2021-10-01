#Import the stuff we need
#pip install influxdb 
from influxdb_client import InfluxDBClient, Point
from datetime import datetime
import pandas as pd
from influxdb_client.client.write_api import SYNCHRONOUS


#Setup database
client = InfluxDBClient(url='http://localhost:8086', token='mH0GWU72y-kEXd0ql7WwzPb54KSCC4DjIqUaVX4UCDhofIWB7IiQ3NXNA4Q6-FfaoQj2E_O8cWIF38kY-CQdpg==', org='org')
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
data = pd.read_csv('./aes2020.csv')
write_client = client.write_api(write_options=SYNCHRONOUS)
query_api = client.query_api()
write_client.write('bucket', 'org', record=data, data_frame_measurement_name='data', data_frame_tag_columns=['flash_id'])

results = query_api.query_data_frame('from(bucket:"bucket") '
                                        '|> range(start: 0) '
                                        '|> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value") '
                                        '|> keep(columns: ["Years", "Units"])')

print(results)
