from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    username = models.CharField(max_length=128, unique=True,
                                help_text=(
                                    "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
                                ),
                                error_messages={
                                    "unique": ("A user with that username already exists."),
                                },
                                )
    full_name = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=13)
    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username