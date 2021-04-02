class CircleArray:
    def __init__(self, size):
        self._size = size  # 实际容量
        self._length = self._size + 1  # 数组长度
        self._array = [None] * self._length
        self._recv_index = 0
        self._send_index = 0

    def send(self, x):
        if (self._send_index + 1) % self._length == self._recv_index:
            raise Exception()
        self._array[self._send_index] = x
        self._send_index = (self._send_index + 1) % self._length

    def recv(self):
        if self._recv_index == self._send_index:
            raise Exception()
        res = self._array[self._recv_index]
        self._recv_index = (self._recv_index + 1) % self._length
        return res


if __name__ == "__main__":
    c = CircleArray(3)
    c.send(1)
    c.send(2)
    c.send(3)
    print(c.recv(), c.recv(), c.recv())
    c.send(1)
    c.send(2)
    c.send(3)
    print(c.recv(), c.recv(), c.recv())
    # c.recv()
