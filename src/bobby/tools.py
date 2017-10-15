from . import Task, Tool, Download, InstallTar

import subprocess

class Ruby(Tool):
    bin = 'ruby'

    def is_downloaded(self):
        return True

    def is_installed(self):
        return subprocess.call(['which', self.bin]) == 0

    def install(self):
        raise Error('Ruby is part of Osx. What did you do to delete it?')


class Brew(Tool, Download):
    dependsOn = Ruby
    url = 'https://raw.githubusercontent.com/Homebrew/install/master/install'
    dist_dir = './.bobby/tools/brew/'
    dist_file = dist_dir + 'brew_install.ruby'
    dist_file_sha = '4c00cabd72bee331531b97f0c2f90fd104ee06f96155b9a35a29ced6accc85ca'

    bin = 'brew'

    def is_installed(self):
        return subprocess.call(['which', self.bin]) == 0

    def install(self):
        self.ruby(['-e', self.dist_file])



##
# Python Tools
##

class Python(Tool):
    dependsOn = Brew
    bin = 'python'

    def is_installed(self):
        return subprocess.call(['which', self.bin]) == 0

    def install(self):
        self.brew(['install', 'python'])


class PythonEasyInstall(Python):
    bin = 'easy_install'
    sudo = True


class Pip(Tool):
    dependsOn = PythonEasyInstall
    bin = 'pip'

    def is_installed(self):
        return subprocess.call(['which', self.bin]) == 0

    def install(self):
        self.pythoneasyinstall(['pip'])



##
# NodeJS Tools
##

class Node(Tool, Download, InstallTar):

    url = 'https://nodejs.org/dist/v6.9.1/node-v6.9.1-darwin-x64.tar.gz'
    dist_file = './.bobby/tools/node/node-v6.9.1-darwin-x64.tar.gz'
    dist_file_sha = '392e511ca0d6203c80700ed753187535e04069d0df0074cbfd1e4f1bd571d4c5'

    dist_dir = './.bobby/tools/node/'
    bin = dist_dir + 'node-v6.9.1-darwin-x64/bin/node'
    bin_sha = '3d343f4a8d38bcd60b45162b1e89cbcc1baf0ad1661ac6b116a20ebbcb372663'



class Npm(Node):
    bin = Node.dist_dir + 'node-v6.9.1-darwin-x64/bin/npm'
    bin_sha = '7187bc63311f292ef43a470f2d4c01c5e4e67888276530c5365d8b6035fa7712'


class Yarn(Tool, Download, InstallTar):
    dependsOn = Node
    url = 'https://yarnpkg.com/latest.tar.gz'

    dist_dir = '.bobby/tools/yarn/'
    dist_file = dist_dir + 'latest.tar.gz'
    dist_file_sha = '73be27c34ef1dd4217fec23cdfb6b800cd995e9079d4c4764724ef98e98fec07'


    bin = dist_dir + 'dist/bin/yarn.js'
    bin_sha = '886592175c15d9849bd5730ce13bd0679eba6fc74554b748f109908859e82315'




##
# AWS Tools
##

class AwsEbCli(Tool):
    dependsOn = Pip
    bin = 'eb'

    def is_installed(self):
        return subprocess.call(['which', self.bin]) == 0

    def install(self):
        self.pip(['install', 'awsebcli'])
