import time

class Graph():
    graph:          str
    graph_width:    int
    graph_heigth:   int
    num:            int
    graph_data =    [
        '.',
        '.',
        '.',
        '.',
        '.',
        '.',
        '.',
        '.',
        '.',
        '.',
        '.',
        '.',
        '.',
        '.',
        '.',
        '.',
        '.',
        '.',
        '.',
        '.',
        '.',
        '.',
        '.'
    ]

    def __init__(self, h: int, w: int) -> None:
        self.graph_heigth, self.graph_width = [h, w]
        pass

    def get_graph_layout(self) -> str:
        gFile = open("assets/graph.txt", "r")
        g = gFile.read()
        gFile.close()
        return g

    def render_graph(self) -> str:
        self.graph = ""
        for line in self.graph_data:
            self.graph += f"{line}\r\n"
        
        return self.graph

    def append_to_graph(self, data: int) -> None:
        self.num = data
        new_data = self.generate_bar(data)
        graph_w = self.graph_width
        for i in range(0, self.graph_heigth):
            if len(self.graph_data[i]) >= self.graph_width:
                self.graph_data[i] = self.graph_data[i][1:graph_w]
            
            if i >= (self.graph_heigth - new_data):
                self.graph_data[i] += "#"
            else:
                self.graph_data[i] += "."

    def generate_bar(self, num: int) -> int:
        bar = 0
        if self.num < 1000: bar = 1
        elif self.num == 1000: bar = 2
        elif self.num > 1000 and self.num < 5000: bar = 3
        elif self.num == 5000: bar = 4
        elif self.num > 5000 and self.num < 10000: bar = 5
        elif self.num == 10000: bar = 6
        elif self.num > 10000 and self.num < 15000: bar = 7
        elif self.num == 15000: bar = 8
        elif self.num > 15000 and self.num < 20000: bar = 9
        elif self.num == 20000: bar = 10
        elif self.num > 20000 and self.num < 25000: bar = 11
        elif self.num == 25000: bar = 12
        elif self.num > 25000 and self.num < 30000: bar = 13
        elif self.num == 30000: bar = 14
        elif self.num > 30000 and self.num < 35000: bar = 15
        elif self.num == 35000: bar = 16
        elif self.num > 35000 and self.num < 40000: bar = 17
        elif self.num == 40000: bar = 18
        elif self.num > 40000 and self.num < 45000: bar = 19
        elif self.num == 45000: bar = 20
        elif self.num > 45000 and self.num < 50000: bar = 21
        elif self.num == 50000: bar = 22
        elif self.num > 50000: bar = 23

        return bar