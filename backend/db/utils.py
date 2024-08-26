import uuid

def generate_numeric_uuid() -> int:
    """ Генерирует уникальный UUID в виде числа. """ 
    return uuid.uuid4().int % 2_147_483_640 #  Для того, чтобы можно было вставить в поле Integet 
