from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .forms import BugRegistrationForm
from .models import Bug

class IndexView(generic.ListView):
    template_name = "Bug/index.html"
    context_object_name = "latest_bug_list"

    def get_queryset(self):
        """Return the last five published bugs."""
        return Bug.objects.order_by("-report_date")[:5]

class ViewBugView(generic.DetailView):
    model = Bug
    template_name = "Bug/view_bug.html"

class ListBugView(generic.ListView):
    template_name = "Bug/list_bug.html"
    context_object_name = "bugs"

    def get_queryset(self):
        """Return all bugs."""
        return Bug.objects.all()
    
def index(request):
    latest_bug_list = Bug.objects.order_by("-report_date")[:5]
    context = {"latest_bug_list": latest_bug_list}
    return render(request, "Bug/index.html", context)

def register_bug(request):
    if request.method == 'POST':
        form = BugRegistrationForm(request.POST)
        if form.is_valid():
            bug = form.save()
            return redirect('view_bug', bug_id=bug.pk)
    else:
        form = BugRegistrationForm()
    
    return render(request, 'register_bug.html', {'form': form})

def view_bug(request, bug_id):
    bug = get_object_or_404(Bug, pk=bug_id)
    return render(request, 'view_bug.html', {'bug': bug})

def list_bug(request):
    bugs = Bug.objects.all()
    return render(request, 'list_bug.html', {'bugs': bugs})


def vote(request, bug_id):
    bug = get_object_or_404(Bug, pk=bug_id)
    try:
        selected_bug_type = request.POST["bug_type"]
    except KeyError:
        return render(
            request,
            "Bug/detail.html",
            {
                "bug": bug,
                "error_message": "You didn't select a bug type.",
            },
        )
    else:
        bug.bug_type = selected_bug_type
        bug.save()
        return HttpResponseRedirect(reverse("Bug:view_bug", args=(bug.id,)))
