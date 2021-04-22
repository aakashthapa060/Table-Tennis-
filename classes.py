
class Employee:
	
	raise_amount = 1.05
	num_of_emp = 0

	def __init__(self, first,last,pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = f"{first}.{last}@company.com"

	def fullname(self):
		return f"{self.first} {self.last}"

	def amount_raise(self):
		self.pay = self.pay * self.raise_amount

	@classmethod
	def set_amount_raise(cls, amount):
		cls.raise_amount = amount

	@classmethod
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split("-")
		return cls(first,last,pay)


emp1 = Employee("Aakash", "Thapa",5000)

print(emp1.pay)
emp1.set_amount_raise(5)
print(Employee.raise_amount)

emp_str_1 = "Randi-maya-7000"
new_emp1 = Employee.from_string(emp_str_1)
print(new_emp1.fullname())