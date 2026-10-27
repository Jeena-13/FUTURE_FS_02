from django.conf import settings
from django.db import models
class Lead(models.Model):
    STATUS_CHOICES = [("new","New"),("contacted","Contacted"),("converted","Converted")]
    SOURCE_CHOICES = [("website","Website"),("linkedin","LinkedIn"),("referral","Referral"),("social","Social media"),("other","Other")]
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    company = models.CharField(max_length=120, blank=True)
    source = models.CharField(max_length=20, choices=SOURCE_CHOICES, default="website")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="new")
    summary = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="leads")
    class Meta:
        ordering = ["-updated_at"]
    def __str__(self): return f"{self.name} ({self.email})"
class LeadNote(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name="notes")
    body = models.TextField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta: ordering = ["-created_at"]
    def __str__(self): return f"Note for {self.lead.name}"
class FollowUp(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name="followups")
    title = models.CharField(max_length=160)
    due_at = models.DateTimeField()
    completed = models.BooleanField(default=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta: ordering = ["completed", "due_at"]
    def __str__(self): return self.title
