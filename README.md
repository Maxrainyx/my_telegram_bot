# my_telebot

```
ИТОГОВОЕ ЗАДАНИЕ 5.6.1 (PJ-02)
```

<h2>Текс задания: </h2>
<ul>
    <li>Бот возвращает цену на определённое количество валюты (евро, доллар или рубль).</li>
    <li>При написании бота необходимо использовать библиотеку pytelegrambotapi.</li>
    <li>Человек должен отправить сообщение боту в виде <имя валюты, цену которой он хочет узнать> <имя валюты, в которой надо
    узнать цену первой валюты> <количество первой валюты>.</li>
    <li>При вводе команды /start или /help пользователю выводятся инструкции по применению бота.</li>
    <li>При вводе команды /values должна выводиться информация о всех доступных валютах в читаемом виде.</li>
    <li>Для получения курса валют необходимо использовать любое удобное API и отправлять к нему запросы с
    помощью библиотеки Requests.</li>
    Для парсинга полученных ответов использовать библиотеку JSON.</li>
    <li>При ошибке пользователя (например, введена неправильная или несуществующая валюта или неправильно введено число)
    вызывать собственно написанное исключение APIException с текстом пояснения ошибки.</li>
    <li>Текст любой ошибки с указанием типа ошибки должен отправляться пользователю в сообщения.</li>
    <li>Для отправки запросов к API описать класс со статическим методом get_price(), который принимает три аргумента и
    возвращает нужную сумму в валюте:
        <ul>
            <li>имя валюты, цену на которую надо узнать, — base;</li>
            <li>имя валюты, цену в которой надо узнать, — quote;</li>
            <li>количество переводимой валюты — amount.</li>
        </ul>
    </li>
    <li>Токен Telegram-бота хранить в специальном конфиге (можно использовать .py файл).</li>
    Все классы спрятать в файле extensions.py.
</ul>
