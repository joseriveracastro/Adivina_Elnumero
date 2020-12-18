import random
intentosRealizados = 0
print('¡Hola! ¿Cómo te llamas?')
nombre = input('escriba su nombre ')
número = random.randint(1, 11)
print('Bueno, ' + nombre + ', estoy pensando en un número entre 1 y 10.')
estimacion = input()
estimacion = int(estimacion)
while intentosRealizados < 3:
  
  print('Intenta adivinar.') 
 
  intentosRealizados = intentosRealizados + 1

  if estimacion < número:
    print('Tu estimación es muy baja.') 
  elif estimacion > número:
    print('Tu estimación es muy alta.')
  else:
    if estimacion == número:
      print('¡Buen trabajo, ' + nombre + '! ¡Has adivinado mi número')


if estimacion != número:

  número = str(número)

  print('Pues no. El número que estaba pensando era ' + número)