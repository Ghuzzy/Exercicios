segundos = input(
    "Por favor, entre com o número de segundos que deseja converter: ")

dias = int(segundos)//86400
restdias = int(segundos) % 86400
horas = restdias//3600
resthoras = restdias % 3600
minutos = resthoras//60
restminutos = resthoras % 60
restsegundos = restminutos % 60

print(dias, "dias,", horas, "horas,", minutos,
      "minutos e", restsegundos, "segundos")
