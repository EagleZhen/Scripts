#include<bits/stdc++.h>
#include<unistd.h>
using namespace std;

#define ll long long
#define sz(x) (int)x.size()

const int maxn=1e5+5;

int i;
int id;

vector<string> app={
"0",
"Sky",
"Phigros",
"PUBG",
};

string tmp;

int main(){
	//connect phone wirelessly
	printf("connect? (1/0) = ");
	scanf("%d",&id);
	if (id==1){
		chdir("C:\\Apps\\scrcpy-win64-v1.14\\");
		//clear the devices connected to avoid "more than one device/emulator"
		system("adb kill-server");
		//change the connection method from USB to TCP through port 5555
		system("adb tcpip 5555");	
		system("adb connect 192.168.1.104:5555");
	}
	printf("\n====================\n");

	//cast phone's screen
	printf("\nscreen? (1/0) = ");
	scanf("%d",&id);
	if (id==1){
		for (i=1; i<sz(app); ++i) cout<<i<<" : "<<app[i]<<endl;
		
		printf("\nID = ");
		scanf("%d",&id);
		
		chdir("C:\\Apps\\scrcpy-win64-v1.14\\");
		//'start' run in a new window, can continue the next decision without stucking on this process
		tmp="start scrcpy-noconsole.exe --window-title "+app[id]+" -s 192.168.1.104:5555";
		system(tmp.c_str());
	}
	printf("\n====================\n");
	
	//cast phone's audio
	printf("\naudio (1/0) = ");
	scanf("%d",&id);
	if (id==1){
		chdir("C:\\Apps\\sndcpy-with-adb-windows-v1.0\\");
		tmp="sndcpy 192.168.1.104:5555";
		system(tmp.c_str());
//		system("C:\\Apps\\sndcpy-with-adb-windows-v1.0\\audio");
	}

	return 0;
}
/*
C:\Apps\sndcpy-with-adb-windows-v1.0\sndcpy.bat 192.168.1.104:5555
*/

