# ⚠️ Project Archived — No Longer Maintained

This repository is preserved for historical reference only.

Active development has moved to the new LogExp project, which contains the current codebase, architecture, and supported features.

👉 **New repository:** https://github.com/gaspode-wonder/logexp

Please do not open issues or pull requests on this archived repository.




# log_exp

geiger-flask-app/
├── app/                     # Flask application package
│   ├── __init__.py          # App factory, init db, register blueprints
│   ├── models.py            # GeigerReading model
│   ├── routes.py            # API endpoints
│   ├── static/              # Static assets
│   └── templates/           # Jinja2 templates
│
├── wsgi.py                  # WSGI entrypoint for uWSGI
├── config.py                # Configuration (env-driven)
├── requirements.txt         # Python dependencies
│
├── migrations/              # Alembic migrations
│
├── tests/                   # Unit/integration tests
│   └── test_app.py
│
├── ansible/                 # Infrastructure automation
│   ├── inventory.ini
│   ├── playbooks/
│   │   ├── web.yml
│   │   ├── db.yml
│   │   └── site.yml
│   ├── roles/
│   │   ├── flask_app/
│   │   │   ├── tasks/main.yml
│   │   │   ├── templates/uwsgi.ini.j2
│   │   │   └── templates/nginx.conf.j2
│   │   └── postgres/
│   │       └── tasks/main.yml
│   └── group_vars/db.yml    # Vaulted DB credentials
│
├── .github/
│   └── workflows/deploy.yml # CI/CD pipeline
│
├── .gitignore
├── README.md
└── LICENSE
