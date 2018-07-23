# waldo-chliviu

Script that checks if an image is a subimage of another one.

## Install

* Install OpenCV -
  follow instructions at
  [Opencv docs](https://docs.opencv.org/3.4.1/d7/d9f/tutorial_linux_install.html)

  * Install OpenCV python -
    follow instructions at
    [Opencv tutorial](https://docs.opencv.org/3.4.1/d2/de6/tutorial_py_setup_in_ubuntu.html)

  * To make it work with virtualenv,
    you might need to set `PYTHONPATH`

    ```
    export PYTHONPATH=$PYTHONPATH:/usr/lib/python2.7/dist-packages:/usr/local/lib/python2.7/dist-packages
    ````

    This would make the virtualenv aware
     of the OpenCV Python library installed in `dist`.

* Install Python requirements

  ```
  $ pip install -r requirements.txt
  ```


## Feature development

* Install dev requirements

  ```
  $ pip install -r requirements-dev.txt
  ```

* Running tests

  ```
  $ cd tests
  $ pytest -q test_subimage.py
  ```
