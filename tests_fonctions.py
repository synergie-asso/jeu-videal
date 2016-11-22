from fonctions import positif, pair, egalDix, tableauEgalDix

def testPositif(x) :
    if positif(x) :
        print('{:6}'.format(x), " est positif")
    else:
        print('{:40}'.format(x), "est négatif")
        


def testPair(x) :
    if pair(x) :
        print('{:6}'.format(x),  "est pair")
    else:
        print('{:40}'.format(x), "est impair")



def testEgalDix(x, y) :
    if egalDix(x,y) :
        print('{:6}'.format(str(x) + " + " +  str(y)),  "est égal à 10")
    else:
        print('{:40}'.format(str(x) + " + " +  str(y)), "est différent de 10")


def testTableauEgalDix(tab) :
    if tableauEgalDix(tab) :
        print('{:30}'.format(str(tab)),  "est égal à 10")
    else:
        print('{:40}'.format(str(tab)), "est différent de 10")


def test():
    testPositif(0)
    testPositif(1)
    testPositif(2)
    testPositif(10)
    testPositif(123456)
    testPositif(-1)
    testPositif(-5)
    testPositif(-12345)
    
    testPair(0)
    testPair(2)
    testPair(48)
    testPair(4)
    testPair(7892)
    testPair(8)
    testPair(3)
    testPair(5)
    testPair(5)
    testPair(789456123)
    testEgalDix(4,6)
    testEgalDix(5,5)
    testEgalDix(5,5)
    testEgalDix(5,8)
    testEgalDix(2,2)
    testEgalDix(3,5)



    testTableauEgalDix([1,2,3,4])
    testTableauEgalDix([2,2,2,2,2])
    testTableauEgalDix([1,1,1,1,1,1,1,1,1,1])
    testTableauEgalDix([3,3,3,1])
    testTableauEgalDix([9,2,3,1])
    testTableauEgalDix([4,2,3,2])
    testTableauEgalDix([1,2,3,5])

if __name__ == '__main__':
    test();
