#include <stdio.h>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <string>
#include <fstream>
#include <iostream>
using namespace std;
#define d 5

struct data{
	double x[d];
	int y;
};
vector<data> training_data;
int data_size=0;

int dot_and_sign(double w[d], double x[d])
{
	double sum = 0.0;
	for(int i = 0; i < d; i++)
		sum += w[i]*x[i];
	if(sum >= 0)
		return 1;
	else
		return -1;
}

int main(){
	ifstream file("training_data.txt");
	string line;
	double w[d];
	int good=0, total=0;
	int freq[100];
	memset(freq, 0, sizeof(freq));
	while( !file.eof() ){
		data buf;
		buf.x[0] = 1;
		for(int i = 1; i < d; i++)
			file>>buf.x[i];
		file>>buf.y;
		training_data.push_back(buf);
		data_size++;
	}
	file.close();
	for(int i = 0; i < 2000; i++){
		random_shuffle(training_data.begin(), training_data.end());
		memset(w, 0.0, sizeof(w));
		bool OK=0;
		int idx = 0, times=0;
		while( !OK ){
			if(training_data[idx].y == dot_and_sign(w, training_data[idx].x))
				good++;
			else{
				double tmp[d];
				memset(tmp, 0.0, sizeof(tmp));
				for(int j = 0; j < d; j++)
					w[j] += training_data[idx].y*training_data[idx].x[j];
				times++;
				good = 0;
			}
			if(good == data_size)
				OK = 1;
			if(idx != data_size-1)
				idx++;
			else
				idx = 0;

		}
		printf("the %dth step : %d\n", i, times);
		total += times;
		freq[times]++;
	}
	printf("average step : %d\n", total/2000);
	return 0;
}
