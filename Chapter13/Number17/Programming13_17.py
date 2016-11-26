import urllib.request
import Header_13_17_func

def main():
    url = "http://cs.armstrong.edu/liang/data/Salary.txt"
    web_page = urllib.request.urlopen(url)
    
    proflist = []
    linelist = []
    salarylist = []

    Header_13_17_func.parseWeb(web_page,proflist)
    Header_13_17_func.setlist(proflist,linelist,salarylist)
    Header_13_17_func.ordSalaryList(salarylist)
    Header_13_17_func.classify(linelist,salarylist)    
    web_page.close()


main()
