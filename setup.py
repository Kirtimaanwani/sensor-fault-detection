from setuptools import find_packages, setup

REQUIREMENT_FILE_NAME = "requirements.txt"
HYPHEN_E_DOT = "-e ."
DESCRIPTIONS = "SENSOR FAULT DETECTION"


def get_requirements():
    """
    This function will return list of requirements
    """
    requirement_list = []
    """
    assignment1
    write a code to read requirements.txt file and 
    append each requirements in requirement_list variable
    """

    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list


setup(

    name = "sensor",
    version="0.0.1",
    author = "kirtimaan",
    author_email="sushilsw111@gmail.com",
    description=DESCRIPTIONS,
    packages=find_packages(),
    install_requires= get_requirements() #["pymongo==4.2.0"],

)

