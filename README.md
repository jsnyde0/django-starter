# django-starter
Django with preferred packages like htmx, alpine, tailwind, whitenoise, postgres, docker,...

## Development Setup

1. Generate secret key:
```bash
uv run python -c 'import secrets; print(secrets.token_urlsafe(32))'
```

2. Set up `.env` file with your credentials (see `.env.example` for reference)


3. Install pre-commit and run on all files:
```bash
uv run pre-commit install
uv run pre-commit run --all-files
```

4. Install frontend dependencies (tailwind, daisyui, flowbite):
```bash
cd node
npm install
```


## Running with Docker (Recommended)
Start the development environment with hot-reloading:
```bash
docker compose up
```

Your app will be available at http://localhost:8000

The development setup includes:
- Hot-reloading for Python code changes
- PostgreSQL database
- Automatic database migrations
- Superuser creation (if specified in .env)

## Frontend Development

Run Tailwind in watch mode (in a separate terminal):
```bash
cd node
npm run build
```

### Using flowbite
Unfortunately when importing Flowbite, you have to convert the Tailwind classes to DaisyUI classes.

Use this prompt with an AI assistant to convert the classes to DaisyUI:

```
Please convert this Flowbite component to use DaisyUI classes. Consider:

1. Color Mapping:
   - Map Flowbite's light/dark theme colors to DaisyUI's base colors
   - Convert background colors (bg-white, bg-gray-*) to bg-base-*
   - Convert text colors to text-base-content with appropriate opacity
   - Ensure proper contrast for the dark theme

2. Component Classes:
   - Replace Flowbite's utility classes with DaisyUI component classes
   - Maintain responsive and interactive states
   - Preserve any data-attributes needed for Flowbite's JavaScript

3. Structure:
   - Use DaisyUI's semantic component structure (menu, dropdown, etc.)
   - Keep accessibility attributes
   - Maintain responsive breakpoints

Example mapping:
- bg-white → bg-base-100
- dark:bg-gray-900 → bg-base-300
- text-gray-500 → text-base-content/70
- shadow-lg → shadow-xl
```

This will help maintain consistent styling while leveraging both DaisyUI's theming and Flowbite's JavaScript functionality.

## Quality Checks

Run tests:
```bash
uv run pytest tests
```

Run code formatting:
```bash
uv run ruff check .
uv run ruff format --check .
```

## Running Without Docker

If you prefer to run without Docker:

1. Set up a PostgreSQL database locally
2. Run migrations:
```bash
uv run python manage.py migrate
```

3. Create superuser:
```bash
uv run python manage.py createsuperuser
```

4. Run development server:
```bash
uv run python manage.py runserver
```

## Email Setup

For email notifications to work, you need to:
- set up an email account and add the credentials to the `.env` file.
- set the domain your app is running on in the django admin -> Sites -> Sites -> example.com

If you want to use Google's SMTP server, you need to create an app password for the account you want to use and add it to the `.env` file.
