# Django Multi-App Project (Authentication + Static Pages)

## 📌 Overview
This is a Django web application demonstrating a **multi-app architecture** with clear separation of concerns:

- `accounts` app → handles authentication (login, register, logout)
- `stat_pgs_tmplate` app → handles UI pages and layout (home, contact, page1,page2.)

The project uses Django’s built-in authentication system, template inheritance, and static files.

---

## 🚀 Features

- User authentication (login, register, logout)
- Protected dashboard using `@login_required`
- Template inheritance with shared `base.html`
- Multiple pages (home, contact, page1, page2)
- Dynamic data rendering (lists and dictionaries)
- Static file integration (CSS/JS)
- DaisyUI theme support

---
  


## Example
### code

config/settings.py
```Python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'stat_pgs_tmplate',         #added app
    'accounts',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
         'DIRS': [BASE_DIR / 'templates' / 'accounts', BASE_DIR / 'templates' / 'static_pages_templ'],   #modified
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

STATIC_URL = '/static/' # modified

STATICFILES_DIRS = [   # added
    BASE_DIR / "static",
]
#login path
LOGIN_URL = 'login'
```

config/urls.py
```Python
from django.contrib import admin
from django.urls import path, include
from stat_pgs_tmplate import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name="home"),  
    path('contact/', views.contact, name="contact"),         
    path('', include('accounts.urls')),
    path('page1/', views.p1, name='page1'),
    path('page2/', views.p2, name='page2'),
]


```

templates/static_pages_templ/base.html
```HTML
{% load static %}
<!DOCTYPE html>
<html lang="en" {% block theme %}data-theme="dark"{% endblock %}>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {% load static %}
    <title>{% block title %}My cool website with templates {% endblock %}</title>
    <link rel="stylesheet" href="{% static 'stat_pages_tmplate/css/daisyui.css'%}" >
    <script src="{% static 'stat_pages_tmplate/js/tailwindcss.js'%}"></script>
    <link rel="stylesheet" href="{% static 'stat_pages_tmplate/css/themes.css'%}" >
</head>
<body>
    <header>
        <div class="navbar bg-base-100 shadow-sm">
                <a class="btn btn-ghost text-xl" href="/">Home</a>
                <a class="btn btn-ghost text-xl" href="/contact/">Contact</a>
                <a class="btn btn-ghost text-xl" href="/page1/">Page1</a>
                <a class="btn btn-ghost text-xl" href="/page2/">Page2</a>  
        </div>   
    </header>
    <h1 class="text-4xl font-bold text-primary">{% block h1 %}My H1{% endblock %}</h1>
    <h2 class="text-2xl font-semibold text-neutral">{% block h2 %}My H2{% endblock %}</h2>
    <p class="py-4 text-base-content">{%block p %}MY PARAGRAPH {% endblock %}</p>
    <main>
        {% block main %}MY MAIN CONTENT VALUE{% endblock %}
    </main>
</body>
</html>



templates/stat_pgs_templ/home.html
```HTML
{% extends 'base.html' %}
{% load static %}

{% block theme %}data-theme="cyberpunk"{% endblock %}

{% block title %}My Cool Website{% endblock %}

{% block h1 %}My Cool Website{% endblock %}
{% block h2 %}Come and see{% endblock %}
{% block p %}Explore at your own risk{% endblock %}

{% block main %}

<ol>
    <li>Name: {{ name }}</li>
    <li> Age: {{ age }} </li>
    <li>Gains: {{ gains }}</li>
</ol>

{% endblock %}
```
