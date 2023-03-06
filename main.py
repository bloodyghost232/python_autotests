import requests
token = '436bfc0967f949e829fea696a6bebee9'
response = requests.post  ('https://pokemonbattle.me:9104/trainers/reg', headers= {'Content-Type': 'application/json'}, 
                json= {"trainer_token": token, "email": "bloodyghosts23@gmail.com","password": "QALinda1"})

print (response.text)

response_confirm = requests.post('https://pokemonbattle.me:9104/trainers/confirm_email', headers= {'Content-Type': 'application/json'}, json = {"trainer_token": token})
print(response_confirm.text)

add_pokemon_response= requests.post('https://pokemonbattle.me:9104/pokemons', headers= {'Content-Type': 'application/json', 'trainer_token':token},json = {"name": "Nyashka",
                                                                                                                                                           "photo": "https://dolnikov.ru/pokemons/albums/010.png"})
print(add_pokemon_response.text)
if add_pokemon_response.status_code == 201: print('OK')
else: print ('Not ok')

response_put=requests.put('https://pokemonbattle.me:9104/pokemons', headers= {'Content-Type': 'application/json', 'trainer_token':token}, json = {"pokemon_id": 5999,
                                                                                                                                                  "name": "Meow",
                                                                                                                                                  "photo":"https://dolnikov.ru/pokemons/albums/010.png"})
print(response_put.text)

response_add_pokeball=requests.post('https://pokemonbattle.me:9104/trainers/add_pokeball', headers= {'Content-Type': 'application/json', 'trainer_token':token},json = {"pokemon_id": "5999"})

print(response_add_pokeball.text)





