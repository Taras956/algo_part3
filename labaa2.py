#lab2
import unittest

def shopping(prices, discount):
    prices.sort(reverse=True)

    n = len(prices)

    num_discounted = min(n // 3, n)

    for i in range(num_discounted):
        prices[i] *= (1 - discount / 100)

    total_cost = sum(prices)

    return total_cost

prices = [1,2,3,4,5,6,7]
discount = 100
total_cost = shopping(prices, discount)
print("Загальна сума покупки:", "{:.2f}".format(total_cost))
print(prices)
print(len(prices))

class TestShoppingFunction(unittest.TestCase):

    def test_no_discount(self):
        prices = [2, 5, 8, 7, 8, 4, 7]
        discount = 0
        total_cost = shopping(prices, discount)
        self.assertEqual(total_cost, sum(prices))

if __name__ == '__main__':
    unittest.main()
