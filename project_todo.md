# 📌 ToDone Project TODO

This document tracks the current and planned tasks for the ToDone app development.

---

## ✅ Completed

- Project structure defined and implemented
- SQLAlchemy setup (database, models, sessions)
- Devtools with seed data and development database
- Testing foundation with pytest and tests/ folder
- CI/CD pipeline with GitHub Actions (black, isort, pytest checks)
- Basic README and LICENSE

---

## 🚧 Next Steps

### 1️⃣ Service Layer (Business Logic)

- [ ] Implement KPI calculations (average time, completed actions) in `kpi_service.py`
- [ ] Implement task handling logic (create, query, complete tasks)
- [ ] Implement user connection and management logic

### 2️⃣ UI Layer

- [ ] Connect `dashboard_screen.py` to KPI service
- [ ] Connect `task_screen.py` to task service
- [ ] Add logic to `home_screen.py` to list and create tasks

### 3️⃣ Sync and Persistence (Optional/Next)

- [ ] Implement simple export/import logic in `sync_service.py`
- [ ] Enable local backup and restoration of actions/tasks

### 4️⃣ Testing

- [ ] Write test files for each service (`test_kpi_service.py`, `test_task_service.py`, etc.)
- [ ] Use fixtures or seed data for test preparation
- [ ] Add integration and unit tests
- [ ] (Optional) Add pytest markers for test categorization

### 5️⃣ CI/CD Improvements (Optional/Next)

- [ ] Add pre-commit hook with black and isort
- [ ] Add type checking (mypy) to CI
- [ ] Add coverage reporting to CI

### 6️⃣ Future roadmap

- [ ] Implement frontend (Kivy, web, or mobile)
- [ ] Add gamification logic (points, streaks, badges)
- [ ] User invites and permissions
- [ ] Sync across devices (cloud support)

---

## 📎 Notes

This TODO is updated regularly as progress is made and priorities shift. Focus on service layer and UI next to make the app interactive and usable.
