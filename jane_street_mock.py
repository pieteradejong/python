"""
Jane Street Mock interview

Answer process:
https://youtu.be/V8DGdPkBBxg?t=317

# Question:

example facts:
    m = 3.28 ft
    ft = 12 in
    hr = 60 min
    min = 60 sec
example queries:
    2 m = ? in   --> answer = 78.72
    13 in = ? m  --> answer = 0.330 (roughly)
    13 in = ? hr --> "not convertible!"

input: 
    facts as (string, float, string)
    query as (float, string, string)

TODO: 
- enable chaining of units, e.g. m -> ft -> in
- approach: each set of related units can be represented by a connected graph, 
and the set of all units as a union of those disjointed graph.
- algorithm: graph search starting at the first unit given, target the second unit.

"""
from typing import List, Tuple, Dict

class Solution:
    NOT_CONVERTIBLE_STRING = "not convertible!"

    def parse_facts(self, facts: List[Tuple[str, float, str]]) -> None:
        self.facts = dict()
        for _f in facts:
            unit_from, quantity, unit_to = _f[0], _f[1], _f[2]
            if unit_from not in self.facts:
                self.facts[unit_from] = dict()
            self.facts[unit_from][unit_to] = quantity
        
    
    def parse_facts_to_graph(self, facts: List[Tuple[str, float, str]]) -> List[list[float]]:
        pass
    
    def parse_query(self, queries: List[Tuple[float, str, float]]) -> None:
        for _q in queries:
            quantity_from, unit_from, unit_to = _q[0], _q[1], _q[2]
            if unit_from not in self.facts:
                # print(Solution.NOT_CONVERTIBLE_STRING)
                print("unit_from not in facts")
                continue
            if unit_to not in self.facts[unit_from]:
                # print(Solution.NOT_CONVERTIBLE_STRING)
                print("unit_to not in facts[unit_from]")
                continue
            print(str(self.facts[unit_from][unit_to] * quantity_from))

def main():
    s = Solution()
    facts = [
        ('m', 3.28, 'ft'),
        ('ft', 12, 'in'),
        ('hr', 60, 'min'),
        ('min', 60, 'sec')
    ]
    queries = [
        (2, 'm', 'in'),
        (13, 'in', 'm'),
        (13, 'in', 'hr')
    ]

    s.parse_facts(facts)
    s.parse_query(queries)

if __name__ == "__main__":
    main()    
