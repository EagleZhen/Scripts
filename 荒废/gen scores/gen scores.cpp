#include<cstdio>
#include<vector>
#include<algorithm>
#include<string>
#include<iostream>
#include<cmath>
using namespace std;

#define ll long long
#define debug_message 0
#define debug if (debug_message)
#define debug0 if (0)
#define sz(x) (int)x.size()

struct subtask {
	int val,cnt;
};

struct score {
	int val;
	vector<int> sub;
};

int attempt=75;
double sd=33.51,gap=1;

int freq_sub[20],freq_sc[20];
char c;
string s;
bool deter[20];

vector<subtask> sub;
vector<score> sc;

double cal_sum(vector<double> v) {
	double sum=0;
	int i;
	for (i=0; i<sz(v); ++i) sum+=v[i];
	return sum;
}

double cal_sd() {
	int i,t;
	vector<double> tmp= {};

	for (i=0; i<sz(sc); ++i) {
		for (t=1; t<=freq_sc[i]; ++t) {
			tmp.push_back(sc[i].val);
		}
	}

//	for (i=0; i<sz(tmp); ++i) printf("%.0lf%c",tmp[i],i==sz(tmp)-1?'\n':' ');

	double sum=cal_sum(tmp),mean=sum/sz(tmp);
	double ans=0;

	for (i=0; i<sz(tmp); ++i) ans+=(tmp[i]-mean)*(tmp[i]-mean)/(attempt-1);
	return sqrt(ans);
}

void ex(int id, int total) {
	int i,t,j;

	//already determined
	if (deter[id]) {
		ex(id+1,total);
		return;
	}

	if (id>=sz(sc) || total>=attempt) {
//		if (total==attempt) {
//			for (i=0; i<sz(sc); ++i) {
//				printf("%d: %d\n",i,freq_sc[i]);
//			}
//			printf("%lf\n",cal_sd());
//			printf("===================\n");
//		}

//freq_sc[2]+freq_sc[3]+freq_sc[6]+freq_sc[7]+freq_sc[8]+freq_sc[10]+freq_sc[12]+freq_sc[14]<=2 && 
		
		if (total==attempt && cal_sd()-sd<0.001 && cal_sd()-sd>=0) {
			for (i=0; i<sz(sc); ++i) {
				printf("%d:%d | ",sc[i].val,freq_sc[i]);
			}
			printf("\n");
			
			for (i=0; i<sz(sc); ++i) {
				for (t=1; t<=freq_sc[i]; ++t) {
					printf("%d ",sc[i].val);
				}
			}
			printf("\n");
			
			printf("%lf\n",cal_sd());
			printf("===================\n");
		}
		return;
	}

//	for (i=0; i<sz(sc); ++i) {
//		printf("%d: %d\n",i,freq_sc[i]);
//	}
//	printf("===================\n");

	for (i=0; i<=attempt; ++i) {
		freq_sc[id]+=i;

		//add frequency
		for (j=0; j<sz(sc[id].sub); ++j) {
			freq_sub[sc[id].sub[j]]+=i;
		}

		//too many people in that subtask
		for (t=0; t<sz(sub); ++t) {
			if (freq_sub[t]>sub[t].cnt) {
				//minus the previous frequency
				goto out;
			}
		}

		ex(id+1,total+i);
		freq_sc[id]-=i;

		//minus frequency
out:
		;
		freq_sc[id]-=i;
		for (j=0; j<sz(sc[id].sub); ++j) {
			freq_sub[sc[id].sub[j]]-=i;
		}
	}
}

int main() {
//	freopen("J211.txt","w",stdout);
	
	sub= {
		(subtask){0,75},
		(subtask){11,69},
		(subtask){14,68},
		(subtask){23,61},
		(subtask){19,57},
		(subtask){27,48},
		(subtask){6,45},
	};

	sc= {
		(score) { //0
			0, {0}
		},
		(score) { //1
			11, {1}
		},
		(score) { //2
			14, {2}
		},
		(score) { //3
			19, {4}
		},
		(score) { //4
			25, {1,2}
		},
		(score) { //5
			30, {1,4}
		},
		(score) { //6
			33, {2,4}
		},
		(score) { //7
			37, {2,3}
		},
		(score) { //8
			46, {4,5}
		},
		(score) { //9
			48, {1,2,3}
		},
		(score) { //10
			56, {2,3,4}
		},
		(score) { //11
			57, {1,4,5}
		},
		(score) { //12
			60, {2,4,5}
		},
		(score) { //13
			67, {1,2,3,4}
		},
		(score) { //14
			83, {2,3,4,5}
		},
		(score) { //15
			94, {1,2,3,4,5}
		},
		(score) { //16
			100, {1,2,3,4,5,6}
		},
	};

//	deter[0]=1;
//	freq_sub[0]=6;
//	freq_sc[0]=6;
	
//	int i=0;
	deter[2]=1,freq_sc[2]=0;
	deter[3]=1,freq_sc[3]=0;
	deter[6]=1,freq_sc[6]=0;
	deter[7]=1,freq_sc[7]=0;
	deter[8]=1,freq_sc[8]=0;
	deter[10]=1,freq_sc[10]=0;
	deter[12]=1,freq_sc[12]=0;
	deter[14]=1,freq_sc[14]=0;

	deter[16]=1;
	freq_sc[16]=45;
	for (int i=1; i<=6; ++i) freq_sub[i]=45;

	ex(0,45);

	return 0;
}
/*

*/
