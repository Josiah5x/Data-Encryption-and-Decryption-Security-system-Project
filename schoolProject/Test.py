import os
filename = '/home/josiah5x/Downloads'
print(os.path.isdir(filename))
print(os.listdir(filename))

lst = os.listdir(filename)
filec = 'LINUS IKWOYI ULOKO PROJECT TOPIC_AIM AND OBJECTIVE.docx'
for l in lst:
    if filec in l:
        split_up = os.path.splitext(filec)
        file_name = split_up[0]
        file_extension = split_up[1]
        if file_extension == '.pdf':
            print('It is Pdf: ' + file_extension )
        elif file_extension == '.docx':
            print('It is Pdf: ' + file_extension )
        elif file_extension == '.txt':
            print('It is Pdf: ' + file_extension )

        else:
            print('Extension None')
        
        # print('file: ' + file_name + ' extension: ' + file_extension)