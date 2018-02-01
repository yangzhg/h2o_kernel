h2o_kernel
===========

``h2o_kernel`` is a simple h2o wrapper to Jupyter kernel.

Installation
------------
To install ``h2o_kernel`` from PyPI::

    pip install h2o_kernel
    python -m h2o_kernel.install

Using the H2o kernel
---------------------
**Notebook**: The *New* menu in the notebook should show an option for an H2o notebook.

**Console frontends**: To use it with the console frontends, add ``--kernel h2o`` to
their command line arguments.

**H2O Config**: You can use config file or evn to config h2o cluster addr, all configs are the same with h2o.connect() parameters, priority ``/etc/h2okernelrc`` < ``$HOME/.h2okernelrc`` < ``env``,
environment only can changes url(by H2O_URL), ip(by H2O_IP), port(by H2O_PORT).