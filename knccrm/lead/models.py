from django.db import models
from django.contrib.auth.models import User



class Lead(models.Model):
    LOW='low'
    MEDIUM='medium'
    HIGH='high'
    
    LEAD_PRIORITY_CHOICES = (
        (LOW, 'Low'),
        (MEDIUM,'Medium'),
        (HIGH,'High')
        )
    
    
    NEW = 'new'
    CONTACTED = 'contacted'
    WON = 'won'
    LOST = 'lost'

    STATUS_CHOICES = (
        (NEW, 'New'),
        (CONTACTED, 'Contacted'),
        (WON, 'Won'),
        (LOST, 'Lost'),
    )

    
    
    priority=models.CharField(max_length=10, choices=LEAD_PRIORITY_CHOICES, default='medium')
    created_by = models.ForeignKey(User, related_name='leads', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    company = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    converted_to_clients=models.BooleanField(default=False)
    assigned_to = models.ForeignKey(User, related_name='assigned_leads', on_delete=models.SET_NULL, null=True, blank=True)
    notes = models.TextField(blank=True)
    
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

