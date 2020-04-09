# Codelist Updater

[![Build Status](https://travis-ci.com/codeforIATI/codelist-updater.svg?branch=master)](https://travis-ci.com/codeforIATI/codelist-updater)

A set of daily Travis CI cron jobs that check for updates to various codelists, and send pull requests when something changes.

## Overview

If a codelist is covered by the codelist updater, this will allow the relevant codelist to be kept up to date in a very streamlined and automated way (updates are made as pull requests to the relevant repository, so that a human can verify and approve them).

There are two codelist repositories that we can update to:
- [codeforIATI/IATI-Codelists-NonEmbedded](https://github.com/codeforIATI/IATI-Codelists-NonEmbedded/): for IATI-recognised replicated codelists
- [codeforIATI/Unofficial-Codelists](https://github.com/codeforIATI/Unofficial-Codelists/): for codelists which are not replicated by IATI, but are useful to users (and often are referenced in various IATI documentation)

Codelists from both of these repositories are visible in the replicated codelists interface: [codelists.codeforiati.org](https://codelists.codeforiati.org)

## Adding a codelist

It is now relatively straightforward to add a new codelist here (we're trying to gradually make it even easier).

We generally encourage you to do any scraping or wrangling outside of this repository, and then make pre-processed files available for the codelist updater to check and import nightly if there are any updates.

For example, if you need to scrape a web page to keep a codelist up to date, you can do this on [morph.io](https://morph.io) and then access that data via the morph.io API.

Currently, this is the process:

1. Make a codelist template: this is a codelist with none of the `codelist-item` elements. The easiest way to do this is to copy and rename one of the files in the `templates` folder.
2. Add a the (empty) codelist template to the relevant repository (via a pull request).
3. Add the same template to the `templates` folder. It must have the same name as the codelist template in step (2).
4. Create an importer: you can start by copying and renaming an importer from the `importers` folder.
5. Update `.travis.yml` to include your importer.
