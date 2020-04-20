from observer import Observer

class UpdateFirestore(Observer):

    def __init__(self):
        Observer.__init__(self)

    def update(self, arg):
        print(arg)

    def error(self):
        pass
