Website dedicated to the COMET LiCSAR system that generates interferometric products from Sentinel-1 satellite mission.
The primary objective of LiCSAR is to measure and monitor terrain deformation over tectonic and volcanic areas,
and provide relevant and timely information to Earth-centered researchers.

Our data are freely available through the `COMET LiCSAR Portals <https://comet.nerc.ac.uk/COMET-LiCS-portal/>`_.
For more information about the LiCSAR products, please visit `LiCSAR Product Details <https://comet.nerc.ac.uk/comet-lics-portal-product-details/>`_.
Here we focus on the `LiCSAR processing architecture <https://www.mdpi.com/2072-4292/12/15/2430>`_, document some of the tools that might be of general interest,
and provide necessary information for our students and postdocs.

The architecture of the LiCSAR system, with some relevant information, is schematised in the image below.
The system contains set of tools to operate on Sentinel-1 SLC data, ingested to LiCSInfo database.
We name the core set of processing tools (on top of GAMMA software) as ``LiCSAR proc``, while ``LiCSAR Framebatch`` focuses on systematic processing in LiCSAR frames.

.. image:: images/licsar_arch.png
   :width: 600
   :alt: Scheme of the LiCSAR system architecture