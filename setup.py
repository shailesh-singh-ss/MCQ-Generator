from setuptools import find_packages,setup

setup(
    name='mcq_generator',
    version='0.0.1',
    author='shailesh singh',
    author_email='shaileshsingh121122.gmail.com',
    install_requires= ["openai", "langchain", "stremlit", "python-dotenv", "PyPDF2"],
    packages=find_packages()
)