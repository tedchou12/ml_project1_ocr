import glob

mode = 'valid'

i = 0
while i < 10 :
    list = []
    for file in glob.glob('./' + mode + '/processed/' + str(i) + '/*.jpg') :
        path = file.replace('./', '')
        list.append(path)


    with open(mode + '/nlist/' + str(i) + '.txt', 'w') as handle:
        string = '\n'.join(list)
        handle.write(string)


    i += 1


exit()
