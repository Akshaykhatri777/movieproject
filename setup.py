from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

AUTHER_NAME = "AKSHAY KHATRI"
SRC_REPO = 'src'
LIST_OF_REQUIREMENTS = ['streamlit']

setup(
    name = SRC_REPO,
    version='0.0.1',
    auther = AUTHER_NAME,
    auther_mail = 'akshkhatri4@gmail.com',
    description='a small example package for movie project',
    long_description= long_description,
    long_description_content_type='text/markdown',
    package = [SRC_REPO],
    python_requires = '>=3.13',
    install_requires = LIST_OF_REQUIREMENTS,
)