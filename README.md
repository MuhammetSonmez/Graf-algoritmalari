# Graf-algoritmalari

Bu proje, graf teorisi kavramlarını ve Dijkstra algoritmasını kullanarak malzeme tedarik uygulaması için bir çözüm önermektedir. Dijkstra algoritması, verilen ağırlıklı bir graf üzerinde en kısa yol problemi çözmek için kullanılır.

## Graf Teorisi Hakkında Genel Bilgiler

Graf teorisi, objeler arasındaki bağlantıları temsil etmek için kullanılan matematiksel bir yapıdır. Graf teorisi, ayrık matematikte kullanılan bir alandır ve pek çok alanda uygulanabilir. Örnek olarak, bir bilgisayar ağını, bir sosyal ağı veya bir ulaşım ağı temsil etmek için kullanılabilir.

### Graf Algoritmaları

Graf teorisi, birçok uygulama için kullanışlı olan çeşitli algoritmalara sahiptir. Bunlar arasında en kısa yol bulma, minimum kesimler, maksimum akış, çizge boyama ve çok daha fazlası bulunur.

Bu projede kullanılan Dijkstra algoritması, ağırlıklı bir graf üzerinde en kısa yol problemi çözmek için kullanılır. Dijkstra algoritması, başlangıç düğümünden diğer tüm düğümlere olan en kısa yolu bulmak için kullanılır.

## Malzeme Tedarik Uygulaması

Bu proje, bir malzeme tedarik uygulaması için bir çözüm önermektedir. Bu uygulama, belirli bir malzemeyi üretmek için gerekli olan tüm malzemeleri tedarik etmek için kullanılır.

Bu uygulama, graf teorisine dayalı bir yaklaşım kullanır. Her malzemenin bir düğüm olarak temsil edildiği bir graf oluşturulur. Her bağlantı, iki malzeme arasındaki ilişkiyi temsil eder.

### Kullanılan Teknolojiler

Bu uygulama Python programlama dili kullanılarak oluşturulmuştur. Ayrıca, OpenStreetMap matplotlib, ve heapq kütüphaneleri kullanılmıştır.

## Kullanım

1. Öncelikle, `networkx` ve `osmnx` kütüphanelerini kurun. Aşağıdaki komutları kullanabilirsiniz:

   ```
   pip install matplotlib
   pip install osmnx
   pip install heapq
   ```

2. Projenin ana dizinindeki `main.py` dosyasını çalıştırın:

   ```
   python main.py
   ```

3. Program çalıştırıldığında, önce OpenStreetMap'den bir kentsel alan yüklenir ve bu alanın grafiği oluşturulur. Daha sonra, kullanıcının seçtiği bir başlangıç ve bitiş noktası belirlenir. Son olarak, Dijkstra algoritması kullanılarak en kısa yol hesaplanır ve sonuç kullanıcıya gösterilir.

4. Opsiyonel olarak, program sonucunu görselleştirmek için `folium` kütüphanesi kullanılabilir. 

## Algoritma

Dijkstra algoritması, en kısa yol problemini çözmek için kullanılan bir algoritmadır. Algoritma, ağırlıklı bir graf (yani, kenarların her birinin bir ağırlığı veya maliyeti vardır) verildiğinde, iki düğüm arasındaki en kısa yolu bulmak için kullanılır.

Dijkstra algoritması, grafın düğüm sayısı ve kenar sayısı ile orantılı olarak performansı azalır, ancak genellikle uygulamalar için yeterli hızda çalışır.

## DIPNOT
   bu ödev, Muhammet Sönmez ve Mehmet Koyuncuoğlu tarafından hazırlanmıştır.
