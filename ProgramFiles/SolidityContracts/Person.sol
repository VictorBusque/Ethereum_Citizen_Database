pragma solidity ^0.4.0;

import "./Manager.sol";

contract Person {

    address owner;
	address manager;
    uint money = 0;

    //not verified
    string name;
    string firstSurname;
    string secondSurname;
    string DNI;
    uint gender;
    uint age;
    string country;
    string province;
	string addr;
    string city;
    uint postalCode;

    //verified
    string name_verified;
    string firstSurname_verified;
    string secondSurname_verified;
    string DNI_verified;
    uint gender_verified;
    uint age_verified;
    string country_verified;
    string province_verified;
    string city_verified;
    string addr_verified;
    uint postalCode_verified;

	//Constructor
	//Name, FirstSurname, SecondSurname, DNI, Gender, Age, Country, Province, City, PostalCode, managerAddress
	function Person(string newName, string newFirstSurname, string newSecondSurname, string newDNI, uint newGender, uint newAge, string newCountry, string newProvince, string newCity, string newAddress, uint newPostalCode, address managerAddress) public {
        owner = msg.sender;
		manager = managerAddress;
		//Dirty
        name = newName;
        firstSurname = newFirstSurname;
		secondSurname = newSecondSurname;
        DNI = newDNI;
        gender = newGender;
        age = newAge;
		country = newCountry;
		province = newProvince;
        city = newCity;
        addr = newAddress;
        postalCode = newPostalCode;
		//Verified
		name_verified = "None";
    	firstSurname_verified = "None";
    	secondSurname_verified = "None";
		DNI_verified = "None";
		gender_verified = 0;
		age_verified = 0;
    	country_verified = "None";
    	province_verified = "None";
		city_verified = "None";
		addr_verified = "None";
		postalCode_verified = 0;
    }


	//set functions
    function setAttrs(string newName, string newFirstSurname, string newSecondSurname, string newDNI, uint newGender, uint newAge, string newCountry, string newProvince, string newCity, string newAddress, uint newPostalCode) public  {
        require(msg.sender == owner);
    	//if (!stringsEqual(newName, "-1")){
        	name = newName;
        //}
        //if (!stringsEqual(newFirstSurname, "-1")){
        	firstSurname = newFirstSurname;
        //}
        //if (!stringsEqual(newSecondSurname, "-1")){
			secondSurname = newSecondSurname;
        //}
        //if (!stringsEqual(newDNI, "-1")){
		    DNI = newDNI;
        //}
        //if (newGender != uint(-1)){
		    gender = newGender;
        //}
        //if (newAge != uint(-1)){
		    age = newAge;
        //}
        //if (!stringsEqual(newCountry, "-1")){
			country = newCountry;
        //}
        //if (!stringsEqual(newProvince, "-1")){
			province = newProvince;
        //}
        //if (!stringsEqual(newCity, "-1")){
		    city = newCity;
        //}
        //if (!stringsEqual(newAddress, "-1")){
		    addr = newAddress;
        //}
        //if (newPostalCode != uint(-1)){
		    postalCode = newPostalCode;
        //}
    }

	//confirm function 
	//0 es q no fas res
	//1 es q confirma
	//2 es q rebutga
	
	function confirm(uint field, bool allow) public {
        require(Manager(manager).originIsEntity());
		if(field==0) { 
			if (allow) name_verified = name;
		    name = "-1";
		}else{if(field==1) { 
			if (allow) firstSurname_verified = firstSurname;
		    firstSurname = "-1";
		}else{if(field==2) {
			if (allow) secondSurname_verified = secondSurname;
		    secondSurname = "-1";
		}else{if(field==3) { 
			if (allow) DNI_verified = DNI;
		    DNI = "-1";
		}else{if(field==4) { 
			if (allow) gender_verified = gender;
		    gender = uint(-1);
		}else{if(field==5) { 
			if (allow) age_verified = age;
		    age = uint(-1);
		}else{if(field==6) { 
			if (allow) country_verified = country;
		    country = "-1";
		}else{if(field==7) { 
			if (allow) province_verified = province;
		    province = "-1";
		}else{if(field==8) { 
			if (allow) city_verified = city;
		    city = "-1";
		}else{if(field==9) { 
		    if (allow) addr_verified = addr;
		    addr = "-1";
		}else{if(field==10) { 
		    if (allow) postalCode_verified = postalCode;
		    postalCode = uint(-1);
		}}}}}}}}}}}
				
		//notify Manager
		if (allow) Manager(manager).modifiedPerson(address(this));
    }
	
    /*function confirm(uint allowName, uint allowFirstSurname, uint allowSecondSurname, uint allowDNI, uint allowGender, uint allowAge, uint allowCountry, uint allowProvince, uint allowCity, uint allowAddress, uint allowPostalCode) public onlyEntity {
    	bool notify=false;
		if (allowName>0){
		    if (allowName==1) {
		        name_verified = name;
				notify=true;
		    }
		    name = "-1";
		}
		if (allowFirstSurname>0){
		    if (allowFirstSurname==1) {
		        firstSurname_verified = firstSurname;
				notify=true;
		    }
		    firstSurname = "-1";
		}
		if (allowSecondSurname>0){
		    if (allowSecondSurname==1) {
		        secondSurname_verified = secondSurname;
				notify=true;
		    }
		    secondSurname = "-1";
		}
		if (allowDNI>0){
		    if (allowDNI==1) {
		        DNI_verified = DNI;
				notify=true;
		    }
		    DNI = "-1";
		}
		if (allowGender>0){
		    if (allowGender==1) {
		        gender_verified = gender;
				notify=true;
		    }
		    gender = uint(-1);
		}
		if (allowAge>0){
		    if (allowAge==1) {
		        age_verified = age;
				notify=true;
		    }
		    age = uint(-1);
		}
		if (allowCountry>0){
		    if (allowCountry==1) {
		        country_verified = country;
				notify=true;
		    }
		    country = "-1";
		}
		if (allowProvince>0){
		    if (allowProvince==1) {
		        province_verified = province;
				notify=true;
		    }
		    province = "-1";
		}
		if (allowCity>0){
		    if (allowCity==1) {
		        city_verified = city;
				notify=true;
		    }
		    city = "-1";
		}
		if (allowAddress>0){
		    if (allowAddress==1) {
		        addr_verified = addr;
				notify=true;
		    }
		    addr = "-1";
		}
		if (allowPostalCode>0){
		    if (allowPostalCode==1) {
		        postalCode_verified = postalCode;
				notify=true;
		    }
		    postalCode = uint(-1);
		}
		
		//notify Manager
		if (notify) Manager(manager).modifiedPerson(address(this));
    }*/

	//Get functions		return: real, dirty
	function getStr(uint field) public constant  returns (string, string) {
        require(Manager(manager).originIsEntity());
		if(field==0) { return (name_verified, name);}
		else{if(field==1) { return (firstSurname_verified, firstSurname);}
		else{if(field==2) { return (secondSurname_verified, secondSurname);}
		else{if(field==3) { return (DNI_verified, DNI);}
		else{if(field==6) { return (country_verified, country);}
		else{if(field==7) { return (province_verified, province);}
		else{if(field==8) { return (city_verified, city);}
		else{if(field==9) { return (addr_verified, addr);}
		else{return ("None", "None");}
		}}}}}}}
    }
    function getInt(uint field) public constant  returns (uint, uint) {
        require(Manager(manager).originIsEntity());
		if(field==4) { return (gender_verified, gender);}
		else{if(field==5) { return (age_verified, age);}
		else{if(field==10) { return (postalCode_verified, postalCode);}
		else{return (uint(-1), uint(-1));}
		}}
    }
    
	//Get functions all
    //Returns the follow Verified variables: - Name - FirstSurname - SecondSurname - DNI - Gender - Age
	function getAll_verified1() public constant  returns (string, string, string, string, uint, uint) {
        require(msg.sender == owner);
        return (name_verified, firstSurname_verified, secondSurname_verified, DNI_verified, gender_verified, age_verified);
    }
    //Returns the follow Verified variables: - Country - Province - City - Address - PostalCode - Money
    function getAll_verified2() public constant  returns (string, string, string, string, uint, uint) {
        require(msg.sender == owner);
        return (country_verified, province_verified, city_verified, addr_verified, postalCode_verified, money);
    }
    //Returns the follow Dirty variables: - Name - FirstSurname - SecondSurname - DNI - Gender - Age
    function getAll1() public constant  returns (string, string, string, string, uint, uint) {
        require(msg.sender == owner);
        return (name, firstSurname, secondSurname, DNI, gender, age);
    }
    //Returns the follow Dirty variables: - Country - Province - City - Address - PostalCode
    function getAll2() public constant  returns (string, string, string, string, uint) {
        require(msg.sender == owner);
        return (country, province, city, addr, postalCode);
    }
    
	//other
    /*function isDirty() public constant returns (bool) {
        require (msg.sender == manager);
	    return (!stringsEqual(name, "-1") || !stringsEqual(firstSurname, "-1") || !stringsEqual(secondSurname, "-1") || !stringsEqual(DNI, "-1") || gender != uint(-1) || age != uint(-1) || !stringsEqual(country, "-1") || !stringsEqual(province, "-1") || !stringsEqual(city, "-1") || !stringsEqual(addr, "-1") || postalCode != uint(-1));
    }*/
    function whoDirty1() public constant returns (bool, bool, bool, bool, bool, bool) {
        require(Manager(manager).originIsEntity());
        return (!stringsEqual(name, "-1"), !stringsEqual(firstSurname, "-1"), !stringsEqual(secondSurname, "-1"), !stringsEqual(DNI, "-1"), gender != uint(-1), age != uint(-1));
    }
    function whoDirty2() public constant returns (bool, bool, bool, bool, bool) {
        require(Manager(manager).originIsEntity());
        return (!stringsEqual(country, "-1"), !stringsEqual(province, "-1"), !stringsEqual(city, "-1"), !stringsEqual(addr, "-1"), postalCode != uint(-1));
    }

	/*function getMoney() public constant onlyOwner returns (uint) {
        return money;
    }*/
    
    //Get for subvention
    function getForSubv() public constant returns (uint, uint, uint) {
        require(Manager(manager).addrIsSubvention(msg.sender));
        return (age_verified, gender_verified, postalCode_verified);
    }
    function addMoney(uint newMoney)  public {
        require(Manager(manager).addrIsSubvention(msg.sender));
        money += newMoney;
    }

	function joinNet() public  {
        require(msg.sender == owner);
		Manager(manager).addPerson(address(this));
	}
	/*function notifyManager() internal {
		Manager(manager).modifiedPerson(address(this));
	}*/
	
	/*function getManager() public constant returns (address) {
		return manager;
	}
	function getOwner() public constant returns (address) {
		return owner;
	}*/
	
    function stringsEqual(string _a, string _b) internal pure returns (bool) {
		bytes memory a = bytes(_a);
		bytes memory b = bytes(_b);
		if (a.length != b.length)
			return false;
		for (uint i = 0; i < a.length; ++i)
			if (a[i] != b[i])
				return false;
		return true;
	}
}
