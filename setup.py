# responsible in creating my machine learning application as a package
# So that it can be used as a package and anyone can use it.
from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []

    HYPHEN_E_DOT  = '-e .'
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]

        if HYPHEN_E_DOT  in requirements:
            requirements.remove(HYPHEN_E_DOT )

    return requirements


setup(
name='ml_project',
version='0.0.1',
author='Rethik',
author_email = 'rbhat@shipbob.com',
packages=find_packages(),
install_requires= get_requirements('requirements.txt')
)




