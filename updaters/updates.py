from observer import Observer

# Imports below require firestore on device
from google.cloud import firestore
import google.auth

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
    def _setup_creds(self):
        self._key = "./secrets.json"
        self._client = firestore.Client.from_service_account_json(self.key)

    def __init__(self, doc_ref):
        """:arg doc_ref: is the document that should be updated in the firestore"""
        Observer.__init__(self)
        self._doc_ref = doc_ref
        self._key = ""
        self._client = ""
        self._setup_creds()

    def update(self, arg):
       doc_ref = self._client.collection()

    def error(self):
        pass


class SendWaterEmail(Observer):
    """
    Class used to receive a notiftication to send an email about a subject

    """

    def __init__(self):
        Observer.__init__(self)

    def update(self, arg):
        pass

    def error(self):
        pass
