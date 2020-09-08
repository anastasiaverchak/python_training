from selenium.webdriver.support.ui import Select

from model.contact import Contact

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def add(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_form(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.app.open_home_page()
        self.contacts_cache = None

    def fill_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_calendar_value("bday",contact.bday)
        self.change_calendar_value("bmonth",contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_calendar_value("aday",contact.aday)
        self.change_calendar_value("amonth",contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def change_calendar_value(self, par, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(par).click()
            Select(wd.find_element_by_name(par)).select_by_visible_text(text)
            #wd.find_element_by_name(par).click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        #select first contact
        self.select_contact_by_index(index)
        #submit deletion
        wd.find_element_by_xpath("//input[contains(@value,'Delete')]").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_xpath("//input[contains(@value,'Delete')]")

    def edit_first_contact(self):
        self.edit_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def edit_contact_by_index(self, contact, index):
        wd = self.app.wd
        #select first contact
        self.select_contact_by_index(index)
        #submit deletion
        wd.find_element_by_xpath("//img[contains(@title,'Edit')]").click()
        #update
        self.fill_form(contact)
        wd.find_element_by_name("update").click()
        self.app.open_home_page()
        self.contacts_cache = None

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_xpath("//form[@name='MainForm']//div[1]//input[1]")) >0):
            wd.find_element_by_xpath("//a[contains(text(),'home')]").click()

    contacts_cache = None

    def get_contact_list(self):
        if self.contacts_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contacts_cache = []
            for element in wd.find_elements_by_xpath("//tr[contains(@name,'entry')]"):
                cells = element.find_elements_by_tag_name("td")
                lastname = cells[1].text
                firstname = cells[2].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contacts_cache.append(Contact(lastname = lastname, firstname= firstname, id = id))
        return list(self.contacts_cache)