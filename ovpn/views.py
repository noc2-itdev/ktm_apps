from django.shortcuts import render, redirect, get_object_or_404
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


def team_update(request, pk):
    # team = get_object_or_404(Team, pk=pk)
    # if request.method == "POST":
    #     form = TeamForm(request.POST, instance=team)
    #     if form.is_valid():
    #         team = form.save(commit=False)
    #         # team = Team(
    #         #     name=form.cleaned_data["name"],
    #         #     desc=form.cleaned_data["desc"],
    #         #     block=form.cleaned_data["block"],
    #         # )
    #         team.save()
    #         # return redirect('team_index')
    # else:
    #     form = TeamForm(instance=team)
    # context = {
    #     "form": form,
    #     "team": team
    # }
    # return render(request, 'team_update.html', context)
    pk = int(pk)
    try:
        team = Team.objects.get(pk=pk)
        # team, created = Team.objects.get_or_create(pk = pk)                
    except Team.DoesNotExist:
        return redirect('team_index')

    form = TeamForm()
    form.fields['name'].initial = team.name
    form.fields['desc'].initial = team.desc
    form.fields['block'].initial = team.block

    if request.method == 'POST':
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            team = form.save(commit=False)
            team.save()
    context = {
        "form": form,
        "team": team
    }
    return render(request, "team_update.html", context)