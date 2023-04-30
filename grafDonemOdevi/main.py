import heapq
import osmnx as ox
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, koordinat):
        self.G = ox.graph_from_point(koordinat, dist=1500, dist_type='network', network_type='drive')

    def show(self):
        ox.plot_graph(self.G)
        plt.show()

    def dijkstra(self, start, end):
        heap = [(0, start)]
        visited = set()
        
        while heap:
            (cost, node) = heapq.heappop(heap)
            if node not in visited:
                visited.add(node)
                if node == end:
                    return cost
                for neighbor, data in self.G[node].items():
                    c = data.get('length', 1) 
                    heapq.heappush(heap, (cost + c, neighbor))
        return -1

    def distribute(self):
        materials = [
            {'type': 'Saglik malzemesi', 'stock': 100},
            {'type': 'Temel gıda', 'stock': 100},
            {'type': 'Isinma Gereci', 'stock': 70},
            {'type': 'Giyecek', 'stock': 70}
        ]
        for material in materials:
            material_type = material['type']
            stock = material['stock']
            print('Dagitimi yapilan malzeme -->', material_type)
            node_list = list(self.G.nodes())
            start = node_list[0]
            for node in self.G.nodes():
                if material_type == 'Saglik malzemesi':
                    dist = self.dijkstra(start, node)
                elif material_type == 'Temel gıda':
                    dist = self.dijkstra(start, node)
                elif material_type == 'Isinma Gereci':
                    dist = self.dijkstra(start, node)
                elif material_type == 'Giyecek':
                    dist = self.dijkstra(start, node)
                
                if dist != -1 and dist <= stock:
                    stock -= dist
                
                    if dist > 0:
                        print(f'{dist} birim {node} noktasina isaretlendi.')
                        print(f'kalan stok: {stock}')
def main():
    koordinat = (41.7359782, 27.2230101)
    graph = Graph(koordinat)
    graph.distribute()
    graph.show()

if __name__ == '__main__':
    main()
