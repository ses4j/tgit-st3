"""
Invoke useful TortoiseGit GUI windows from Sublime Text 3

By Scott Stafford, https://github.com/ses4j

With borrowed contributions from the wonderful Git plugins: 
	* https://github.com/kemayo/sublime-text-git

"""


import os
import time
import sublime

import subprocess

git_root_cache = {}
def git_root(directory):
    global git_root_cache

    retval = False
    leaf_dir = directory

    if leaf_dir in git_root_cache and git_root_cache[leaf_dir]['expires'] > time.time():
        return git_root_cache[leaf_dir]['retval']

    while directory:
        print('dir', directory)
        if os.path.exists(os.path.join(directory, '.git')):
            retval = directory
            break
        parent = os.path.realpath(os.path.join(directory, os.path.pardir))
        if parent == directory:
            # /.. == /
            retval = False
            break
        directory = parent

    git_root_cache[leaf_dir] = {
        'retval': retval,
        'expires': time.time() + 5
    }

    return retval

def is_git_controlled(directory):
    return bool(git_root(directory))


def run_tortoise_git_command(command, path):
    args = ()
    settings = sublime.load_settings('TortoiseGIT.sublime-settings')
    tortoisegit_path = settings.get('tortoisegit_path')

    if tortoisegit_path is None or not os.path.isfile(tortoisegit_path):
        # sublime.error_message("Can't find TortoiseGitProc.exe.")
        # raise
        tortoisegit_path = 'TortoiseGitProc.exe'

    # if path is None:
    #     path = sublime.active_window().active_view().file_name()

    cmd = '%s /command:"%s" /path:"%s" %s' % (
        tortoisegit_path, 
        command,
        path,
        " ".join(args))

    print(cmd)
    try:
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    except FileNotFoundError as ex:
        sublime.error_message("Failed to execute command: {}".format(
            str(ex)
            ))
        raise
