import os


class FileSystemError(Exception):
    ''' Class for errors in filesystem module '''
    pass


class FSItem(object):
    ''' Common class for OS items OS: Files and Directories '''

    def __init__(self, path):
        ''' Creates new FSItem instance by given path to file '''
        self.path = path
        self.cur_dir, self.name = os.path.split(self.path)

    def rename(self, newname):
        ''' Renames current item
                        raise FileSystemError if item does not exist
                        raise FileSystemError if item "newname" already exists '''
        try:
            newname = os.path.join(self.cur_dir, newname)
            return os.rename(self.path, newname)
        except:
            if self.name == newname:
                raise FileSystemError(f'Name "{newname}" exist.')
            elif FileNotFoundError:
                raise FileSystemError(f'Path "{self.path}" not found.')


    def create(self):
        ''' Creates new item in OS
                 raise FileSystemError if item with such path already exists '''

        if os.path.exists(self.path):
            raise FileSystemError(f'Path "{self.path}" exist.')
        elif os.path.isdir(self.path):
            os.mkdir(self.path)
        else:
            f = open(self.path, "w")
            f.close()
            return File(self.path)

    def getname(self):
        ''' Returns name of current directory '''
        return self.name

    def isfile(self):
        ''' Returns True if current item exists and current item is file, False otherwise '''
        return os.path.isfile(self.path)

    def isdirectory(self):
        ''' Returns True if current item exists and current item is directory, False otherwise '''
        return os.path.isdir(self.path)


class File(FSItem):
    ''' Class for working with files '''

    def __init__(self, path):
        ''' Creates new File instance by given path to file
                 raise FileSystemError if there exists directory with the same path '''
        super(File, self).__init__(path)

    def __len__(self):
        ''' Returns size of file in bytes
                raise FileSystemError if file does not exist '''
        if os.path.exists(self.path):
            return os.path.getsize(self.name)
        else:
            raise FileSystemError(f'Path "{self.path}" not found.')

    def getcontent(self):
        ''' Returns list of lines in file (without trailing end-of-line)
                raise FileSystemError if file does not exist '''
        with open(self.path, 'r') as file:
            content = file.readlines()
        return content

    def __iter__(self):
        ''' Returns iterator for lines of this file
                raise FileSystemError if file does not exist '''
        if os.path.exists(self.path):
            with open(self.path, 'r') as file:
                for lines in file:
                    yield lines
        else:
            raise FileSystemError(f'Path "{self.path}" not found.')


class Directory(FSItem):
    ''' Class for working with directories '''

    def __init__(self, path):
        super(Directory, self).__init__(path)
        ''' Creates new Directory instance by given path
                raise FileSystemError if there exists file with the same path '''

    def items(self):
        ''' Yields FSItem instances of items inside of current directory
                raise FileSystemError if current directory does not exists '''
        try:
            for item in os.listdir(self.path):
                if os.path.isfile(os.path.join(self.path, item)):
                    yield File(os.path.join(self.path, item))
                else:
                    yield Directory(os.path.join(self.path, item))
        except FileNotFoundError:
                raise FileSystemError(f'Path "{self.path}" not found.')

    def files(self):
        ''' Yields File instances of files inside of current directory
                raise FileSystemError if current directory does not exists '''
        try:
            for item in os.listdir(self.path):
                if os.path.isfile(os.path.join(self.path, item)):
                    yield File(os.path.join(self.path, item))
        except FileNotFoundError:
                raise FileSystemError(f'Path "{self.path}" not found.')

    def subdirectories(self):
        ''' Yields Directory instances of directories inside of current directory
                raise FileSystemError if current directory does not exists '''
        try:
            for item in os.listdir(self.path):
                if os.path.isfile(os.path.join(self.path, item)):
                    yield Directory(os.path.join(self.path, item))
        except FileNotFoundError:
            raise FileSystemError(f'Path "{self.path}" not found.')


    def filesrecursive(self):
        ''' Yields File instances of files inside of this directory,
                inside of subdirectories of this directory and so on...
                raise FileSystemError if directory does not exist '''
        try:
            for item in os.listdir(self.path):
                if os.path.isfile(os.path.join(self.path, item)):
                    yield File(os.path.join(self.path, item))
                else:
                    for subitem in Directory(os.path.join(self.path, item)).filesrecursive():
                        yield subitem
        except FileNotFoundError:
            raise FileSystemError(f'Path "{self.path}" not found.')

    def getsubdirectory(self, name):
        ''' Returns Directory instance with subdirectory of current directory with name "name"
                raise FileSystemError if item "name" already exists and item "name" is not directory '''
        for item in os.listdir(self.path):
            if not os.path.isfile(os.path.join(self.path, item)):
                subdir = Directory(os.path.join(self.path, item))
                if subdir.getname() == name:
                    yield subdir
                for subsubdir in subdir.getsubdirectory(name):
                    yield subsubdir



for i in (Directory('/Users/mariaromanova/PycharmProjects/untitled1').items()):
    print(i)