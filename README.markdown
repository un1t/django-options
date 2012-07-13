# options
Kind of reusable django application. You could use this code for you project,
but you have to modify it for your needs. 

Open options/models.py and modify Options class.

## Installation
    Copy this app to ypu project, then change settings.py

    INSTALLED_APPS = (
        ..
        'options',
    )

    TEMPLATE_CONTEXT_PROCESSORS = (
        ...
        'djtest.options.context_processors.options_cp',
    )

## Usage

### In templates

    {{ options.site_name }}

### In views
    
    from options.models import get_option
    site_name = get_option('site_name')


