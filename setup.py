from setuptools import setup

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name="Flask",
    install_requires=[
        "Werkzeug @ git+ssh://git@github.com:ectoglasses/werkzeug.git@v2.0#egg=Werkzeug",
        "Jinja2 >= 3.0",
        "itsdangerous >= 2.0",
        "click >= 8.0",
    ],
    extras_require={
        "async": ["asgiref >= 3.2"],
        "dotenv": ["python-dotenv"],
    },
)
