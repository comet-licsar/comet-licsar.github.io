.. include:: links.rst

Documentation
=============

Currently, most COMET LiCSAR documentation is stored in a GitLab wiki at:

  https://gitlab.com/comet_licsar/licsar_documentation/-/wikis/home.

This wiki contains quite a lot of useful information, and the GitLab wiki renders the content in an easily readable format.

The markdown format used by the wiki makes creating documentation fairly quick and simple.

There is already interest in the group to further improve the documentation of the COMET LiCSAR activities and interest in the benefits which may be gained by making use of Sphinx and Read The Docs.

Sphinx And Read The Docs
------------------------

`Read The Docs`_ is a documentation hosting platform which generates documentation written with the `Sphinx`_ documentation generator

A set of documentation hosted using the Read The Docs service is know as a *Project*.

A Read The Docs account can easily be linked with a repository hosted on GitHub or GitLab, which allows the documentation to automatically be rebuilt and updated when changes are made.

Sphinx
------

Sphinx is a documentation generator, which is able to generate formatted documentation in a range of formats (HTML, PDF, etc.) from plain text source files.

Sphinx was originally created to produce the Python documentation, and has become a widely used tool for generating documentation.

Examples
~~~~~~~~

Some example of Sphinx generated documentation

* `Matplotlib Documentation`_
* `QGIS Documentation`_
* `NCAS UM Training`_

Many more listed at the `Sphinx Examples`_

Getting Started
~~~~~~~~~~~~~~~

Sphinx documentation can be created on a local machine using the ``sphinx`` Python library.

This library can be installed in an anaconda environment using the ``conda`` command::

  conda install sphinx

The library can also be installed using ``pip``::

  pip install sphinx

The Read The Docs theme is also available for install using either ``conda`` or ``pip`` and can be useful for generating HTML documentation::

  conda install sphinx_rtd_theme

or::

  pip install sphinx_rtd_theme

A skeleton Sphinx project can be created with the command::

 sphinx-quickstart

This will prompt for some information, such as the name of the project, and create the required files to get started, most notably the files:

* ``source/conf.py``
* ``source/index.rst``
* ``Makefile``

The first is the configuration file where various project parameters are set, such as the theme for HTML documentation::

  html_theme = 'sphinx_rtd_theme'

The second is a sample index file for the documentation, and the third is the ``Makefile`` which can be used to build the documentation, for example to build HTML output::

  make html

RST Files
---------

By default, Sphinx uses the *rst* (`reStructuredText`_) format for generating documentation.

The rst format was developed for writing documentation. There are numerous markup options available such as using asterisks to emphasise text::

  *emphasised text*

will be rendered as:

*emphasised text*

The Sphinx web pages include a useful rst primer:

* `reStructuredText Primer`_

The rst web pages include detailed information regarding markup specification and available directives:

* `RST Markup Specification`_
* `RST Directives`_

Autodoc
-------

The *autodoc* feature of Sphinx can be used to automatically generate documentation from docstrings in Python code.

To enable this feature the autodoc extension first needs to be enabled in the ``conf.py`` file::

  extensions = ['sphinx.ext.autodoc']

Sphinx also needs to be able to import the Python code from which the documentation should be generated, so it will likely also be necessary to make sure the directory containing the Python code is in the Python path.

This can be done in ``conf.py`` file, and the default file contains a (commented) example:

.. code:: python

  # If extensions (or modules to document with autodoc) are in another directory,
  # add these directories to sys.path here. If the directory is relative to the
  # documentation root, use os.path.abspath to make it absolute, like shown here.
  #
  # import os
  # import sys
  # sys.path.insert(0, os.path.abspath('.'))

In the above example, the current directory (``.``), relative to the documentation root is added to the path.

Documenting The Python Code
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Python code documentation can be included in docstrings, for example this function includes a docstring describing it can be used:

.. code:: python

  def function_a(arg_a, arg_b):
      """
      This is function a, which adds two values 
  
      :param arg_a: first argument is a ``float``
      :param arg_b: second argument in an ``int``
      :return: arg_a + arg_b
  
      Example usage::
  
        >>> from python_library import function_a
        >>> function_a(2, 3)
        5
      """
      return arg_a + arg_b

