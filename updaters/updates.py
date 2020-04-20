from observer import Observer


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

    def __init__(self):
        Observer.__init__(self)

    def update(self, arg):
        print(arg)

    def error(self):
        pass
