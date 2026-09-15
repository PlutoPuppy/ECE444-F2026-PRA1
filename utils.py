class utils:
    def __init__(self):
        pass
    
    def reversed(number):
        if not isinstance(number, int) or isinstance(number, bool):
            raise TypeError("reversed() expects an int")
        
        sign = -1 if number < 0 else 1

        return sign * int(str(abs(number))[::-1])
    
    def formatter(number):
        if not isinstance(number, int) or isinstance(number, bool):
            raise TypeError("formatter() expects an int")
        
        return bin(number), oct(number)
