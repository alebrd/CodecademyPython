toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']

prices = [2, 6, 1, 3, 2, 7, 2]

num_pizzas = len(toppings)

print('We sell {} different kinds of pizza!'.format(num_pizzas))

pizzas = list(zip(prices, toppings))

print(pizzas)

pizzas.sort()

cheapest_pizza = pizzas[0]

priciest_pizza = pizzas[-1]

three_cheapest = pizzas[:4]

print(three_cheapest)

num_two_dollar_slices = prices.count(2)

