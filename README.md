# PythonWk2

# Restaurant Review System

Welcome to the Restaurant Review System, a Python script designed to manage customer reviews for restaurants. This system consists of three main classes: `Customer`, `Restaurant`, and `Review`.

## Customer Class

The `Customer` class represents a customer with given and family names. It provides methods for accessing and modifying the customer's name, as well as retrieving the full name. The class also offers a class-level method for retrieving a list of all customer instances.

## Restaurant Class

The `Restaurant` class represents a restaurant with a name. It provides methods for retrieving the restaurant's name, reviews, customers who have reviewed the restaurant, and the average star rating of the restaurant. The class also offers a class-level method for retrieving names of all restaurants.

## Review Class

The `Review` class enables customers to leave reviews for restaurants. It stores information about the customer, the restaurant, and the rating given. The class provides methods for accessing the rating, customer name, and restaurant name. It also offers a class-level method to retrieve all reviews.

## Usage

Here's how you can use these classes:

```python
# Create customer instances
customer1 = Customer('Patience', 'Mugambi')
customer2 = Customer('Alice', 'Minaj')

# Create restaurant instances
restaurant1 = Restaurant("Shakes Diner")
restaurant2 = Restaurant("Tasty Bites")

# Create review instance
review1 = Review(customer1, restaurant1, 4)

# Accessing customer and review information
print(customer1.full_name())        # Output: Patience Mugambi
print(customer2.full_name())        # Output: Alice Minaj
print(Customer.all())               # Output: ['Patience Mugambi', 'Alice Minaj']

print(review1.rating())             # Output: 4
print(Review.all())                 # Output: [review1]
print(review1.customer())           # Output: Patience Mugambi
print(review1.restaurant())         # Output: Shakes Diner

# Accessing restaurant information
print(restaurant1.get_name())       # Output: Shakes Diner
print(restaurant2.get_name())       # Output: Tasty Bites
print(Restaurant.all())             # Output: ['Shakes Diner', 'Tasty Bites']

``` 

## Author

**Patience Mugambi**
- LinkedIn: [Patience Mugambi](http://www.linkedin.com/in/patience-mugambi-7621b5249)


