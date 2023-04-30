# Malzeme Dağıtımı
Bu proje, belirli bir koordinattaki harita verileri kullanılarak malzeme dağıtımını gerçekleştirmeyi amaçlamaktadır. Program, sağlık malzemeleri, temel gıda, giyim ve ısınma gereci gibi farklı türdeki malzemelerin dağıtımını yapabilir.

# Kullanım
Graph sınıfı, belirli bir koordinatta osmnx kütüphanesi kullanarak bir graf oluşturur. show() metodu, oluşturulan grafi görselleştirmek için kullanılabilir.

dijkstra(start, end) metodu, Dijkstra algoritmasını kullanarak start ve end noktaları arasındaki en kısa yolu hesaplar.

distribute() metodu, belirli türdeki malzemelerin dağıtımını yapar. Öncelikle belirli bir başlangıç noktası belirlenir ve dijkstra() metodu kullanılarak tüm diğer noktalara olan en kısa mesafe hesaplanır. Bu mesafe, malzemenin stokundan düşülür ve malzeme diğer noktalara dağıtılır.

# Kütüphaneler
Bu proje, osmnx ve matplotlib kütüphanelerini kullanır. İkisi de Python'da kurulum için pip aracılığıyla kolayca indirilebilir.


# Örnek Kullanım:
def main():
    # Belirli bir koordinat seçin
    koordinat = (41.7359782, 27.2230101)

    # Grafı oluşturun
    graph = Graph(koordinat)

    # Malzeme dağıtımını yapın
    graph.distribute()

    # Grafi gösterin
    graph.show()
if __name__ == '__main__':
    main()

Bu örnek, belirtilen koordinatta bir graf oluşturacak, malzeme dağıtımını yapacak ve son olarak oluşan grafi gösterecektir.

# dipnot:
    Verilen koordinatlar kırklareli merkez/valilik binasını referans alır.