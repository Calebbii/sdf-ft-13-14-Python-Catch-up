# sdf-ft-13-14 Python-Catch-up

 
## Technologies Used
This application has been built with the following tools:  

- **Python `v3.9.+`**
- **SQLalchemy `v3.3.3`**
    
    
## Project Setup  
You can set up this repository by following this manual

1. Clone the repository 
    ```{shell}
    git clone https://github.com/Calebbii/sdf-ft-13-14-Python-Catch-up.git
   ```
2. Ensure the Python libraries are set up in your machine
    ```{shell} 
    python3.8 -m venv env
    source env/bin/activate
    pip install requests
   ```
3. Run the application
    ```{shell}
    python script.py
    ```




## Database Setup
Our application uses two main types of databases:

- **PostgreSQL** - Used in all our `development` and `production` environments.
- **SQLite3** - Used when running our tests.

The following section illustrates how to set up PostgreSQL on Debian-based Linux distros `Ubuntu, Parrot, Kali Linux, etc.`<br/>
You can find alternate installation instructions for a different operating system [here](https://www.postgresql.org/download/).

### Step 1 :- Installing PostgreSQL

Postgres is available from the default repositories of all Debian distributions. You can use `apt` for installation.

- Install Postgres
```
$ sudo apt update
$ sudo apt install postgresql postgresql-contrib
```

- Ensure that the server is running using the systemctl start command:
```{shell}
$ sudo systemctl start postgresql.service
```

### Step 2 :- Using PostgreSQL Roles and Databases

- Switch over to the postgres account on your server by typing:
```{shell}
$ sudo -i -u postgres
```
- Access the Postgres prompt immediately by typing:
```{shell}
$ psql
```
- Exit out of the PostgreSQL prompt by typing:
```{shell}
$ \q
```

### Step 3 (`optional`) :- Setting up a custom user role on Postgres
Since the `postgres` user is the default user upon installation, you can set up a new user to access the db with the application.

- Create a new user, make sure you replace `$USER` with the name of the user you want:
```{shell}
$ sudo -u postgres createuser --superuser $USER
```


## Application

### Folder Structure
 
    .
    ├── ...
    ├── python-catchup                  
    │   ├── app.py              
    │   ├── car.py            
    │   ├── students.db            
    │   ├── script.py          
    │   └── ...                 
    └── ...

## Resources
https://www.jetbrains.com/#

