import json

from decouple import config
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from django.utils.text import slugify
from django.views.decorators.csrf import csrf_exempt

from fouruc.manager.facade import qty_all_records
from fouruc.manager.forms import ContaNovaForm, RelatorioForm
from fouruc.manager.models import Account
from fouruc.manager.resources.api_handle import DataManager
from fouruc.manager.resources.tools import *
from fouruc.manager.resources.update_bd import *


#  Views para gerenciar as contas

@login_required
def contas(request):
    if request.method == 'POST':
        form = ContaNovaForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.name = name_of_account(form.data['url'])
            account.slug = slugify(account.name)
            account.save()
            return HttpResponseRedirect(reverse('manager:contas'))
        else:
            contas = Account.objects.all()
            return render(request, 'manager/contas.html', {'form': form, 'contas': contas}, status=400)
    contas = Account.objects.all()
    return render(request, 'manager/contas.html', {'contas': contas})


@login_required
def conta_detalhe(request, slug):
    conta = get_object_or_404(Account, slug=slug)
    ctx = {'conta': conta, 'total_records': qty_all_records(conta)}
    return render(request, 'manager/conta_detalhe.html', ctx)


def update_all_data_account(request, slug):
    conta = Account.objects.get(slug=slug)
    account = DataManager(conta.token)
    account.get_media_category(), account.get_medias(), account.get_playlists(), account.get_players()
    msg_errors = ''
    msg_sucess = []
    if not account.media_category:
        msg_errors += "• Não foi possível capturar informações das categorias."
    else:
        if categories_entered := update_or_insert_categories(conta, account.media_category):
            msg_sucess.append(f'{categories_entered} Categorias')

    if not account.medias:
        msg_errors += "\n• Não foi possível capturar informações dos conteúdos."
    else:
        if medias_entered := update_or_insert_medias(conta, account.medias):
            msg_sucess.append(f'{medias_entered} Medias')

    if not account.playlists:
        msg_errors += "\n• Não foi possível capturar informações das playlists e por causa disso não podem ser obtidos os dados dos players."
    elif not account.players:
        if playlists_entered := update_or_insert_playlists(conta, account.playlists):
            msg_sucess.append(f'{playlists_entered} Playlists')
        msg_errors += "\n• Não foi possível capturar informações dos players."
    else:
        if playlists_entered := update_or_insert_playlists(conta, account.playlists):
            msg_sucess.append(f'{playlists_entered} Playlists')
        if players_entered := update_or_insert_players(conta, account.players):
            msg_sucess.append(f'{players_entered} Players')

    messages.success(request, f"{', '.join(msg_sucess)} obtidos com sucesso !")
    messages.error(request, msg_errors)
    # By passing some object to redirect(); that object’s get_absolute_url() method will be called to figure out the redirect URL
    return redirect(conta)


def update_players(request, slug):
    conta = Account.objects.get(slug=slug)
    account = DataManager(conta.token)
    account.get_players()
    if not account.players:
        messages.error(request, "Não foi possível capturar informações dos players.")
        return redirect(conta)
    else:
        if records := update_or_insert_players(conta, account.players):
            messages.success(request, f'{records} Players obtidos!')
            return redirect(conta)
        else:
            messages.error(request, "Não foi possível capturar informações dos players.")
            return redirect(conta)


def update_categories(request, slug):
    conta = Account.objects.get(slug=slug)
    account = DataManager(conta.token)
    account.get_media_category()
    if not account.media_category:
        messages.error(request, "Não foi possível capturar informações das categorias")
        return redirect(conta)
    else:
        if categories_entered := update_or_insert_categories(conta, account.media_category):
            messages.success(request, f'{categories_entered} Categorias obtidas!')
            return redirect(conta)


def update_playlists(request, slug):
    conta = Account.objects.get(slug=slug)
    account = DataManager(conta.token)
    account.get_playlists()
    if not account.playlists:
        messages.error(request, "Não foi possível capturar informações das playlists")
        return redirect(conta)
    else:
        if playlists_entered := update_or_insert_playlists(conta, account.playlists):
            messages.success(request, f'{playlists_entered} Playlists obtidas!')
            return redirect(conta)


def update_medias(request, slug):
    conta = Account.objects.get(slug=slug)
    account = DataManager(conta.token)
    account.get_medias()
    if not account.medias:
        messages.error(request, "Não foi possível capturar informações dos conteúdos")
        return redirect(conta)
    else:
        if medias_entered := update_or_insert_medias(conta, account.medias):
            messages.success(request, f'{medias_entered} Medias obtidas!')
            return redirect(conta)


def delete(request, slug):
    conta = Account.objects.get(slug=slug)
    conta.delete()
    return HttpResponseRedirect(reverse('manager:contas'))


#  Views para relatório

@csrf_exempt
def playlogs(request):
    """
    Essa view corresponde a url path informada como webhook para receber os relatórios solicitados vía api do 4yousee manager.
    :param request:
    :return: Não retorna informações úteis pois o objetivo é so receber requesições post.
    """
    if request.method == 'POST':
        content = bytes_to_dict(request.body)
        data_response = json.dumps(content, indent=2)
        print(content)
        file = download_gz(content['url'])
        if data := process_file(file):
            #  Se o relatório recebido possui playlogs
            name_account = name_of_account(content['url'])
            try:
                conta = Account.objects.get(name__contains=name_account.split('-')[0].capitalize())
                records = insert_records(conta, data)
            except Exception as e:
                print('Error: ', e)
            return HttpResponse(f"<h4>{records} playlogs inseridos com sucesso!'</h4>")
        else:
            return HttpResponse(f"<h6 class='lead'>Não houve resultados no relatório solicitado da conta {name_of_account(content['url']).capitalize()}</h6>")
    return HttpResponse("<h4 class='lead'>Site usado como webhook para receber respostas da API do 4YouSee Manager</h4>")


@login_required
@csrf_exempt
def solicitar_relatorio(request):
    if request.method == 'POST':
        form = RelatorioForm(request.POST)
        if form.is_valid():
            slug_conta = (form.cleaned_data['conta'])
            startdate = str(form.cleaned_data['startdate'])
            enddate = str(form.cleaned_data['enddate'])
            conta = Account.objects.get(slug=slug_conta)
            account = DataManager(conta.token)
            params = dict(type='detailed', webhook=request.build_absolute_uri(reverse('manager:playlogs')),
                          filter={'startDate': startdate, 'endDate': enddate,
                                  'startTime': '00:00:00', 'endTime': '23:59:59',
                                  'mediaId': [], 'playerId': [], 'sort': -1})
            if params['webhook'].startswith('http://127.0.0.1'):
                messages.error(request, 'Não é possível solicitar o relatório com o ambiente local configurado')
                return HttpResponseRedirect(reverse('manager:solicitar_relatorio'))
            elif (resp_post := account.post_report(params)):
                    if resp_post.status_code != 200:
                        resp = json.loads(resp_post.text)
                        messages.error(request, resp['details']['report'][0])
                        return HttpResponseRedirect(reverse('manager:solicitar_relatorio'))
                    else:
                        messages.success(request, f"Relatório solicitado com sucesso. <a href={conta.get_absolute_url()}#playlogs>Ver Playlogs</a>")
                        return HttpResponseRedirect(reverse('manager:solicitar_relatorio'))
        else:
            ctx = {'contas': Account.objects.all(), 'form': form}
            return render(request, 'manager/solicitar_relatorio.html', ctx, status=400)


    else:
        form = RelatorioForm()
        ctx = {'contas': Account.objects.all(), 'form': form}
        return render(request, 'manager/solicitar_relatorio.html', ctx)
