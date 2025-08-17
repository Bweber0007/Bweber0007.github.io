#pragma once
#include <map>
#include <string>
#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

class itemList
{
public:
	void addFromSource(ifstream& stream);
	void printSingle(string item);
	void printAll();
	void printHistogram();
	void backupData(ofstream& stream, string filename);
private:
	map<string, int> items;
};

