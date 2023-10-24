# Реализация очереди на основе АТД


``` c#
abstract class Queue<T>

    // конструктор

    // постусловие: создана пустая очередь
     public Queue<T> Queue();

    // команды

    // предусловие: нет;
    // постусловие: последним элементом в очереди является i
    public void put(i);

    // предусловие: в очереди есть элементы;
    // постусловие: первый элемент очереди уделён;
    public void pop();

    // постусловие: очередь пуста
    public void clear();

    // запросы

    // предусловие: в очереди есть элементы;
    // постусловие: нет;
    public void peek();

    // предусловие: в очереди есть элементы;
    // постусловие: нет;
    public int size();

    // запросы статусов (возможные значения статусов)

    public int get_pop_status(); // успешно; неудоачно
    public int get_peek_status(); // успешно; неудачно
```