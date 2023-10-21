class DynArray:
    REALLOCATION_NOT_NEED = -1
    STANDART_CAPACITY = 10
    LAST_GET_ITEM_OK = 0
    LAST_GET_ITEM_ERROR = 1

    def __init__(self):
        self._buffer = [None] * DynArray.STANDART_CAPACITY * 2
        self._array_size = DynArray.STANDART_CAPACITY
        self.last_get_item = 0

    def make_array(self, new_capacity):
        if new_capacity == len(self._buffer):
            return

        new_buffer = [None] * new_capacity

        for i in range(self._array_size):
            new_buffer[i] = self._buffer[i]

        assert len(new_buffer) == new_capacity

        for i in range(self._array_size):
            assert(new_buffer[i] == self._buffer[i])

        self._buffer = new_buffer

    def append(self, itm):
        self.make_array(self._estimate_new_size())

        self._buffer[self._array_size] = itm
        self._array_size += 1

        # У меня нет понимания, как осуществить тут проверку постусловия

    def _estimate_new_size(self):
        current_size = len(self._buffer)

        if current_size == self._array_size:
            return current_size * 2
        if current_size > self._array_size * 1.5:
            return current_size // 1.5 + 1

        return current_size

    def insert(self, itm, index):
        self.make_array(self._estimate_new_size())

        # пользуемся эффективной реализацией стандартной библиотеки. Хоть и
        # немного стыдно за то, что стандартная библиотека уже реализовала
        # DynArray -_-
        self._buffer.insert(index, itm)
        self._array_size += 1

        # Тут я также не понимаю, как осуществить проверку постусловия. Неужели
        # достаточно этого?
        # assert self._buffer[index] == itm

    def remove(self, index):
        old_size = self._array_size
        old_array = self._buffer[:old_size]

        if index >= self._array_size:
            return
        self._buffer.pop(index)
        self._array_size -= 1

        # Наверное, это имеет смысл, если программа работает в условиях
        # конкуренции, пока не понимаю
        assert old_size == self._array_size + 1
        assert old_array[: index] + old_array[index + 1:old_size] == self._buffer[:self._array_size]

    def get_item(self, index):
        if index < self._array_size:
            self.get_get_item_status = DynArray.LAST_GET_ITEM_OK
            return self._buffer[index]

        self.get_get_item_status = DynArray.LAST_GET_ITEM_ERROR
        return self._buffer[0]

    def get_get_item_status(self):
        return self.last_get_item
