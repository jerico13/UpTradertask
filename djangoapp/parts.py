from djangooo import MenuItem
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                ...
                'menu.context_processors.menu_context',  # Add this line
            ],
        },
    },
]
