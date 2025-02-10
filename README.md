# Index Client

This project is a home task given by Gosolve. 

## Introduction

This project is a basic CLI written in Python that uses [Index Server API](https://www.github.com/fmoura/index-server) to query indexes given numbers ranging from `0` till `1000000`

## Prerequisites

- Python 3.11 or higher
- Make

## Features

This project showcases the usage of async calls to the API to make parallel queries to the Index Server. It also let the user configure another base url for the Index Server, the default value is http://localhost:8000 for Index Server running locally.

## Development

Clone the repository and navigate to the project directory:

```sh
git clone https://github.com/fmoura/index-client.git
cd index-client
```

It is advised to use a virtual environment. You can create one as follows:

```sh
python python -m venv .venv
```

And the activate it:

```sh
./.venv/bin/activate
```

Then install all the development requirements using:

```sh
make requirements
```


## Run

### Running Index Server locally

If you want to run everything locally make sure you have Docker installed, and the execute the following command:

```sh
make run-index-server
```

## Run Client

Then you can run the Index Client either directly from source, or as a installed python package

### Run directly from source

To run it from source, just execute :

```sh
make run NUM_1 NUM_2 NUM_3
```

### Run as python package

To run it as python package first install package from source. The following command will package and install the module

```sh
make install
```

```sh
python -m index-client NUM_1 NUM_2 NUM_3
```


### Results

Running it as a installed python module or directly from code should yeld the same results. The results should be something like this.
Executing the module like this: 

```sh
python -m index_client.cli 100 110 150 200
```
Should give a result like this

```sh
Index value for 110: {'index': 1, 'value': 100}
Index not found for 150: Value not found
Index value for 200: {'index': 2, 'value': 200}
Index value for 100: {'index': 1, 'value': 100}
```

## Running Tests

To run the tests, use the following command:

```sh
make test
```


## Code Structure

The code follows a simple architecture where the [IndexService](src//index_client/index.py) 
is responsible for making requests and correctly treating responses from the Index Server API. And the [CLI](src/index_client/cli.py) 
is responsible for argument parsing and console output