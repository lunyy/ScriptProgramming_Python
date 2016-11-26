def parseWeb(web_page,proflist):
    strings = web_page.read().decode()
    strings = strings.split("\r\n")
    for i in range(0,len(strings)):
        proflist.append(strings[i])
# Web에서 text를 가져와 잘라서 list에 넣기
def setlist(proflist,linelist,salarylist):
    for index in range(0,len(proflist)):
        salarystr = ''
        linestr = ''
        for i in range(19,len(proflist[index])) :
            if proflist[index][i] == ' ' : 
                i+=1
                while True : # 교직원의 이름 저장.
                    if proflist[index][i] == ' ' : 
                        break
                    linestr += proflist[index][i]
                    i += 1
                i += 1
                while True : # 교직원의 급여 저장.
                    if i == (len(proflist[index])) :
                        break
                    salarystr += proflist[index][i]
                    i += 1
                break
        linelist.append(linestr)
        salarylist.append(salarystr)

def ordSalaryList(salarylist): 
    for i in range(0,len(salarylist)) : # 교직원의 급여를 string -> float 형식으로 변환
        salarylist[i] = float(salarylist[i])

def classify(linelist,salarylist):
    assistant = 0
    associate = 0
    full = 0
    
    assistantnum = 0
    associatenum = 0
    fullnum = 0
    
    for i in range(len(linelist)) :
        if (linelist[i] == 'assistant'):
            assistant += salarylist[i] # 조교수의 급여
            assistantnum += 1 # 조교수의 인원수
        elif (linelist[i] == 'associate'):
            associate += salarylist[i] # 부교수의 급여
            associatenum += 1 # 부교수의 인원수
        else :
            full += salarylist[i] # 정교수의 급여
            fullnum += 1 # 정교수의 인원 수
    printComponent(assistant,associate,full,assistantnum,associatenum,fullnum)

def printComponent(assistant,associate,full,assistantnum,associatenum,fullnum):
    print("Assistant : ", assistantnum , " people. Average Pay : ", round(assistant / assistantnum,3))
    print("Associate : ", associatenum , " people. Average Pay : ", round(associate / associatenum,3))
    print("Full      : ", fullnum , " people. Average Pay : ",round(full / fullnum,3))
    print("Sum of ",assistantnum + associatenum + fullnum,"people's pay is : ",round(assistant + associate + full,3))
