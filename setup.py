from setuptools import find_packages,setup
from typing import List


def get_requirements()->List[str]:
    """
    This function will return the list of requirements
    """
    req_list:List[str] = []
    
    try:
        with open("requirements.txt",'r') as file:
            lines = file.readlines() # read the lines from file
            
            for line in lines:
                line = line.strip() # strip the newLine Chars
                
                if line and not line == '-e .':
                    req_list.append(line)
            
    except FileNotFoundError:
        print("requirements.txt file's not Found")
          
    return req_list


# print(get_requirements())

setup(
    name="Network Security",
    version='0.0.1',
    author='Yaswanth Garlapati',
    author_email="saiyaswanthgarlapati006@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)