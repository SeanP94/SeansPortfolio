from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tasks(models.Model):
    name = models.CharField(max_length=256, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task_author')
    createdon = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        ordering = ('-createdon',)
    
    def __str__(self):
        return self.name