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