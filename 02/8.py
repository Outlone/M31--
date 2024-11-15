class Person:
    def __init__(self, first_name, patronymic, last_name, phones):
        self.first_name = first_name
        self.patronymic = patronymic
        self.last_name = last_name
        self.phones = phones

    def get_phone(self):
        return self.phones.get('private', None)

    def get_name(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"

    def get_work_phone(self):
        return self.phones.get('work', None)

    def get_sms_text(self):
        return f"Уважаемый {self.first_name} {self.patronymic}! Примите участие в нашем беспроигрышном конкурсе для физических лиц"

class Company:
    def __init__(self, name, company_type, phones, *workers):
        self.name = name
        self.company_type = company_type
        self.phones = phones
        self.workers = workers

    def get_phone(self):
        contact_phone = self.phones.get('contact', None)
        if contact_phone:
            return contact_phone
        for worker in self.workers:
            if worker.get_work_phone():
                return worker.get_work_phone()
        return None

    def get_name(self):
        return self.name

    def get_sms_text(self):
        return f"Для компании {self.name} есть супер предложение! Примите участие в нашем беспроигрышном конкурсе для {self.company_type}"

def send_sms(*recipients):
    for recipient in recipients:
        phone = recipient.get_phone()
        if phone:
            print(f"Отправлено СМС на номер {phone} с текстом: {recipient.get_sms_text()}")
        else:
            print(f"Не удалось отправить сообщение абоненту: {recipient.get_name()}")

person1 = Person("Ivan", "Ivanovich", "Ivanov", {"private": 123, "work": 456})
person2 = Person("Ivan", "Petrovich", "Petrov", {"private": 789})
person3 = Person("Ivan", "Petrovich", "Sidorov", {"work": 789})
person4 = Person("John", "Unknown", "Doe", {})
company1 = Company("Bell", "ООО", {"contact": 111}, person3, person4)
company2 = Company("Cell", "АО", {"non_contact": 222}, person2, person3)
company3 = Company("Dell", "Ltd", {"non_contact": 333}, person2, person4)
send_sms(person1, person2, person3, person4, company1, company2, company3)/.'
