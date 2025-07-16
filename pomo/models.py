from django.db import models

# Create your models here.
class Pomo(models.Model):
    time = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pomo #{self.id} {self.created.strftime('%Y/%m/%d %H:%M')}"