from jinja2 import Template

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