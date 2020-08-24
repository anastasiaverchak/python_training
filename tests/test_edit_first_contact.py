from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="firstname_upd", middlename="middlename_upd", lastname="lastname_upd",
                             nickname="nickname_upd",
                             title="title_upd", company="company_upd", address="address_upd", home="home_upd",
                             mobile="mobile_upd",
                             work="work_upd", fax="fax_upd",
                             email="email_upd", email2="email2_upd", email3="email3_upd", homepage="homepage_upd",
                             bday="2",
                             bmonth="February", byear="2019",
                             aday="2", amonth="March", ayear="2021", address2="address2_upd",
                             phone2="phone2_upd", notes="notes_upd"))
    app.session.logout()
