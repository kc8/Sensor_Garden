from sensors_observers import Observer
# Imports below require firestore on device
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud import pubsub_v1
import json
# Imports for time series DB
from .time_series_db.models import Readings
from .time_series_db.engine import session

class UpdatePostgres(Observer):

    def __init__(self):
        Observer.__init__(self)

    def update(self, arg, opt=None, kwarg_opts=None):
        pass
        # data = Readings(
        #     soil_temperature_1 =
        #     soil_temperature_2 =
        #     soil_moisture_1 =
        #     soil_moisture_2 =
        #     ambient_temperature =
        #     ambient_humidity =
        #     ambient_pressure =
        # )
        # session.add(data)
        # session.commit()

    def error(self):
        pass



class UpdateFirestoreFilteredData(Observer):
    """
        Updates Firebase Firestore when there is a change detected.
    """
    def _setup_creds(self, _key="/home/pi/sensor_garden/tom_project_2020/secrets.json"):
        _cred = credentials.Certificate(_key)
        firebase_admin.initialize_app(_cred, name="update_filter")
        self._db = firestore.client()

    def __init__(self):
        """:arg doc_ref: is the document that should be updated in the firestore"""
        Observer.__init__(self)
        #self._doc_ref = doc_ref
        self._key = ""
        self._client = ""
        self._db  = ""
        self._setup_creds()
        self._doc_ref = self._db.collection("tom_plant_sensor_readings")

    def update(self, arg, opts=None, kwarg_opts=None):
        doc_to_update = self._doc_ref.document(opts)
        doc_to_update.set(kwarg_opts)

    def error(self):
        pass


class UpdateFirestore(Observer):
    """
        Updates Firebase Firestore when there is a change detected.
    """
    def _setup_creds(self, _key="/home/pi/sensor_garden/tom_project_2020/secrets.json"):
        _cred = credentials.Certificate(_key)
        firebase_admin.initialize_app(_cred)
        self._db = firestore.client()

    def __init__(self):
        """:arg doc_ref: is the document that should be updated in the firestore"""
        Observer.__init__(self)
        #self._doc_ref = doc_ref
        self._key = ""
        self._client = ""
        self._db  = ""
        self._setup_creds()
        self._doc_ref = self._db.collection("tom_plant_sensor_readings").document("readings")

    def update(self, arg, opts=None, kwarg_opts=None):
        print(f"Updating info: {arg} with {opts}") # Replace with logging function to keep track of updates
        self._doc_ref.update({opts:arg})

    def error(self):
        pass


class SendEmail(Observer):
    """
    Class used to receive a notiftication to send an email about a subject

    """

    def __init__(self):
        Observer.__init__(self)

    def update(self, vale, opts=None, kwarg_opts=None):
        pass

    def error(self):
        pass


class GCloudPublisher(Observer):

    def __init__(self, project_id, topic_name):
        Observer.__init__(self)
        self._project_id =  project_id
        self._topic_name = topic_name
        self.publisher = pubsub_v1.PublisherClient()
        self.topic_path = self.publisher.topic_path(project_id, topic_name)

    def update(self, arg, opts=None, kwarg_opts=None):
        data = [opts, arg]
        data = json.dumps(data).encode("utf-8")
        future = self.publisher.publish(
            self.topic_path, data, origin=f"{opts}", username="RpiSensor"
        )

    def error(self):
        pass