[![Maintainability](https://api.codeclimate.com/v1/badges/117ac5239a854f8c86df/maintainability)](https://codeclimate.com/github/Abdujabbar/ccwc/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/117ac5239a854f8c86df/test_coverage)](https://codeclimate.com/github/Abdujabbar/ccwc/test_coverage)

About
================

This project is just reimplementation of wc command in Linux.


How to run
================

First you need to clone it from repo. 

```
git clone git@github.com:Abdujabbar/ccwc.git
```


Then you need to run install command:

```
make install
```

After you can run with the next command:

```
poetry run ccwc ...
```


How to install
===================

You need first build package:
```
make build
```

Then you can install the package with the next command:

```
make package-install
```

After you can run with the next command:

```
ccwc -c README.md 
```

Sometimes you can get error, because usually when you install package it will install into your ~/.local/bin/ directory, and cannot be access via command line, in these case you need to add that directory into your global PATH
