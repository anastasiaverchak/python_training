from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="test_upd", header="upd", footer="upd"))
    app.session.logout()
