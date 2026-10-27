from django.contrib import admin
from django.urls import path
from leads import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("", views.dashboard, name="dashboard"),
    path("leads/create/", views.lead_create, name="lead_create"),
    path("leads/<int:pk>/", views.lead_detail, name="lead_detail"),
    path("leads/<int:pk>/edit/", views.lead_edit, name="lead_edit"),
    path("leads/<int:pk>/delete/", views.lead_delete, name="lead_delete"),
    path("leads/<int:pk>/notes/add/", views.note_add, name="note_add"),
    path("leads/<int:pk>/followups/add/", views.followup_add, name="followup_add"),
    path("followups/<int:pk>/complete/", views.followup_complete, name="followup_complete"),
]
