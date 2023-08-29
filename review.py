from customer import Customer
from restaurant import Restaurant

class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self._customer = customer  # Using underscores to distinguish from the method with the same name
        self._restaurant = restaurant  # Using underscores to distinguish from the method with the same name
        self._rating = rating
        Review.all_reviews.append(self)

    def rating(self):
        return self._rating

    @classmethod
    def all(cls):
        return cls.all_reviews

    def customer(self):
        return self._customer  # Using underscores to distinguish from the attribute with the same name

    def restaurant(self):
        return self._restaurant  # Using underscores to distinguish from the attribute with the same name

# Test the Review class
customer1 = Customer("John", "Doe")
restaurant1 = Restaurant("Restaurant A")
review1 = Review(customer1, restaurant1, 4)

print(review1.rating())         # Output: 4
print(Review.all())            # Output: [review1]
print(review1.customer())      # Output: <__main__.Customer object at 0x...>
print(review1.restaurant())    # Output: <__main__.Restaurant object at 0x...>
