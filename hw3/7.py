import random
import time
import operator
import numpy as np
import matplotlib.pyplot as plt

def sign(x):
	if x > 0:
		return 1
	else:
		return -1

if __name__ == '__main__':
	random.seed(time.time())
	N = 1000
	E_in_sum = 0.0
	E_out_sum = 0.0
	out = []
	out2 = []
	x = np.zeros(shape=(N, 3))
	test_x = np.zeros(shape=(N, 3))
	z = np.zeros(shape=(N, 6))
	test_z = np.zeros(shape=(N, 6))
	y = np.zeros(shape=(N, 1))
	test_y = np.zeros(shape=(N, 1))
	weight = np.zeros(shape=(6, 1))
	total_w = np.zeros(shape=(6, 1))
	for j in range(N):
		for i in range(N):
			dice = random.uniform(0, 1)
			dice2 = random.uniform(0, 1)
			x[i][0] = 1.0
			test_x[i][0] = 1.0
			x[i][1] = random.uniform(-1, 1)
			test_x[i][1] = random.uniform(-1, 1)
			x[i][2] = random.uniform(-1, 1)
			test_x[i][2] = random.uniform(-1, 1)
			y[i][0] = sign(x[i][1]*x[i][1] + x[i][2]*x[i][2] - 0.6)
			test_y[i][0] = sign(test_x[i][1]*test_x[i][1] + test_x[i][2]*test_x[i][2] - 0.6)
			if dice < 0.1:
				y[i][0] *= -1
			if dice2 < 0.1:
				test_y[i][0] *= -1
		for i in range(N):
			z[i][0] = 1;
			z[i][1] = x[i][1]
			z[i][2] = x[i][2]
			z[i][3]	= x[i][1]*x[i][2]
			z[i][4] = x[i][1]*x[i][1]
			z[i][5] = x[i][2]*x[i][2]
			test_z[i][0] = 1;
			test_z[i][1] = test_x[i][1]
			test_z[i][2] = test_x[i][2]
			test_z[i][3] = test_x[i][1]*test_x[i][2]
			test_z[i][4] = test_x[i][1]*test_x[i][1]
			test_z[i][5] = test_x[i][2]*test_x[i][2]
		weight = np.dot(np.dot(np.linalg.inv(np.dot(z.transpose(), z)), z.transpose()), y)
		err_num = 0
		err_num2 = 0
		tmp = np.zeros(shape=(N, 1))
		tmp = np.dot(z, weight)
		tmp2 = np.zeros(shape=(N, 1))
		tmp2 = np.dot(test_z, weight)
		for i in range(N):
			if sign(tmp[i][0]) != y[i][0]:
				err_num += 1
			if sign(tmp2[i][0]) != test_y[i][0]:
				err_num2 += 1 
		E_in_sum += err_num/N
		E_out_sum += err_num2/N
		# out.append(j+1)
		# out2.append(err_num2/N)
		total_w = np.add(total_w, weight)
	print("average E_in = ", E_in_sum/N)
	print("average E_out = ", E_out_sum/N)
	# print(total_w/1000)
	# plt.bar(out, out2)
	# plt.title("histogram")
	# plt.xlabel("iter")
	# plt.ylabel("E_out")
	# plt.show()







