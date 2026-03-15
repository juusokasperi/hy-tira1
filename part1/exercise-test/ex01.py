# Tee Python-funktio create_list(n), joka palauttaa listan, jossa on kerran luku 1, kahdesti luku 2, kolmesti luku 3, jne. lukuun n asti. Esimerkiksi jos n = 4, funktion tulee palauttaa lista [1, 2, 2, 3, 3, 3, 4, 4, 4, 4].

def create_list(n):
    result = []
    for i in range(1, n + 1):
        for j in range(i):
            result.append(i)
    return result

if __name__ == "__main__":
    print(create_list(4))
