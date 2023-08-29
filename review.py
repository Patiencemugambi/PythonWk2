from customer import Customer
from restaurant import Restaurant

class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self._rating = rating
        Review.all_reviews.append(self)

    def rating(self):
        return self._rating

    @classmethod
    def all(cls):
        return cls.all_reviews

    def customer(self):
        return self._customer.full_name() if self._customer else "Unknown Customer"

    def restaurant(self):
        return self._restaurant.get_name() if self._restaurant else "Unknown Restaurant"

# Test the Review class
customer1 = Customer("John", "Doe")
restaurant1 = Restaurant("Restaurant A")
review1 = Review(customer1, restaurant1, 4)

print(review1.rating())         # Output: 4
print(Review.all())            # Output: [review1]
print(review1.customer())      # Output: John Doe
print(review1.restaurant())    # Output: Restaurant A


