class Customer:
    _all_customers = []  # variable to store all customer instances

    def __init__(self, given_name, family_name):
        self._given_name = given_name
        self._family_name = family_name
        Customer._all_customers.append(self)  # Add the instance to the list of all customers

    # Methods for accessing and modifying the given_name
    def given_name(self):
        return self._given_name

    def set_given_name(self, new_given_name):
        self._given_name = new_given_name

    # Methods for family namepi
    def family_name(self):
        return self._family_name

    def set_family_name(self, new_family_name):
        self._family_name = new_family_name

    # Method for getting the full name of the customer
    def full_name(self):
        return f"{self._given_name} {self._family_name}"
    
    # def __str__(self):
    #     return self.full_name()

    # method to retrieve all customer instances
    @classmethod
    def all(cls):
        return [customer.full_name() for customer in cls._all_customers]

# Test the Customer class
customer1 = Customer('Patience', 'Mugambi')
customer2 = Customer('Alice', 'Minaj')

print(customer1.full_name())  # Output: Patience Mugambi
print(customer2.full_name())  # Output: Alice Minaj
print(Customer.all())  # Output: ['Patience Mugambi', 'Alice Minaj']
