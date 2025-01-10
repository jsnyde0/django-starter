# django-starter
Django with preferred packages like htmx, alpine, tailwind, whitenoise, postgres, docker,...


Generate secret key:
```bash
uv run python -c 'import secrets; print(secrets.token_urlsafe(32))'
```

Install pre-commit and run on all files:
```bash
uv run pre-commit install
uv run pre-commit run --all-files
```

Run tests:
```bash
uv run pytest tests
```

Run ruff:
```bash
uv run ruff check .
uv run ruff format --check .
```
