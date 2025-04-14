## Setup

If you don't yet have a .venv directory (which will be the case on first checkout)
```shell
python3 -m venv .venv
```

```shell
source .venv/bin/activate
pip install -r requirements.txt
playwright install
```

## Run Unit Tests

Run the entire unit test suite:

```shell
pytest
```
Run unit tests on change

```shell
ptw
```

## Run Functional Tests

By default the functional tests run in headless mode:

```shell
behave
```

To show the browser while running and slow it down by 1,000 ms per call so a human can see what is happening: 

```shell
HEADLESS=false SLOW_BY=1000 behave
```

You can also change the location of the application you are testing using the BASE_URL environment variable. 

This is used to point at the site on different environments such as development, test, production, etc. By default this is set to http://localhost:5063/

```shell
BASE_URL="http://example.org:1234" behave
```

