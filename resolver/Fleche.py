#p = position de depart
#rep = le nombre de repetition
#dist = la distance du depart à la cible
def flecche (p = 0, rep = 10, dist = 50):
    dist = 50
    for j in range (rep) :
        for i in range (dist) :
            if i == p :
                print ("f",end ='')
            else :
                print ("_",end ='')
        print ("c; p = " + str(p + 1) + " rep = " + str(j + 1) + " dist = " + str(dist))
        p += dist // rep

if __name__ == "__main__" :
    flecche ()