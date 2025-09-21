from django.db import models

class SignedMessage(models.Model):
    message = models.BinaryField()
    signature = models.BinaryField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"SignedMessage(id={self.id}, created_at={self.created_at})"
