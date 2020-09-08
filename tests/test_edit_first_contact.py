from model.contact import Contact

def test_edit_firstname(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Updated")
    contact.id = old_contacts[0].id

    if app.contact.count() == 0:
        app.contact.add(
            Contact(firstname="firstname", middlename="middlename", lastname="lastname", nickname="nickname",
                    title="title", company="company", address="address", home="home", mobile="mobile", work="work",
                    fax="fax",
                    email="email", email2="email2", email3="email3", homepage="homepage", bday="1", bmonth="January",
                    byear="2020",
                    aday="1", amonth="January", ayear="2020", address2="address2",
                    phone2="phone2", notes="notes"))

    app.contact.edit_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)


