COMET Members Information
=========================

Publishing your data on CEDA Archive
------------------------------------

This section will show how to publish your data at CEDA Archive,
get DOI and direct link, and what to do further
(basically, we encourage you to have COMET results shared through EPOS system, just let us know)

steps
^^^^^
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
