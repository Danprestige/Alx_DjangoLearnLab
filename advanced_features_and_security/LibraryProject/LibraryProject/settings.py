from pathlib import Path

# =========================
# BASE DIRECTORY
# =========================
BASE_DIR = Path(__file__).resolve().parent.parent


# =========================
# SECURITY SETTINGS
# =========================

# Strong custom secret key (must NOT start with django-insecure-)
SECRET_KEY = 'a9#Lk29x!PqTz8@WmR7$yHcV6&uN3*eS1^fG0!kLmZxQwErTyUiOpAsDfGhJ'

# Disable debug in production
DEBUG = False

# Must not be empty (ALX requirement)
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


# =========================
# APPLICATION DEFINITION
# =========================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps
    'csp',

    # Local apps
    'bookshelf',
]


# =========================
# MIDDLEWARE CONFIGURATION
# =========================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Required for security headers
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # CSRF protection
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Prevent clickjacking
    'csp.middleware.CSPMiddleware',  # Content Security Policy
]


ROOT_URLCONF = 'LibraryProject.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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


WSGI_APPLICATION = 'LibraryProject.wsgi.application'


# =========================
# DATABASE
# =========================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# =========================
# PASSWORD VALIDATION
# =========================

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# =========================
# INTERNATIONALIZATION
# =========================

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# =========================
# STATIC FILES
# =========================

STATIC_URL = 'static/'


# =========================
# DEFAULT PRIMARY KEY FIELD TYPE
# =========================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# =========================
# EXTRA SECURITY CONFIGURATION
# =========================

# Prevent MIME type sniffing
SECURE_CONTENT_TYPE_NOSNIFF = True

# Enable browser XSS filtering
SECURE_BROWSER_XSS_FILTER = True

# Prevent clickjacking
X_FRAME_OPTIONS = "DENY"

# Secure cookies (HTTPS only in production)
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Content Security Policy (django-csp 4.0+ format)
CONTENT_SECURITY_POLICY = {
    "DIRECTIVES": {
        "default-src": ("'self'",),
        "script-src": ("'self'",),
        "style-src": ("'self'",),
    }
}


# ==========================================================
# PRODUCTION SECURITY SETTINGS - HTTPS ENFORCEMENT
# ==========================================================

# Disable debug mode in production
DEBUG = False

# Allowed hosts (update with your domain in production)
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# ----------------------------------------------------------
# HTTPS REDIRECTION
# ----------------------------------------------------------

# Redirect all HTTP requests to HTTPS
SECURE_SSL_REDIRECT = True

# If the app is behind a reverse proxy (e.g., Nginx),
# this tells Django to trust the X-Forwarded-Proto header
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# ----------------------------------------------------------
# HTTP STRICT TRANSPORT SECURITY (HSTS)
# ----------------------------------------------------------

# Instruct browsers to only access the site via HTTPS for 1 year
SECURE_HSTS_SECONDS = 31536000  # 1 year in seconds

# Apply HSTS policy to all subdomains
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# Allow the site to be included in browser preload lists
SECURE_HSTS_PRELOAD = True


# ----------------------------------------------------------
# SECURE COOKIES
# ----------------------------------------------------------

# Ensure session cookies are only sent over HTTPS
SESSION_COOKIE_SECURE = True

# Ensure CSRF cookies are only sent over HTTPS
CSRF_COOKIE_SECURE = True


# ----------------------------------------------------------
# SECURITY HEADERS
# ----------------------------------------------------------

# Prevent clickjacking attacks
X_FRAME_OPTIONS = "DENY"

# Prevent browsers from MIME-sniffing
SECURE_CONTENT_TYPE_NOSNIFF = True

# Enable browser XSS filtering protection
SECURE_BROWSER_XSS_FILTER = True


# ----------------------------------------------------------
# ADDITIONAL RECOMMENDED SECURITY SETTINGS
# ----------------------------------------------------------

# Prevent session fixation attacks
SESSION_COOKIE_HTTPONLY = True

# CSRF cookie not accessible via JavaScript
CSRF_COOKIE_HTTPONLY = True

# Secure referrer policy
SECURE_REFERRER_POLICY = "same-origin"
