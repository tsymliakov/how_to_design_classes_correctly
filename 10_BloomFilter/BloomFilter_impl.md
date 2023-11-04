# Реализация фильтра Блюма на АТД


``` c#
abstract class BloomFilter<T>

    // конструктор

    // постусловие: создан фильтр на size элементов
    public BloomFilter<T> BloomFilter(int size);

    // команды

    // предусловие: в фильтре есть место;
    // постусловие: значение добавлено;
    public void put(T value);

    // запросы

    // проверка наличия value в фильтре
    public bool is_value(T value);

    // запросы статусов (возможные значения статусов)

    public int last_put_succes(); // да; случилась коллизия, которая не была устранена
```
