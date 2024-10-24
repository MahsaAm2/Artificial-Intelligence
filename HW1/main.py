from collections import deque
import pandas as pd

df = pd.read_excel('straight.xlsx')

class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    # heuristic function
    def h(self, n,stop_node):
        for i in range(0, 31):
            if stop_node == df['name'][i]:
                x = i
        return (df[n][x])



    def a_star_algorithm(self, start_node, stop_node):

        open_list = set([start_node])
        first=0;
        closed_list = set([])
        g = {}
        g[start_node] = 0
        parents = {}
        parents[start_node] = start_node
        while len(open_list) > 0:
            n = None
            for v in open_list:
                if n == None or g[v] + self.h(v,stop_node) < g[n] + self.h(n,stop_node):
                    n = v;

            if (n == None):
                print('Path does not exist!')
                return None

            if (n == stop_node):
                reconst_path = []

                while parents[n] != n:
                    if first==0:
                        flag=n
                        first=1
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)

                reconst_path.reverse()

                print(reconst_path)
                print(g[flag]);
                return reconst_path


            for (m, weight) in self.get_neighbors(n):

                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                else:
                    if (g[m] > g[n] + weight):
                        g[m] = g[n] + weight
                        parents[m] = n

                        if (m in closed_list):
                            closed_list.remove(m)
                            open_list.add(m)


            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None


adjacency_list = {
    'اراک': [('اصفهان', 282), ('تهران', 280), ('خرم آباد', 211), ('قزوین', 320), ('قم', 135), ('کرج', 310), ('همدان', 167)],
    'اردبیل': [('تبریز', 277), ('رشت', 262), ('زنجان', 261)],
    'ارومیه': [('تبریز', 146), ('زنجان', 434), ('سنندج', 409)],
    'اصفهان': [('اراک', 282), ('خرم آباد', 391), ('سمنان', 570), ('شهرکرد', 100), ('شیراز', 481), ('قم', 273), ('یاسوج', 322), ('یزد', 311)],
    'اهواز': [('ایلام', 448), ('بوشهر', 431), ('خرم آباد', 328), ('شهرکرد', 468), ('یاسوج', 425)],
    'ایلام': [('اهواز', 448), ('خرم آباد', 249), ('کرمانشاه', 172)],
    'بجنورد': [('سمنان', 509), ('گرگان', 304), ('مشهد', 275)],
    'بندر عباس': [('بوشهر', 713), ('زاهدان', 763), ('شیراز', 575), ('کرمان', 490)],
    'بوشهر': [('اهواز', 431), ('بندر عباس', 713), ('شیراز', 302), ('یاسوج', 291)],
    'بیرجند': [('زاهدان', 466), ('سمنان', 850), ('کرمان', 566), ('مشهد', 492), ('یزد', 628)],
    'تبریز': [('اردبیل', 277), ('ارومیه', 146), ('زنجان', 307)],
    'تهران': [('اراک', 280), ('ساری', 280), ('سمنان', 266), ('قزوین', 150), ('قم', 148), ('کرج', 51)],
    'خرم آباد': [('ارک', 211), ('اصفهان', 391), ('اهواز', 328), ('ایلام', 249), ('شهرکرد', 275), ('کرمانشاه', 145), ('همدان', 140)],
    'رشت': [('اردبیل', 262), ('زنجان', 197), ('ساری', 364), ('قزوین', 172)],
    'زاهدان': [('بندر عباس', 763), ('بیرجند', 466), ('کرمان', 519)],
    'زنجان': [('اردبیل', 261), ('تبریز', 307), ('ارومیه', 434), ('رشت', 197), ('سنندج', 285), ('قزوین', 178), ('همدان', 259)],
    'ساری': [('تهران', 280), ('رشت', 364), ('سمنان', 197), ('قزوین', 397), ('کرج', 299), ('گرگان', 133)],
    'سمنان': [('اصفهان', 570), ('بجنورد', 509), ('بیرجند', 850), ('تهران', 226), ('ساری', 197), ('قم', 281), ('گرگان', 309), ('مشهد', 673)],
    'سنندج': [('ارومیه', 409), ('زنجان', 285), ('کرمانشاه', 136), ('همدان', 176)],
    'شهرکرد': [('اصفهان', 100), ('اهواز', 468), ('خرم آباد', 275), ('یاسوج', 270)],
    'شیراز': [('اصفهان', 481), ('بندر عباس', 575), ('بوشهر', 302), ('کرمان', 570), ('یاسوج', 181), ('یزد', 442)],
    'قزوین': [('اراک', 320), ('تهران', 150), ('رشت', 172), ('زنجان', 178), ('ساری', 397), ('کرج', 101), ('همدان', 273)],
    'قم': [('اراک', 135), ('اصفهان', 273), ('تهران', 148), ('سمنان', 281)],
    'کرج': [('اراک', 310), ('تهران', 51), ('ساری', 299), ('قزوین', 101)],
    'کرمان': [('بندر عباس', 490), ('بیرجند', 566), ('زاهدان', 516), ('یزد', 368)],
    'کرمانشاه': [('ایلام', 172), ('خرم آباد', 145), ('سنندج', 136), ('قزوین', 419), ('همدان', 183)],
    'گرگان': [('بجنورد', 304), ('ساری', 133), ('سمنان', 309), ('قزوین', 535)],
    'مشهد': [('بجنورد', 275), ('بیرجند', 492), ('سمنان', 673)],
    'همدان': [('اراک', 167), ('خرم آباد', 140), ('زنجان', 259), ('سنندج', 176), ('کرمانشاه', 183)],
    'یاسوج': [('اصفهان', 322), ('اهواز', 425), ('بوشهر', 291), ('شهرکرد', 270), ('شیراز', 181)],
    'یزد': [('اصفهان', 311), ('بیرجند', 628), ('شیراز', 442), ('کرمان', 368)]




}
graph1 = Graph(adjacency_list)
#graph1.a_star_algorithm('قم', 'ساری')
graph1.a_star_algorithm('اصفهان', 'مشهد')


