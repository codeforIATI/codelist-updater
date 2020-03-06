#!/bin/bash

cd codelists || exit 1
if [[ $(hub pr list -h codeforIATI:${1}-update | wc -c) -ne 0 ]]; then
  git stash
  git checkout ${1}-update || exit 1
  git stash pop
else
  git checkout -b ${1}-update || exit 1
fi
git add -u || exit 1
git commit --author="CodeforIATIbot <57559326+codeforIATIbot@users.noreply.github.com>" -m "${1} update" || exit 1
git push origin ${1}-update || exit 1
hub pull-request -r andylolz,markbrough -a andylolz -m "${1} update" -m "Codelist update, sent from [this TravisCI build](https://travis-ci.com/codeforIATI/codelist-updater/builds/${TRAVIS_BUILD_ID})." || exit 1
