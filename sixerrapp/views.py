from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import *
from .forms import *



# Create your views here..
def home(request):
    gigs = Gig.objects.filter(status=True)
    return render(request, 'home.html', {"gigs": gigs})

##### Gig related #####

def gig_detail(request, id):
    try:
        gig = Gig.objects.get(id=id)
    except Gig.DoesNotExist:
        return redirect('/')



    companies = Company.objects.filter(gig=gig)
    return render(request, 'gig_detail.html', {"companies": companies, "gig": gig})

@login_required(login_url="/")
def create_gig(request):
    error = ''
    if request.method == 'POST':
        gig_form = GigForm(request.POST, request.FILES)
        if gig_form.is_valid():
            gig = gig_form.save(commit=False)
            gig.user = request.user
            gig.save()
            return redirect('my_gigs')
        else:
            error = "Data is not valid"

    gig_form = GigForm()
    return render(request, 'create_gig.html', {"error": error})

@login_required(login_url="/")
def edit_gig(request, id):
    try:
        gig = Gig.objects.get(id=id, user=request.user)
        error = ''
        if request.method == 'POST':
            gig_form = GigForm(request.POST, request.FILES, instance=gig)
            if gig_form.is_valid():
                gig.save()
                return redirect('my_gigs')
            else:
                error = "Data is not valid"

        return render(request, 'edit_gig.html', {"gig": gig, "error": error})
    except Gig.DoesNotExist:
        return redirect('/')

@login_required(login_url="/")
def my_gigs(request):
    gigs = Gig.objects.filter(user=request.user)
    return render(request, 'my_gigs.html', {"gigs": gigs})

##### Profile related ######

@login_required(login_url="/")
def profile(request, username):
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

    gigs = Gig.objects.filter(user=profile.user, status=True)
    return render(request, 'profile.html', {"profile": profile, "gigs": gigs})

def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('created'))
    else:
        form = ProfileForm()

    return render(request, 'profile.html',{'form':form})

def category(request, link):
    categories = {
        "graphics-design": "GD",
        "digital-marketing": "DM",
        "video-animation": "VA",
        "music-audio": "MA",
        "programming-tech": "PT"
    }
    try:
        gigs = Gig.objects.filter(category=categories[link])
        return render(request, 'home.html', {"gigs": gigs})
    except KeyError:
        return redirect('home')

def search(request):
    gigs = Gig.objects.filter(title__contains=request.GET['title'])
    return render(request, 'home.html', {'gigs': gigs})

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
            # profile = Profile.objects.get(user=request.user)

            # Register the company
            company = company_form.save(commit=False)
            # profile.company = company
            company.save()
            # profile.save()
            # print(profile)
            # print(profile.company)
            Profile.objects.filter(user=request.user).update(company=company)
            return redirect('edit_company')
        else:
            error = "Data is not valid"
    return render(request, 'register_company.html', {"error": error})

# TODO:
@login_required(login_url="/")
def edit_company(request):
    try:
        profile = Profile.objects.get(user=request.user)
        company = profile.company
        error = ''
        if request.method == 'POST':
            company_form = CompanyForm(request.POST, request.FILES, instance=company)
            if company_form.is_valid():
                company.save()
                return redirect('edit_company')
            else:
                error = "Data is not valid"

        return render(request, 'edit_company.html', {"error": error})
    except Company.DoesNotExist:
        return redirect('/') # TODO

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None



