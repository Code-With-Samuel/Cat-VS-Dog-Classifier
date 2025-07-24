from django.db import models

class PredictionHistory(models.Model):
    image = models.ImageField(upload_to='history_images/')
    prediction = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.prediction} at {self.created_at}"
