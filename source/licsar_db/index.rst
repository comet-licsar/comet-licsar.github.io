LiCSInfo db
===========

Here we describe the LiCSInfo database that plays a key role in LiCSAR processing chain, especially in the LiCSAR FrameBatch solutions.
For overall description, you may visit `article about LiCSAR system <https://doi.org/10.3390/rs12152430>`_ - we build on top of the existing architecture.

In brief, as our frames are defined based on unique Sentinel-1 burst identifiers (that were not existing in the first years of S1 existence), we built a MySQL/MariaDB database that would link Sentinel-1 SLC zip files with their bursts and the LiCSAR frame definitions (polygs) - a LiCSInfo database. We further extended the database to contain geometric information (polygs2geom and bursts2geom are geodatabase tables) and some other relevant information, for example the ``esd`` table contains frame-scale offsets to measure development of tectonic plates (through `daz <https://comet-licsar.github.io/daz/index.html>`_ tool). See the 'base metadata' block at figure below:


.. image:: ../../images/licsinfo.png
   :width: 600
   :alt: Basic flowchart of LiCSInfo database

Further on, the LiCSBatch processing database uses a view (a link) to the base metadata of LiCSInfo database and links requested files (through frames-bursts-files joins) with LiCSAR FrameBatch processing jobs that control frame-based processing from SLC files through coregistration to RSLCs to generation of (unwrapped) interferograms, in given configuration.

Finally, we implemented additional tables related to the LiCSAR Earthquake InSAR Data Provider (for rapid generation of coseismic interferograms covering significant earthquakes) and LiCSVolc tables to map frame subsets with active volcanoes (currently under development).

The LiCSInfo database solution is at the core of LiCSAR and was deployed in other systems as well, including `Czech IT4S1 <https://www.mdpi.com/2072-4292/12/18/2960>`_ solution (combining LiCSInfo-ISCE-STAMPS for open-source nation-wide Sentinel-1 InSAR). We can provide the database codes upon request.

For tools to directly access information in LiCSInfo, see API of LiCSAR_proc and LiCSAR_framebatch (e.g. ``framecare`` python library).
