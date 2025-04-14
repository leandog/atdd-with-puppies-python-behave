## Setup

If you don't yet have a .venv directory (which will typically be the case on first checkout)

```shell
python3 -m venv .venv
```


Setup your virtual environment and install dependencies:

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

Run unit tests every time a file changes:

```shell
ptw
```

## Run Functional Tests

By default, the functional tests run in headless mode:

```shell
behave
```

To show the browser while running and slow it down by 1,000 ms per call so a human can see what is happening: 

```shell
HEADLESS=false SLOW_BY=1000 behave
```

You can also change the location of the application you are testing using the BASE_URL environment variable. 

This is used to point at the site on different environments such as development, test, production, etc. By default, this is set to http://localhost:5063/

```shell
BASE_URL="http://example.org:1234" behave
```

## Formatting

Format all files:

```shell
ruff format
```

Check if all files are properly formatted and return a non-zero exit code if they are not:

```shell
ruff format --check
```

## Linting

Lint the application's code:

```shell
ruff check
```

Lint and automatically fix any errors it can safely:

```shell
ruff check --fix
```
