import os

path = os.getcwd()
print(path)
count = 13  # number of folders required

for i in range(count):
    try:
        if i < 9:
            os.makedirs('./Labs/Week0' + str(i + 1), exist_ok=True)  # append 0
        else:
            os.makedirs('./Labs/Week' + str(i + 1), exist_ok=True)
    except OSError:
        print('Could not create folder')
