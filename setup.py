from setuptools import setup

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name="Flask",
    install_requires=[
        "Werkzeug @ git+https://github.com/ectoglasses/werkzeug.git#egg=Werkzeug",
        "Jinja2 @ git+https://github.com/ectoglasses/jinja.git#egg=Jinja2",
        "itsdangerous >= 2.0",
        "click >= 8.0",
    ],
    extras_require={
        "async": ["asgiref >= 3.2"],
        "dotenv": ["python-dotenv"],
    },
)
