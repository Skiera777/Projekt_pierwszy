import chardet
# pip install chardet - w terminalu mozemy wydac taka komende, jesli powyzsze nie zadziala to

file_pth = 'test.log'
with open(file_pth, 'rb') as file:
    raw_data = file.read()

#print(raw_data)
result = chardet.detect(raw_data)
print(result)
# dla wiekszej probki znakow poprawnie przypisał kodowanie utf-8
kodowanie = result['encoding']
confidence = result['confidence']
print(kodowanie, confidence)
print(raw_data.decode(encoding=kodowanie))