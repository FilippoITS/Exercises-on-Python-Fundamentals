persone = ["antonio", "marco", "andrea", "luigi", "tony", "bruno", "laura", "anita", "annarita", "lucia"]
persone.pop(0)
persone.pop(0)
persone.append("jhon")#Nuovi_entrati=("jhon","alice","mary")
persone.append("alice")#persone.extend(Nuovi_entrati)
persone.append("mary")#si puo fare anche così cone extend
persone.pop(0)
persone.pop(0)
print(persone)
persone.sort()
print(persone)


#Versione del prof
stanza = ["antonio","marco","andrea","luigi","tony","bruno","laura","anita","annarita","lucia",]
stanza = stanza[2:]
stanza.extend(["john", "alice", "mary"])
stanza = stanza[2:]
print(stanza)
stanza.sort()
print(stanza)
