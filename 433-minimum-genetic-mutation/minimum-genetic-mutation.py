from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        return self.bfs(startGene, endGene, bank)
  
    def bfs(self, startGene, endGene, bank):
        q = deque()
        num_mutations = 0
        q.append((startGene, num_mutations))
        while q:
            currentGene, num_mutations = q.popleft()
            if currentGene == endGene:
                return num_mutations
    
            for index in range(len(currentGene)):
                for s in ["A", "C", "G", "T"]:
                    new_gene = currentGene[0:index] + s + currentGene[index + 1:]
                    if new_gene in bank:
                        bank.remove(new_gene)
                        q.append((new_gene, num_mutations + 1))
        return -1
