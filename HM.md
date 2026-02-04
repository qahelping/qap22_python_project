1. Написать автотесто с использование параметризации для функции format_price,
- написать негативные и позитивные автотесты
- найти ошибки в функции (не исправлять функцию, это нормально если тесты будут падать)
``` python
def format_price(price: str) -> str:
    """
    Форматирует строковое представление цены в человекочитаемый вид.

    Функция:
    - пытается преобразовать входное значение в число (`float`);
    - округляет значение до двух знаков после запятой;
    - разделяет целую часть на группы по три цифры с пробелом;
    - всегда использует точку как десятичный разделитель.

    Если входное значение нельзя преобразовать в число (например, это
    не строка или строка не является числом), функция возвращает его
    без изменений.

    Примеры:
        >>> format_price("1234")
        '1 234.00'
        >>> format_price("1234567.8")
        '1 234 567.80'
        >>> format_price("99.999")
        '100.00'
        >>> format_price("abc")
        'abc'
        >>> format_price(None)
        None

    :param price: Цена в виде строки, содержащей числовое значение.
    :return: Отформатированная строка цены или исходное значение,
             если форматирование невозможно.
    """

    try:
        price_float = float(price)
        price_str = f"{price_float:.2f}"
        integer_part, decimal_part = price_str.split(".")
        formatted_parts = []
        for i in range(len(integer_part), 0, -3):
            start = max(0, i - 3)
            formatted_parts.insert(0, integer_part[start:i])
        return " ".join(formatted_parts) + "." + decimal_part
    except (ValueError, AttributeError):
        return price

```

2. Написать автотесто с использование параметризации для функции format_price,
- написать негативные и позитивные автотесты
- найти ошибки в функции (не исправлять функцию, это нормально если тесты будут падать)

```python
def generate_week_schedule(
    days_ahead: int = 7, tz: str = "Europe/Helsinki"
) -> list[tuple[str, str, str]]:
    """
    Генерирует расписание на несколько дней вперёд с учётом часового пояса.

    Для каждого дня формируется кортеж из трёх элементов:
    - сокращённое название дня недели (Mo, Tu, We, Th, Fr, Sa, Su);
    - дата в формате DD/MM;
    - строка с временем работы или значением "Closed" для выходных.

    Логика работы:
    - отсчёт начинается с текущей даты в указанном часовом поясе;
    - для будних дней (понедельник–пятница) время работы фиксировано:
      "00:05–22:55";
    - для выходных (суббота и воскресенье) возвращается "Closed";
    - количество дней определяется параметром `days_ahead`.

    Примеры:
        >>> generate_week_schedule(3, tz="Europe/Helsinki")
        [('Mo', '01/01', '00:05–22:55'),
         ('Tu', '02/01', '00:05–22:55'),
         ('We', '03/01', '00:05–22:55')]

        >>> generate_week_schedule(2, tz="Europe/Helsinki")
        [('Sa', '06/01', 'Closed'),
         ('Su', '07/01', 'Closed')]

    :param days_ahead: Количество дней вперёд, для которых нужно сгенерировать
                       расписание (по умолчанию 7).
    :param tz: Часовой пояс в формате IANA (например, "Europe/Helsinki").
    :return: Список кортежей вида (день_недели, дата, время_работы).
    """
    day_names = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
    today = datetime.now(ZoneInfo(tz)).date()
    lst = []
    for i in range(days_ahead):
        d = today + timedelta(days=i)
        wd = d.weekday()  # 0..6
        day_abbr = day_names[wd]
        date_str = d.strftime("%d/%m")
        time_str = "Closed" if wd >= 5 else "00:05–22:55"
        lst.append((day_abbr, date_str, time_str))
    return lst
```
