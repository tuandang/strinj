from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Gig, Profile, Purchase, Review, Company
from .forms import GigForm



# Create your views here..
def home(request):
    gigs = Gig.objects.filter(status=True)
    return render(request, 'home.html', {"gigs": gigs})

def gig_detail(request, id):
    if request.method == 'POST' and \
        not request.user.is_anonymous() and \
        Purchase.objects.filter(gig_id=id, buyer=request.user).count() > 0 and \
        'content' in request.POST and \
        request.POST['content'].strip() != '':
        Review.objects.create(content=request.POST['content'], gig_id=id, user=request.user)

    try:
        gig = Gig.objects.get(id=id)
    except Gig.DoesNotExist:
        return redirect('/')

    if request.user.is_anonymous() or \
        Purchase.objects.filter(gig=gig, buyer=request.user).count() == 0 or \
        Review.objects.filter(gig=gig, user=request.user).count() > 0:
        show_post_review = False
    else:
        show_post_review = Purchase.objects.filter(gig=gig, buyer=request.user).count() > 0

    reviews = Review.objects.filter(gig=gig)
    companies = Company.objects.filter(gig=gig)
    return render(request, 'gig_detail.html', {"show_post_review": show_post_review ,"reviews": reviews, "companies": companies, "gig": gig})

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

@login_required(login_url="/")
def profile(request, username):
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
        profile.about = request.POST['about']
        profile.slogan = request.POST['slogan']
        profile.save()
    else:
        try:
            profile = Profile.objects.get(user__username=username)
        except Profile.DoesNotExist:
            return redirect('/')

    gigs = Gig.objects.filter(user=profile.user, status=True)
    return render(request, 'profile.html', {"profile": profile, "gigs": gigs})



@login_required(login_url="/")
def my_sellings(request):
    purchases = Purchase.objects.filter(gig__user=request.user)
    return render(request, 'my_sellings.html', {"purchases": purchases})

@login_required(login_url="/")
def my_buyings(request):
    purchases = Purchase.objects.filter(buyer=request.user)
    return render(request, 'my_buyings.html', {"purchases": purchases})

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
