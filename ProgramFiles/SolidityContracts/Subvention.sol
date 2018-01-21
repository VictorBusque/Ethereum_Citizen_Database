pragma solidity ^0.4.18;

import "./Person.sol";

contract Subvention {

	struct Condition{
        uint8 variable;
        uint8 operator;
        uint value;
    }
   
	uint money;
    uint numConditions;
	address[] internal granted;
    mapping (uint => Condition) checker;

	function Subvention (uint amount, uint8[] variable, uint8[] operator, uint[] value) public {
		money=amount;
		addCondition(variable, operator, value);
	}

	//variable, operator, value
	function addCondition(uint8[] variable, uint8[] operator, uint[] value) internal {
		for (uint i = 0; i < variable.length; i++){
		    checker[numConditions++] = Condition(variable[i],operator[i],value[i]);
		}
	}

	function compareEq(uint8 op, uint realValue, uint compareValue) pure internal returns(bool){
        bool eq = (realValue == compareValue);
        if (op==0){//--------------------------------------------------------------------  ==	->	0
            return eq;
        } else { if (op==1){//-----------------------------------------------------------  !=	->	1	
            return !eq;
		} else {//-----------------------------------------------------------------------  Error
			return false;
		}}
    }

	function compareInt(uint op, uint realValue, uint compareValue) pure internal returns(bool){
        if (op==0){//--------------------------------------------------------------------  ==	->	0
            return realValue == compareValue;
        } else { if (op==1){//-----------------------------------------------------------  !=	->	1
            return realValue != compareValue;
        } else { if (op==2){//-----------------------------------------------------------  <=	->	2
            return realValue <= compareValue;
        } else { if (op==3){//-----------------------------------------------------------  >=	->	3
            return realValue >= compareValue;
        } else { if (op==4){//-----------------------------------------------------------  <	->	4
            return realValue < compareValue;
        } else { if (op==5){//-----------------------------------------------------------  >	->	5
            return realValue > compareValue;	
		} else {//-----------------------------------------------------------------------  Error
			return false;
        }}}}}}
    }

    function check(address p) public {
		//0x955236e1e3bbb6bc5df1dfc346b197efd9b785ab
		if(!isGranted(p)){
			Person pers = Person(p);
			uint age;
			uint gen;
			uint cod;
			(age,gen,cod) = pers.getForSubv();
			if(checkConditionFor(age,gen,cod)){
				pers.addMoney(money);
				granted.push(p);
			}
		}
    }

	function isGranted(address p) view internal returns(bool){
		for (uint i=0; i<granted.length; i++){
			if (granted[i] == p) return true;
		}
		return false;
	}

	function checkConditionFor(uint age, uint gen, uint cod) view internal returns (bool _b) {
		_b = true;
		for (uint i = 0; _b && (i<numConditions); i++){
			uint8 variable = checker[i].variable;
			uint8 op = checker[i].operator;
			uint value = checker[i].value;

			if (variable == 0) {//-------------------------------------------------------  Age			->	0
				_b = _b && compareInt(op,age,value);
			} else { if(variable == 1) {//-----------------------------------------------  Gender		->	1
				_b = _b && compareEq(op,gen,value);
			} else { if(variable == 2) {//-----------------------------------------------  PostalCode	->	2
				_b = _b && compareEq(op,cod,value);	
			} else {//-------------------------------------------------------------------  Error
				_b = false;			
			}}}
		}
	}

	//debug
	function getMoney() view public returns (uint){
		return money;
	}
	//debug
	function setMoney (uint a) public {
		money = a;
	}
	//debug
	function getGranted() view public returns (address[]){
		return granted;
	}
	//debug
	function addGranted(address p) public {
		granted.push(p);
	}
	//debug
	function getCond(uint idx) view public returns (uint8,uint8,uint) {
        Condition storage c = checker[idx];        
        return (c.variable,c.operator,c.value);
    }
}
