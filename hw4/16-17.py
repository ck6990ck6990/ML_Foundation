import numpy as np
import matplotlib.pyplot as plt
def sign(x):
	if x >= 0:
		return 1
	else:
		return -1
def regulize(x, tmp_y, lamda, n):
	y = np.mat(tmp_y)
	w = ( x.T*x + lamda*np.mat(np.eye(3, 3)) ).I * (x.T * y.T)
	return w

def error(x, y, w, n):
	num = 0
	tmp = x*w
	for i in range(n):
		if sign(tmp[i][0]) != y[i]:
			num += 1
	err = num/n
	return err

if __name__ == "__main__":
	training_x = []
	training_y = []
	testing_x = []
	testing_y = []
	train_idx = 0
	test_idx = 0
	for line in open("training_data.txt", "r"):
		train_x = line.split()[:-1]
		for i in range (len(train_x)):
			train_x[i] = float(train_x[i])
		train_x.insert(0, 1)
		training_x.append(train_x)
		train_y = float(line.split()[2])
		training_y.append(train_y)
		train_idx += 1
	for line in open("testing_data.txt", "r"):
		test_x = line.split()[:-1]
		for i in range (len(test_x)):
			test_x[i] = float(test_x[i])
		test_x.insert(0, 1)
		testing_x.append(test_x)
		test_y = float(line.split()[2])
		testing_y.append(test_y)
		test_idx += 1
	x1 = np.mat(training_x)
	x2 = np.mat(testing_x)
	lamda_arr = []
	E_in_arr = []
	E_out_arr = []
	E_val_arr = []
	for i in range(-10, 3):
		lamda = 10**i
		# print(x1[0][0], [0][0])
		w = regulize(x1[:120], training_y[:120], lamda, 120)
		E_in = error(x1[:120], training_y[:120], w, 120)
		E_val = error(x1[121:], training_y[121:], w, train_idx-121)
		E_out = error(x2, testing_y, w, test_idx)
		lamda_arr.append(lamda)
		E_in_arr.append(E_in)
		E_out_arr.append(E_out)
		E_val_arr.append(E_val)
		print("lamda = ", lamda, "E_in = ", E_in)
		print("lamda = ", lamda, "E_out = ", E_out)
		print("lamda = ", lamda, "E_val = ", E_val)
	plt.plot(lamda_arr, E_in_arr)
	plt.plot(lamda_arr, E_val_arr)
	plt.xlabel("lamda")
	plt.ylabel("E_in and E_val")
	plt.show()


