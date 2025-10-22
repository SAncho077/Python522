from jinja2 import Template
html = """
{% macro input_func(type='text', name='', placeholder='') %}
    <input type="{{ type }}" name="{{ name }}" placeholder="{{ placeholder }}">
{% endmacro %}


<p> {{ input_func(name="firstname", placeholder="Имя") }} </p>
<p> {{ input_func(name="lastname", placeholder="Фамилия") }} </p>
<p> {{ input_func(name="address", placeholder="Адрес") }} </p>
<p> {{ input_func(type="tel", name="phone", placeholder="Телефон") }} </p>
<p> {{ input_func(type="email", name="email", placeholder="Почта") }} </p>

"""

tm = Template(html)
msg = tm.render()

print(msg)


# Задача 2

data = {"index": "Главная",
        "news": "Новости",
        "about": "О компании",
        "shop": "Магазин",
        "contacts": "Контакты",

        }

link = """
<ul>
    {% for key, value in data.items() %}
        <li><a href="/{{ key }}" {% if value == "Главная" %}class="active"{% endif %}>{{ value }}</a></li>
    {% endfor %}
</ul>
"""

tm = Template(link)
msg = tm.render(data=data)
print(msg)