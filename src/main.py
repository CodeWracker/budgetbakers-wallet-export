import os

from contextlib import redirect_stdout
from config import *


if __name__ == "__main__":
    driver = configuration()
    driver.get("file://" + FILE_PATH )
    #els = driver.find_elements_by_css_selector('._3wwqabSSUyshePYhPywONa')
    els = driver.find_element_by_css_selector(".VypTY5DQ_tmahm5VdHFJK")
    
    els = els.find_elements_by_tag_name("div")
    cont = 0
    date = ""
    ach = True

    with open('../export/out.json', 'w',encoding="utf-8") as f:
        with redirect_stdout(f):
            print("[")
            for el in els:
                if cont >5:
                    try:
                        date = el.find_element_by_css_selector(".MhNEgOnlVNRo3U-Ti1ZHP").text
                        ach = True
                    except:
                        ach = False
                    
                    elements = el.find_elements_by_css_selector('._3wwqabSSUyshePYhPywONa')
                    #print(date)
                    for ele in elements:
                        text = []
                        data ={
                            "Categoria": "",
                            "Conta": "",
                            "Valor": 0,
                            "Descricao": "",
                            "Data": ""
                        }
                        text = ele.text.split("\n")
                        if len(text) == 3:
                            data["Categoria"] = text[0]
                            data["Conta"] = text[1]
                            data["Valor"] = text[2]
                        if len(text) == 4:
                            data["Categoria"] = text[0]
                            data["Conta"] = text[1]
                            data["Descricao"] = text[2]
                            data["Valor"] = text[3]
                        if len(text) == 5:
                            data["Categoria"] = text[0]
                            data["Conta"] = text[1]
                            data["Descricao"] = text[2] + " " + text[3]
                            data["Valor"] = text[4]
                        data["Data"] = date
                        print(data)
                        print(",")
                cont = cont+1
            
            print("]")
    driver.close()
    