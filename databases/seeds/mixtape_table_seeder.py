"""MixtapeTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Mixtape import Mixtape

class MixtapeTableSeeder(Seeder):
    def run(self):
        Mixtape.create({
            "title": "Sweatpants @ Night",
            "verse": "Everybody know I like my jeans, but it ain't lean, so I switch to my sweaties",
            "audio": "<soundcloud link>"
            })
        Mixtape.create({
            "title": "4-Eyez",
            "verse": "Checkin my vision, don't need no derision, you in my field of vision, no cap",
            "audio": "<soundcloud link>"
        })
