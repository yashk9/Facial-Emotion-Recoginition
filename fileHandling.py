import os, random
import shutil

emo_file = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']
for x in emo_file:
    arr = []
    for file_name in os.listdir("C:\\Users\\manvi moza\\Desktop\\ALL CODES\\FERcodebase\\Images\\{}".format(x)):
        arr.append(file_name)
    str = random.choice(arr)

    str_path = r'C:\\Users\\manvi moza\\Desktop\\ALL CODES\\FERcodebase\\Images\\{emotion}\\{filename}'.format(emotion=x, filename=str)
    # print(str_path)


    original = str_path
    target = r'C:\\Users\\manvi moza\\Desktop\\ALL CODES\\FERcodebase\\finals\\{emotion}\\{filename}'.format(emotion=x, filename=str)

    try:
        shutil.copyfile(original, target)
        print("File copied successfully.")

    # If source and destination are same
    except shutil.SameFileError:
        print("Source and destination represents the same file.")

    shutil.copyfile(original, target)

    dir = r'C:\\Users\\manvi moza\\Desktop\\ALL CODES\\FERcodebase\\Images\\{emotion}\\'.format(emotion=x)

    for files in os.listdir(dir):
        path = os.path.join(dir, files)
        try:
            shutil.rmtree(path)
        except OSError:
            os.remove(path)

    original_new = r'C:\\Users\\manvi moza\\Desktop\\ALL CODES\\FERcodebase\\finals\\{emotion}\\{filename}'.format(emotion=x, filename=str)
    target_new = r'C:\\Users\\manvi moza\\Desktop\\ALL CODES\\FERcodebase\\Images\\{emotion}\\{filename}'.format(emotion=x, filename=str)

    shutil.copyfile(original_new, target_new)
