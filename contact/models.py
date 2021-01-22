from django.db import models


# Create your models here.

class Contact(models.Model):
    """
    A contact model to provide mechanism for
    end user to raise queries with store admins
    """
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    subject = models.CharField(max_length=80, null=True, blank=True)
    message = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.full_name
