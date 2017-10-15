import urllib.request
import os
import tarfile
import hashlib
from os import walk
import subprocess


class Tool:
    ''' Represents a tool to run.
    '''

    # def is_downloaded(self):
    # def download(self):

    # def is_installed(self):
    # def install(self):

    def __call__(self, arguments):
        ''' Assumptions:
            - All Tools are command line tools.
            - All Tool objects has an attribute called 'bin'
        '''
        args = [self.bin]
        args.extend(arguments)
        subprocess.check_call(args)


class Task:
    ''' Represents a single task to be run by a tool.
    '''

    # def usesTool(self, tool):
    #     pass

    # def dependsOn(self, *tasks):
    #     pass

    # def run(self):
    #     pass


class Download:

    def is_downloaded(self):
        return (os.path.exists(self.dist_file) and
                sha256sum(self.dist_file) == self.dist_file_sha)


    def download(self):
        print(self.dist_dir)
        os.makedirs(self.dist_dir, exist_ok=True)
        urllib.request.urlretrieve(self.url, self.dist_file)


class InstallTar:

    def is_installed(self):
        return (os.path.exists(self.bin) and
                sha256sum(self.bin) == self.bin_sha)

    def install(self):
        tar = tarfile.open(self.dist_file)
        tar.extractall(path=self.dist_dir)
        tar.close()


def sha256sum(filepath):
    BLOCKSIZE = 65536
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)
    return hasher.hexdigest()
