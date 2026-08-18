class Layer:
    def __init__(self, name="Layer"):
        self.next_layer = None
        self.name = name

    def __call__(self, layer):
        self.next_layer = layer
        return layer


class Input(Layer):
    def __init__(self, inputs):
        super().__init__(name="Input")
        self.inputs = inputs


class Dense(Layer):
    def __init__(self, inputs, outputs, activation):
        super().__init__("Dense")
        self.inputs = inputs
        self.outputs = outputs
        self.activation = activation


class NetworkIterator:
    def __init__(self, network):
        self.network = network

    def __iter__(self):
        return self

    def __next__(self):
        if self.network == None:
            raise StopIteration
        value = self.network
        self.network = self.network.next_layer
        return value


a = Layer("A")
b = Layer("B")

c = a(b)

print(a.next_layer is b)  # True
print(c is b)  # True
inp = Input(128)
dense = Dense(128, 1024, "relu")
