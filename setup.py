from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open (file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup (

    name ='END_to_END_ML',
    version = '0.0.1',
    author = 'ik1110',
    author_email = 'ishita.kapoor11@gmail.com',
    packages = find_packages(),
    ## install_requires = ['pandas','numpy','seaborn'], its not feasible to write each and every library here as it is
    ## so we create a function for it
    install_requires = get_requirements('requirements.txt')

)
