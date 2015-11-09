"""
Invoke useful TortoiseGit GUI windows from Sublime Text 3

Scott Stafford, https://github.com/ses4j
"""


import os
import time
import sublime, sublime_plugin

from tgit_utils import *

class TortoiseGitCommandBase(sublime_plugin.WindowCommand):
    def is_enabled(self):
        return is_git_controlled(self._relevant_path())

    def _active_file_path(self):
        view = self.window.active_view()
        if view and view.file_name() and len(view.file_name()) > 0:
            return view.file_name()

    def _active_repo_path(self):
        path = self._active_file_path()
        if not path:
            path = self.window.project_file_name()
        if not path:
            path = self.window.folders()[0]
        if path is None:
            return

        root = git_root(path)

        if root is False:
            return
        else:
            return root

    def _active_file_or_repo_path(self):
        path = self._active_file_path()
        if path is not None:
            return path

        # If no active file, then guess the repo.
        return self._active_repo_path()

    def _execute_command(self, command):
        run_tortoise_git_command(command, self._relevant_path())


class TgitLogCommand(TortoiseGitCommandBase):
    def run(self, edit=None):
        self._execute_command('log')
    
    def _relevant_path(self):
        return self._active_file_or_repo_path()


class TgitDiffCommand(TortoiseGitCommandBase):
    def run(self, edit=None):
        self._execute_command('diff')

    def _relevant_path(self):
        return self._active_file_or_repo_path()


class TgitCommitCommand(TortoiseGitCommandBase):
    def run(self, edit=None):
        self._execute_command('commit')

    def _relevant_path(self):
        return self._active_file_path()


class TgitCommitRepoCommand(TortoiseGitCommandBase):
    def run(self, edit=None):
        self._execute_command('commit')

    def _relevant_path(self):
        return self._active_repo_path()


class TgitSyncCommand(TortoiseGitCommandBase):
    def run(self, edit=None):
        self._execute_command('sync')

    def _relevant_path(self):
        return self._active_repo_path()


