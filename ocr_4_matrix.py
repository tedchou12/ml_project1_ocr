from PIL import Image






mode = 'valid'


index = 0
while index < 10 :
    matrix = []

    with open(mode + '/nlist/' + str(index) + '.txt', 'r') as handle :
        files = handle.read()
        files = files.split('\n')

        for file in files :
            im = Image.open(file)
            px = im.load()

            row = []
            i = 0
            j = 0
            for i in range(0, 12) :
                for j in range(0, 25) :
                    hex = str(px[i, j])
                    # parts = hex.replace('(', '').replace(')', '').split(',')
                    # hex = parts[0]
                    row.append(hex)

            matrix.append(','.join(row))

        matrix_string = '\n'.join(matrix)

        handle = open(mode + '/matrix/' + str(index) + '.txt', 'w')
        handle.write(matrix_string)

    index = index + 1
