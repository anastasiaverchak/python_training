# -*- coding: utf-8 -*-
from fixture.application import Application
import pytest

from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_new_contact(app):
    app.session.login(username="admin", password="secret")
    app.add_new_contact(Contact(firstname ="firstname", middlename= "middlename",lastname= "lastname", nickname= "nickname",
                                         title="title", company="company", address="address", home="home", mobile="mobile", work="work", fax="fax",
                                         email="email", email2="email2", email3="email3", homepage="homepage", bday="1", bmonth="January", byear="2020",
                                         aday="1", amonth="February", ayear="2020", address2="address2",
                                         phone2="phone2", notes="notes"))
    app.session.logout()
