# Cropwise Live Table (Flask + PostgreSQL)

## 📦 Установка локально
```bash
pip install -r requirements.txt
python app.py
```

## 🚀 Деплой на Render.com
1. Залей этот проект в GitHub
2. На [render.com](https://render.com):
   - Create New → Web Service
   - Укажи свой репозиторий
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python app.py`
3. В настройках добавь Environment Variables:
   - `DB_HOST` (например: your-db-host.render.com)
   - `DB_PORT` (обычно: 5432)
   - `DB_NAME` = `cropwise_database`
   - `DB_USER` = `postgres`
   - `DB_PASSWORD` = `123`