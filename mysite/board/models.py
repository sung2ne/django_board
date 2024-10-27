from django.db import models

class Board(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    password = models.CharField(max_length=20)
    created_by = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'board'
        verbose_name = 'board'
        verbose_name_plural = 'boards'
        ordering = ['-created_at']

    def __str__(self):
        return self.title
