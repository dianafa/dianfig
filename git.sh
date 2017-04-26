[alias]
    st = status
    cam = commit -am
    uncam = reset --soft HEAD~1
    cane = commit --amend --no-edit
    br = branch
    co = checkout
    p-r = pull --rebase
    df = diff
    lg = log -p
    who = shortlog -s --
    commit-a = "!f() { x=$(git current-branch)\" \"$1;git commit -m \"$x\"; }; f"
    current-branch = "!git branch | grep -e '^*' | cut -d' ' -f 2"
    task-id = "!git current-branch | grep -o -P '([A-Z]+\\-[0-9]+)'"
    branch-name = "!git rev-parse --abbrev-ref HEAD"
    c = "!f() { x=$(git current-branch)\" \"$1;git commit -m \"$x\"; }; f"
    p-ro = "!git pull --rebase origin $(git branch-name)"
    shipit = "!git push origin $(git branch-name)"
    yolo = "!git push origin $(git branch-name) --force"
    clean-repo = "!git stash-all && git reset --hard && git clean -fd && git checkout dev && git pull"
    stash-all = "!git add . && git stash"
    delete-merged-branches = "!git co master && git branch --merged | grep -v '\\*' | xargs -n 1 git branch -d"
    
#git
#git config --global alias.c '!b=$(git rev-parse --abbrev-ref HEAD);git commit -am "$b" -m'
