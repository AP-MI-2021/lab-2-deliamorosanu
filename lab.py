'''
9. Transformă un număr dat din baza 2 în baza 16. Numărul se dă în baza 2.
'''

def get_base_16_from_2(n: str):
    nr=int(n,2)
    return hex(nr)



'''
10. Calculează combinări de n luate câte k (n și k date).
'''

def get_n_choose_k_v1(n: int, k: int):
  import math
  return math.factorial(n)/ (math.factorial(n-k)*math.factorial(k))

'''
sau
'''
def factorial(n:int):
  p=1
  for i in range (1,n+1):
    p=p*i
  return p

def get_n_choose_k(n: int, k: int):
  return factorial(n)// (factorial(n-k)*factorial(k))

def test_get_n_choose_k():
assert get_n_choose_k(5,3)==10
assert get_n_choose_k(7,4)==35
assert get_n_choose_k(5,2)==10

def main():
    while True:
        print("1. Transformarea unui numar din baza 2 in baza 16.")
        print("2. Combinari de n luate cate k.")
        print("3. Iesire din program.")
        optiune=input("Alege optiunea")
        if optiune="1":
            m=input("Dati numarul n:")
            print("Numarul n in baza 16 este {hex(nr}")
            print("\n")
        elif optiune="2":
            n=int(input("dati numarul n:"))
            k=int(input("Dati numarul k:"))
            print(f"Combinari de n luate cate k este: {get_n_choose_k(n,k)}")
            print("\n")
        elif optiune="3":
            break
        else:
            print("Reincercati")


main()