# Codelist Updater

[![Build Status](https://github.com/codeforIATI/codelist-updater/workflows/CI/badge.svg?branch=main)](https://github.com/codeforIATI/codelist-updater/actions?query=workflow%3A%22Run+importers%22)

A daily GitHub Action that checks for updates to various codelists, and sends pull requests when something changes.

## Overview

If a codelist is covered by the codelist updater, this will allow the relevant codelist to be kept up to date in a very streamlined and automated way (updates are made as pull requests to the relevant repository, so that a human can verify and approve them).

There are two codelist repositories that we can update to:
- [codeforIATI/IATI-Codelists-NonEmbedded](https://github.com/codeforIATI/IATI-Codelists-NonEmbedded/): for IATI-recognised replicated codelists
- [codeforIATI/Unofficial-Codelists](https://github.com/codeforIATI/Unofficial-Codelists/): for codelists which are not replicated by IATI, but are useful to users (and often are referenced in various IATI documentation)

Codelists from both of these repositories are visible in the replicated codelists interface: [codelists.codeforiati.org](https://codelists.codeforiati.org)

## Running the importers

To run an individual importer, use e.g.:

```
python -m importers.currency
```

## Adding a codelist

It is now relatively straightforward to add a new codelist here (we're trying to gradually make it even easier).

We generally encourage you to do any scraping or wrangling outside of this repository, and then make pre-processed files available for the codelist updater to check and import nightly if there are any updates.

For example, if you need to scrape a web page to keep a codelist up to date, you can do this on [morph.io](https://morph.io) and then access that data via the morph.io API.

Currently, this is the process:

1. Make a codelist template: this is a codelist with none of the `codelist-item` elements. The easiest way to do this is to copy and rename one of the files in the `templates` folder.
2. Add the (empty) codelist template to the `templates` folder.
3. Create an importer: you can start by copying and renaming an importer from the `importers` folder.
