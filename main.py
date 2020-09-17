#---------(Sınıflandırıcı Kullanarak Yaş ve Cinsiyet  Tespiti)--------------
#--------(VERİLERE DİKKAT EDİLMEMİŞTİR SINIFLANDIRICI KULLANIMINA ORNEKTIR )---------------------
from sklearn import tree
o = [[9.65,76],[9.2,74.1],[6.8,68.2], [9.6,75.7] , [ 12.2 , 86.9 ] , [ 15.8,95.5 ] , [ 9.0 , 79.5 ] , [12.7 , 85.5 ] ,[13.9,96.8] , [14.5,97.4] , [15.3,98.1] , [7.1,64.5] , [9.9,73.0] , [12.1,77.0] ,[9.2,76.5],[12.2,85.5],[15.1,91.1],[10.6,85.5],[14.0,95.0],[17.5,100] ] 
k = [1,1,1,1,2,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6]
sn = tree.DecisionTreeClassifier()
sn = sn.fit(o,k) 
kilo = int(input("Kilo Giriniz(kg)"))
boy = int(input("Boy Giriniz(cm)"))
ornek = sn.predict([[kilo,boy]])
if ornek == 1:
	print( "YAŞ = 1" )
	print("Cinsiyet = Erkek")
elif ornek == 2 :
	print( "YAŞ = 2" )
	print("Cinsiyet = Erkek")
elif ornek == 3:
	print( "YAŞ = 3" )
	print("Cinsiyet = Erkek")
elif ornek == 4 :
	print( "YAŞ = 1" )
	print("Cinsiyet = Kız")
elif ornek == 5 :
	print( "YAŞ = 2" )
	print("Cinsiyet = Kız")
elif ornek == 6 :
	print( "YAŞ = 3" )
	print("Cinsiyet = Kız")
	
