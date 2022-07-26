# Readme
	
## Require
    - Python 3.8
    

## Install
- Create environment (https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) 
    on Windows using CMD (run as admin)

        + Install virtualenv
            $ python -m pip install --user virtualenv
        + Creating a virtual environment
            $ python -m venv venv
        + Activate a virtual environment
            $ .\venv\Scripts\activate
        + Leave the virtual environment
            $ deactivate

- Install (create env before run install.sh
    > $ ./tools/install.sh
## Config
- Enter Username and Password correct for test into "env.ini" file

    
## Run
- Browser list: Chrome, Opera, Firefox, Edge, Safari. Browser default is Chrome
- Use one of the commands to run

    >  .\venv\Scripts\python main.py
    
    > .\venv\Scripts\pytest main.py

    > .\venv\Scripts\pytest main.py --browser=Firefox

## Run + Export HTML report
- Install : pip install pytest-html
- Command : pytest -v -s --html=report.html --self-contained-html main.py

