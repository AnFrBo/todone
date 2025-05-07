# 📌 ToDone — Gamify Your Household Tasks

**ToDone** is a smart app that helps you and your partner/roomies manage household chores together in a gamified way.  
Create tasks, track actions, and monitor KPIs to make household management collaborative and fun.

---

## 🚀 Features

- Create household tasks (with e.g. title, descriptions, solution times)
- Record actions when tasks are completed
- View KPIs (average solution time, completion rates)
- Connect users and sync actions
- SQLite backend using SQLAlchemy
- Developer-friendly setup with seeding, testing and CI/CD

---

## 📂 Project Structure

```tree
project/
├── README.md                # Project overview and setup instructions
├── pyproject.toml           # Poetry configuration (dependencies, scripts, formatting)
├── poetry.lock              # Poetry lockfile
├── .gitignore               # Files/folders to ignore in version control
├── main.py                  # (Optional) App entry point
├── app/                     # Main application package
│   ├── __init__.py
│   ├── assets/              # Static assets (if needed later)
│   ├── config.py            # App configuration (e.g. DB URL)
│   ├── database/            # Database logic and models
│   │   ├── base.py
│   │   ├── db.py
│   │   ├── mixins/          # Shared utilities (e.g. serializer)
│   │   └── model/           # SQLAlchemy ORM models
│   ├── devtools/            # Developer utilities (seed data etc.)
│   │   └── todone_dev.db    # Local development database
│   ├── services/            # Business logic (KPI, sync, notifications)
│   ├── ui/                  # UI components and screens
│   └── utils/               # General helper functions
└── tests/                   # Automated tests (pytest)
    └── test_core.py
```

---

## 📥 Getting Started

### Install dependencies

```bash
poetry install
```

### Initialize database + add demo data

```bash
poetry run seed (alternatively: poetry run python -m app.devtools.populate_seed_data)
```

### Run tests

```bash
poetry run pytest
```

### Format code (optional)

```bash
poetry run black .
poetry run isort .
```

---

## ⚙️ Development Tools

- **Poetry** → dependency and script management
- **Black + isort** → automatic code formatting
- **Pre-commit hook (optional)** → enforce formatting on commit
- **VSCode recommended extensions** → Python, Black Formatter, Material Icon Theme
- **GitHub Actions** → automatic CI for tests + formatting checks

---

## ✅ GitHub CI Status

```markdown
![CI](https://github.com/AnFrBo/ToDone/actions/workflows/ci.yml/badge.svg)
```

---

## 🚧 Roadmap

- Frontend / UI integration (Kivy, mobile or web)
- Advanced KPI visualizations
- Gamification features (points, badges, streaks)
- User invites and permissions
- Sync across devices

---

## 🤝 Contributing

This project is in early development.  
Feel free to fork, submit PRs, or suggest features and improvements via issues.

---

## 📄 License

This project is licensed under the **Apache License 2.0**.  
You may use, distribute, and modify this software under the terms of the license.

See [LICENSE](./LICENSE) for full details.
