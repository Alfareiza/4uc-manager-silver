from django.shortcuts import render


def home(request):
    return render(request, 'base/index.html')


def dashboard(request):
    return render(request, 'base/index.html')


def reset_pass(request):
    return render(request, 'auth-reset-pass.html')


def charts(request):
    return render(request, 'charts-morris.html')


def login(request):
    return render(request, 'login.html')


def maps(request):
    return render(request, 'maps-google.html')


def blank(request):
    return render(request, 'page-blank.html')


def register(request):
    return render(request, 'register.html')


def badges(request):
    return render(request, 'ui-badges.html')


def breadcrumb_pagination(request):
    return render(request, 'ui-breadcrumb-pagination.html')


def forms(request):
    return render(request, 'ui-forms.html')


def button(request):
    return render(request, 'ui-button.html')


def collapse(request):
    return render(request, 'ui-collapse.html')


def icons(request):
    return render(request, 'ui-icons.html')


def tables(request):
    return render(request, 'ui-tables.html')


def tabs(request):
    return render(request, 'ui-tabs.html')


def typography(request):
    return render(request, 'ui-typography.html')
