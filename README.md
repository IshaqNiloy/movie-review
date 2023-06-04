# movie-review

1. Create virtual environment and activate venv in project

```
virtualenv venv
source venv/bin/activate
```

2. Install project dependencies and configure .env file

- Install libraries using requirements.txt

```
make install-requirements
```

- Create .env file and copy .env.sample and update all data

# Create super user

```
make create-super-user
```

# Run the server

```
make run
```
