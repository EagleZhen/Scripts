#include<cstdio>
#include<vector>
#include<cstdlib>
using namespace std;

#define ll long long
#define debug_message 0
#define debug if (debug_message)
#define debug0 if (0)
#define sz(x) (int)x.size()

int i,t,j;
int nt,n,m;
vector<int> a;

int main(){
//	freopen(".in","r",stdin);
//  freopen(".out","w",stdout);
	
	printf("Total number of pages = ");
	scanf("%d",&n);
	
	printf("Number of pages in one page (1/2) = ");
	scanf("%d",&m);
	
	printf("\n");
	if (m==1) {
		if (n%2!=0) {
			printf("special:\n\n");
			for (i=n-n%2+1; i<=n; ++i) printf("%d%c",i,i==n?' ':',');
			printf("\n\n");
		}
		
		printf("first:\n\n");
		for (i=2; i<=n-n%2; i+=2) printf("%d%c",i,i==n-n%2?' ':',');
		printf("\n\n");
		
		printf("second:\n\n");
		for (i=n-n%2-1; i>=1; i-=2) printf("%d%c",i,i==1?' ':',');
		printf("\n\n");
	}
	
	else {
		if (n%4!=0) {
			printf("special first:\n\n");
			for (i=n-n%4+1; i<=min(n,n-n%4+2); ++i) printf("%d ",i);
			printf("\n\nspecial second:\n\n");
			for (;i<=n; ++i) printf("%d ",i);
			printf("\n\n");
		}
		
		printf("first:\n\n");
		for (i=3; i<=n-n%4; i+=4) printf("%d,%d%c",i,i+1,i==n-n%4-1?' ':',');
		printf("\n\n");
		
		printf("second:\n\n");
		for (i=n-n%4-2; i>=1; i-=4) printf("%d,%d%c",i-1,i,i==2?' ':',');		
		printf("\n\n");
	}
	
	system("pause");
	
	return 0;
}
/*

*/
