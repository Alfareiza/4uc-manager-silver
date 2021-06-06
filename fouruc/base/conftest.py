import pytest
from model_mommy import mommy

""""
Esse arquivo é criado na raíz do projeto pois as apps vão usar os elementos criados aqui. 
Nele vamos ter alguns recursos como criação de usuário
"""


@pytest.fixture
def user_logged(db, django_user_model):
    username = mommy.make(django_user_model, first_name='Thiago')
    return username


@pytest.fixture
def client_with_user_logged(user_logged, client):
    client.force_login(user_logged)
    return client
