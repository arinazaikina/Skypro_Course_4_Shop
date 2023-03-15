class InstantiateCSVError(Exception):
    """
    Класс, описывающий исключения для ошибок,
    связанных с повреждением файла.
    Attributes:
        message: объяснение ошибки
    """

    def __init__(self, message):
        self.message = message
