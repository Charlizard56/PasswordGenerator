import random as r
import List_and_tuples
import itertools



def ran():
    try:
        n = r.randint(0, len(List_and_tuples.List) - 1)
        for key,v in List_and_tuples.List.items():
                if(n == key):
                    return v
    except:
        print("Random Failed")

def gen(times, t):
    try:
        _times = times
        _t = t
        # So the string array isn't empty
        List_and_tuples.Password_Gen.append(ran())
        #print(f"Starting: {List_and_tuples.Password[0]}")

        while _times > 0:
            n = ran()
            l = List_and_tuples.Password_Gen[len(List_and_tuples.Password_Gen) - 1]

            #print(f"Random: {n} Last: {l}")

            #Turn Upper or Lower Letters
            upper = r.randint(0,1)
            #print(upper)
            if upper:
                try:
                    n = n.upper()
                except:
                    n = n

            # Check if letter,num or char was used last
            if n != l:
                List_and_tuples.Password_Gen.append(n)
                _times -= 1

    except:
        print("Generate Failed")

def Check(symbol, number, letters_lower, letters_upper):

    try:
        # Compare the password list to the other tuples
        for p, s, n, l, L in itertools.product(List_and_tuples.Password_Gen, List_and_tuples.Symbols,
                                               List_and_tuples.Numbers,
                                               List_and_tuples.letters, List_and_tuples.Letters):
            # Check if there is at least 1 Symbol
            if p == s:
                symbol = True
            # Check if there is at least 1 Number
            if p == n:
                number = True
            if p == l:
                letters_lower = True
            if p == L:
                letters_upper = True
        if symbol & number & letters_lower & letters_upper:
            return True
        else:
            return False

    except:
        print("Check Failed")
