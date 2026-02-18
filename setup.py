from setuptools import find_packages, setup

setup(
    name="medical_chatbot",
    version="0.1.0",
    author="Neerav",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[]

)