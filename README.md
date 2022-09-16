# Sphinx Seeta Theme

This sphinx theme extends the customization of navigation and side bar for the project with complex code structures, e.g., the deep learning framework.

## Installation

Install from PyPI:

```bash
pip install sphinx-seeta-theme
```

Or, clone this repository to local disk and install:

```bash
cd sphinx_seeta_theme && pip instsall .
```

You can also install from the remote repository: 

```bash
pip install git+ssh://git@github.com/seetaresearch/sphinx_seeta_theme.git
```

## Configuration

### Theme options

For example:

```python
html_theme_options = {
    'navbar_links': {
        'Install': '/install/index.html'
        'API': [
            ('master', '/api/master/index.html'),
            ('v1.0.0', '/api/v1.0.0/index.html'),
        ],
        'Github': 'https://github.com/seetaresearch/sphinx_seeta_theme',
    },
    'navbar_logo_link': '/index.html',
    'sidebar_title': 'v1.0.0',
    'sidebar_title_link': '/versions/index.html',
    'breadcrumb_links': [
        ('Project', '/index.html'),
        ('API', '/versions/index.html'),
        ('v1.0.0', '/api/v1.0.0/index.html'),
    ],
}
```

## License
[BSD 2-Clause license](LICENSE)
