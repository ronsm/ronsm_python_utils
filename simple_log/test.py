from simple_log import SimpleLog
from another_class import AnotherClass

SIMPLE_LOG_CONFIG = {
    'package_name' : 'a_test_package',
    'package_git' : 'https://github.com/ronsm/test',
    'author_name' : 'Ronnie Smith',
    'author_git' : '@ronsm',
    'author_email' : 'r.smith@hw.ac.uk',
}

class Test():
    def __init__(self):
        self.sl = SimpleLog(SIMPLE_LOG_CONFIG)
        self.sl.welcome()
        self.ac = AnotherClass(self.sl)
        self.sl.log_normal('hello')
        self.sl.log_bad('oh dear')
        self.sl.log_good('good news')
        self.sl.log_math('2 x 3')
        self.sl.log_mini_header('test')
        self.sl.log_state(0)

t = Test()