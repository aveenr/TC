from bs4 import BeautifulSoup

#get data from source
soup = BeautifulSoup(open('TC_Weekly.html'),'html.parser')

# get code
code = []
analysis = []
code = soup.find_all('strong')
for i in code:
    raw_to_string = str(i)
    # print(j[j.find("(") + 1:j.find(")")])
    # get 3 letter code between brackets
    code.append((raw_to_string[raw_to_string.find("(") + 1:raw_to_string.find(")")]))
    # print(i.next_sibling)
    analysis.append((i.next_sibling.replace(': ', '')))

with open("myweek.txt","a") as file_date:
    for i in range(0,len(jsecode)):
        print(jsecode[i],file=file_date)
        print(analysis[i],file=file_date)

