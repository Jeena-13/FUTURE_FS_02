# Generated initial migration
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models
class Migration(migrations.Migration):
    initial = True
    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]
    operations = [
        migrations.CreateModel(name="Lead", fields=[
            ("id",models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name="ID")),
            ("name",models.CharField(max_length=120)),("email",models.EmailField(max_length=254)),
            ("phone",models.CharField(blank=True,max_length=30)),("company",models.CharField(blank=True,max_length=120)),
            ("source",models.CharField(choices=[("website","Website"),("linkedin","LinkedIn"),("referral","Referral"),("social","Social media"),("other","Other")],default="website",max_length=20)),
            ("status",models.CharField(choices=[("new","New"),("contacted","Contacted"),("converted","Converted")],default="new",max_length=20)),
            ("summary",models.TextField(blank=True)),("created_at",models.DateTimeField(auto_now_add=True)),("updated_at",models.DateTimeField(auto_now=True)),
            ("owner",models.ForeignKey(blank=True,null=True,on_delete=django.db.models.deletion.SET_NULL,related_name="leads",to=settings.AUTH_USER_MODEL)),
        ],options={"ordering":["-updated_at"]}),
        migrations.CreateModel(name="LeadNote", fields=[
            ("id",models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name="ID")),
            ("body",models.TextField()),("created_at",models.DateTimeField(auto_now_add=True)),
            ("created_by",models.ForeignKey(null=True,on_delete=django.db.models.deletion.SET_NULL,to=settings.AUTH_USER_MODEL)),
            ("lead",models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,related_name="notes",to="leads.lead")),
        ],options={"ordering":["-created_at"]}),
        migrations.CreateModel(name="FollowUp", fields=[
            ("id",models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name="ID")),
            ("title",models.CharField(max_length=160)),("due_at",models.DateTimeField()),("completed",models.BooleanField(default=False)),("created_at",models.DateTimeField(auto_now_add=True)),
            ("created_by",models.ForeignKey(null=True,on_delete=django.db.models.deletion.SET_NULL,to=settings.AUTH_USER_MODEL)),
            ("lead",models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,related_name="followups",to="leads.lead")),
        ],options={"ordering":["completed","due_at"]}),
    ]
