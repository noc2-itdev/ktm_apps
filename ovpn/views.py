from django.shortcuts import render
from ovpn.models import Team, Member, Route
from .forms import TeamForm

def team_index(request):
    teams = Team.objects.all().order_by('-name')
    context = {
        "teams": teams,
    }
    return render(request, "team_index.html", context)

# def blog_category(request, category):
#     posts = Post.objects.filter(
#         categories__name__contains=category
#     ).order_by(
#         '-created_on'
#     )
#     context = {
#         "category": category,
#         "posts": posts
#     }
#     return render(request, "blog_category.html", context)


# def blog_detail(request, pk):
#     post = Post.objects.get(pk=pk)
#     comments = Comment.objects.filter(post=post)
#     context = {
#         "post": post,
#         "comments": comments,
#     }

#     return render(request, "blog_detail.html", context)

def team_create(request):
    form = TeamForm()
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            team = Team(
                name=form.cleaned_data["name"],
                desc=form.cleaned_data["desc"],
                block=form.cleaned_data["block"],
            )
            team.save()
    context = {
        "form": form,
    }
    return render(request, "team_create.html", context)