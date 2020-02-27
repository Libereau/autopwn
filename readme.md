# Readme First

L'objectif de ce programme est d'essayer de créer un autopwn.
Pour cela, le programme va lancer divers outils comme :
- nmap pour scanner l'ensemble des ports / service de la cible
- wfuzz pour connaitre les répertoires présents sur la machine cible
- sqlmap si des fichiers avec des formulaires sont présents
- ...
- recherche de LFI pouvant mener à une RCE
- reverse shell

# Usage

Pour lancer le programme il vous faudra tout d'abord installer les outils présents dans le requirement.txt.

Une fois ceci fait, donner les droits d'exécution au programme et laissez le faire !

`chmod +x autopwn.py`

`./autopwn.py <ip_address>`

- Exemple : 
`./autopwn 127.0.0.1`

Have fun !
