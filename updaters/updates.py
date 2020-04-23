from sensors_observers import Observer

# Imports below require firestore on device
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class UpdatePostgres(Observer):

    def __init__(self):
        Observer.__init__(self)

    def update(self, arg):
        print(arg)

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

    def update(self, arg, opts):
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

    def update(self, vale, opts=None):
        pass

    def error(self):
        pass
