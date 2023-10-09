import collections


class Resource(collections.abc.Mapping):
    def __init__(self, **kwargs):
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def add(self, attr, value):
        setattr(self, attr, value)
        return self

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.__dict__}"

    def __str__(self):
        return f"{self.__dict__}"

    def __iter__(self):
        return iter(self.__dict__.keys())

    def __getitem__(self, key):
        return getattr(self, key)

    def __len__(self):
        return len(self.__dict__.items())
