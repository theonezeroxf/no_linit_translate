# googletrans
import os
import asyncio
from googletrans import Translator
from googletrans import LANGUAGES
import yaml
input_dir='D:\code\Translate\InfinityMageNovel-main\Infinity Mage Chapters 1-1277 Translated'
output_dir='D:\code\Translate\InfinityMageNovel-main\en2zh'
input_filename='Chapter - 43 - 리미트리스(2) 8.txt'
# 
modify_dir='D:\code\Translate\InfinityMageNovel-main\en2zh_modify'
dictionary={'西罗尼':'西罗纳','西罗娜':'西罗纳','白音':'西罗纳','西罗妮':'西罗纳','雪隆':'罗纳','雪音':'罗纳','白龙':'罗纳'}
one_file='D:\code\Translate\InfinityMageNovel-main\Infinite_Mage_from_en.txt'

def all_one_file():
    filenames=os.listdir(modify_dir)
    filenames.sort(key=file_no)
    fa=open(one_file,'a',encoding='utf-8')
    for filename in filenames:
        path=os.path.join(modify_dir,filename)
        f=open(path,'r',encoding='utf-8')
        content=f.read()
        f.close()
        fa.write(content)
    fa.close()
    print('all chapter in %s'%one_file)

def modify_file(oldpath,newpath):
    old_f=open(oldpath,'r',encoding='utf-8')
    content=old_f.read()
    for k,v in dictionary.items():
        content=content.replace(k,v)
    new_f=open(newpath,'a',encoding='utf-8')
    new_f.write(content)
    print('\n===%s modify completed! ===\n'%oldpath)
    print('\n===Saved as %s ===\n'%newpath)
    
def test_modify_all():
    translated_files=[]
    modify_files=os.listdir(modify_dir)
    modify_files.sort(key=file_no)
    with open('./config_en.yml', 'r', encoding='utf-8') as f:
        result = yaml.load(f.read(), Loader=yaml.FullLoader)
        translated_files=result['translated_files']
    # print(translated_files)
    if translated_files==modify_files:print('[Warning]all files modified !,no need to modify!\n')
    else:
        for filename in translated_files:
            if filename not in modify_files:
                oldpath=os.path.join(output_dir,filename)
                newpath=os.path.join(modify_dir,filename)
                modify_file(oldpath,newpath)

        print('[INFO]  all modify completed!\n modify files saved in %s'%modify_dir)
    # # pass

def progress_bar(x,total):
    
    ratio=int(x/total*100)
    print("["+"="*ratio+" "*(100-ratio)+']'+'{:.2f}%'.format(x/total*100))
    if ratio==100:
        print()

def translate_progress(config_file):
    pass

def file_no(filename:str):
    pos1=filename.find('-')
    pos2=filename.find('-',pos1+1)
    no=filename[pos1+1:pos2]
    no=no.replace('\u200b','')
    return int(no)

def save_config_file():
    all_files=os.listdir(input_dir)
    translated_files=os.listdir(output_dir)
    untranslate_files=[item for item in all_files if item not in translated_files]
    all_files.sort(key=file_no)
    translated_files.sort(key=file_no)
    untranslate_files.sort(key=file_no)
    sorted(all_files)
    config_str={
        'input_dir':'D:\code\Translate\InfinityMageNovel-main\Infinity Mage Chapters 1-1277 Translated',
        'output_dir':'D:\code\Translate\InfinityMageNovel-main\en2zh',
        'all_files':all_files,
        'translated_files':translated_files,
        'untranslate_files':untranslate_files
    }
    with open('./config_en.yml', 'w', encoding='utf-8') as f:
        yaml.dump(data=config_str, stream=f, allow_unicode=True)
    print('config_en.yaml saved in '+os.curdir)

def load_config_file():
    global input_dir
    global output_dir
    global input_filename
    with open('./config_en.yml', 'r', encoding='utf-8') as f:
        result = yaml.load(f.read(), Loader=yaml.FullLoader)
        print(result['input_dir'])
        print(result['output_dir'])
        print(result['untranslate_files'][0])
        input_dir=result['input_dir']
        output_dir=result['output_dir']
        input_filename=result['untranslate_files'][0]

    
def test_new():
    import asyncio
    from googletrans import Translator
    path=os.path.join(input_dir,input_filename)
    print('\n %s is ready to translate'%path)
    f= open(path,'r',encoding='utf-8')
    lines=f.readlines()
    f.close()
    # 
    path2=os.path.join(output_dir,input_filename)
    f2= open(path2,'a',encoding='utf-8')
    # 
    n_line=len(lines)
    step=10
    n_grp=n_line//step
    # n_grp=10
    async def translate_text():
        
        async with Translator() as translator:
            for i in range(n_grp):
                content=''.join(lines[i*step:(i+1)*step])
                result = await translator.translate(content,dest='zh-cn')
                f2.write(result.text)
                progress_bar(i,n_grp)
                # print(result.text)  # <Translated src=ko dest=en text=Good evening. pronunciation=Good evening.>

            content=''.join(lines[n_grp*step:])
            result = await translator.translate(content,dest='zh-cn')
            f2.write(result.text)

            # result = await translator.translate('안녕하세요.', dest='ja')
            # print(result.text)  # <Translated src=ko dest=ja text=こんにちは。 pronunciation=Kon'nichiwa.>
   
            # result = await translator.translate('veritas lux mea', src='la')
            # print(result.text)  # <Translated src=la dest=en text=The truth is my light pronunciation=The truth is my light>
        
    try:
        asyncio.run(translate_text())
    except:
        f2.close()
        os.remove(path2)
        print('\n [Error]===tranlated file %s is auto delete'%path2)
    else:
        f2.close()
        print('\n ===tranlate Completed!===\n Saved as %s'%path2)

def test_simple_unit():
    test_new()
    save_config_file()
    load_config_file()

def Translate_one():
    load_config_file()
    test_new()
    save_config_file()
    test_modify_all()

if __name__=="__main__":

    # pass
    for i in range(100):
        print('==========the {} chapter ============'.format(i+1))
        Translate_one()
