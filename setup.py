from setuptools import find_packages,setup

setup(
    name='mcq_generator',
    version='0.0.1',
    author='shailesh singh',
    author_email='shaileshsingh121122.gmail.com',
    install_requires= ["cohere", "langchain", "streamlit", "python-dotenv", "PyPDF2" ,"langchain_cohere"],
    packages=find_packages()
)