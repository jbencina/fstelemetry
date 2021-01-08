from SimConnect import AircraftRequests, SimConnect
import csv
import os
import time

class Telemetry():
    def __init__(self, keys):
        self.requests = self._make_connection()
        self.keys = keys

    def _make_connection(self):
        sm = SimConnect()
        return AircraftRequests(sm, _time=0)

    def get_data(self):
        d = {}
        d['time'] = time.time()

        for k in self.keys:
            d[k] = self.requests.get(k)
            
        return d

    def write_log(self, data, path):
        fieldnames = [k for k in data]
        exists = os.path.exists(path)

        with open(path, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if not exists:
                writer.writeheader()

            writer.writerow(data)
        
    def listen(self, path, interval=1.0):
        print(f'Listening for FS events with {interval} second delay')

        while True:
            data = self.get_data()
            self.write_log(data, path)
            print(f'Logged event at {data["time"]}')
            time.sleep(interval)