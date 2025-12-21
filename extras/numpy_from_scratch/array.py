class Array(list):
    def __init__(self, values: list = None):

        values = values or []
        self.dtype = type(values[0]) if values else None
        for v in values:
            assert self.dtype == type(v), "all values must be of same type"

        super().__init__(values)

    def dot(self, other: "Array") -> "Array":
        result = Array()
        for v1, v2 in zip(self, other):
            if isinstance(v1, type(self)) and isinstance(v2, type(self)):
                result.extend(v1.dot(v2))
            elif isinstance(v1, (float, int)) and isinstance(v2, (float, int)):
                result.append(v1 * v2)
            else:
                raise TypeError(f"cannot do {self} with type {type(v1)}")
        return result


def main():
    a = Array([1,2,3])
    b = Array([1,2,3])

    print(a.dot(b))


if __name__ == "__main__":
    main()
