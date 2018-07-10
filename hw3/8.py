import sys
import math
import matplotlib.pyplot as plt
d = 20
class record():
	def __init__(self, x, y):
		self.x = x
		self.y = y	
def sign(x):
	if x > 0:
		return 1
	else:
		return -1
def dog(a, b):
	tmp = 0.0
	for i in range(d+1):
		tmp += a[i]*b[i]
	return tmp
def sigmoid(x):
	return 1.0/(1.0 + math.exp(-1*x))

if __name__ == "__main__":
	training_data = []
	testing_data = []
	for line in open("training_data.txt", "r"):
		tmp_x = line.split()[:-1]
		for i in range(len(tmp_x)):
			tmp_x[i] = float(tmp_x[i])
		tmp_x.append(0.0)
		tmp_y = line.split()[20]
		tmp_y = float(tmp_y)
		tmp = record(tmp_x, tmp_y)
		training_data.append(tmp)
	N = len(training_data)
	for line in open("testing_data.txt", "r"):
		tmp_x2 = line.split()[:-1]
		for i in range(len(tmp_x2)):
			tmp_x2[i] = float(tmp_x2[i])
		tmp_x2.append(0.0)
		tmp_y2 = line.split()[20]
		tmp_y2 = float(tmp_y2)
		tmp2 = record(tmp_x2, tmp_y2)
		testing_data.append(tmp2)
	N2 = len(testing_data)
	ita = 0.01
	iteration = 2000
	it = []
	version1 = []
	version2 = []

	# version1
	weight = []
	for i in range(d+1):
		weight.append(1.0)
	for i in range(iteration):
		g = [0.0 for t in range(d+1)]
		for j in range(N):
			tmp = sigmoid(-1*dog(weight, training_data[j].x)*training_data[j].y)
			for k in range(d+1):
				g[k] += -1.0*tmp*training_data[j].x[k]*training_data[j].y
		for j in range(d+1):
			g[j] = g[j]/N
		
		for j in range(d+1):
			weight[j] -= ita * g[j]
		
		# calculate E_IN 
		error = 0
		for j in range(N):
			if sign(dog(training_data[j].x, weight)) != training_data[j].y:
				error += 1
		err_rate1 = error/N
		print("v1 -> ", "E_IN = ", err_rate1)

		# calculate E_OUT
		# error = 0
		# for j in range(N2):
		# 	if sign(dog(testing_data[j].x, weight)) != testing_data[j].y:
		# 		error += 1
		# err_rate1 = error/N2
		# print("E_OUT = ", err_rate1)	

		it.append(i+1)
		version1.append(err_rate1)
	
	# version2
	weight = []
	for i in range(d+1):
		weight.append(1)
	for i in range(iteration):
		g = [0.0 for t in range(d+1)]
		tmp = sigmoid(-1*dog(weight, training_data[i%N].x)*training_data[i%N].y)
		for j in range(d+1):
			g[j] += -1*tmp*training_data[i%N].x[j]*training_data[i%N].y
		# upgrade weight
		for j in range(d+1):
			weight[j] = weight[j] - (ita*g[j])
		
		# calculate E_IN 
		error = 0
		for j in range(N):
			if sign(dog(training_data[j].x, weight)) != training_data[j].y:
				error += 1
		err_rate1 = error/N
		print("v2 -> ", "E_IN = ", err_rate1)

		# calculate E_OUT
		# error = 0
		# for j in range(N2):
		# 	if sign(dog(testing_data[j].x, weight)) != testing_data[j].y:
		# 		error += 1
		# err_rate1 = error/N2
		# print("E_OUT = ", err_rate1)	

		version2.append(err_rate1)

	plt.plot(it, version1)
	plt.plot(it, version2)
	plt.title("histogram")
	plt.xlabel("iter")
	plt.ylabel("E_in")
	plt.show()







