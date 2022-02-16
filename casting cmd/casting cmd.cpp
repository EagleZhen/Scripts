#include<bits/stdc++.h>
#include<unistd.h>
using namespace std;

#define ll long long
#define sz(x) (int)x.size()

const string cpp_path="D:\\Github\\Scripts\\casting cmd\\";
const string scrcpy_path=cpp_path+"scrcpy\\";
const string sndcpy_path=cpp_path+"sndcpy\\";

int i;
int device_id,app_id;
string tmp;
fstream file;
bool video,audio;

vector<string> app= {
	"0",
	"Tablet",
	"Phone",
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

void choose_device() {
	//choose device to connect
	for (i=1; i<sz(device); ++i) cout<<i<<" : "<<device[i].name << " || " << device[i].ip <<endl;
	device_id=ask("\ndevice = ");
	print_divider();
}

void reconnect(bool asked) {
	//connect phone wirelessly

	//list out the devices connected
	chdir(scrcpy_path.c_str());
	system("adb devices");

	//change the connection method from USB to TCP through port 5555
	if (device_id==1) {
		device[device_id].port="5555";
		system("adb -s e718ad0 tcpip 5555");
	}

	else if (device_id==2) {
		if (asked==0) {
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
	if (asked || (video=ask("screen? (1/0) = "))==1) {
		if (asked==0) {
			for (i=1; i<sz(app); ++i) cout<<i<<" : "<<app[i]<<endl;
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
	//port
	//app id
	//video
	//audio
	chdir(cpp_path.c_str());
	file.open("info"+to_string(device_id)+".txt");
	file >> device[2].port >> app_id >> video >> audio;

	//print the infomation for checking
	cout << "Device: " << device[device_id].name << "\nApp: " << app[app_id] << "\nVideo: " << video << "\nAudio: " << audio << endl;
	print_divider();
	file.close();
}

void write_info() {
	chdir(cpp_path.c_str());
	file.open("info"+to_string(device_id)+".txt");
	file << device[2].port << "\n" << app_id << "\n" << video << "\n" << audio << endl;
	file.close();
}

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
/*

*/

