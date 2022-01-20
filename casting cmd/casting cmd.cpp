#include<bits/stdc++.h>
#include<unistd.h>
using namespace std;

#define ll long long
#define sz(x) (int)x.size()

const string scrcpy_path=".\\scrcpy\\";
const string sndcpy_path=".\\sndcpy\\";

int i;
int device_id;
string tmp;

vector<string> app= {
	"0",
	"Tablet",
	"Sky",
};

struct device_info {
	string name,ip,port;
};

vector<device_info> device= {
	{"","",""},
	{"POCO F2 Pro","192.168.1.102","5555"}, //phone
	{"Samsung Tab S7","192.168.1.103",""}, //tablet
};

void print_divider() {
	printf("\n============================\n");
}

int ask(string question) {
	cout << question;
	int ans;
	scanf("%d",&ans);
	return ans;
}

void choose_device(){
	//choose device to connect
	for (i=1; i<sz(device); ++i) cout<<i<<" : "<<device[i].name << " || " << device[i].ip <<endl;
	device_id=ask("\ndevice = ");
	print_divider();
}

void reconnect(){
	//connect phone wirelessly
	fstream file("wireless debugging port.txt");

	//list out the devices connected
	chdir(scrcpy_path.c_str());
	system("adb devices");
	
	if (ask("reconnect? (1/0) = ")==1) {
		//change the connection method from USB to TCP through port 5555
		if (device_id==1) {
			system("adb -s e718ad0 tcpip 5555");
			device[device_id].port="5555";
		}

		else if (device_id==2) {
			printf("\nPort = ");
			cin >> device[device_id].port;
			file << device[device_id].port;
		}
		tmp="adb connect "+device[device_id].ip+":"+device[device_id].port;
		system(tmp.c_str());
	}
	//read the port for samsung tab s7 last time used from file
	else if (device_id==2){
		file >> device[device_id].port;
	}
	print_divider();
	chdir("..\\");
}

void cast_screen(){
	//cast phone's screen
	if (ask("screen? (1/0) = ")==1) {
		for (i=1; i<sz(app); ++i) cout<<i<<" : "<<app[i]<<endl;
		int app_id = ask("\nID = ");

		chdir(scrcpy_path.c_str());
		
		//'start' run in a new window, can continue the next decision without stucking on this process
		tmp="start "+app[app_id]+".vbs --window-title "+app[app_id]+" -s "+device[device_id].ip+":"+device[device_id].port;
		system(tmp.c_str());
		
		chdir("..\\");
	}
	print_divider();
}

void cast_audio(){
	//cast phone's audio
	if (ask("\naudio (1/0) = ")==1) {
		chdir(sndcpy_path.c_str());
		
		tmp="sndcpy "+device[device_id].ip+":"+device[device_id].port;
		system(tmp.c_str());
		
		chdir("..\\");
	}
	print_divider();
}

int main() {
	choose_device();
	reconnect();
	cast_screen();
	cast_audio();
	
	return 0;
}
/*
C:\Apps\sndcpy-with-adb-windows-v1.0\sndcpy.bat 192.168.1.104:5555
*/

