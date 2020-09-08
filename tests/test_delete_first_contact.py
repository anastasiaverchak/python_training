from random import randrange

from model.contact import Contact


def test_delete_random_contact(app):
    if app.group.count() == 0:
        old_contacts = app.contact.get_contact_list()
        app.contact.add(
            Contact(firstname="firstname", middlename="middlename", lastname="lastname", nickname="nickname",
                    title="title", company="company", address="address", home="home", mobile="mobile", work="work",
                    fax="fax",
                    email="email", email2="email2", email3="email3", homepage="homepage", bday="1", bmonth="January",
                    byear="2020",
                    aday="1", amonth="January", ayear="2020", address2="address2",
                    phone2="phone2", notes="notes")
        )
        index = randrange(len(old_contacts))

        app.contact.delete_contact_by_index(index)
        new_contacts = app.contact.get_contact_list()
        assert len(old_contacts) - 1 == len(new_contacts)
        old_contacts[index:index+1] = []
        assert old_contacts == new_contacts