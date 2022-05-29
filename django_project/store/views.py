from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RatingForm, ReviewForm
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .models import *


class CategoryFilter:
    def get_category(self):
        return Category.objects.all()

class FlowersView(CategoryFilter, ListView):
    model = Flowers
    queryset = Flowers.objects.all()


class FlowersDetailView(CategoryFilter, DetailView):
    model = Flowers
    slug_field = "url"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["star_form"] = RatingForm()
        return context

class AddStarRating(View):
    """Добавление рейтинга цветам"""

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        form = RatingForm(request.POST)
        if form.is_valid():
            Rating.objects.update_or_create(
                ip=self.get_client_ip(request),
                flowers_id=int(request.POST.get("flowers")),
                defaults={'star_id': int(request.POST.get("star"))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)

class Search(ListView):
    paginate_by = 3

    def get_queryset(self):
        return Flowers.objects.filter(title__icontains=self.request.GET.get("q"))

class AddReview(View):
    """Отзывы"""
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        flowers = Flowers.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.flowers = flowers
            form.save()
        return redirect(flowers.get_absolute_url())

class FilterFlowersView(CategoryFilter, ListView):
   def get_queryset(self):
        queryset = Flowers.objects.filter(
            Q(category__in=self.request.GET.getlist("category")) 
        ).distinct()
        return queryset