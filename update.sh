#!/bin/bash

cd codelist_repo
git add . || exit 1
git commit --author="CodeforIATIbot <57559326+codeforIATIbot@users.noreply.github.com>" -m "${1} update" || exit 1
git push origin ${1}-update || exit 1
hub pull-request -r andylolz,markbrough -a andylolz -m "${1} update" -m "Codelist update, sent from [this TravisCI build](https://travis-ci.com/codeforIATI/codelist-updater/builds/${TRAVIS_BUILD_ID})." || exit 1
