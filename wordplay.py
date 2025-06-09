


def main():
  print('----------------')
  print('    WordPLay    ')
  pedido = input("""
  1. Palavra com N tamanho
  2. Palavra sem caracteres proibido.
  0. sair

""")
  if pedido == '1':
    palavra_com_n_tamanho()
  elif pedido == '2':
    palavra_carac_proibido()
  else:
    print('Adeus!')

def palavra_com_n_tamanho():
  pedido = int(input('Quantos caracteres no mínimo? > '))
  file = open('br-sem-acentos.txt')
  counter = 0
  filter_counter = 0
  for line in file:
    word = line.strip()
    counter += 1
    if len(word) >= pedido:
      filter_counter += 1
      print(word)
  percentage = filter_counter / counter * 100
  print('-----------------')
  print(f'Total/Fitro > {counter}/{filter_counter}. {percentage}% cumpria seus critérios!')


def palavra_carac_proibido():
  carac = input('Qual o caractere proibido? > ').strip()
  file = open("br-sem-acentos.txt")
  counter = 0
  filter_counter = 0
  for line in file:
    word = line.strip()
    counter += 1
    if has_no_char_x(word, carac):
      filter_counter +=1
      print(word)
    percentage = filter_counter / counter * 100
  print(f'{percentage:.2f}% das palavras cumpria seu critério!')

def has_no_char_x(word, carac):
  for char in word:
    if char == carac:
      return False
    
  return True






main()
