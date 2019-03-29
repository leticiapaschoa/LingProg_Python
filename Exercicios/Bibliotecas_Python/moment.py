import moment
import calendar

list(calendar.day_name)
dataUsuario = input("Digite a data:")

try:
  dataFormatada = moment.date(dataUsuario).format("DD/MM/YYYY")

  print("Formatando data:")
  print(moment.date(dataFormatada).format("DD-MM-YYYY"))  
  print(moment.date(dataFormatada).format("DD/MM/YY")) 
  print(moment.date(dataFormatada).format("MMMM, YYYY")) 

  print("Separando dados:")
  dia = moment.utc(dataFormatada).weekday  
  mes = moment.utc(dataFormatada).month
  ano = moment.utc(dataFormatada).year

  print("Dia da semana: " + calendar.day_name[int(dia)])
  print("Mês: " + str(mes))
  print("Ano: " + str(ano))

except:
  print("Formato incorreto, informe no formato DD-MM-YYYY")
  