import math

class factored_number:
    def __init__(self):
        self.factors = {}

    def push_factor(self, base, exp):
        key = str(base)
        if( not key in self.factors ):
            self.factors[key] = {"number": base, "count": 0}
        self.factors[key]["count"] += exp
    
    def divide(self, divider):
        result = factored_number()
        
        all_keys = set( list(self.factors.keys()) + list(divider.factors.keys()) )
        for key in all_keys:
            divident_exponent = 0
            divider_exponent = 0
            base_num = int(key)
            if( key in self.factors ):
                divident_exponent = self.factors[key]["count"]
            if( key in divider.factors ):
                divider_exponent = divider.factors[key]["count"]
            exponent_difference = divident_exponent - divider_exponent
            if( exponent_difference != 0 ):
                result.push_factor(base_num, exponent_difference )
                
        return result
            
    def print_factors(self):
        out_str = " ="
        for key in self.factors:
            out_str += " {}^{}".format(self.factors[key]["number"], self.factors[key]["count"])
        print( out_str)
        
    def convert_to_float(self):
        result = 1
        for key in self.factors:
            component = self.factors[key]
            result *= component["number"]**component["count"]
        
        return result
    
    def naive_factor(self, number):
        i = 2

        while( i*i <= number ):
            if( number%i ):
                i += 1
            else:
                number = number//i
                self.push_factor(i,1)
        if( number > 1 ):
            self.push_factor(number,1)
            


    def multiply_factorial(self, num):
        if( num == 0 ):
            self.push_factor(1,1)
        for ix in range(2,num+1):
            self.naive_factor(ix)
            
    
    
if __name__ == "__main__":
    numerator = 500
    denominator = 300
    
    
    my_number = factored_number()
    my_number.multiply_factorial(10)
    #my_number.multiply_factorial(10)
    my_number.print_factors()
    float_res = my_number.convert_to_float()
    print("{}".format(float_res))
    
    my_number_2 = factored_number()
    try_this = math.factorial(500)
    my_number_2.naive_factor(try_this)
    my_number_2.print_factors()
    float_res = my_number_2.convert_to_float()
    print("{}".format(float_res))
    
    another_number = factored_number()
    another_number.multiply_factorial(300)
    
    ratio = my_number.divide(another_number)
    ratio.print_factors()
    float_res = ratio.convert_to_float()
    print("{}".format(float_res))
 
