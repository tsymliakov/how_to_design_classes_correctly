``` c#
abstract class DynArray<T>

  // конструктор
// постусловие: создан пустой массив
  public DynArray<T> DynArray();

  // команды
// предусловие: i лежит в допустимых границах массива;
// постусловие: значение элемента i изменено на value
  public void put(i, T value);

// предусловие: i лежит в допустимых границах массива;
// постусловие: перед элементом i добавлен
// новый элемент с значением value;
  public void put_left(i, T value);

// предусловие: i лежит в допустимых границах массива;
// постусловие: после элемента i добавлен
// новый элемент с значением value;
  public void put_right(i, T value);

// предусловие: нет;
// постусловие: в хвост массива добавлен
// новый элемент
  public void append(T value);

// предусловие: i лежит в допустимых границах массива;
// постусловие: элемент i удалён из массива;
  public void remove(int i);

  // запросы
// предусловие: i лежит в допустимых границах массива;
  public T get(int i); // значение i-го элемента
  public int size(); // текущий размер массива

  // запросы статусов (возможные значения статусов)
  public int get_put_status(); // успешно; индекс за пределами массива
  public int get_put_left_status(); // успешно; индекс за пределами массива
  public int get_put_right_status(); // успешно; индекс за пределами массива
  public int get_remove_status(); // успешно; индекс за пределами массива
  public int get_get_status(); // успешно; индекс за пределами массива
```