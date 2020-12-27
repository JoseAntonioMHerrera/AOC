#include <iostream>
#include <fstream>
#include <string>
#include <unordered_set>
#include <vector>
#include <set>
#include <algorithm>
#include <sstream>
using namespace std;

void match2space(string* text, set<char> patterns) {
    for(auto it = (text)->begin(); it != (text)->end(); ++it) {
    	char value = *it;
    	auto pos = patterns.find(value);
    	if(pos != patterns.end()){
    		*it = ' ';
    	}
    }
}

int main(){
	fstream instream;
	std::unordered_set<std::string> passwords_policy;
	instream.open("input.txt",ios::in);
	int valid_passwords=0;
	if(instream.is_open()){
		string line;
		while(getline(instream,line)){
			passwords_policy.insert(line);
		}
	}

	// PART ONE
	for(auto it=passwords_policy.begin(); it != passwords_policy.end();it++){
		set<char> patterns;
		patterns.insert('-');
		patterns.insert(':');
		string token = (*it);
		match2space(&token,patterns);
		stringstream ss;
		string temp;
		vector<int> numbers;
		vector<string> letter_password;
		int number=0;

		ss << token;
		while(!ss.eof()){
			ss >> temp;
			if(stringstream(temp) >> number){
				numbers.push_back(number);
			}else{
				letter_password.push_back(temp);
			}
		}

		int reps = std::count(letter_password[1].begin(), letter_password[1].end(), letter_password[0][0]);
		if(reps >= numbers[0] && reps <= numbers[1]){
			valid_passwords++;
		}

	}
	cout <<"(PART ONE) Valid passwords are: " << valid_passwords << endl;
	valid_passwords = 0;
	
	//PART TWO
	for(auto it=passwords_policy.begin(); it != passwords_policy.end();it++){
		set<char> patterns;
		patterns.insert('-');
		patterns.insert(':');
		string token = (*it);
		match2space(&token,patterns);
		stringstream ss;
		string temp;
		vector<int> numbers;
		vector<string> letter_password;
		int number=0;

		ss << token;
		while(!ss.eof()){
			ss >> temp;
			if(stringstream(temp) >> number){
				numbers.push_back(number-1); // No 0 index! Those barbarians don't know anything...
			}else{
				letter_password.push_back(temp);
			}
		}
		
		if(letter_password[1][numbers[0]] != letter_password[1][numbers[1]]){
			if(letter_password[1][numbers[0]] == letter_password[0][0] || 
				letter_password[1][numbers[1]] == letter_password[0][0]){
				valid_passwords++;
			}
		}
	}
	
	cout <<"(PART TWO) Valid passwords are: " << valid_passwords << endl;

}