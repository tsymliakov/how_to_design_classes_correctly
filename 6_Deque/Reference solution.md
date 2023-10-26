 АТД ParentQueue

``` c#
abstract class ParentQueue<T>

    // конструктор
    public ParentQueue<T> ParentQueue();

    // команды
    // постусловие: в хвост очереди добавлен новый элемент
    public void add_tail(T value);

    // предусловие: очередь не пуста;
    // постусловие: из головы очереди удалён элемент
    public void remove_front();

    // запросы
    // предусловие: список не пуст
    public T get_front(); // значение элемента в голове очереди;

    public int size(); // текущий размер очереди

    // запросы статусов (возможные значения статусов)
    public int get_remove_front_status(); // успешно; очередь пуста
    public int get_get_front_status(); // успешно; очередь пуста
```

АТД Queue

``` c#
abstract class Queue<T> : ParentQueue<T>

    // конструктор
    public Queue<T> Queue();
```

АТД Deque

``` C#
abstract class Deque<T> : ParentQueue<T>

    // конструктор
    // постусловие: создана пустая очередь
    public Deque<T> Deque();

    // команды
    // постусловие: в голову очереди добавлен новый элемент
    public void add_front(T value);

    // предусловие: очередь не пуста;
    // постусловие: из хвоста очереди удалён элемент
    public void remove_tail();

    // запросы
    // предусловие: список не пуст
    public T get_tail(); // значение элемента в хвосте очереди;

    public int size(); // текущий размер очереди

    // запросы статусов (возможные значения статусов)
    public int get_remove_tail_status(); // успешно; очередь пуста
    public int get_get_tail_status(); // успешно; очередь пуста
```
