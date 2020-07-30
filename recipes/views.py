from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Recipe
from django.utils import timezone


def home(request):
    recipes = Recipe.objects
    return render(request, "recipes/home.html", {"recipes": recipes})


@login_required(login_url="/accounts/signup")
def create(request):
    if request.method == "POST":
        if request.POST["title"] and request.POST["body"] and request.POST["url"] and request.FILES["icon"] and request.FILES["image"]:
            recipe = Recipe()
            recipe.title = request.POST["title"]
            recipe.body = request.POST["body"]
            if request.POST["url"].startswith("http://") or request.POST["url"].startswith("https://"):
                recipe.url = request.POST["url"]
            else:
                recipe.url = "http://" + request.POST["url"]
            recipe.icon = request.FILES["icon"]
            recipe.image = request.FILES["image"]
            recipe.pub_date = timezone.datetime.now()
            recipe.publisher = request.user
            recipe.votes_total = 1
            recipe.save()
            return redirect("/recipes/" + str(recipe.id))
        else:
            return render(request, "recipes/create.html", {"error": "All fields are required"})
    else:
        return render(request, "recipes/create.html")


def detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, "recipes/detail.html", {"recipe": recipe})


@login_required(login_url="/accounts/signup")
def upvote(request, recipe_id):
    if request.method == "POST":
        product = get_object_or_404(Recipe, pk=recipe_id)
        product.votes_total += 1
        product.save()
        return redirect("/recipes/" + str(recipe_id))
