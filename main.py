import requests
import json
import sys
import os


def main():

    SysLog = open("SystemLOG.txt","a")

    while True:

        print("Ingrese el ID del vendedor que desea ver los items, si desea salir escriba exit: ")
        seller_id = input()

        if seller_id == "exit":
            SysLog.close()
            sys.exit(0)

        response = requests.get('https://api.mercadolibre.com/sites/MLA/search?seller_id=' + seller_id).json()

        print("Recibiendo items del vendedor:" + seller_id)

        for result in response["results"]:



            category_id = result["category_id"]

            productstring = "ID: " + result["id"] + " | Título: " + result["title"] + " | ID Categoría: " + category_id + " | Nombre categoría: "

            new_response = requests.get('https://api.mercadolibre.com/categories/'+category_id).json()
            productstring += new_response["name"]

            SysLog.write(productstring + os.linesep)
        print("Log escrito")


if __name__ == '__main__':
    main()
