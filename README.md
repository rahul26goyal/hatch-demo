# hatch-demo
A repository for learning about Python Distribution Packaging with Hatch

## Create a conda env 
```bash
conda create -n hatch-demo python=3.8.5 
conda activate hatch-demo  
```

## Install Hatch 
```python
pip install hatch
```

## Initialize the repo with hatch 
```python
hatch new "Hatch Demo"
```

## Build 
```python
hatch build
```

## Publishing the package to TestPypi repository.
The first thing you’ll need to do is register an account on TestPyPI, which is a separate instance of the package index intended for testing and experimentation. It’s great for things like this tutorial where we don’t necessarily want to upload to the real index. To register an account, go to https://test.pypi.org/account/register/ and complete the steps on that page. You will also need to verify your email address before you’re able to upload any packages. For more details, see Using [TestPyPI](https://packaging.python.org/en/latest/guides/using-testpypi).
Once created, you should have the username and passowrd handy to publish. 

The link for uploading to testPypi repo is: https://test.pypi.org/legacy/
There are many tools available to publish to pypi. We will explore using `hatch publish` for the same.

1. Using hatch publish command and inline repository args
```python
hatch publish -r https://test.pypi.org/legacy/
```

2. Using the  keywork "test" which is a named repo poiting to TestPypi with hatch publish. Here, we do not have to define where test points to. 
```python
hatch publish -r test
```

3. Specifying the args via environment variable:
```python
export HATCH_INDEX_REPO=https://test.pypi.org/legacy/
export HATCH_INDEX_USER=goyal.1234rahul
export HATCH_INDEX_AUTH=xxxx
# Publish
hatch publish   
```

### Testing the published package
The regular pip install points to the non-test env. So, we need to pass the index-url 
where the test packages are published. The url is different from where it was uploaded. 

```python
pip install --index-url https://test.pypi.org/simple/ hatch-demo

pip list | grep hatch-demo

> python
from hatch_demo import calculation 
calculation.print_version()
```
