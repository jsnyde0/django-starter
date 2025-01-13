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

install tailwind, daisyui, flowbite:
```bash
cd node
uv run npm install
```

Run tailwind in watch mode for development:
```bash
uv run npm run build_minified
```

Don't forget to collect static files for deployment:
```bash
uv run python manage.py collectstatic
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

## Running locally
Set up `.env` file with your secret key, see `.env.example` for reference.

If it's the first time running the project, you need to run the migrations and create a superuser:
```bash
uv run python manage.py migrate
uv run python manage.py createsuperuser
```

Run local development server:
```bash
uv run python manage.py runserver
```

For email notifications to work, you need to set up an email account and add the credentials to the `.env` file. Also set the domain your app is running on in the django admin -> Sites -> Sites -> example.com.
If you want to use Google's SMTP server, you need to create an app password for the account you want to use and add it to the `.env` file.
