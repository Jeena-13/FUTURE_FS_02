from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from .forms import LeadForm, NoteForm, FollowUpForm
from .models import Lead, FollowUp
class LoginView(DjangoLoginView):
    template_name = "registration/login.html"
    redirect_authenticated_user = True
@login_required
def dashboard(request):
    qs = Lead.objects.all()
    q = request.GET.get("q","").strip()
    status = request.GET.get("status","")
    if q: qs = qs.filter(Q(name__icontains=q)|Q(email__icontains=q)|Q(company__icontains=q))
    if status in dict(Lead.STATUS_CHOICES): qs = qs.filter(status=status)
    leads = qs
    all_leads = Lead.objects.all()
    stats = {"total": all_leads.count(), "new": all_leads.filter(status="new").count(),
             "contacted": all_leads.filter(status="contacted").count(), "converted": all_leads.filter(status="converted").count()}
    return render(request,"leads/dashboard.html",{"leads":leads,"stats":stats,"q":q,"selected_status":status})
@login_required
def lead_create(request):
    form = LeadForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        lead = form.save(commit=False); lead.owner = request.user; lead.save()
        messages.success(request,"Lead created successfully.")
        return redirect("lead_detail",pk=lead.pk)
    return render(request,"leads/lead_form.html",{"form":form,"heading":"Add a lead","button":"Create lead"})
@login_required
def lead_detail(request,pk):
    lead = get_object_or_404(Lead,pk=pk)
    return render(request,"leads/lead_detail.html",{"lead":lead,"note_form":NoteForm(),"followup_form":FollowUpForm()})
@login_required
def lead_edit(request,pk):
    lead=get_object_or_404(Lead,pk=pk); form=LeadForm(request.POST or None,instance=lead)
    if request.method=="POST" and form.is_valid():
        form.save(); messages.success(request,"Lead updated."); return redirect("lead_detail",pk=lead.pk)
    return render(request,"leads/lead_form.html",{"form":form,"heading":"Edit lead","button":"Save changes"})
@login_required
@require_POST
def lead_delete(request,pk):
    lead=get_object_or_404(Lead,pk=pk); lead.delete()
    messages.success(request,"Lead deleted."); return redirect("dashboard")
@login_required
@require_POST
def note_add(request,pk):
    lead=get_object_or_404(Lead,pk=pk); form=NoteForm(request.POST)
    if form.is_valid():
        note=form.save(commit=False); note.lead=lead; note.created_by=request.user; note.save()
        messages.success(request,"Note added.")
    else: messages.error(request,"Please enter a note.")
    return redirect("lead_detail",pk=pk)
@login_required
@require_POST
def followup_add(request,pk):
    lead=get_object_or_404(Lead,pk=pk); form=FollowUpForm(request.POST)
    if form.is_valid():
        item=form.save(commit=False); item.lead=lead; item.created_by=request.user; item.save()
        messages.success(request,"Follow-up scheduled.")
    else: messages.error(request,"Check the follow-up title and date.")
    return redirect("lead_detail",pk=pk)
@login_required
@require_POST
def followup_complete(request,pk):
    item=get_object_or_404(FollowUp,pk=pk); item.completed=not item.completed; item.save(update_fields=["completed"])
    return redirect("lead_detail",pk=item.lead_id)
@require_POST
def logout_view(request):
    logout(request); return redirect("login")
