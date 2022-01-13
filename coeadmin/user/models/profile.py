""" Profile Model """

# Django.
from django.db import models

# Utilities
from coeadmin.utils.models import BaseModel


# Create your models here.

class Profile(BaseModel):
    """
    User profile model.
    Public profile of each user.
    """

    user = models.OneToOneField(
        'user.User',
        related_name="profile", 
        on_delete=models.CASCADE
    )

    picture = models.ImageField(
        'profile picture', 
        upload_to = 'user/pictures/',
        blank = True,
        null = True,
        )

    polls = models.IntegerField(default=0) 

    def __str__(self):
        """ Return the user """

        return str(self.user)