# Реализация BoundedStack на основе АТД

BoundedStack - ограниченный стек. Его конструктор получает целое положительное
число, задающее максимальное количество элементов в стеке.

Дополнительное условие: если параметр не задан, то стек рассчитан на 32
элемента.

Я реализовываю BoundedStack на смеси языков из C# и Python.

## Шаг 1. Определение типа

При определении типа задается его название, а также тип-параметр (это вот это,
вот то самое, в общем T из дженериков C#)

```
class BoundedStack<T>
```

## Шаг 2. Опредление сигнатур всех методов АТД

Что можно сделать со стеком?
1) Создать объект класса BoundedStack.
2) Положить элемент (push);
3) Вытащить элемент (pop);
4) Посмотреть на элемент без вытаскивания (peek);
5) Узнать количество элементов внутри стека (size);
6) Узнать максимальный размер стека (max_size);
7) Очистить стек (clear).

Изходя из требований к методам, имеем следующую картину:

```
abstract class BoundedStack<T>
    public BoundedStack(T value);
    public void push(T value);
    public T pop();
    public T peek();
    public int size();
    public int max_size();
    public void clear();
```

## Шаг 3. Определение условий и ограничений на работу методов

На этом шаге для каждого метода необходимо определить **предусловия**, а также диапазон принимаемых значений.

```
abstract class BoundedStack<T>
    public BoundedStack(T value);
    public void push(T value); / предусловие: в стеке есть место
    public T pop(); // предусловие: стек не пустой
    public T peek(); // предусловие: стек не пустой
    public int size();
    public int max_size();
    public void clear();
```

## Шаг 4. Определение постусловий

```
abstract class BoundedStack<T>
    public BoundedStack(T value);

    // предусловие: в стеке есть место
    // постусловие: в стек добавлен новый элемент
    public void push(T value);

    // предусловие: стек не пустой
    // постусловие: из стека удален верхний элемент
    public T pop();

    public T peek(); // предусловие: стек не пустой
    public int size();
    public int max_size();

    // постусловие: из стека удаляются все значения
    public void clear();
```


## Шаг 5. Распределение методов по типам: конструктор, команды, запросы

```
abstract class BoundedStack<T>
    // КОНСТРУКТОР
    public BoundedStack(T value);

    // КОМАНДЫ

    // предусловие: в стеке есть место
    // постусловие: в стек добавлен новый элемент
    public void push(T value);

    // предусловие: стек не пустой
    // постусловие: из стека удален верхний элемент
    public T pop();

    // постусловие: из стека удаляются все значения
    public void clear();

    // ЗАПРОСЫ

    public T peek(); // предусловие: стек не пустой
    public int size();
    public int max_size();
```

## Шаг 6. Определение дополнительных запросов

Определение дополнительных запросов необходимо для того, чтобы разрешать
подобные ситуации:

Хочется положить элемент в стек, а он уже полон. Что должнен сделать метод push?
1) проверив size стека, не делая никаких объявлений, не сделать ничего ничего;
1) проверив size стека, выбросить исключение;
2) проверив size стека, вернуть из метода push() константу;

Все эти способы не верны, а верной реализацией считается реализация дополнительных запросов, которые проверят, допустима ли команда.

Запросы будут возвращать числа, которые сравниваются с именнованными константами - атрибутами класса.

```
public const int POP_NIL = 0; // push() ещё не вызывалась
public const int POP_OK = 1; // последняя pop() отработала нормально
public const int POP_ERR = 2; // стек пуст

public const int PEEK_NIL = 0; // push() ещё не вызывалась
public const int PEEK_OK = 1; // последняя peek() вернула корректное значение
public const int PEEK_ERR = 2; // стек пуст


public const int PUSH_OK = 1; // последний push() вернул корректное значение
public const int PUSH_Error = 2; // стек полон

public int get_pop_status(); // возвращает значение POP_*
public int get_peek_status(); // возвращает значение PEEK_*
public int get_push_status(); // возвращает значение PUSH_*
```

Смысл PIP_NIL и PEEK_NIL в том, что, в принципе, возможна ситуация, когда стек находится в неопределенном состоянии, если он реализован аппаратно.


Использование таких запросов и статусов приводит к тому, что алгоритм работы с методами peek(), pop() и push() выглядит примерно так:

```
x = stack1.peek()
if stack1.get_peek_status() == Stack.PEEK_OK
    // обрабатываем x

stack1.pop()
y = stack1.peek()
if stack1.get_peek_status() == Stack.PEEK_OK and
    stack1.get_pop_status() == Stack.POP_OK
    // обрабатываем y

stack1.push()
if stack1.get_push_status() == Stack.PUSH_OK
    // считается, что элемент был занесе в стек, можно выполнять программу дальше
```


Финальная версия:

```
abstract class BoundedStack<T>
    public const int POP_NIL = 0; // push() ещё не вызывалась
    public const int POP_OK = 1; // последняя pop() отработала нормально
    public const int POP_ERR = 2; // стек пуст

    public const int PEEK_NIL = 0; // push() ещё не вызывалась
    public const int PEEK_OK = 1; // последняя peek() вернула корректное значение
    public const int PEEK_ERR = 2; // стек пуст

    public const int PUSH_OK = 1; // последний push() вернул корректное значение
    public const int PUSH_Error = 2; // стек полон

    // КОНСТРУКТОР
    public BoundedStack(T value, int max_size = 32);

    // КОМАНДЫ

    // предусловие: в стеке есть место
    // постусловие: в стек добавлен новый элемент
    public void push(T value);

    // предусловие: стек не пустой
    // постусловие: из стека удален верхний элемент
    public T pop();

    // постусловие: из стека удаляются все значения
    public void clear();

    // ЗАПРОСЫ

    // предусловие: стек не пустой
    public T peek();
    public int size();
    public int max_size();

    // ДОПОЛНИТЕЛЬНЫЕ ЗАПРОСЫ

    public int get_pop_status(); // возвращает значение POP_*
    public int get_peek_status(); // возвращает значение PEEK_*
    public int get_push_status(); // возвращает значение PUSH_*
```

Более приближенная к реальности реализация. Использование self или this подразумевается.

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
