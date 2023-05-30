# web_anal
<h1>На основі будь-якого access.log сформувати статистику про користувачів веб-ресурсу:
    a.	Кількість користувачів за днями 
    b.	Ранжувати користувачів за User-Agent
    c.	Ранжувати користувачів за операційними системами
    d.	Ранжувати користувачів за країною запиту
    e.	Виокремити пошукових ботів</h1>
<details>
  <summary><strong>Опис коду</strong></summary>
  <p>Цей код призначений для обробки і аналізу веб-серверного журналу.</p>
  <ul>
    <li><code>pandas</code> використовується для роботи з даними у форматі таблиці та операцій над ними.</li>
    <li><code>user_agents</code> використовується для парсингу інформації з User-Agent рядків.</li>
    <li><code>geoip2.database</code> використовується для визначення країни на основі IP-адреси.</li>
  </ul>
  <p>Основні етапи обробки даних:</p>
  <ol>
    <li>Завантаження веб-серверного журналу у форматі CSV за допомогою <code>pd.read_csv</code>.</li>
    <li>Об'єднання стовпців User-Agent у єдиний рядок за допомогою конкатенації.</li>
    <li>Перетворення формату часу на коректний тип даних за допомогою <code>pd.to_datetime</code>.</li>
    <li>Використання бібліотеки <code>user_agents</code> для визначення операційних систем та браузерів.</li>
    <li>Використання бібліотеки <code>geoip2.database</code> для визначення країни на основі IP-адреси.</li>
    <li>Обчислення статистики за допомогою групування та підрахунку кількості користувачів за різними параметрами.</li>
    <li>Виведення результатів аналізу, таких як загальна інформація про файл, кількість користувачів за днями, ранжування користувачів за User-Agent, операційними системами, країною запиту та інформації про ботів.</li>
  </ol>
    <h2>Демонстрація проекту</h2>
    <figure>
  <img src="https://github.com/mrotonik/mrotonik/blob/master/show2.gif" />
</figure>
</details>
