#!/bin/bash

#git
git config --global alias.st status
git config --global alias.uncam 'reset --soft HEAD~1'
git config --global alias.cam 'commit -am'
git config --global alias.co checkout
git config --global alias.p-r 'pull --rebase'
git config --global alias.p-ro '!b=$(git rev-parse --abbrev-ref HEAD);git pull --rebase origin "$b"'
git config --global alias.shipit '!b=$(git rev-parse --abbrev-ref HEAD);git push origin "$b"'