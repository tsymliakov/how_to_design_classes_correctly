# Реализация без теории и размышлений

Размышления в файле [BoundedStack.md](BoundedStack.md).

```
abstract class BoundedStack<T>
    private List<T> stack;
    private int max_size;
    private int peek_status;
    private int pop_status;
    private int push_status;

    public const int POP_NIL = 0; // push() ещё не вызывалась
    public const int POP_OK = 1; // последняя pop() отработала нормально
    public const int POP_ERR = 2; // стек пуст

    public const int PEEK_NIL = 0; // push() ещё не вызывалась
    public const int PEEK_OK = 1; // последняя peek() вернула корректное значение
    public const int PEEK_ERR = 2; // стек пуст

    public const int PUSH_NIL = 0; // push() ещё не вызывалась
    public const int PUSH_OK = 1; // последний push() вернул корректное значение
    public const int PUSH_Error = 2; // стек полон

    public BoundedStack(T value, int max_size = 32):
        this.max_size = max_size // тут в качестве исключения оставлю this
        clear()

    public void push(T value):
        if size() < max_size:
            stack.Append(value)
            push_status = PUSH_OK
        else:
            push_status = PUSH_ERROR

    public T pop():
        if size() > 0
            stack.RemoveAt(-1)
            pop_status = POP_OK
        else
            pop_status = POP_ERR


    public void clear():
        stack = []

        peek_status = PEEK_NIL
        pop_status = POP_NIL
        push_status = PUSH_NIL

    public T peek():
        if size() > 0
            result = stack[-1]
            peek_status = PEEK_OK
        else
            result = 0
            peek_status = PEEK_ERR
        return result

    public int size():
        return stack.Length()

    public int max_size():
        return staack.max_size()

    public int get_pop_status():
        return pop_status

    public int get_peek_status():
        return peek_status

    public int get_push_status():
        return push_status
```
