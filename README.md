# Vend-o-Matic

### Set Up
This application utilizes Flask to create the web server. You will need to have pip installed to download and use Flask. The following setup will install pip in a virtual environment, but if you choose to run it a different way, please see the [pip documentation site](https://pip.pypa.io/en/stable/installation/) for installation instructions. 

- Open folder and navigate to main directory (`/vend-o-matic`)

- Add the virtual environment by running the following in your terminal 
    - (Mac) `python3 -m venv .venv`

    - (Windows) `py -3 -m venv .venv`

- Activate the virtual environment
    - (Mac) `. .venv/bin/activate`

    - (Windows) `.venv\Scripts\activate`

- Install the necessary dependencies
    - `pip install -r requirements.txt`

The server should run on http://127.0.0.1:5000

For testing purposes, the vending machine instantiates with full inventory. This can be altered in the `VendingMachine.py` class file.