tgit-st3
========

TortoiseGit Plugin for Sublime Text 2/3

A simple plugin to expose the best of the TortoiseGit GUI to the 
Sublime Text 2/3 context menu.

Adds the following to the context menu for an active file:

* Diff
* Show log
* Commit
* Sync

If there is no active file, it tries to guess the "relevant" repository
by looking at the project file or the first open folder.

## Installation

Until this plugin is added to Package Control, try this:

1. Go to folder `Packages`: 
   It can be found at `%APPDATA%\Sublime Text 3\Packages`.  Also, clicking `Preferences/Browse Packages...` in Sublime Text will open the right directory.
2. In that directory, run `git clone git@github.com:ses4j/tgit-st3.git`

## Thanks

Thanks to the authors and contributors of the following repositories, 
from whom I got useful direction:

* https://github.com/fyneworks/sublime-TortoiseGIT
* https://github.com/kemayo/sublime-text-git

