"""Whitespace and naming exercise."""


class Pizza:
    """Pizza class."""

    def __init__(self, bread_type, cheese_type, meat_type, toppings, size):
        """Initialize pizza."""
        self.bread_type = bread_type
        self.cheese_type = cheese_type
        self.meat_type = meat_type
        self.toppings = toppings
        self.size = size

    @classmethod
    def make_chicago_pizza(cls, size):
        """Make a Chicago pizza."""
        bread = 'deep-dish bread'
        cheese = 'mozzarella cheese'
        meat_type = 'Italian sausage'
        toppings = ['green bell pepper', 'mushroom',
                    'chunky tomato sauce', 'onion']
        return cls(bread, cheese, meat_type, toppings, size)

    @classmethod
    def make_california_pizza(cls, meat_type, size):
        """Make a California pizza."""
        bread = 'thin crust'
        cheese_type = 'feta cheese'
        toppings = ['garlic', 'spinach', 'broccoli',
                    'olives', 'red onion', 'red bell pepper']
        return cls(bread, cheese_type, meat_type, toppings, size)

    def print_info(self):
        """Print pizza info."""
        print('Bread type is: ', self.bread_type)
        print('Cheese type is: ', self.cheese_type)
        print('Meat type is: ', self.meat_type)
        print('Toppings are: ', end='')
        print(', '.join(map(str, self.toppings)))


myPizza = Pizza.make_california_pizza('chicken', 'large')
myPizza.print_info()
