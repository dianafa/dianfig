#!/bin/bash

#git
git config --global alias.st status
git config --global alias.uncam 'reset --soft HEAD~1'
git config --global alias.cam 'commit -am'
git config --global alias.co checkout
git config --global alias.p-r 'pull --rebase'
git config --global alias.p-ro '!b=$(git rev-parse --abbrev-ref HEAD);git pull --rebase origin "$b"'
git config --global alias.shipit '!b=$(git rev-parse --abbrev-ref HEAD);git push origin "$b"'
git config --global alias.yolo 'shipit --force'

#colorful terminal
cat > .bash_profile << EOF1
parse_git_branch() {
     git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}
export PS1="\[\033[1;35m\]\u ♡ \h\ \[\033[32m\]\w\[\033[33m\]\$(parse_git_branch)\[\033[00m\] $ "
EOF1
