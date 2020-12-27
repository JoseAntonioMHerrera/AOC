









#include <iostream>
#include <fstream>
#include <string>
#include <unordered_set>
#include <vector>
#include <set>
#include <sstream>
#include <algorithm>
using namespace std;

void match2space(string* text, char pattern) {
    for(auto it = (text)->begin(); it != (text)->end(); ++it) {
    	if(*it == pattern){
    		*it = ' ';
    	}
    }
}

int main(){
	fstream instream;
	std::unordered_set<std::string> passwords_policy;
	int counter= 0,counter2=0;
	instream.open("input.txt",ios::in);
	int valid_passwords=0;
	if(instream.is_open()){
		string line;
		while(getline(instream,line)){
			passwords_policy.insert(line);
			counter++;
		}
	}
	// PART ONE // 
	for(auto it=passwords_policy.begin(); it != passwords_policy.end();it++){
		int token_position = (*it).find(":");
		string char_rule = (*it).substr(token_position-1,1);
		string token = (*it).substr(0,token_position);
		string password = (*it).substr(token_position,string::npos);
		stringstream ss;
		string temp;
		vector<int> numbers;
		
		int number=0;
		match2space(&token,'-');
		ss << token;
		while(!ss.eof() && numbers.size()<2){
			ss >> temp;
			if(stringstream(temp) >> number){
				numbers.push_back(number);
			}
		}
		int number_of_reps = count(password.begin(), password.end(), char_rule[0]);
		if( number_of_reps >= numbers[0] && number_of_reps <= numbers[1]){
			valid_passwords++;
		}
	}

	//PART TWO
/*
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

		cout << letter_password[1][numbers[0]] << endl;
		cout << letter_password[1][numbers[1]] << endl;
		exit(0);
		/*
		if(letter_password[1][numbers[0]] != letter_password[1][numbers[1]]){
			if(letter_password[1][numbers[0]] == letter_password[0] || 
				letter_password[1][numbers[1]] == letter_password[0]){
				valid_passwords++;
			}
		}
	}*/
	cout <<"Valid passwords are: " << valid_passwords << endl;

}
