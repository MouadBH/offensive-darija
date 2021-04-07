# offensive-darija

Flask App to consume a Machine Learning model and classify between offensive and no offensive language by writing a sentence.

## Technologies

* [Flask](http://flask.pocoo.org/)
* [keras](https://keras.io)
* [tensorflow](https://www.tensorflow.org/)
* [scikit-learn](https://scikit-learn.org/)
* [pandas](https://pandas.pydata.org/)
* [NLTK](https://www.nltk.org/)

## Deployment

You can either use virtual environments or Docker containers:

### Virtual Environment using Bash

1. Creation of a virtual environments done by executing the command venv
2. Command to activate virtual environment
3. Install dependencies
4. List the libraries installed on your environment
5. Do your work!
6. When you are done, the command to deactivate virtual environment
```
$ python3 -m venv env/
$ source env/bin/activate
(env) $ pip install -r requirements.txt
(env) $ pip freeze
(env) $ ...
(env) $ deactivate
```

### Docker

Build image with Docker Compose using the Makefile's command:
```
$ make build
```

Run the image to start the mongo and web containers:
```
$ make run
```

## Authors

* **Mouad Boulahdoud**
* **Hassan Ait Baha**

### Sponsor
This project sponsored by tea 🥃 & msemen 🧇.