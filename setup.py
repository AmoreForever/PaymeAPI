from setuptools import setup

__version__ = "1.0.4"


setup(
    name="PaymeAPI",
    version=__version__,
    description="Easy and convenient library to create receipts and check the status of the created receipt for https://payme.uz/",
    author="AmoreForever",
    url="https://github.com/AmoreForever/PaymeAPI",
    author_email='me.thefarkhodov@gmail.com',
    license="MIT",
    project_urls={"Source": "https://github.com/AmoreForever/PaymeAPI"},
    package_data={
        "PaymeAPI": ["py.typed"],
    },
    requires=["requests"]
)