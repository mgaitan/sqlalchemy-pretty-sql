===============================
sqlalchemy-pretty-sql
===============================

Given a sqlalchemy query, display a well formatted and highlighted sql code.

Install and usage
=================

.. code-block:: bash

    pip install sqlalchemy-pretty-sql

And then just import the package in your notebook session

.. code-block:: python


    In[3]: import sqlalchemy_pretty_sql
    In[4]: query

After ``sqlalchemy_pretty_sql`` is imported, its ``pretty_sql`` function
is registered to display the sql of any ``sqlalchemy.orm.query.Query`` object.


See the `example <https://github.com/mgaitan/sqlalchemy-pretty-sql/blob/master/example.ipynb>`_.