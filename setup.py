
from setuptools import setup, version
from discord_template import *

setup(
    name="discord_template",
    description="A new and enhanced boilerplate template for discord.py",
    author=__author__,
    url="https://github.com/znqi/discord_template",
    license=__license__,
    include_package_data=True,
    packages=['discord_template', 'discord_template.env'],
    python_requires=">=3.5",
    version=__version__,
    entry_points = {
        "console_scripts": [
            "discord = discord_template.__main__:run"
        ]
    },
    zip_safe = False,
    install_requires=[
        "jinja2",
        "InquirerPy",
        "requests",
        "tabulate",
        "discord.py"
    ],
)