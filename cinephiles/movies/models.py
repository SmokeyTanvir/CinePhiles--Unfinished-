from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Actor(models.Model):
    name = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True)
    release_date = models.DateField()
    duration = models.PositiveIntegerField()  # Duration in minutes
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    genres = models.ManyToManyField(Genre)
    description = models.TextField()
    trailer_link = models.URLField(null=True)
    downloadable_links = models.JSONField(null=True)  # Storing links as JSON
    cast = models.ManyToManyField(Actor, through='Role')  # Use a through model for the role of actors

    def __str__(self):
        return self.title

class Role(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    role_name = models.CharField(max_length=100)  # Name of the role played by the actor

    def __str__(self):
        return f"{self.actor.name} as {self.role_name} in {self.movie.title}"

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=100)
    rating = models.PositiveIntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"Review for {self.movie.title} by {self.reviewer_name}"