This will produce documentation which renders as:

.. py:function:: python_library.function_a(arg_a, arg_b)
  :noindex:

  This is function a, which adds two values

  :param arg_a: first argument is a ``float``
  :param arg_b: second argument in an ``int``
  :return: arg_a + arg_b

  Example usage::

    >>> from python_library import function_a
    >>> function_a(2, 3)
    5

To include autogenerated documentation, there are various methods available (see the `Sphinx Autodoc Documentation`_), for example, to include documentation for all members of the Python library ``python_library``::

  .. automodule:: python_library
      :members:

Building The Documentation
--------------------------

The documentation can be built by running the ``make`` command in the documentation source directory.

By default, ``make help`` will be run, which will display information about how to build various targets::

  $ make 
  Sphinx v4.4.0
  Please use `make target' where target is one of
    html        to make standalone HTML files
    dirhtml     to make HTML files named index.html in directories
    singlehtml  to make a single large HTML file
  ...

For example, to build HTML documentation, run::

  make html

This will produce create HTML files in the ``build`` directory::

  $ make html
  Running Sphinx v4.4.0
  loading pickled environment... done
  building [mo]: targets for 0 po files that are out of date
  building [html]: targets for 1 source files that are out of date
  ...
  build succeeded.

  The HTML pages are in build/html.

Hosting HTML Documentation On The Web
-------------------------------------

Once HTML documentation has been generated it can be hosted on the web in various ways.

The content of the HTML directory could be copied to any web server and requires no special server capabilities.

Documentation can also be hosted using popular services such as GitHub, GitLab and Read The Docs.

Read The Docs
~~~~~~~~~~~~~

The `Read The Docs`_ service provides a service for building and hosting Sphinx documentation.

Once an account has been created, this can be linked with a GitHub or GitLab account, which then allows a Read The Docs project to be created from a repository hosted on one of these services.

A Read The Docs project requires a unique name, with the documentation being published at *https://project-name.readthedocs.io/*.

When integrated with a GitHub or GitLab repository, each time the repository is updated, the documentation will be rebuilt and updated.

The Read The Docs service will search the repository for the ``conf.py`` and use this to build the documentation.

There are various options available via the Read The Docs interface, such the branch in the repository from which the documentation will be built.

Git tags will be recognised, and by default the most recent tag will be labelled as *stable* and the most recent commit labelled as *latest*.

Documentation builds can be triggered for additional versions (from Git tags), and so it is possible to have multiple versions of the documentation available, such as:

* https://project-name.readthedocs.io/en/latest/
* https://project-name.readthedocs.io/en/stable/
* https://project-name.readthedocs.io/en/v0.1/

GitHub
~~~~~~

The `GitHub Pages`_ allows web content to easily be created and served from a GitHub repository.

The Pages service can be enabled in the repository settings, for example to make the content of:

  https://github.com/username/repo-name

available at:

  https://username.github.io/repo-name.

The simplest way to host HTML documentation with GitHub pages would be to build the files on a local machine, and then commit and push to a GitHub repository.

A more automated method is possible using GitHub workflows. If a repository contains the Sphinx source files, a workflow can be created to automatically build and publish the documentation when the repository is updated.

The source of this documentation is stored on GitHub at:

  https://github.com/cemacrr/sphinx-rtd

This repository contains a ``.github/workflows`` directory, where the `GitHub pages.yml`_ file  contains the instructions for building the documentation, which includes building the documentation with Python and then pushing the built HTML files to the ``gh-pages`` branch, which is then available at:

  https://cemacrr.github.io/sphinx-rtd/

GitLab
~~~~~~

GitLab also offers a `GitLab Pages`_ service, very similar to the GitHub service.

The GitLab service is not quite so simple to use, and requires creating a ``.gitlab-ci.yml`` file, which works in a similar way to the GitHub workflows, containing instructions on how to build the web content.

At present, it seems it is not currently possible to to use the GitLab CI service without first registering a credit card with GitLab ...

Similar to GitHub, it would be possible to either build the HTML files locally and the commit and push to GitLab, or to have the HTML documentation built automatically when changes are made to the repository. An example of how to automate the Sphinx build with GitLab can be found at the `GitLab Pages Sphinx`_ documentation.
