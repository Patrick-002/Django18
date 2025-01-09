from django.shortcuts import render
from django.views.generic import TemplateView


class Platform(TemplateView):
    template_name = 'third_task/platform.html'


class Games(TemplateView):
    template_name = 'third_task/games.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['game1'] = "MiSide"
        context['game2'] = "Love, Money, Rock'n'Roll"
        context['game3'] = "Rain World"

        return context



class Cart(TemplateView):
    template_name = 'third_task/cart.html'