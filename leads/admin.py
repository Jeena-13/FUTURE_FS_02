from django.contrib import admin
from .models import Lead, LeadNote, FollowUp
class NoteInline(admin.TabularInline):
    model = LeadNote
    extra = 0
class FollowUpInline(admin.TabularInline):
    model = FollowUp
    extra = 0
@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("name","email","company","source","status","updated_at")
    list_filter = ("status","source","created_at")
    search_fields = ("name","email","company")
    inlines = [NoteInline, FollowUpInline]
admin.site.register(LeadNote)
admin.site.register(FollowUp)
