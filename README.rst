===============================
sqlalchemy-pretty-sql
===============================

Given a sqlalchemy query, display a well formatted and highlighted sql code.

Install and usage
=================

.. code-block:: bash

    pip install sqlalchemy-pretty-sql

And then just import the package in your IPython/Jupyter session

.. code-block:: python


    In[3]: import sqlalchemy_pretty_sql
    In[4]: query

After ``sqlalchemy_pretty_sql`` is imported, its ``pretty_sql`` function
is registered to display the sql of any ``sqlalchemy.orm.query.Query`` object.

![](https://user-images.githubusercontent.com/2355719/137128073-7361c3e8-01e6-4a51-82dc-849ffc843d37.png)

