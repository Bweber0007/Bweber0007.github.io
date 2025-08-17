#include "itemList.h"

// function to create list from input stream
void itemList::addFromSource(ifstream& stream) {
	// variables for storing info
	string item;
	int num = 0;
	// loop through all input from file
	while (!stream.eof()) {
		getline(stream, item);
		// checks if item is already in list
		if (items.count(item) == 1) {
			items[item]++; // increments frequency
		}
		else {
			items.emplace(item, 1); // add item to list with frequency of 1
		}
	}
	stream.close();
}

// function to print frequency of a single item
void itemList::printSingle(string item) {
	// checks if item is in list
	if (items.count(item) == 1) {
		cout << items.at(item) << endl;
	}
	else {
		cout << "Item not in list" << endl;
	}
}

// function to print all items with corresponding frequency
void itemList::printAll() {
	for (auto const& x : items) {
		cout << setw(15) << setfill(' ') << x.first << " " << x.second << endl;
	}
}

// function to print all items with corresponding frequency as stars to represent a histogram
void itemList::printHistogram() {
	for (auto const& x : items) {
		cout << setw(15) << setfill(' ') << x.first << " " << setw(x.second) << setfill('*') << "" << endl;
	}
}

// function to backup data in list to a given output file
void itemList::backupData(ofstream& stream, string filename) {
	stream.open(filename);
	if (!stream.is_open()) {
		cout << "output file could not open";
	}
	for (auto const& x : items) {
		stream <<  x.first << " " << x.second << endl;
	}
	stream.close();
}