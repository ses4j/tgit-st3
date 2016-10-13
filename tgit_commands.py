"""
Invoke useful TortoiseGit GUI windows from Sublime Text

Scott Stafford, https://github.com/ses4j
"""


import os
import time
import sublime, sublime_plugin

try:
    from .tgit_utils import *
except ValueError:
    # We get `ValueError: Attempted relative import in non-package` in ST2.
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

    def _selected_dir(self, dirs):
        if len(dirs):
            return dirs[0]
        else:
            return

    def _execute_command(self, command, path=None):
        if path is None:
            run_tortoise_git_command(command, self._relevant_path())
        else:
            run_tortoise_git_command(command, path)


class TgitLogCommand(TortoiseGitCommandBase):
    def run(self, edit=None, dirs=[]):
        self._execute_command('log', self._selected_dir(dirs))
    
    def _relevant_path(self):
        return self._active_file_or_repo_path()


class TgitDiffCommand(TortoiseGitCommandBase):
    def run(self, edit=None, dirs=[]):
        self._execute_command('diff', self._selected_dir(dirs))

    def _relevant_path(self):
        return self._active_file_or_repo_path()


class TgitCommitRepoCommand(TortoiseGitCommandBase):
    def run(self, edit=None):
        self._execute_command('commit')

    def _relevant_path(self):
        return self._active_repo_path()


class TgitCommitCommand(TortoiseGitCommandBase):
    def run(self, edit=None, dirs=[]):
        self._execute_command('commit', self._selected_dir(dirs))

    def _relevant_path(self):
        return self._active_file_or_repo_path()


class TgitStatusCommand(TortoiseGitCommandBase):
    def run(self, edit=None, dirs=[]):
        self._execute_command('repostatus', self._selected_dir(dirs))

    def _relevant_path(self):
        return self._active_file_or_repo_path()


class TgitSyncCommand(TortoiseGitCommandBase):
    def run(self, edit=None):
        self._execute_command('sync')

    def _relevant_path(self):
        return self._active_repo_path()


class TgitBlameCommand(TortoiseGitCommandBase):
    def run(self, edit=None):
        self._execute_command('blame')

    def _relevant_path(self):
        return self._active_file_path()


