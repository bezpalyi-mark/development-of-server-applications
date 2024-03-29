# Лабораторна робота №7
## Декоратори
### Загальне завдання.
Напишіть декоратори:
1. Для відстежування часу початку та завершення виконання програми
(використовуйте модуль datetime); для симуляції довгих обчислень можна
використовувати sleep().
2. Для декількох запусків функції у разі її неуспішного виконання (функція
виконується успішно з деякою вірогідністю р);
3. Декоратор, що буде додавати у змінну REGISTERED усі продекоровані
функції програми.
#### Умови виконання:
1. Передбачити, що декоратори можуть приймати аргументи.
2. Продемонструвати виклики декораторів за допомогою звичайних викликів
та нотації @. Приклад декорування: @measure_time(timezone=”US/Eastern”).
3. Передбачити, що функції, які будуть декоровані приймають аргументи.
4. Зробити описи Doc strings.
5. Перевірити, що після декорування метадані початкової функції збережені.

### <div align="center">Хід роботи:</div>

Для виконання цього завдання було створено функції `very_complicated_function`, що приймає аргумент 
та `potential_broken_function`, що не приймає аргумент, а також `collect_all_decorated_functions`,
що збирає у лист усі продекоровані функції. Перші дві декоруються за допомогою анотацій, а остання прямою передачею
функції як аргументу. 
Також було створено самі декоратори `tracker_decorator`, що не приймає аргументи та `restart_if_fault` усередені 
`decorator_factory` для демонстрації передачі аргументів до декоратору. В цьому випадку ми передаємо максимальну 
кількість разів повторення виклику функції.

**Висновок**: навчився використовувати декоратори в мові Python. 