class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name = name
        Restaurant.all_restaurants.append(self)

    def get_name(self):
        return self.name

    def reviews(self):
        return [review for review in Review.all() if review.restaurant() == self]

    def customers(self):
        customers = set()
        for review in self.reviews():
            customers.add(review.customer())
        return list(customers)

    def average_star_rating(self):
        restaurant_reviews = self.reviews()
        if not restaurant_reviews:
            return 0
        total_ratings = sum(review.rating() for review in restaurant_reviews)
        return total_ratings / len(restaurant_reviews)

    @classmethod
    def all(cls):
        return [restaurant.get_name() for restaurant in cls.all_restaurants]

# Test the Restaurant class
restaurant_a = Restaurant("Shakes Diner")
restaurant_b = Restaurant("Tasty Bites")

print(restaurant_a.get_name())  # Output: Shakes Diner
print(restaurant_b.get_name())  # Output: Tasty Bites
print(Restaurant.all())         # Output: ['Shakes Diner', 'Tasty Bites']
