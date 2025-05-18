from googletrans import Translator
import os
# deepL API:60f4d7ab-7fee-4e57-b475-eb2feb2879c4:fx

def translate(text, src, dest):
    translator = Translator(service_urls=['translate.google.com',])# 如果可以上外网，还可添加 'translate.google.com' 等
    trans=translator.translate(text, src='en', dest='zh-cn')
    return trans.text
# # 原文
# print(trans.origin)
# # 译文
# print(trans.text)
def translate_dir(dir, dst_dir):
    filenames=os.listdir(dir)
    files=[os.path.join(dir,filename) for filename in filenames if filename.endswith('.txt')]
    n=len(files)
    i=0
    for file in files:
        with open(file, 'r') as f:
            content = f.read() # 读取文件内容
        # print(content)
        content_zh=translate('hello world', 'en', 'zh-cn')
        dst_files=os.path.join(dst_dir, filenames)
        with open(dst_files, 'w') as f:
            f.write(content_zh)
            i+=1
            print(f'翻译完成：{file}',i,'%d/%d'%(i,n))

def test():
    path='D:\code\Translate\InfinityMageNovel-main\Infinity Mage Volumes 1-51 Translated\Infinity Mage Volume 01.txt'
    translator = Translator(service_urls=['translate.google.com'])
    
    with open(path, 'r') as file:
        lines = file.readlines() # 读取文件内容
        trans=translator.translate(lines[0], src='en', dest='zh-cn')
    print(trans.text)

def test0():
    translator = Translator(service_urls=['translate.google.com'])# 如果可以上外网，还可添加 'translate.google.com' 等
    trans=translator.translate('Hello World', src='en', dest='zh-cn')
    # 原文
    print(trans.origin)
    # 译文
    print(trans.text)

dir='D:\code\Translate\InfinityMageNovel-main\Infinity Mage Volumes 1-51 Translated'
dst_dir='D:\code\Translate\InfinityMageNovel-main\Infinity Mage Volumes 1-51 Translated\zh-cn'
if __name__ == '__main__':
    test()