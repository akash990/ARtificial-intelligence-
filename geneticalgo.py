import random
POPULATION_SIZE=100
GENES='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz,+-'
GOAL='I know c++, but I love python'
class Individual_Genes(obj):
	def__init__(self,chromosome):
		self.chromosome=chromosome
		self.fitness=self.calc_fitness()
	
    def calc_fitness(self):
		global GOAL
		fitness=0
		for i,j in zip(self.chromosome,Goal):
			if i!=j:
				fitness+=1
		
		return fitness
	@classmethod
	def create_gene(self):
		global GOAL
		g_len=len(GOAL)
		return [self.mutate_gene() for i in range (g_len)]
		
	@classmethod
	def mutate_genes(self):
		global GENES
		gene=random.choice(GENES)
		return gene
		
	def cross_over(self,obj2):
		child_chromosome=[]
		for i,j in zip(self.chromosome,obj2.chromosome):
			p=random.random()
			if p<0.45:
				child_chromosome.append(i)
			elif p<0.90:
				child_chromosome.append(j)
			else:
				child_chromosome.append(self.mutate_genes())
		return Individual_Genes(child_chromosome)
		
	def main():
		global POPULATION_SIZE
		generation=1
		sol_found=False
		population=[]
		for i in range(POPULATION_SIZE):
			g=individual_Genes.create_gene()
			population.append(Individual_Genes)
			
		while not sol_found:
			population=sorted(population,key=lambda x:x.fitness)
			if population[0].fitness<=0:
				sol_found=True
				break
				
			new_gene=[]
			tmp=int((10*POPULATION_SIZE)/100)
			new_gene.extend(population[:tmp])
			for i in range(tmp):
				item1=random.choice(population[:50])
				item1=random.choice(population[:50])
				new_gene.append(child)
				population=new_geneprint("Generation",generation,population[0].chromosome,population[0].chromosome,population[0].fitness)
				generation+=1
				
			if__name__=='__main__':
				main()