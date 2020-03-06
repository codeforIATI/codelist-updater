#!/bin/bash

cd codelists
if [[ $(hub pr list -h codeforIATI:${1}-update | wc -c) -ne 0 ]]; then
  git stash
  git checkout ${1}-update
  git stash pop
else
  git checkout -b ${1}-update
fi
git add -u
git commit --author="CodeforIATIbot <57559326+codeforIATIbot@users.noreply.github.com>" -m "${1} update"
git push origin ${1}-update
hub pull-request -r andylolz,markbrough -a andylolz -m "${1} update" -m "Codelist update, sent from [this TravisCI build](https://travis-ci.com/codeforIATI/codelist-updater/builds/${TRAVIS_BUILD_ID})."
