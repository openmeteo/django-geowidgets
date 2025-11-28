=================
django-geowidgets
=================


.. image:: https://img.shields.io/pypi/v/django-geowidgets.svg
    :target: https://pypi.python.org/pypi/django-geowidgets

.. image:: https://github.com/openmeteo/django-geowidgets/actions/workflows/run-tests.yml/badge.svg
    :alt: Build button
    :target: https://github.com/openmeteo/django-geowidgets/actions/workflows/run-tests.yml

.. image:: https://codecov.io/github/openmeteo/django-geowidgets/coverage.svg
    :target: https://codecov.io/gh/openmeteo/django-geowidgets
    :alt: Coverage

Currently this only contains ``LatLonWidget`` and ``LatLonField``.
``LatLonWidget`` is a simple ``MultiWidget`` showing latitude and
longitude. ``LatLonField`` is a form field that by default uses
``LatLonWidget``.

::

   from django import forms

   from geowidgets import LatLonField

   from . import models


   class MyForm(forms.ModelForm):
       location = LatLonField(
           label="Co-ordinates",
           help_text="Longitude and latitude in decimal degrees",
       )

       class Meta:
           model = models.MyModel


django-geowidgets is free software, available under the GNU General
Public License v3. See the LICENCE file for details.
