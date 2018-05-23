# System requirements

* PostgreSQL 9.6.5+
* Python 3.6.5+
* Docker (optional)


# Pipenv 

### Install https://github.com/pypa/pipenv#installation

#### Install deps

    $ pipenv install
    
#### Activate

    $ pipenv shell

 
#### Migrate
    $ pipenv run migrate

#### Server

    $ pipenv run service
      

# Dockerized environment
 
    $ docker-compose -f docker/docker-compose-local.yml up
    
# Examples

Using https://httpie.org/
    
    $ http 0.0.0.0:8080/restaurants
    
    $ http POST 0.0.0.0:8080/restaurants name=Sadhu opens_at=2018-05-23T09:49:30Z closes_at=2018-06-23T09:49:30Z
    
    $ http 0.0.0.0:8080/restaurant/1
    
    $ http PUT 0.0.0.0:8080/restaurant/1 name='Sadhu Sundar'
    
    $ http DELETE 0.0.0.0:8080/restaurants/1

# Tests
    
    $ pipenv run tests
    
    
