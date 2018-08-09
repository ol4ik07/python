# -*- coding: utf-8 -*-

import pytest
from group import group
from application import Application

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False
@pytest.fixture()
def app(request):
    fixture=Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    success = True
    app.login(username="admin", password="secret")
    app.create_group( group(name="test_group1", header="test_group1_header", footer="test_group1_footer"))
    app.logout()
def test_empty_group(app):
    success = True
    app.login( username="admin", password="secret")
    app.create_group( group(name="", header="", footer=""))
    app.logout()



