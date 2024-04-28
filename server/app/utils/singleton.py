class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

    async def release_instances_of(cls, function=None):
        """
        cls이거나 cls의 하위클래스로 생성된 모든 singleton 인스턴스를 해제한다.
        """
        for subclass, instance in list(cls._instances.items()):
            if issubclass(type(instance), cls):
                if function:
                    await function(cls._instances[subclass])
                del cls._instances[subclass]

