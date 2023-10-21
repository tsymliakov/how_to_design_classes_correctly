Сама по себе концепция динамического массива заключается в том, что класс содержит внутреннее хранилище и время от времени его увеличивает, или даже и уменьшает.

``` c#
abstract class AbstractDynArray<T> {
    // ВНУТРЕННЕЕ СОСТОЯНИЕ
    private T buffer[]
    private int array_size
    private STANDART_CAPACITY = 10

    // СТАТУСЫ
    public LastGetItem_Ok = 0
    public LastGetItem_Error = 1
    private int ReallocationNotNeed = -1

    // КОНСТРУКТОР

    public AbstractDynArray<T> AbstractDynArray(int capacity = STANDART_CAPACITY)

    // КОМАНДЫ

    // предусловие: new_capacity отличается от текущего размера буфера
    // постусловие: все значения внутреннего массива до
    // реаллокации сохранились в неизменном порядке, а сам
    // внутренний массив изменился в размере
    public void MakeArray(int new_capacity)

    // предусловие: в буфере найдется место для нового элемента
    // постусловие: в конец массива добавлен элемент
    public void Append(T itm)

    // предусловие: в буфере найдется место для нового элемента
    // постусловие: в массив добавлен элемент по указанному
    // индексу
    public void Insert(T itm, int index)

    // предусловие: index < array_size
    // постусловие: элемент по индексу удален, массив сжался,
    // заполнив освободившееся место
    public void Remove(int index)

    // ЗАПРОСЫ

    // предусловие: index < array_size
    public T GetItem(int index)

    // ДОПОЛНИТЕЛЬНЫЕ ЗАПРОСЫ
    private int estimate_new_size() // размер, до которого требуется
    // изменить буффер
    public int get_item_value_correct() // GetItem_Ok; GetItem_OutOfRange
}
```
