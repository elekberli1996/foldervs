xallar=[15,13,4,2,1]
xallar2=[1,2,5,4,3]

def sirala(oyuncu_xallari):
    yerler=[]
    yer=5
    for i in oyuncu_xallari:
        for j in oyuncu_xallari:
            if i>j:
                yer-=1
        sira=f"{i} xalla {yer}-ci yer"
        yerler.append(sira)
        yer=5
    return yerler
# siralar=sirala(xallar)
siralar=sirala(xallar2)

print(siralar)
        