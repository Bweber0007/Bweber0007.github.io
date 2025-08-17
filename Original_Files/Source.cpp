/*
Developer: Brady Weber
Date: 4/21/2024
Project: Project three. Input a list of grocery items and track the 
	frequency at which they appear. Be able to print the frequency of a
	single user identified item, the entire list with corresponding
	frequencies, and the list as a histogram.
*/
#include "itemList.h"

// function to open file and check if opened correctly
void openfile(ifstream& stream, string filename) {
	stream.open(filename);
	if (!stream.is_open()) {
		cout << "input file could not open";
	}
}

// function to display menu and execute related function
void displayMenu(itemList& items) {
	string userIn;
	string item;
	while (userIn != "4") {
		cout << "Press 1 to print the frequency of a single item." << endl;
		cout << "Press 2 to print the frequency of all items." << endl;
		cout << "Press 3 to print the frequency of all items as a histogram." << endl;
		cout << "Press 4 to exit." << endl;
		cin >> userIn;
		if (userIn == "1") {
			cout << "Please enter an item to search" << endl;
			cin >> item;
			items.printSingle(item);
		}
		else if (userIn == "2") {
			items.printAll();
		}
		else if (userIn == "3") {
			items.printHistogram();
		}
		else if (userIn == "4") {
			return;
		}
		else {
			cout << "Please enter a valid number" << endl;
		}
	}
}

int main() {
	// declare filestreams and filenames and instantiate list class
	ifstream inFS;
	ofstream outFS;
	string outfilename = "frequency.dat";
	string infilename = "CS210_Project_Three_Input_File.txt";
	itemList items;

	openfile(inFS, infilename);
	items.addFromSource(inFS);
	items.backupData(outFS, outfilename);
	displayMenu(items);

	return 0;
}