from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from fouruc.base.server.main import Client
from decouple import config

account = Client(token=config('TOKEN_4UC'))
account.get_players()


# print(account.players)

@login_required
def dashboard(request):
    return render(request, 'base/index.html', context={'name': 'Players', 'players': account.players})


@login_required
def charts(request):
    return render(request, 'charts-morris.html')


@login_required
def maps(request):
    return render(request, 'maps-google.html')


@login_required
def blank(request):
    return render(request, 'page-blank.html')


@login_required
def badges(request):
    return render(request, 'ui-badges.html')


@login_required
def breadcrumb_pagination(request):
    return render(request, 'ui-breadcrumb-pagination.html')


@login_required
def forms(request):
    return render(request, 'ui-forms.html')


@login_required
def button(request):
    return render(request, 'ui-button.html')


@login_required
def collapse(request):
    return render(request, 'ui-collapse.html')


@login_required
def icons(request):
    return render(request, 'ui-icons.html')


@login_required
def tables(request):
    return render(request, 'ui-tables.html')


@login_required
def tabs(request):
    return render(request, 'ui-tabs.html')


@login_required
def typography(request):
    return render(request, 'ui-typography.html')
