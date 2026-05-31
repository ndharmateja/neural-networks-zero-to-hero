class Value:
    # _children is a tuple of Value objects
    # _op is the operation that created the current Value object from the children
    def __init__(self, data, _children=(), _op="", label=""):
        self.data = data
        self._prev = set(_children)
        self._op = _op
        self.label = label

    def __repr__(self):
        return f"Value(data={self.data}, label={self.label})"

    # + operator
    def __add__(self, other):
        # The new Value object will have self and other as the children
        # and the operator as '+'
        return Value(self.data + other.data, (self, other), "+")

    # * operator
    def __mul__(self, other):
        # The new Value object will have self and other as the children
        # and the operator as '*'
        return Value(self.data * other.data, (self, other), "*")
