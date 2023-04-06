====================
Get HTML from Safari
====================


.. image:: https://img.shields.io/pypi/v/get_html_from_safari.svg
        :target: https://pypi.python.org/pypi/get_html_from_safari

.. image:: https://img.shields.io/travis/sdondley/get_html_from_safari.svg
        :target: https://travis-ci.com/sdondley/get_html_from_safari

.. image:: https://readthedocs.org/projects/get-html-from-safari/badge/?version=latest
        :target: https://get-html-from-safari.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status


Description
-----------

Gets HTML code from web pages open in the Safari browser.

Usage
-----

The get_html_from_safari package fetches the HTML source code of the currently
active Safari browser tab on macOS. This package utilizes AppleScript to
interact with the Safari browser and retrieve the HTML content.

**Example Usage**
To use get_html_from_safari, follow these steps:

Install the package:
::

        pip install get_html_from_safari

Import the package and fetch the HTML source code of the active Safari tab:
::

        from get_html_from_safari import get_html
        html_content = get_html()

You can now process the retrieved HTML content as needed.

To fetch the HTML source code of a specific URL, pass the URL as an argument:
::

        from get_html_from_safari import get_html
        url = "https://www.example.com"
        html_content = get_html(url)

This will open up a new browser window and fetch the HTML source code of the url
specified.

Please note that this package is specifically designed for macOS and the Safari
browser. It will not work with other operating systems or web browsers.

**From the command line:**
::

        $ html-source-get <url>

Requirements
------------

* Python 3.6 or higher
* macOS

Features
--------

Contains an entry point `html-source-get <url>`.

If no url is supplied, it will get the HTML code from the current Safari tab. If
a url is supplied, it will open a new tab and get the HTML code from that tab.

The HTML code is dumped directly to the terminal.

License
-------

* Free software: Apache Software License 2.0

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
