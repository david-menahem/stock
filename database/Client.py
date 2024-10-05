from pymongo import MongoClient


class Client:
    def __init__(self):
        super().__init__()

    def create_client(self):
        MONOGODB_URI = "mongodb+srv://dvmena39:dvmena39@cluster0.blbhpmi.mongodb.net/?retryWrites=true&w=majority"
        client = MongoClient(MONOGODB_URI)
        return client
