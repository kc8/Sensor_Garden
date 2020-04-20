from sensors_observers import Observer

# Imports below require firestore on device
from google.cloud import firestore
#import google.auth

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
    #def _setup_creds(self):
    #    self._key = "./secrets.json"
    #    self._client = firestore.Client.from_service_account_json(self.key)

    def __init__(self):
        """:arg doc_ref: is the document that should be updated in the firestore"""
        Observer.__init__(self)
        #self._doc_ref = doc_ref
        self._key = ""
        self._client = ""
 #       self._setup_creds()

    def update(self, arg, opts):
        print("updating")
        data = {
            opts: arg
        }

#        self._client.collection("tom_plant_sensor_reading").document("readings").set(data)

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
