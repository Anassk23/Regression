from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def getrequirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]


        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='RegressionProject',
    version='0.0.1',
    author='Anas Shaikh',
    author_email='shaikhanas.2012@gmail.command_options',
    install_requires=getrequirements('requirements.txt'),
    packages=find_packages()
)