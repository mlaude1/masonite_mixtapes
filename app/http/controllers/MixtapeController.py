""" A MixtapeController Module """

from masonite.controllers import Controller
from masonite.request import Request
from app.Mixtape import Mixtape


class MixtapeController(Controller):
    """Class Docstring Description
    """
    
    def __init__(self, request: Request):
        self.request = request 

    def show(self):
        id = self.request.param("id")
        return Mixtape.find(id)
        

    def index(self):
        return Mixtape.all()

    def create(self):
        title = self.request.input("title")
        verse = self.request.input("verse")
        audio = self.request.input("audio")
        mixtape = Mixtape.create({
            "title": title,
            "verse": verse,
            "audio": audio
            })
        return mixtape


    def update(self):
        title = self.request.input("title")
        verse = self.request.input("verse")
        audio = self.request.input("audio")
        id = self.request.param("id")
        Mixtape.where("id", id).update({
            "title": title,
            "verse": verse,
            "audio": audio
        })
        return Mixtape.where("id", id).get()

    def destroy(self):
        id = self.request.param("id")
        mixtape = Mixtape.where("id", id).get()
        Mixtape.where("id", id).delete()
        return mixtape