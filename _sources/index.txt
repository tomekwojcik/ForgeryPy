.. ForgeryPy documentation master file, created by
   sphinx-quickstart on Wed Jul 11 20:31:25 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

ForgeryPy documentation
=======================

ForgeryPy is an easy to use forged data generator. It's a (somewhat incomplete)
port of `forgery Ruby gem <http://rubygems.org/gems/forgery>`_.


Example usage
-------------

>>> import forgery_py
>>> forgery_py.address.street_address()
u'4358 Shopko Junction'
>>> forgery_py.basic.hex_color()
'3F0A59'
>>> forgery_py.currency.description()
u'Slovenia Tolars'
>>> forgery_py.date.date()
datetime.date(2012, 7, 27)
>>> forgery_py.internet.email_address()
u'brian@zazio.mil'
>>> forgery_py.lorem_ipsum.title()
u'Pretium nam rhoncus ultrices!'
>>> forgery_py.name.full_name()
u'Mary Peters'
>>> forgery_py.personal.language()
u'Hungarian'


Modules
=======

.. toctree::

   address
   basic
   currency
   date
   internet
   lorem_ipsum
   name
   personal


Source code and license
=======================

Much like the original Ruby gem this module is licensed under MIT License.

Source code is available `on GitHub <https://github.com/tomekwojcik/ForgeryPy>`_.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

