from setuptools import find_packages,setup
from typing import List
HYPHEN_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    Docstring for get_requirements
    
    :param file_path: Description
    :type file_path: str
    :return: Description
    :rtype: List[str]
    This function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ") for req in requirements]

        if HYPHEN_DOT in requirements:
            requirements.remove(HYPHEN_DOT)

    return requirements

setup(
    name="ml_project",
    version="0.0.1",
    author="Rahul Giri",
    author_email="rahul22035662@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
