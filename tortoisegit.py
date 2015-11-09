"""
Invoke useful TortoiseGit GUI windows from Sublime Text 3

By Scott Stafford, https://github.com/ses4j

With borrowed contributions from the wonderful Git plugins: 
	* https://github.com/kemayo/sublime-text-git

"""


import os
import time
import sublime, sublime_plugin

from .tgit_utils import *

class TortoiseGitCommandBase(sublime_plugin.TextCommand):
    def _active_file_name(self):
        view = self.view
        if view and view.file_name() and len(view.file_name()) > 0:
            return view.file_name()

    def is_enabled(self):
        view = self.view
        if view and view.file_name() and len(view.file_name()) > 0:
            return is_git_controlled(view.file_name())
        return False

    def _repository_root_path(self):
        root = git_root(self._active_file_name())
        if root is False:
            return None
        else:
            return root

class TgitLogCommand(TortoiseGitCommandBase):
    def run(self, edit=None):
        run_tortoise_git_command('log', self._active_file_name())

class TgitDiffCommand(TortoiseGitCommandBase):
    def run(self, edit=None):
        run_tortoise_git_command('diff', self._active_file_name())

class TgitCommitCommand(TortoiseGitCommandBase):
    def run(self, edit=None):
        root = self._repository_root_path()
        if root:
            run_tortoise_git_command('commit', self._repository_root_path())

class TgitSyncCommand(TortoiseGitCommandBase):
    def run(self, edit=None):
        root = self._repository_root_path()
        if root:
            run_tortoise_git_command('sync', self._repository_root_path())

