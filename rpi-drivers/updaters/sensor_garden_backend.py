from sensors_observers import Observer
import json
import requests

class UpdateSensorGardenBackend(Observer):

    def __init__(self):
        Observer.__init__(self)
        self.auth_header = "AUTH-HEADER"
        self.auth_value = "TEMP I think"
        self.update_url = "https://sgb.cooperkyle.com/sendData"

    def update(self, arg, opts, kwarg_opts):
        headers = {self.auth_header: self.auth_value}
        print(f"received values to update {opts}")
        data = {
                "measurment": kwarg_opts["measurement_precise"],
                "sensorName": kwarg_opts["common_name"],
                "id": kwarg_opts["sensor_id"],
                "unit": kwarg_opts["units_of_measure"]
                }
        requests.post(self.update_url, data=data, headers=headers)

    def error(self):
        pass
