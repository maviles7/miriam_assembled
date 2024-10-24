from django.db import models

class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    image = models.URLField(max_length=500)
    deploy_link = models.URLField(max_length=500)
    github_link = models.URLField(max_length=500)

    def __str__(self):
        return self.title

class Engineer(models.Model):
    name = models.CharField(max_length=100)
    linkedin = models.URLField(max_length=500)
    github = models.URLField(max_length=500)
    resume = models.URLField(max_length=500)
    bio = models.TextField(max_length=500)

    def __str__(self):
        return self.name