from django.db import models

class Experience(models.Model):
    poste = models.CharField(max_length=200, default="")
    description = models.TextField()
    company = models.CharField(max_length=200)
    periode = models.CharField(max_length=200, default="")
    outils = models.TextField(default="")

    def __str__(self):
        return self.poste

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    lieu = models.CharField(max_length=200, default="")
    technologies = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Education(models.Model):
    periode = models.CharField(max_length=200)
    specialite = models.TextField()
    ecole = models.TextField(max_length=200)

    def __str__(self):
        return self.specialite


class Skill(models.Model):
    name = models.CharField(max_length=200)
    level = models.IntegerField()

    def __str__(self):
        return self.name


class Detailproject(models.Model):
    projet = models.ForeignKey(Project, on_delete=models.CASCADE)
    objectifs = models.TextField()
    donnees = models.TextField(default="")
    pretraitement = models.TextField(default="")
    experimentations =models.TextField(default="")
    dossier_images = models.CharField(max_length=200, default="")


    def __str__(self):
        return self.projet.title
