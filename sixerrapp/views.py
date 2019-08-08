from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.http import HttpResponse, HttpResponseRedirect 
from django.core.urlresolvers import reverse
from django.utils import timezone


from .models import *
from .forms import *



# Create your views here..
def home(request):
    stories = Story.objects.all()
    jobs = Job.objects.filter(deadline__gte=timezone.now())
    # TODO: Add a filter for jobs 
    return render(request, 'home.html', {"stories": stories, "jobs": jobs})

##### Story related #####

def story_detail(request, id):
    try:
        story = Story.objects.get(id=id)
    except Story.DoesNotExist:
        return redirect('/')

    companies = Company.objects.filter(story=story)
    return render(request, 'story_detail.html', {"companies": companies, "story": story})

@login_required(login_url="/")
def create_story(request):
    error = ''
    if request.method == 'POST':
        story_form = StoryForm(request.POST, request.FILES)
        if story_form.is_valid():
            story = story_form.save(commit=False)
            story.user = request.user
            story.save()
            return redirect('my_stories')
        else:
            error = "Data is not valid"

    story_form = StoryForm()
    return render(request, 'create_story.html', {"error": error})

@login_required(login_url="/")
def edit_story(request, id):
    try:
        story = Story.objects.get(id=id, user=request.user)
        error = ''
        if request.method == 'POST':
            story_form = StoryForm(request.POST, request.FILES, instance=story)
            if story_form.is_valid():
                story.save()
                return redirect('my_stories')
            else:
                error = "Data is not valid"

        return render(request, 'edit_story.html', {"story": story, "error": error})
    except Story.DoesNotExist:
        return redirect('/')

@login_required(login_url="/")
def my_stories(request):
    stories = Story.objects.filter(author=request.user)
    return render(request, 'my_stories.html', {"stories": stories})

##### Profile related ######

@login_required(login_url="/")
def profile(request, username):
    try:
        profile = Profile.objects.get(user=request.user)
    except:
        profile = ""
    if not profile:
        return HttpResponseRedirect(reverse('create_profile'))
    if request.method == 'POST': # if upload/update profile
        profile = Profile.objects.get(user=request.user)
        profile_update = ProfileForm(request.POST, request.FILES, instance=profile)
        if profile_update.is_valid():
            profile_update.save()
        else:
            error = "Data is not valid"
    else:
        try:
            profile = Profile.objects.get(user__username=username)
        except Profile.DoesNotExist:
            return redirect('/')

    stories = Story.objects.filter(author=profile.user)
    return render(request, 'profile.html', {"profile": profile, "stories": stories})

def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profile'))
    else:
        form = ProfileForm()

    return render(request, 'create_profile.html',{'form':form})

def search(request):
    stories = Story.objects.filter(title__contains=request.GET['title'])
    return render(request, 'home.html', {'stories': stories})

def register(request):
    # if sending data to server
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = UserCreationForm()

        args = {'form': form}
        return render(request, 'reg_form.html', args)

##### Company Subscription ######
@login_required(login_url="/")
def register_company(request):
    error = ''
    if request.method == 'POST':
        company_form = CompanyForm(request.POST, request.FILES)
        if company_form.is_valid():
            # TODO: Verify user's relation with company

            # Check if the company is already registered by other users
            profile = Profile.objects.get(user=request.user)
            if Company.objects.filter(title=company_form.cleaned_data['title']).exists():
                # profile.company = Company.objects.filter(title=company_form.cleaned_data['title'])[0]
                # profile.save()
                error = "Company is already registered. The company will be notified" # TODO: pass this error to edit_company
            # Register the company
            else:
                company = company_form.save(commit=False)
                company.save()
                Profile.objects.filter(user=request.user).update(company=company)
                return redirect('edit_company')
        else:
            error = "Data is not valid"
    return render(request, 'register_company.html', {"error": error})

@login_required(login_url="/")
def edit_company(request):
    try:
        company = Profile.objects.get(user=request.user).company
        error = ''
        if request.method == 'POST': # update company info
            company_form = CompanyForm(request.POST, request.FILES, instance=company)
            if company_form.is_valid():
                company_form.save()
                return redirect('edit_company')
            else:
                error = "Data is not valid"
                return render(request, 'edit_company.html', {"error": error})

        # retrieve company info: story, all registered people, jobs
        stories = Story.objects.filter(company=company)
        profiles = Profile.objects.filter(company=company)
        jobs = Job.objects.filter(company=company)
        return render(request, 'edit_company.html', {
            "error": error,
            "company": company, 
            "stories": stories,
            "profiles": profiles,
            "jobs": jobs
            })
    except Company.DoesNotExist: # Need checking
        error = "There is no such company"
        return render(request, 'edit_company.html', {"error": error})

@login_required(login_url="/")
def create_job(request):
    error = ''
    if request.method == 'POST':
        job_form = JobForm(request.POST, request.FILES)
        if job_form.is_valid():
            # Add the job
            job = job_form.save(commit=False)
            job.company = Profile.objects.get(user=request.user).company
            job.save()
            return redirect('edit_company')
        else:
            error = "Data is not valid"
    return render(request, 'create_job.html', {"error": error})

@login_required(login_url="/")
def edit_job(request, id):
    try:
        job = Job.objects.get(id=id)
        if job.company != Profile.objects.get(user=request.user).company:
            error = 'You do not have access to view this job'
            return render(request, 'edit_job.html', {"job": job, "error": error})
        error = ''
        if request.method == 'POST':
            job_form = JobForm(request.POST, request.FILES, instance=job)
            if job_form.is_valid():
                job.save()
                return redirect('edit_company')
            else:
                error = "Data is not valid"

        return render(request, 'edit_job.html', {"job": job, "error": error})
    except Job.DoesNotExist:
        return redirect('/')

@login_required(login_url="/")
def view_job(request, id):
    try:
        job = Job.objects.get(id=id)
        error = ''
        return render(request, 'view_job.html', {"job": job, "error": error})
    except Job.DoesNotExist:
        return redirect('/')

@login_required(login_url="/")
def create_feedback(request):
    error = ''
    if request.method == 'POST':
        feedback_form = FeedbackForm(request.POST, request.FILES)
        if feedback_form.is_valid():
            # print("Valid")
            feedback = feedback_form.save(commit=False)
            # feedback.user = request.user
            feedback.save()
            return render(request, 'create_feedback.html', {"success": True})
        else:
            error = "Data is not valid"

    feedback_form = FeedbackForm()
    return render(request, 'create_feedback.html', {"error": error})

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None



