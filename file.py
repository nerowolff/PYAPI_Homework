def line_counter(txt):
    with open (txt,'r',encoding='UTF-8') as f:
        counter=0
        for line in f:
            counter+=1
        return counter

def line_writer(txt):
    with open (txt,'r',encoding='UTF-8') as f:
        file=f.read()
        with open ('result.txt','a',encoding='UTF-8') as f:
            f.write(f'имя файла {txt} \n')
            f.write(f'в файле {str(line_counter(txt))} строк \n')
            f.write(f'{file} \n \n')  


def rewrite(first,second,third):
    with open ('result.txt','w',encoding='UTF-8') as f:
        f.write("") 
    arr=[[line_counter(first),first],[line_counter(second),second],[line_counter(third),third]]
    arr.sort()
    for elements in arr:
        line_writer(elements[1])

rewrite('3.txt','1.txt','2.txt')