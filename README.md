# RESTful_CRUD_API
A RESTful implementation of CRUD API using Django rest_framework + MySql

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the modules.


Also install [MySql server](https://dev.mysql.com/downloads/mysql/) for the MySql database.

Chage the DATABASE details in settings.py

```bash
pip install -r requirements.txt
```
## Usage

Create the customer database in MySql

Run the manage.py in localhost:8000

```bash
python manage.py runserver localhost:8000
```
### Methods

On any web browser, to access the browsable API

#### GET request
 
 ```bash
 http://localhost:8000/customers/<id>/
 ```
 #### PUT request
 
 ```bash
 http://localhost:8000/customers/<id>/
 ```
#### DELETE request

 ```bash
 http://localhost:8000/customers/<id>/
 ```
#### POST request


 ```bash
 http://localhost:8000/customers/
 ```
