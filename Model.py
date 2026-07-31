class Model:
    def __init__(self):
        self.kwargs = {}

    def query(self, **kwargs):
        self.kwargs = kwargs

    def __str__(self):
        if not self.kwargs:
            return "Model"
        parts = [f"{key} = {value}" for key, value in self.kwargs.items()]
        return "Model: " + ", ".join(parts)
