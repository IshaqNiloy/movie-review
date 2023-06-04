# movie-review

### Create virtual environment and activate venv in project

```
virtualenv venv
source venv/bin/activate
```

### Install project dependencies and configure .env file

- Install libraries using requirements.txt

```
make install-requirements
```

- Create .env file and copy .env.sample and update all data

### Create super user

```
make create-super-user
```

### Apply migrations

```
make migrate
```

### Run the server

```
make run
```
