# Quickstart

## 1. Project layout

    restapi             # The root project.
        manage.py       # Django commands management
        restapi
            __init__
            asgi.py
            settings.py # Global settings
            urls.py     # Global Urls
            wsgi.py     # Web Server Gateway Interface
        core            # Module: Core with core functions
        authjwt         # Module: Authentication with JWT
        profiles        # Module: User's Profile

## 2. Create Python virtualenv

    virtualenv -p python3 venv
    source venv/bin/activate
    pip install -r requirements.txt
    
## 3. Run Django Project

    python manage.py runserver 8000

## 4. Swagger UI

**Swagger UI for interact with RESTful API.** `http://localhost:8000/swagger/`

![Swagger UI for interact with RESTful API](/img/swagger-ui-1.png)


## 5. ReDoc

API Reference Documentation. `http://localhost:8000/redoc/`

![API Reference Documentation](/img/redoc-1.png)
