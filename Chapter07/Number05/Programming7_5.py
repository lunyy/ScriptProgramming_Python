from RegularPolygon import RegularPolygon

def main():
	pol1 = RegularPolygon()
	pol2 = RegularPolygon(6,4)
	pol3 = RegularPolygon(10,4,5.6,7.8)
	#Polygon 생성
	print("-------------------RegularPolygon1---------------------")
	print(pol1.getPerimeter())
	print(pol1.getArea())
	print("-------------------RegularPolygon2---------------------")
	print(pol2.getPerimeter())
	print(pol2.getArea())
	print("-------------------RegularPolygon1---------------------")
	print(pol3.getPerimeter())
	print(pol3.getArea())
	#Polygon Test
main()