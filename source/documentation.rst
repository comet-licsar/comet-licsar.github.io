.. .. include:: links.rst

Advanced and specific use
=========================

Manual update of hires volcano time series
------------------------------------------

**Processing steps:**

1. Identify volcano ID (e.g. on COMET Volcano Portal: https://comet.nerc.ac.uk/comet-volcano-portal/volcano-index/Search-All  - the number after the volc name upon opening)

2. On any sciX.jasmin.ac.uk server, after loading LiCSAR env/module, run autoupdate LiCSAR procedure using:

``volq_process.sh -L -v YOUR_VOLCANO_ID``

This will check if there is any new unprocessed acquisition and request/download needed data and start LiCSAR processing (running in the background through LOTUS computing nodes) of all frames containing the volcano, ending in up-to-date data stored to the system.
This might finish in a day, check command ``bjobs`` to see status of processing jobs in LOTUS.
The general processing log file is in $BATCH_CACHE_DIR/VOLCLIP.frames.log.FRAME.
Data are automatically clipped to predefined high resolution subsets.

3. Once the data are on portal, you can proceed generating time series using LiCSBAS.
Same command but in time series regime (rather than -L for LiCSAR regime):

``volq_process.sh -v YOUR_VOLCANO_ID``

This will have LOTUS run up-to-date version of LiCSBAS with settings currently considered reliable (without experimental functionality)
on high resolution subsets for all related frames. By default, it will produce dense ifg network (Tien Shan strategy)
and unwrap by lics_unwrap.py (modified STAMPS-Goldstein filter-supported) and process to 30 m resolution datacube.

You should then find your results (and processing status) in your
$BATCH_CACHE_DIR/subsets/per_volcano/YOUR_VOLCANO_ID


**Some more details:**

Each volcano has its unique ID and is linked to at least one volcano clip definition (volclip) that is by default 25x25 km.
If you know your volclip, you can provide it instead of volcano ID, see ``volq_process.sh`` for help.
The operations over volcano database use functionality provided by volcdb python library (licsar_proc), e.g.
to find volcano ID based on name, you can try:

``import volcdb; volcdb.find_volcano_by_name('ernandina')``

The time series procedure (step 3) is copying clipped RSLCs to $BATCH_CACHE_DIR/subsets,
generates ifgs in extended network (with 3-,6-,12-months connections) and then unwraps them prior to LiCSBAS processing.
It will use existing (reunwrapped) interferograms if it finds them in expected path ($BATCH_CACHE_DIR/subsets).
However, the inversion itself (LiCSBAS) will run from the start (ongoing dev towards incremental updates).


For admins
==========

Notes about documentation
-------------------------

The source files for this page are located at https://github.com/comet-licsar/comet-licsar.github.io


Documentation can be updated simply by editing the rst files in the 'source' folder.
After commit, github would auto-recreate web page of https://comet-licsar.github.io .


Earthquake Responder
--------------------

This section will be moved to a better place. Now, only few comments:
1. the table for limits in selection of an EQ to process is:
::python
    from earthquake_responder import eq_limits; eq_limits

2. if the eq is below the thresholds, you can force-ingest it by adding its USGS ID to ``$LiCSAR_public/EQ/exceptions.txt``


How do I..
----------

clone and edit the docs
^^^^^^^^^^^^^^^^^^^^^^^

few steps are needed to clone and set the docs on your computer. first of all, you should set in github page, in Settings of your profile an up-to-date ssh key, formed with the email that is registered with your profile (you may add more emails in github profile settings, it works).

you may do e.g.
::
    ssh-keygen -t ed25519 -f ~/.ssh/id_ed -C "YOURUSERNAME@leeds.ac.uk"

then edit your ~/.ssh/config to contain:
::
    Host github.com
      IdentityFile ~/.ssh/id_ed
      IdentitiesOnly yes

Afterwards, you can just enter some directory and clone (and set) the repo there using:
::
    git clone git@github.com:comet-licsar/comet-licsar.github.io.git
    cd comet-licsar.github.io
    git remote set-url origin git@github.com:comet-licsar/comet-licsar.github.io.git

ok, then you're set and you can edit and push changes (if you are maintainer) as usual.


prepare hi res frames
^^^^^^^^^^^^^^^^^^^^^

say we have an AOI as e.g.

::
    import framecare as fc
    lat1,lon1 = 51.1, 15.7
    lat2,lon2 = 51.8, 16.5
    
    # first get bursts over that AOI, e.g. as:
    bursts = fc.lq.get_bursts_in_polygon(lon1,lon2,lat1,lat2)
    bursts = fc.lq.sql2outlist(bursts)
    
    # now manually check the bursts and select only 1 relorb related..
    bursts = ....
    
    # then generate high res frame with the AOI
    fc.generate_new_frame(bursts, testonly=False, hicode='H')
  

Afterwards initialize the new frame with parameter -C, i.e.:

::
    licsar_initialize_frame.sh -C 15.7/16.5/51.1/51.8 022A_0142H_000203


prepare hi res subframes
^^^^^^^^^^^^^^^^^^^^^^^^

I know this sounds as duplicate - but it is not.
While the above commands would create new hires frame (that will be normally processed through licsar_make_frame.sh etc.),
it is often much better just to crop existing large frame, as this will ensure correct SD estimation, and generally decrease
doubled processing needs.

Now, this is finally prepared in the way that once you initialise such subset (as shown below),
the RSLCs will then automatically get updated/clipped once the frame is processed and you run `store_to_curdir.sh`.

The frame subsets will reside in $LiCSAR_procdir/subsets

Let me show the current approach through real example..

Due to earthquake near to SAREZ dam (!!!! a nightmare for middle East for the last 100 years), John Elliott requested hires frames.
He defined the region as (lons/lats): 72.510/72.845/38.130/38.365.
Thus, let's get frames and initialise their subsets using:

::
    import framecare as fc
    frames=fc.lq.get_frames_in_lonlat(72.7,38.2)
    # returns: (('005D_05199_131313',), ('100A_05236_141313',))
    for frame in frames:
        fc.subset_initialise_corners(frame, 72.510, 72.845, 38.130, 38.365, 'SAREZ')

and that's it. Now you may proceed just to process the frames as usual.
Note that this will not generate interferograms. But this can be done simply by running `framebatch_gapfill.sh`
(more instructions later, or ask Lin Shen for advice).

If this is only one-off procedure (no need to store in `subsets` folder), you may also just 
run in their `$BATCH_CACHE_DIR/$frame` following command that will also generate interferograms:

::
    clip_slc.sh SAREZ_005D 72.510 72.845 38.130 38.365 0 0.00027 1


LiCSAR things admin
-------------------

request binder resources for COMET InSAR Workshop
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Request an issue similar to the previous years:
https://github.com/jupyterhub/mybinder.org-deploy/issues/2733


docs writing tips and examples
------------------------------

Examples
~~~~~~~~

Some example of Sphinx generated documentation

* bullet 1
* bullet 2

link to `Sphinx Examples`_


ok, now this is from RSTPAD:

h1
##

h2
**

# h3
# ==

h4
--

h5
^^

**bold**
*italic*
- list
#. numlist
something

s ---- thing

  tab
`link <http://example.com/>`_
.. image:: image
inline ``code is ``this

code block ::

  is
  this block
  is this

highlighted

.. code:: python3

  block
  of
  code
  is
  this

tralala

The library can also be installed using ``pip``::

  pip install sphinx

The rst format was developed for writing documentation. There are numerous markup options available such as using asterisks to emphasise text::

  *emphasised text*

will be rendered as:

*emphasised text*

code example:

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

this::

  $ make 
  Sphinx v4.4.0
  Please use `make target' where target is one of
    html        to make standalone HTML files
    dirhtml     to make HTML files named index.html in directories
    singlehtml  to make a single large HTML file
  ...

For example, to build HTML documentation, run::

  make html


