# Rivers
rios = {'segura': 'murcia', 'ebro': 'barcelona', 'arlanzón': 'burgos'}

for rio, ciudad in rios.items():
    print("El río " + rio.title() + " corre por " + ciudad.title() + ".")

for rio in rios.keys():
    print("Río: " + rio.title())

for ciudad in rios.values():
    print("Ciudad: " + ciudad.title())
