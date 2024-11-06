# @title Congruenze Lineari Seconda versione con algoritmo di euclide e semplificazione
def Mcd(a,b):
  if b == 0:
    return a
  if a<b:
    a, b = b, a

  q=a // b
  r= a % b

  return Mcd(b,r)

def semplificazione(sxparam,dxparam,modulo):
  mcd=Mcd(sxparam,modulo)
  if dxparam%mcd == 0:
    print('l\'ho semplificata, congruente con:')
    print(sxparam//mcd, dxparam//mcd, modulo//mcd)
  else:
    print('non semplificabile')
    return sxparam, dxparam, modulo
  x=1
  while x <= modulo:
    mod=(sxparam*x)%modulo
    if mod == dxparam%modulo:
      x0=x
      break
    x+=1
  soluzionik=[x0]
  for x in range(1,mcd):
    soluzionik.append(int(x0+(x*(modulo/mcd))))
  print('le soluzioni sono:')
  return soluzionik


def evalsol(sxparam, dxparam,modulo):
  mcd=Mcd(sxparam,modulo)
  if mcd==dxparam: 
    print('ci sono:', mcd,' soluzioni congrue')
    return mcd
  if mcd!=dxparam and mcd!=1:
    print('non ci sono soluzioni congrue, provo a semplificare')
    print(semplificazione(sxparam,dxparam,modulo))
    return exit()
  elif mcd==1: #presenza di una soluzione congrua, il modulo e a sono primi  (a inteso come parametro che moltiplica x)
    print('ci sta 1 soluzione congrua')
    return mcd
  elif mcd==0:  #caso esempio: 5 modulo 5 non potra' mai dare resto o 25 modulo 5
    print('nessuna soluzione')
    return 0

def trovasol(sxparam, dxparam,  modulo):
  mcd = evalsol(sxparam%modulo,dxparam%modulo,modulo)  #applico il percento modulo per ridurre un po' i tempi di computazione
  if mcd==0 or mcd is None:
    return ''
  x=1
  while x <= modulo:
    mod=(sxparam*x)%modulo
    if mod == dxparam%modulo:
      x0=x
      break
    x+=1
  soluzionik=[x0]
 #tutte le soluzioni sono del tipo xo+(x-1)*(n/d) dove d e' il MCD fra a ed n (modulo)  prop. 5.8 pagina 128 Matematica discreta
  for x in range(1,mcd):
    soluzionik.append(int(x0+(x*(modulo/mcd))))
  return soluzionik

def sistemi(sistema):
  N=1
  for x in range(len(sistema)):
    if sistema[x][0] != 1:
      sistema[x][1]=sistema[x][1]*sistema[x][0] #semplifico e porto le moltiplicazioni della x al altra parte, esempio 5.6 pagina 126 piacentini 2x congruente 1 mod 3, x congruente 2 mod 3
      sistema[x][0]= int(sistema[x][0]/sistema[x][0])
    N=N*sistema[x][2]

  #print(sistema)
  for x in range(len(sistema)):
    sistema[x][0]=int(N/sistema[x][2])
  #print(sistema)

  soluzioni=[]
  soluzionefinale=0
  for x in range(len(sistema)):
    soluzioni.append(trovasol(*sistema[x]))
    soluzionefinale=soluzionefinale+sistema[x][0]*soluzioni[x][0]
  print(soluzioni)
  print('la soluzione finale secondo il teorema cinese dei resti: ',soluzionefinale)



def returnr(n, k = 1, end = None):
  divisione = n / (2**k) #vedo per quali potenze di due e' divisibile questo numero, perche' ho bisogno di scriverlo nella forma 2^n per un numero
  
  if end == True:
    
    return k,divisione
    
  if n % (2**k) != 0:   #
    return returnr(n, k-1, end = True)   #quando la divisione da resto diverso da zero essenzialmente torno indietro di un passo e restituiscon l'ultimo valore n e il risultato della divisione
  
  return returnr (n,k+1)
  


def millerrabin(n, s=0,k=0, start = None, potenza=1):
  if n % 2 == 0:
    return False
  if n%5 ==0:
    return False

  if start is None:   #faccio una sola chiamata e converto k in intero che senno' pow non lo prende
    s,k=returnr(n-1)
    k=int(k)
    #print(s,k)
  a=2
  b=pow(a, k,n)  #devo usare il pow perche' senno' il numero calcolato cresce in maniera esponenziale, e da problemi di overflow
  
  if pow(b, 2**potenza,n)==1:
    return print('probabilmente primo')
    

  if potenza == s:
    return print('non primo')

  millerrabin(n, s, k, start=True, potenza=potenza+1)
  

#83207

'''
def main():
  sistema=[[1,3,4],[2,1,3],[1,4,5]]
  sistemi(sistema)
  print(trovasol(6,3,9))
  print(trovasol(6,12,18))
  print(trovasol(4,5,9))
  millerrabin(83207)
main()
'''