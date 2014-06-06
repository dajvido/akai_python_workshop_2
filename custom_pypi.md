## Configure pypi to use a custom package repository

Make sure you are using *Python 3.3 or 3.4* i.e.

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
On windows, an you will need to set a HOME environ var.

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
pip install --use-wheel  -i http://<IP>:<PORT>/simple <package>==<version>
```

and upload your package the following way (credentials are verified):

```
python setup.py bdist_wheel upload -r akai_workshop
```



## Setting up pypi-server

In order to setup a package repository:

```
virtualenv --python=/usr/bin/python3.3 pypi_ex
source pypi_ex/bin/activate
pip install pypiserver
pip install passlib
```

Now You need to generate apache-like password file, use can use an online generator, apache utilities etc. A password file for: pypi_user/1qazxsw2 will look as follows:
```
echo "pypi_user:$apr1$s1idturw$meqRELHDbeR/lH00cnGri/" > .htpasswd
```

Create a dir for sotring packages:
```
mkdir packages
```

Run server, and enjoy owning a pypi repository :)

```
pypi-server -p 8888 -P .htpasswd --disable-fallback packages
```
