from django.db import models


# Create your models here.
class Todo(models.Model):
    TODO = 'Todo'
    DONE = 'Done'

    STATUS_CHOICE = (
        (TODO, 'Todo'),
        (DONE, 'Done')
    )
    description = models.CharField(max_length=255)
    status = models.CharField(choices=STATUS_CHOICE, default=TODO, max_length=255)
    created = models.DateTimeField(auto_now_add=True)
