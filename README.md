# Akademize TDD project setup

**TDD** _Test Driven Development_

## Setting up project

```bash
$ python --version
Python 3.7.6
```

```bash
$ python -m pip --version
pip 20.3 from /Users/sravan/opt/anaconda3/lib/python3.7/site-packages/pip (python 3.7)

```

### Create a virtual environment

The below command creates a python virtual environment in a folder named .venv

```bash
python -m venv .venv
```

### Activate the Virtual environment - Unix Based systems

```bash
$ source .venv/bin/activate
(.venv) $
```

### Activate the Virtual environment - Windows

```bash
$ .venv\scripts\activate
(.venv) $
```

### Install the package pyTest using pip

```bash
$ python -m pip install pytest
Collecting pytest
  Using cached https://files.pythonhosted.org/packages/d7/15/5ef931cbd22585865aad0ea025162545b53af9319cf38542e0b7981d5
  ....
  ....
  ...

```

## Run tests

```bash
(.venv) $ pytest
===================================== test session starts =====================================
platform darwin -- Python 3.7.6, pytest-5.4.2, py-1.8.1, pluggy-0.13.1
rootdir: /Users/sravan/workapce/akademize/akademize-naadam
plugins: hypothesis-5.5.4, arraydiff-0.3, remotedata-0.3.2, openfiles-0.4.0, doctestplus-0.5.0, astropy-header-0.1.2
collected 1 item

src/test_sample.py F                                                                    [100%]

========================================== FAILURES ===========================================
__________________________________________ test_inc ___________________________________________

    def test_inc():
        """Test Increment."""
>       assert inc(3) == 5
E       assert 4 == 5
E        +  where 4 = inc(3)

src/test_sample.py:11: AssertionError
=================================== short test summary info ===================================
FAILED src/test_sample.py::test_inc - assert 4 == 5
====================================== 1 failed in 0.49s ======================================

```

## Run tests with coverage

```bash
pytest --cov=src --cov-report html
```
