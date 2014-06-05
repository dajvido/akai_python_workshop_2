## Configure pypi to use a custom package repository

Make sure you are using *python3.3* i.e.

```
virtualenv --python=/usr/bin/python3.3 pypi_ex
source pypi_ex/bin/activate

```

Upgrade pip to a latest version, and install wheels

```
pip install -U pip
pip install wheel

```

Place a .pypirc file in your $HOME directory on linux. 
On windows, an you’ll need to set a HOME environ var.

Please copy this to your *.pypirc* file,
```
[distutils]
index-servers =
    pypi
    akai_workshop

[pypi]
repository: https://pypi.python.org/
username: user
password: pass

[akai_workshop]
repository: http://127.0.0.1:8888/
username: pypi_user
password: 1qazxsw2

```

You can install a wheel package from *akai_workshop* the following way:

```
pip install --use-wheel <package>==<version> -i http://127.0.0.1:8888/simple
```


