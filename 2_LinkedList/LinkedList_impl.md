# Задание 1

``` c#
abstract class LinkedList<T>
    public const int HEAD_NIL = 0; // head() ещё не вызывалась
    public const int HEAD_OK = 1; // последняя head() отработала нормально
    public const int HEAD_ERR = 2; // список пустой

    public const int TAIL_NIL = 0; // tail() ещё не вызывалась
    public const int TAIL_OK = 1; // последняя tail() отработала нормально
    public const int TAIL_ERR = 2; // список пустой

    public const int RIGHT_NIL = 0; // right() ещё не вызывалась
    public const int RIGHT_OK = 1; // последняя right() отработала нормально
    public const int RIGHT_ERR = 2; // список пустой

    public const int PUT_RIGHT_NIL = 0; // put_right() ещё не вызывалась
    public const int PUT_RIGHT_OK = 1; // последняя put_right() отработала нормально
    public const int PUT_RIGHT_ERR = 2; // список пустой

    public const int PUT_LEFT_NIL = 0; // put_left() ещё не вызывалась
    public const int PUT_LEFT_OK = 1; // последняя put_left() отработала нормально
    public const int PUT_LEFT_ERR = 2; // список пустой

    public const int REMOVE_NIL = 0; // remove() ещё не вызывалась
    public const int REMOVE_OK = 1; // последняя remove() отработала нормально
    public const int REMOVE_ERR = 2; // список пустой

    public const int REPLACE_NIL = 0; // replace() ещё не вызывалась
    public const int REPLACE_OK = 1; // последняя replace() отработала нормально
    public const int REPLACE_ERR = 2; // список пустой

    public const int FIND_NIL = 0; // find() ещё не вызывалась
    public const int FIND_OK = 1; // последняя find() отработала нормально
    public const int FIND_ERR = 2; // список пустой

    public const int REMOVE_ALL_NIL = 0; // remove_all() ещё не вызывалась
    public const int REMOVE_ALL_OK = 1; // последняя remove_all() отработала нормально
    public const int REMOVE_ALL_ERR = 2; // список пустой

    public const int GET_NIL = 0; // get() ещё не вызывалась
    public const int GET_OK = 1; // последняя get() отработала нормально
    public const int GET_ERR = 2; // список пустой

    // постусловие: создан список, внутреннее хранилище пусто
    public LinkedList<T> LinkedList();

    // КОМАНДЫ

    // предусловие: список не пустой
    // постусловие: курсор указывает на голову
    public void head();

    // предусловие: список не пустой
    // постусловие: курсор указывает на конец
    public void tail();

    // предусловие: список не пустой
    // постусловие: курсор указывает на узел справа
    public void right();

    // предусловие: список не пустой
    // постусловие: справа появился новый узел
    public void put_right(T value);

    // предусловие: список не пустой
    // постусловие: слева появился новый узел
    public void put_left(T value);

    // предусловие: список не пустой
    // постусловие: узел удален, курсор указывает на правого соседа, если таковой был, либоа на левого, если таковой был
    public void remove();

    // постусловие: список пустой
    public void clear();

    // постусловие: добавлен новый узел в хвост списка
    public void add_tail(T value);

    // предусловие: список не пустой
    // постусловие: в текущим узле другое значение
    public void replace(T value);

    // предусловие: список не пустой
    // постусловие: курсор установлен на следующий узел с искомым значением (по отношению к текущему узлу)
    public void find(T value);

    // предусловие: список не пустой
    // постусловие: в списке нет узлов с заданным значением
    public void remove_all(T value);

    // ЗАПРОСЫ

    // предусловие: список не пустой
    public T get();

    public int size();

    public bool is_head();

    public bool is_tail();

    public bool is_value();


    // ДОПОЛНИТЕЛЬНЫЕ ЗАПРОСЫ

    public int get_head_status(); // возвращает значение HEAD_*
    public int get_tail_status(); // возвращает значение TAIL_*
    public int get_right_status(); // возвращает значение RIGHT_*
    public int get_put_right_status(); // возвращает значение PUT_RIGHT_*
    public int get_put_left_status(); // возвращает значение PUT_LEFT_*
    public int get_remove_status(); // возвращает значение REMOVE_*
    public int get_replace_status(); // возвращает значение REPLACE_*
    public int get_find_status(); // возвращает значение FIND_*
    public int get_remove_all_status(); // возвращает значение REMOVE_ALL_*
    public int get_get_status(); // возвращает значение GET_*
```

# Задание 2

При реализации метода tail посредством других операций придется вызывать right()
и is_tail, а это приводит к сложности операции O(n).

# Задание 3

Такая операция не нужна поскольку существует операция find(), при её вызове
происходит итерация по списку, который будто был возвращен методом find_all().
