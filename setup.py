from setuptools import setup

__version__ = "1.0.3"


setup(
    name="PaymeAPI",
    version=__version__,
    keywords=["payme", "paymeapi", "paymeapiuz", "paymeuz"],
    description="Easy and convenient library to create receipts and check the status of the created receipt for https://payme.uz/",
    author="AmoreForever",
    url="https://github.com/AmoreForever/PaymeAPI",
    author_email='me.thefarkhodov@gmail.com',
    license="MIT",
    description_file="README.md",
    license_files=["LICENSE.md"],
    requires=["requests"]
)