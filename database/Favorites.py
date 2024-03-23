from database.Client import Client


class Favorites:

    def __init__(self):
        super().__init__()
        client = Client().create_client()
        db = client.stock
        global favorites
        favorites = db.favorites

    def add_to_favorites(self,stock):
        favorites.insert_one({"symbol": stock})

    def get_favorites(self):
        return favorites.find()




