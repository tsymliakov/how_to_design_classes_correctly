# Ассоциативный массив на основе АТД


``` c#
abstract class NativeDictionary<T>

    // конструктор

    // постусловие: создан пустой словарь емкостью на N элементов
    public NativeDictionary<T> NativeDictionary(int N);

    // команды

    // предусловие: нет коллизии с уже существующим ключом key;
    // постусловие: значение value сохранено в словаре;
    public void put(string key, T value);

    // предусловие: по ключу key есть значение;
    // постусловие: пара key и ассоциированный с ним value удалена из словаря;
    public void pop(string key);

    // предусловие: по ключу key есть значение;
    public void get(string key);

    // постусловие: словарь пуст
    public void clear();

    // запросы

    public bool does_contain(T value);

    // запросы статусов (возможные значения статусов)

    public int last_put_succes(); // да; случилась коллизия, которая не была устранена
    public int last_pop_succes(); // да; такого key нет в словаре
```
