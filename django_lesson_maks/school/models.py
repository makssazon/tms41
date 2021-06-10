from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Student(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    group = models.ForeignKey(Group, null=False, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.firstname
