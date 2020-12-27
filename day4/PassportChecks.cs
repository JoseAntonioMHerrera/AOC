using System;
using System.Collections.Generic;
using System.Collections;
using System.Text.RegularExpressions;
namespace day4
{
    class MultiVersePassport {
        private static string[] essentialPassportFields = {"byr","iyr","eyr","hgt","hcl","ecl","pid"};
        private static Dictionary<string,Regex> fieldsPolicy = new Dictionary<string, Regex>();
        public static string nonEssentialPassportField = "cid"; 
        private Dictionary<string,string> passport {get;set;}

        static MultiVersePassport(){
            fieldsPolicy.Add("byr",new Regex(@"^19[2-9][0-9]$|^200[0-2]$"));
            fieldsPolicy.Add("iyr",new Regex(@"^201[0-9]$|^2020$"));
            fieldsPolicy.Add("eyr",new Regex(@"^202[0-9]$|^2030$"));
            fieldsPolicy.Add("hgt",new Regex(@"^1[5-8][0-9]cm$|^19[0-3]cm$|^59in$|^6[0-9]in$|^7[0-6]in$"));
            fieldsPolicy.Add("hcl",new Regex(@"^#[a-f0-9]{6}$"));
            fieldsPolicy.Add("ecl",new Regex(@"^amb$|^blu$|^brn$|^gry$|^grn$|^hzl$|^oth$"));
            fieldsPolicy.Add("pid",new Regex(@"^[0-9]{9}$"));
        }

        public MultiVersePassport(Dictionary<string,string> passport){
            this.passport = new Dictionary<string,string>(passport);
        }
        public Boolean checkPassportIntegrity()
        {   bool passportIntegrity = true;

            if(this.passport.Count == essentialPassportFields.Length){
                if(!fieldsPolicy["byr"].IsMatch(this.passport["byr"])){
                    passportIntegrity = false;
                }else if(!fieldsPolicy["iyr"].IsMatch(this.passport["iyr"])){
                    passportIntegrity = false;
                }else if(!fieldsPolicy["eyr"].IsMatch(this.passport["eyr"])){
                    passportIntegrity = false;
                }else if(!fieldsPolicy["hgt"].IsMatch(this.passport["hgt"])){
                    passportIntegrity = false;
                }else if(!fieldsPolicy["hcl"].IsMatch(this.passport["hcl"])){
                    passportIntegrity = false;
                }else if(!fieldsPolicy["ecl"].IsMatch(this.passport["ecl"])){
                    passportIntegrity = false;
                }else if(!fieldsPolicy["pid"].IsMatch(this.passport["pid"])){
                    passportIntegrity = false;
                }
            }else{
                passportIntegrity = false;
            }
            
            return passportIntegrity;
        }

        public override string ToString()
        {
            string passport = "";
            foreach(KeyValuePair<string,string> k_v in this.passport){
                passport += k_v.Key + ": " + k_v.Value + ",";
            }
            return passport;
        }
    }

    class Program
    {
        static ArrayList readPassportsFromFile(String filename){
            ArrayList passports = new ArrayList();
            Dictionary<string,string> passport = new Dictionary<string,string>();
            string[] lines = System.IO.File.ReadAllLines(filename);
            foreach(var line in lines){
                if(line.Length == 0){
                    passports.Add(new MultiVersePassport(passport));
                    passport.Clear();
                }else{
                    string[] fields = line.Split(' ');
                    foreach(var field in fields){
                        string[] field_value = field.Split(':');
                        if(field_value.Length == 2 && !field_value[0].Equals(MultiVersePassport.nonEssentialPassportField)){
                            passport.Add(field_value[0],field_value[1]);
                        }
                    }
                }
            }
            if(passport.Count > 0){
                passports.Add(new MultiVersePassport(passport));
                passport.Clear();
            }
            return passports;
        }
        static void Main(string[] args)
        {
            String filename = @"your_own_filename";
            ArrayList passports = readPassportsFromFile(filename);
            int validPassportCounter = 0;
            foreach(MultiVersePassport passport in passports){
                if(passport.checkPassportIntegrity()){
                    validPassportCounter++;
                }
            }
            Console.WriteLine("Number of valid passports: {0}", validPassportCounter);
        }
    }
}
