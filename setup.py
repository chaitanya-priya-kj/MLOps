from setuptools import find_packages,setup
from typing import List

def get_requirements(path:str)->List[str] :
    requirement = []
    with open(path) as file_obj:
        requirement=file_obj.readlines()
        requirement = [req.replace("/n","") for req in requirement]

        if '-e .' in requirement:
            requirement.remove('-e .')

    return requirement



setup(
    name="MLOps",
    version='0.0.1',
    author='Chai',
    author_email='chaitanya.priyakj@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirement.txt')
)

