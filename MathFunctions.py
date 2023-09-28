class MathFunctions:
    def add(self, a: int, b: int) -> int:
        # this is a comment
        return a + b

    def subtract(self, a: int, b: int) -> int:
        return a - b
    
    def multiply(self, a: int, b: int) -> int:
        return a * b
    
    def divide(self, a: int, b: int) -> int:
        return a / b
    
    """
        Generates velocity with provided distance, time and direction
        @distance in meters
        @time in seconds
        @direction -- N(orth), E(ast), S(outh), W(est)
    """
    def calculate_velocity(self, distance: float, time: float, direction: str) -> str:
        if direction not in ['N', 'E', 'S', 'W']:
            raise Exception('Direction provided: {} is not valid!'.format(direction))
        speed = distance / time
        print('Velocity is {} m/s due {}'.format(speed, direction))

    """
        Pads a given word with underscore characters "_"
        @word: string to pad with underscores
    """
    def add_underscores_to_word(self, word: str) -> str:
        new_word = "_"
        for char in word:
            new_word += char + "_"
        return new_word

if __name__ == '__main__':
    math_funcs = MathFunctions()
    print(math_funcs.add(20, 30))
    print(math_funcs.add(30, 40))
    print(math_funcs.multiply(0, 7))
    print(math_funcs.divide(90, 0.1))
    try:
        math_funcs.calculate_velocity(100.0, 12.5, 'S')
        math_funcs.calculate_velocity(60.0, 10.0, 'Upwards')
    except Exception as ex:
        print(ex)
    print(math_funcs.add_underscores_to_word('hello'))
    # _h_e_l_l_o_
