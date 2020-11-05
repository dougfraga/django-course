import pytest
from django.urls import reverse
from model_mommy import mommy

from pypro.django_assertions import assert_contains, assert_not_contains


@pytest.fixture
def resp(client, db):
    return client.get(reverse('login'))


def test_login_form_page(resp):
    assert resp.status_code == 200


@pytest.fixture
def usuario(db, django_user_model):
    usuario_modelo = mommy.make(django_user_model)
    senha = 'senha'
    usuario_modelo.set_password(senha)
    usuario_modelo.save()
    usuario_modelo.senha_plana = senha
    return usuario_modelo


@pytest.fixture
def resp_post(client, usuario):
    return client.post(reverse('login'), {'username': usuario.email, 'password': usuario.senha_plana})


def test_login_redirect(resp_post):
    assert resp_post.status_code == 302
    assert resp_post.url == reverse('modules:index')


@pytest.fixture
def resp_home(client, db):
    return client.get(reverse('base:home'))


def test_login_button(resp_home):
    return assert_contains(resp_home, 'Entrar')


def test_login_url(resp_home):
    return assert_contains(resp_home, reverse('login'))


@pytest.fixture
def resp_with_logged_user(client_with_logged_user, db):
    return client_with_logged_user.get(reverse('base:home'))


def test_without_login_button(resp_with_logged_user):
    return assert_not_contains(resp_with_logged_user, 'Entrar')


def test_without_login_url(resp_with_logged_user):
    return assert_not_contains(resp_with_logged_user, reverse('login'))


def test_logout_button_available(resp_with_logged_user):
    return assert_contains(resp_with_logged_user, 'Sair')


def test_name_logged_user_available(resp_with_logged_user, logged_user):
    return assert_contains(resp_with_logged_user, logged_user.first_name)


def test_logout_url_available(resp_with_logged_user):
    return assert_contains(resp_with_logged_user, reverse('logout'))
