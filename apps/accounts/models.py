import os
from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image


# Create your models here.
def get_file_path(instance, filename):
    ext = filename.split(".")[-1]
    # get filename
    if instance.username and instance.id:
        filename = "{}_{}.{}".format(instance.username, instance.id, ext)
        print("filename", filename)
    else:
        # set filename as random string
        filename = "{}.{}".format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join("profile_pics", filename)


class User(AbstractUser):
    avatar = models.ImageField(
        default="defaults/default_profile.png", upload_to=get_file_path
    )

    def __str__(self):
        return f"{self.username} Profile"

    def save(self, *args, **kwargs):
        super().save()  # saving image first

        img = Image.open(self.avatar.path)  # Open image using self

        if img.height > 300 or img.width > 300:
            new_img = (300, 300)
            img.thumbnail(new_img)
            img.save(self.avatar.path)  # saving image at the same path
