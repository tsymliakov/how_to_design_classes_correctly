 АТД PowerSet

``` c#
abstract class PowerSet<T> : HashTable<T>

    // конструктор
    // постусловие: создано пустое множество
    // на максимальное количество элементов sz
    public PowerSet<T> PowerSet(int sz);

    // запросы
    // возвращает пересечение текущего множества
    // с множеством set
    public PowerSet<T> Intersection(PowerSet<T> set);

    // возвращает объединение текущего множества
    // и множества set
    public PowerSet<T> Union(PowerSet<T> set);

    // возвращает разницу между текущим множеством
    // и множеством set
    public PowerSet<T> Difference(PowerSet<T> set);

    // проверка, будет ли set подмножеством
    // текущего множества
    public bool IsSubset(PowerSet<T> set);
```
