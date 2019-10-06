{% extends "base.html" %}

{% block title %}
    vefverslun- körfu eytt
{% endblock %}

{% block refresh %}
    <meta http-equiv="refresh" content="1; url= {{url_for("index.tpl")  }}">
{% endblock %}

{% block content %}
    <h1>Körfu verður eytt....</h1>
{% endblock %}