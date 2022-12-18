from zipfile import ZipFile
zip_ = ZipFile('resources/test.zip')
print(zip_.namelist())
text = zip_.read('file_example.xlsx')
print(text)
zip_.close()
with ZipFile('resources/test.zip') as yzip:
    yzip.extract('file_example.xlsx')

from zipfile import ZipFile
zip_ = ZipFile('resources/test.zip')
print(zip_.namelist())
text = zip_.read('1.pdf')
print(text)
zip_.close()
with ZipFile('resources/test.zip') as yzip:
    yzip.extract('1.pdf')

from zipfile import ZipFile
zip_ = ZipFile('resources/test.zip')
print(zip_.namelist())
text = zip_.read('2.csv')
print(text)
zip_.close()
with ZipFile('resources/test.zip') as yzip:
    yzip.extract('2.csv')







