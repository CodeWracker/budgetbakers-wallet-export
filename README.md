# budgetbakers-wallet-export

Export to json the data from your account in Wallet, by budget bakers without a premium account</br>
(I didn't want to pay it just to export my dat...)

# How to use

You will need firefox installed.

- Go to the web-app records page and select what you want and scroll it to the and
- Hit ctrl+s to save the html page
- Put the files it generated into the "site" folder with the correct name (Tree bellow)
- run `$ python main.py`
- it will save into the JSON file, BUT the quote symbol is wrong, then you have to replace it from ' to " (if you use VSCode, prettier will automatically do it when you save the file)

> This last item will be removed in a future version, but, by now, it works this way

## Files Structure

```
│   .gitignore
│   geckodriver.log
│   README.md
│
├───geckodriver
│       geckodriver.exe
│
├───site
│   │   registros-wallet.html
│
└───src
        config.py
        main.py
        registros.json
```
