from numpy import mat

a = mat("[1,2,3];[4,5,6];[7,8,9]")
b = mat("[1,0,1];[0,1,0];[1,1,0]")
c = mat("[0,2,0];[4,0,6];[7,8,8]")
print("a matrisi:")
print(a)
print("a matrisinin boyutu:")
print(a.shape)
listematris = [[4,5,6],[1,2,3],[7,8,9]]
print("Liste Matrisi:")
print(listematris)
listematris.reverse()
print(listematris)
print(a)
b = a.transpose()
print (b)