from adapters import Options


class ServeProcess:
    """
    Класс запущенного процесса инициализации браузера
    """

    def __init__(self, options: Options):
        self._options = options

    def add_spider(self, spider):
        ...

    def serve(self) -> 'ServeProcess':
        return self
