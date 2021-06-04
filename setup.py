from setuptools import setup

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name="Flask",
    install_requires=[
        "Werkzeug @ git+https://github.com/ectoglasses/werkzeug.git#egg=Werkzeug",
        "Jinja2 @ git+https://github.com/ectoglasses/jinja.git#egg=Jinja2",
        "itsdangerous @ git+https://github.com/ectoglasses/itsdangerous.git#egg=itsdangerous",
        "click @ git+https://github.com/ectoglasses/click.git#egg=click",
    ],
    extras_require={
        "async": ["asgiref >= 3.2"],
        "dotenv": ["python-dotenv"],
    },
)
