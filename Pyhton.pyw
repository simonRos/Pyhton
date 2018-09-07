def pyhtonDotexe():
     import platform, os
     if platform.system()=='Windows':
             os.system('cls')
     else:
             os.system('clear')
     lgr = ''
     while True:
             lgr = input('>>> ')
             if lgr and lgr[-1] == ':':
                     indent_lvl = 1
                     while indent_lvl>0:
                             lgr = input('... ')
                             if lgr == '':
                                     indent_lvl-=1
                             elif lgr[-1] == ':':
                                     indent_lvl+=1

pyhtonDotexe()
