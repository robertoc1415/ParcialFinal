# coding=utf-8
#import time
import requests
#import math
#import random

def get_request(): 
    url = "http://192.168.60.3:5000/books"

    req = requests.get(url=url)
    status = req.status_code
    if status >= 400:
        print("[ERROR] Status: ", status)
        return False

    print("[OK] Status: ", status)
    print(req.text)
    return True

def post_request():
    url = "http://192.168.60.3:5000/books"
    headers = {"Content-Type": "application/json"}
    
    id = raw_input('Ingrese ID ')
    title = raw_input('Ingrese Titulo ')
    description = raw_input('Ingrese Descripción ')
    author = raw_input('Ingrese Autor ')

    payload = {
        "description": description,
        "author": author,
        "title": title
    }

    req = requests.post(url=url, headers=headers, json=payload)
    status = req.status_code

    if status >= 400:
        print("[ERROR] Status: ", status)
        return False

    print("[OK] Status: ", status)
    return True

def put_request():
    id = raw_input('Ingrese ID del libro modificar: ')
    url = "http://192.168.60.3:5000/books/" + str(id)

    headers = {"Content-Type": "application/json"}
    
    title = raw_input('Ingrese Titulo ')
    description = raw_input('Ingrese Descripción ')
    author = raw_input('Ingrese Autor ')

    payload = {
        "author": author,
        "description": description,
        "title": title
    }

    req = requests.put(url=url, headers=headers, json=payload)

    # Processes results
    status = req.status_code
    if status >= 400:
        print("[ERROR] Status: ", status)
        return False

    print("[OK] Status: ", status)
    return True

def delete_request():
    id = raw_input('Ingrese ID de libro a borrar: ')
    url = "http://192.168.60.3:5000/books/" + str(id)
    
    headers = {"Content-Type": "application/json"}
    req = requests.delete(url=url)

    status = req.status_code
    if status >= 400:
        print("[ERROR] Status: ", status)
        return False

    print("[OK] Status: ", status)
    return True



def main():
    metodo = raw_input('Método: ').upper()

    if metodo == "POST":
        print("Método POST")
        post_request()
    elif metodo == "GET":
        print("Método GET")
        get_request()
    elif metodo == "PUT":
        print("Método PUT")
        put_request()
    elif metodo == "DELETE":
        print("Método DELETE")
        delete_request()
    else:
        print("¡El método digitado no es valido!")

if __name__ == '__main__':
    i=0
    while (i<5):
        main()
        i = i+1