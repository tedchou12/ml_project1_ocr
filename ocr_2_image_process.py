from PIL import Image
import glob


counter = 1
mode = 'valid'

for file in glob.glob('./' + mode + '/unprocessed/*.jpg') :
    path_parts = file.split('/')
    name = path_parts[-1].split('.')
    numbers = name[0]

    im = Image.open(file)
    im_crop0 = im.crop((3, 0, 15, 25))
    im_crop0.convert('L').save(mode + '/processed/' + numbers[0] + '/' + str(counter) + '.jpg', quality=95)
    counter = counter + 1

    im_crop1 = im.crop((15, 0, 27, 25))
    im_crop1.convert('L').save(mode + '/processed/' + numbers[1] + '/' + str(counter) + '.jpg', quality=95)
    counter = counter + 1

    im_crop2 = im.crop((27, 0, 39, 25))
    im_crop2.convert('L').save(mode + '/processed/' + numbers[2] + '/' + str(counter) + '.jpg', quality=95)
    counter = counter + 1

    im_crop3 = im.crop((39, 0, 51, 25))
    im_crop3.convert('L').save(mode + '/processed/' + numbers[3] + '/' + str(counter) + '.jpg', quality=95)
    counter = counter + 1

    im_crop4 = im.crop((51, 0, 63, 25))
    im_crop4.convert('L').save(mode + '/processed/' + numbers[4] + '/' + str(counter) + '.jpg', quality=95)
    counter = counter + 1

    im_crop5 = im.crop((63, 0, 75, 25))
    im_crop5.convert('L').save(mode + '/processed/' + numbers[5] + '/' + str(counter) + '.jpg', quality=95)
    counter = counter + 1

    # exit()
