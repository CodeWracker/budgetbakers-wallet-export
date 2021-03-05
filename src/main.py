import os

from contextlib import redirect_stdout
from config import *


if __name__ == "__main__":
    driver = configuration()
    driver.get("file:///C:/Users/Rodrigo Ferraz Souza/Documents/Projetos/Pessoal/wallet-export/site/registros-wallet.html")
    #els = driver.find_elements_by_css_selector('._3wwqabSSUyshePYhPywONa')
    els = driver.find_element_by_css_selector(".VypTY5DQ_tmahm5VdHFJK")
    data ={
        "Categoria": "a",
        "Conta": "BB",
        "Valor": 600,
        "Descricao": "d",
        "Data": "28 de janeiro de 2020"
    }
    allData = [];
    els = els.find_elements_by_tag_name("div")
    cont = 0
    date = ""
    ach = True

    with open('out.json', 'w',encoding="utf-8") as f:
        with redirect_stdout(f):
            print("'data' = [")
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
                            data["Descricao"] = text[2] + text[3]
                            data["Valor"] = text[4]
                        data["Data"] = date
                        print(data)
                        print(",")
                cont = cont+1
            
            print("]")
            
    