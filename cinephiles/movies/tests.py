from django.test import TestCase
from .models import * 
# Create your tests here.

class GenreTestCase(TestCase):
    def test_genre_creation(self):
        genre = Genre.objects.create(name="Action")
        self.assertEqual(genre.name, "Action")

    def test_genre_str_representation(self):
        genre = Genre.objects.create(name="Comedy")
        self.assertEqual(str(genre), "Comedy")

class ActorTestCase(TestCase):
    def test_actor_creation(self):
        actor = Actor.objects.create(name="Tom Hanks")
        self.assertEqual(actor.name, "Tom Hanks")

    def test_actor_str_representation(self):
        actor = Actor.objects.create(name="Leonardo DiCaprio")
        self.assertEqual(str(actor), "Leonardo DiCaprio")