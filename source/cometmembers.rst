COMET Members Information
=========================

COMET InSAR Workshop organising notes
-------------------------------------

For local JupyterHub, contact CEMAC (R. Rigby) in advance - the webpage must be registered prior to the meeting,
and IT ticket must be issued (at least week or two prior to the workshop) so IT team can unblock the webpage in firewall.
Also do not forget to request network access for in-person participants - can be done days before the workshop, at
``https://eva.eduroam.uk``, just press ‘My Groups’, ‘Add Group’, give it a name and an expiry, then wait for the email containing the usernames.

If you decide to continue using mybinder services (still works without issues, in 2025!), then it might be good idea
to request an extension of quota for the event - just raise an issue similar to the previous years:  
https://github.com/jupyterhub/mybinder.org-deploy/issues/2733

Publishing your data on CEDA Archive
------------------------------------

This section will show how to publish your data at CEDA Archive,
get DOI and direct link, and what to do further
(basically, we encourage you to have COMET results shared through EPOS system, just let us know)

steps
^^^^^
1. Organise your data under a ``Jasmin`` folder e.g.,
   ``/gws/nopw/j04/nceo_geohazards_vol1/public/LiCSAR_products/derived_products/Turkey_earthquake/v1.0``
2. Add a ``readme.txt`` to introduce your file structure - this will be in your data archive.
3. Add a completed ``metadata.yaml`` under the same directory - this will populate your data webpage.
4. Open up permission of your folder by typing ``chmod -R 777 * ``
5. Contact CEDA for the DOI. The current point of contact is ``Edward Williamson - STFC UKRI <edward.williamson@stfc.ac.uk>``. 
6. Ed would prepare the online archive and send you a preview, e.g.,
   ``https://data.ceda.ac.uk/neodc/comet/publications_data/Turkey_earthquake/v1.0``
   ``https://catalogue.ceda.ac.uk/uuid/df93e92a3adc46b9a5c4bd3a547cd242``
7. After you've proofread the content, Ed will issue a DOI. 

metadata.yaml
^^^^^
::


  {
    "title": "",
    "description": "equivalent to data abstract",
    "authors": [
      {
        "firstname": "",
        "surname": ""
      },
      {
        "firstname": "",
        "surname": ""
      },
    ],
    "bbox": {
      "north": "geographical coverage of your data",
      "south": "",
      "east": "",
      "west": ""
    },
    "time_range": {
      "start": "yyyy-mm-dd",
      "end": "yyyy-mm-dd"
    },
    "lineage": "equivalent to method section",
    "quality": "",
    "docs": [
      {
        "title": "you can include references or links (such as the comet portal) to particular data set",
        "url": ""
      },
    ],
    "project": {
      "catalogue_url": "",
      "title": "",
      "description": "",
      "PI": {
        "firstname": "",
        "surname": ""
      },
      "funder": "",
      "grant_number": ""
    },
    "instrument": {
      "catalogue_url": "",
      "title": "",
      "description": ""
    },
    "computation": {
      "catalogue_url": "",
      "title": "",
      "description": ""
    }
  }
