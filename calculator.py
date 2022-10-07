def calculator(expression: str):
    '''
    Выводит результат выбранной операции (+ - * /) с двумя целыми, положительными числами
    '''
    signs_allowed = '+-*/'
    if not any(sign in expression for sign in signs_allowed):
        raise ValueError(f'Выражение должно содержать хотя бы один знак {signs_allowed}')
    for sign in signs_allowed:
        if sign in expression:
            try:
                left, right = expression.split(sign)
                left, right = int(left), int(right)
                return {
                    '+': lambda a, b: a + b,
                    '-': lambda a, b: a - b,
                    '*': lambda a, b: a * b,
                    '/': lambda a, b: a / b,
                }[sign](left, right)
            except (ValueError, TypeError):
                raise ValueError('Выражение должно содержать 2 целых числа и 1 знак между ними')



