import unittest
import math
import magnitude_ratio


class Testing(unittest.TestCase):
    def test_factored_number(self):
        for i in range(0,100):
            fact_number = math.factorial(i)
            my_number = magnitude_ratio.factored_number()
            my_number.multiply_factorial(i)
            my_number_float = my_number.convert_to_float()
            self.assertEqual(fact_number, my_number_float)

    def test_ratio(self):
        epsilon = 0.00000001
        for i in range(0,26):
            for j in range(0,26):
                fact_number = math.factorial(i)/math.factorial(j)
                
                numerator = magnitude_ratio.factored_number()
                numerator.multiply_factorial(i)
                
                denominator = magnitude_ratio.factored_number()
                denominator.multiply_factorial(j)
                
                ratio = numerator.divide(denominator)
                my_number_float = ratio.convert_to_float()
                
                difference = abs(fact_number - my_number_float)
                print("{}!/{}! = {} or ({}, magratio)".format(i,j, fact_number, my_number_float))
                self.assertLess(difference, epsilon)

if __name__ == '__main__':
    unittest.main()