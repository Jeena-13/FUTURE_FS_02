from django import forms
from django.utils import timezone
from .models import Lead, LeadNote, FollowUp
class StyledForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.setdefault("class", "field")
class LeadForm(StyledForm):
    class Meta:
        model = Lead
        fields = ["name","email","phone","company","source","status","summary"]
        widgets = {"summary": forms.Textarea(attrs={"rows":3, "placeholder":"Context, requirements, or next steps..."})}
class NoteForm(StyledForm):
    class Meta:
        model = LeadNote
        fields = ["body"]
        widgets = {"body": forms.Textarea(attrs={"rows":3,"placeholder":"Record the conversation or useful context..."})}
class FollowUpForm(StyledForm):
    class Meta:
        model = FollowUp
        fields = ["title","due_at"]
        widgets = {"due_at": forms.DateTimeInput(attrs={"type":"datetime-local"}, format="%Y-%m-%dT%H:%M")}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["due_at"].input_formats = ["%Y-%m-%dT%H:%M"]
