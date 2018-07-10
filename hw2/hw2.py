import random
import time
import operator
import matplotlib.pyplot as plt
class record():
	def __init__(self, x, y):
		self.x = x
		self.y = y
def sign(x):
	if x <= 0:
		return -1.00000
	else:
		return 1.00000
if __name__ == "__main__":
	size = 20
	in_sum = 0.00000
	out_sum = 0.00000
	random.seed(time.time())
	e_in = []
	e_out = []
	for i in range(1000):
		trainingdata = []
		
		# generate trainingdata
		for j in range(size):
			t = random.uniform(-1, 1)
			tmp = record(t, sign(t))
			trainingdata.append(tmp)
		# get noise
		for j in range(size):
			t = random.uniform(-2, 8)
			if t < 0:
				trainingdata[j].y *= -1
		trainingdata.sort(key=operator.attrgetter('x'))
		best_th = 0.00000
		best_s = 0
		# E_in
		min_err = 1.00000
		sz = 20.00000
		for j in range(size+1):
			if j == 0:
				th = -2.00000
			elif j == size:
				th = 2.00000
			else:
				th = (trainingdata[j].x + trainingdata[j-1].x)/2.00000
			err_num = 0.00000
			for k in range(size):
				hyp_ans = sign(trainingdata[k].x-th)
				if hyp_ans != trainingdata[k].y:
					err_num += 1
			if err_num/size < min_err:
				best_s = 1.000000
				best_th = th
				min_err = err_num/sz
			err_num = 0.00000
			for k in range(size):
				hyp_ans = -1.00000*sign(trainingdata[k].x-th)
				if hyp_ans != trainingdata[k].y:
					err_num += 1
			if err_num/size < min_err:
				best_s = -1.00000
				best_th = th
				min_err = err_num/sz
		in_sum += min_err
		e_in.append(min_err)
		# E_out
		if sign(best_th) > 0:
			err = 0.5 + 0.3*best_s*(best_th-1.00000)
		else:
			err = 0.5 + 0.3*best_s*(-1.00000*best_th - 1.00000)
		e_out.append(err)
		out_sum += err
	# print "average E_in : ", in_sum/1000.000
	# print "average E_out : ", out_sum/1000.000
	# plt.scatter(e_in, e_out)
	# plt.xlabel('E_in')
	# plt.ylabel('E_out')
	# plt.show()


