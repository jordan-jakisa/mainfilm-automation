from django.db import models


# Create your models here.
class Email(models.Model):
    from_name = models.TextField()
    from_email = models.EmailField()
    subject = models.TextField()
    body = models.TextField()
    sent_at = models.DateTimeField()
    message_id = models.TextField()

    # status can be received, processed, contacted
    status = models.TextField()
