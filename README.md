tgit-st3
========

**A TortoiseGit Plugin for Sublime Text 2/3**  
*...because who has time to `Open Containing Folder...`
and THEN use TortoiseGit?*

A simple plugin to expose the best of the TortoiseGit GUI to the 
Sublime Text 2/3 context menu.

Adds the following to the context menu for an active file:

* Diff
* Show log
* Commit...
* Commit... (entire repo)
* Sync...

If there is no active file, it tries to guess the "relevant" repository
by looking at the project file or the first open folder.

## Installation

Please be sure you have installed the prerequisites before expecting this to work:
* Sublime Text 2/3
* TortoiseGit

Until this plugin is added to Package Control:

1. Go to folder `Packages`: 
   It can be found at `%APPDATA%\Sublime Text 3\Packages`.  Also, clicking 
   `Preferences/Browse Packages...` in Sublime Text will open the right directory.
2. In that directory, run `git clone git@github.com:ses4j/tgit-st3.git`.

If your `TortoiseGitProc.exe` is not installed in `C:\Program Files\TortoiseGit\bin\TortoiseGitProc.exe` 
(the normal place) AND if it's not in your PATH, you may need to configure the plugin settings.

## Thanks

Thanks to the authors and contributors of the following repositories, 
from whom I got useful direction:

* https://github.com/fyneworks/sublime-TortoiseGIT
* https://github.com/kemayo/sublime-text-git

