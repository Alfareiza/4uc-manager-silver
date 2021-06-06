import pytest
from django.test import TestCase
from django.urls import reverse
from model_mommy import mommy

_test_case = TestCase()

assert_contains = _test_case.assertContains
assert_not_contains = _test_case.assertNotContains


@pytest.fixture
def resp_login(client):
    response = client.get(reverse('login'))
    return response


def test_login_form_page(resp_login):
    assert resp_login.status_code == 200


@pytest.fixture
def user_example(db, django_user_model):
    user_example = mommy.make(django_user_model)
    password = 'pass'
    user_example.set_password(password)
    user_example.save()
    user_example.plain_password = password
    return user_example


@pytest.fixture
def resp_post(client, user_example):
    response = client.post(reverse('login'), {'username': user_example.email, 'password': user_example.plain_password})
    return response


def test_login_redirect(resp_post):
    assert resp_post.status_code == 302
    assert resp_post.url == reverse('base:home')


@pytest.fixture
def resp_home(client, db):
    return client.get(reverse('login'))


def test_login_button(resp_home):
    assert_contains(resp_home, 'Login')


def test_login_link_available(resp_home):
    assert_contains(resp_home, 'type="submit" name="login"')


@pytest.fixture
def resp_home_with_user_logged(client_with_user_logged, db):

    return client_with_user_logged.get(reverse('base:home'))


def test_login_button_not_available(resp_home_with_user_logged):
    assert_not_contains(resp_home_with_user_logged, 'Login')


def test_login_link_not_available(resp_home_with_user_logged):
    assert_not_contains(resp_home_with_user_logged, reverse('login'))


def test_logout_button_available(resp_home_with_user_logged):
    assert_contains(resp_home_with_user_logged, 'Logout')


def test_logout_link_available(resp_home_with_user_logged):
    assert_contains(resp_home_with_user_logged, reverse('logout'))
