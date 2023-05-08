#include<bits/stdc++.h>
#include<unistd.h>
using namespace std;

#define ll long long
#define sz(x) (int)x.size()

const string cpp_path="D:\\Github\\Scripts\\casting\\";
const string scrcpy_path=cpp_path+"scrcpy\\";
const string sndcpy_path=cpp_path+"sndcpy\\";
const string info_path=cpp_path+"info\\";

int i;
int device_id,app_id,connection_type;
string tmp;
fstream file;
bool video,audio;

vector<string> app= {
	"0",
	"Tablet",
	"Phone",
	"Sky",
};

vector<string> connection= {
	"0",
	"WIFI",
	"USB",
};

struct device_info {
	string name,ip,port,model;
};

vector<device_info> device= {
	{"","","",""},
	{"POCO F2 Pro","","",""}, //phone
	{"Samsung Tab S7","","",""}, //tablet
	{"Honor V20","","",""}, //tablet
};

void read_info();
void write_info();

void choose_device();
void same_as_before();

int ask(string question);

void cast_screen(bool asked);
void reconnect(bool asked);
void cast_audio(bool asked);

int main() {
	choose_device();

	read_info();
	if (ask("same as before? (1/0) = ")==1) {
		same_as_before();
	} else {
		reconnect(0);
		cast_screen(0);
		cast_audio(0);
	}
	write_info();

	return 0;
}

void print_divider() {
	printf("\n============================\n");
}

int ask(string question) {
	cout << question;
	int ans;
	scanf("%d",&ans);
	return ans;
}

void choose_device() {
	//choose device to connect
	for (i=1; i<sz(device); ++i) {
		cout<<i<<" : "<<device[i].name<<endl;
	}
	device_id=ask("\ndevice = ");
	print_divider();
}

void reconnect(bool asked) {
	//connect phone wirelessly

	//list out the devices connected
	chdir(scrcpy_path.c_str());
	system("adb devices");

	//Connect using USB
	if (asked==0) {
		for (i=1; i<sz(connection); ++i) {
			cout << i << " : " << connection[i] << endl;
		}
		connection_type = ask("\nConnection Type = ");
	
		if (connection[connection_type]=="USB") {
			//change the connection method from USB to TCP through port 5555
			device[device_id].port="5555";
			tmp="adb -s "+device[device_id].model+" tcpip 5555";
			system(tmp.c_str());
		}

		//connect using WIFI and ask for new port
		else if (connection[connection_type]=="WIFI") {
			device[device_id].port = to_string(ask("Port = "));
		}
	}

	printf("\nConnecting......\n");

	tmp="adb connect "+device[device_id].ip+":"+device[device_id].port;
	system(tmp.c_str());

	print_divider();
}

void cast_screen(bool asked) {
	//cast phone's screen
	if (asked || (video=ask("\nscreen? (1/0) = "))==1) {
		if (asked==0) {
			for (i=1; i<sz(app); ++i) {
				cout<<i<<" : "<<app[i]<<endl;
			}
			app_id = ask("\nID = ");
		}

		chdir(scrcpy_path.c_str());

		//'start' run in a new window, can continue the next decision without stucking on this process
		tmp="start "+app[app_id]+".vbs --window-title "+app[app_id]+" -s "+device[device_id].ip+":"+device[device_id].port;
		system(tmp.c_str());

		printf("Starting screen cast...\n");
	}
	print_divider();
}

void cast_audio(bool asked) {
	//cast phone's audio
	if (asked || (audio=ask("\naudio (1/0) = "))==1) {
		chdir(sndcpy_path.c_str());

		tmp="start sndcpy "+device[device_id].ip+":"+device[device_id].port;
		system(tmp.c_str());

		chdir("..\\");
	}
	print_divider();
}

void same_as_before() {
	reconnect(1);
	if (video) cast_screen(1);
	if (audio) cast_audio(1);
}

void read_info() {
	chdir(info_path.c_str());
	file.open(device[device_id].name+".txt");

	file >> device[device_id].ip;
	file >> device[device_id].port;
	file >> device[device_id].model;
	file >> connection_type;
	file >> app_id;
	file >> video;
	file >> audio;

	//print the infomation for checking
	cout << "Device: " << device[device_id].name << endl;
	cout << "IP:" << device[device_id].ip << endl;
	cout << "Port: " << device[device_id].port << endl;
	cout << "Model: " << device[device_id].model << endl;
	cout << "Connection Type: " << connection[connection_type] << endl;
	cout << "App: " << app[app_id] << endl;
	cout << "Video: " << video << endl;
	cout << "Audio: " << audio << endl;

	print_divider();
	file.close();
}

void write_info() {
	chdir(info_path.c_str());
	file.open(device[device_id].name+".txt");

	file << device[device_id].ip << endl;
	file << device[device_id].port << endl;
	file << device[device_id].model << endl;
	file << connection_type << endl;
	file << app_id << endl;
	file << video << endl;
	file << audio << endl;

	file.close();
}

/*

*/

