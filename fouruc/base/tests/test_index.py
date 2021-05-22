import pytest
from django.test import TestCase
from django.urls import reverse

_test_case = TestCase()

assert_contains = _test_case.assertContains
assert_not_contains = _test_case.assertNotContains


@pytest.fixture
def resp(client):
    response = client.get(reverse('base:home'))
    return response


def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, '<title>Dashboard</title>')


def test_home_link(resp):
    assert_contains(resp, f'href="{reverse("base:home")}"')
