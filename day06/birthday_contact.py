from datetime import datetime
class contact:
  def __init__(self,name,phone_number,email,address):
    self.name=name
    self.phone_number=phone_number
    self.e_mail=email
    self.address=address
  def display_contact(self):
    print("Name:",self.name)
    print("Phone Number:",self.phone_number)
    print("Email:",self.email)
    print("Address:",self.address)

class birthday_contact(contact):
  def __init__(self,name,phone_number,email,address,birthday):
    super().__init__(name,phone_number,email,address)
    self.birthday=birthday
  def days_until_birthday(self):
    today=datetime.today()
    self.birthday="2008-01-15"
    self.birth_date = datetime.strptime(self.birthday, "%Y-%m-%d")
    next_birthday=self.birth_date.replace(year=today.year) 
    if next_birthday<today:
      next_birthday=next_birthday.replace(year=today.year+1)
    days_left=(next_birthday-today).days
    return days_left


person=birthday_contact("Sweksha","9812345675","sweksha123@gmail.com","Bhotebahal","2008-01-15")
print(person.days_until_birthday())

