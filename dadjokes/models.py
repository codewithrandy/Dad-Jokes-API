from django.db import models
import uuid

class DadJoke(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False)
    category = models.CharField(max_length=75)
    setup = models.CharField(max_length=500)
    punchline = models.CharField(max_length=500)