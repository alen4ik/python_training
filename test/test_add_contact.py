# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="", middlename="", lastname="", title="", nickname="", company="", address="", home="", mobile="", work="", fax=""))
    app.session.logout()


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="hhghgh", middlename="grdhrhthh", lastname="rhrhh", title="mr", nickname="rdhhhh", company="hhjj", address="dhjhtjjhjj", home="123456", mobile="123456", work="256398", fax="852588"))
    app.session.logout()