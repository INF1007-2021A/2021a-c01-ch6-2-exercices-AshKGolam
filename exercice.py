#!/usr/bin/env python
# -*- coding: utf-8 -*-

from matplotlib.colors import cnames


def list_to_dict(some_list: list) -> dict:
    # TODO: Transformer la liste en dictionnaire, les éléments de la liste deviennent les clés et leur index deviennent les valeurs
    index = 0
    my_dict = {}
    for each in some_list:
        my_dict[index] = each
        index += 1
    return my_dict


def color_name_to_hex(colors: list) -> list:
    # TODO: Trouver la valeur hex de chaque couleur dans la liste et créer une liste de tupple où le premier élément est le nom de la couleur et le deuxième est la valeur hex
    my_list = []
    my_list = [(each,cnames[each]) for each in colors if each in cnames]
    return my_list


def create_list() -> list:
    # TODO: Créer une liste des 10 000 premiers entiers positif, sauf pour les entiers de 15 à 350
    my_list = []
    my_list= [i for i in range(0,10001) if i < 15 or i > 350]
    return my_list


def compute_mse(model_dict: dict) -> dict:
    # TODO: Calculer l'erreur quadratique moyen pour chaque modèle. Retourner un dictionnaire contenant les MSE.
    my_dict = {}
    for key in model_dict:
        mse = 0
        n = 1
        for tup in model_dict[key]:
           mse = mse + (1/n)*(tup[0]-tup[1])**2
           n = n + 1
        my_dict[key] = mse
    return my_dict


def main() -> None:
    some_list = ["a", "b", "z", "patate"]
    print(f"La liste suivante {some_list} est transformée en dictionnaire: {list_to_dict(some_list)}")

    colors = ["blue", "red", "green", "yellow", "black", "white"]
    print(f"La valeur hex associée aux couleurs est: {color_name_to_hex(colors)}")

    print(f"La liste des 10000 entiers est: {create_list()}")

    model_dict = {"LR": [(90, 92), (96, 100), (20, 25), (21, -2), (3, -20)],
                  "DNN": [(100, 101), (50, 50), (1,2), (-10, -12), (-1, 7)],
                  "RF": [(10, 19), (56, 70), (1, 9), (-100, -12), (-11, 7)]}
    print(f"Le mse des différents modèles est: {compute_mse(model_dict)}")


if __name__ == '__main__':
    main()
