from django.shortcuts import render
from django.views.generic import TemplateView


class Platform(TemplateView):
    template_name = 'fourth_task/platform.html'


class Games(TemplateView):
    template_name = 'fourth_task/games.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['games'] = ["MiSide","Love, Money, Rock'n'Roll","Rain World"]\

        return context



class Cart(TemplateView):
    template_name = 'fourth_task/cart.html'