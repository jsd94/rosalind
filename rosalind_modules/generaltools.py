def func_to_file(filename):
    def logger(func):
        def log_stdout(*args,**kwargs):
            with open(filename,'w') as outfile:
                result = func(*args,**kwargs)
                outfile.write(str(result))
        return log_stdout
    return logger
    
def checker(result,expected,ordered=False):
    with open(result,'r') as infile1:
        with open(expected,'r') as infile2:
            if ordered == True:
                res = infile1.read()
                exp = infile2.read()
                return res == exp
            else:
                res = infile1.readlines()
                exp = infile2.readlines()
                res = sorted([a.strip('\n') for a in res])
                exp = sorted([a.strip('\n') for a in exp])
                return res == exp
