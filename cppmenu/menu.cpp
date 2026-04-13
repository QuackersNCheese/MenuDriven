//Name: Joseph Ferguson
//Program Description

#include<iostream>
#include<fstream>
#include<limits>

using namespace std;

//Function for displaying menu
void displayMenu();

//Overloaded function that verifies that user input is the right data type. It updates a value by reference
void getUserInput(int &menuOption);
void getUserInput(double &num);

//Function that recieves "num1" and "num2" by reference but doesnt update them, and then updates "result" with their sum 
void add(double &num1, double &num2, double &result);

//Function that recieves "num1" and "num2" by reference and doesn't update them. It returns their product
double multiply(double &num1, double &num2);



int main() {
    //Variables
    int menuOption;
    bool wrongInt = false;
    double num1, num2, result;
    ofstream outputFile;

    outputFile.open("data.txt", ios_base::app);

    if (!outputFile) {
        cout << "Couldn't open file successfully.";
        return 1;
    }

    cout << "Welcome to the Function Practice Program" << endl;

    //Main program loop
    do {
        //Only outputs the menu if their last input was valid
        if (!wrongInt) {
            displayMenu();
        }
        getUserInput(menuOption);

        switch (menuOption) {
        case 1:
            wrongInt = false;
            cout << endl;
            
            cout << "Enter first number: ";
            getUserInput(num1);
            cout << "Enter second number: ";
            getUserInput(num2);

            add(num1, num2, result);

            cout << "The sum is: " << result << endl << endl;

            outputFile << "The sum is: " << result << endl;

            break;
        case 2:
            wrongInt = false;
            cout << endl << endl;
            
            cout << "Enter first number: ";
            getUserInput(num1);
            cout << "Enter second number: ";
            getUserInput(num2);

            result = multiply(num1, num2);

            cout << "The product is: " << result << endl << endl;

            outputFile << "The product is: " << result << endl;

            break;
        case 3:
            cout << endl << endl;
            cout << "Exiting program. Goodbye!";
            break;
        default:
            cout << "Please choose a valid option: ";
            wrongInt = true;
        }
    } while (menuOption != 3);

    return 0;
}



void displayMenu() {
    cout << "----------------------------------------" << endl;
	cout << "1. Add two numbers" << endl;
	cout << "2. Multiply two numbers" << endl;
	cout << "3. Exit" << endl;
	cout << "Enter your choice: ";
}

//Loops through asking the user for a valid number for overloaded function until cin doesn't fail, then stores result in reference variable
void getUserInput(int &menuOption) {
    while (true) {
        cin >> menuOption;

        if (cin.fail()) {
            cout << "Invalid input. Please enter a valid number: ";

            cin.clear();

            cin.ignore(numeric_limits<streamsize>::max(), '\n');
        }
        else {
            break;
        }
    }
}
void getUserInput(double &num) {
    while (true) {
        cin >> num;

        if (cin.fail()) {
            cout << "Invalid input. Please enter a valid number: ";

            cin.clear();

            cin.ignore(numeric_limits<streamsize>::max(), '\n');
        }
        else {
            break;
        }
    }
}


void add(double &num1, double &num2, double &result) {
    result = num1 + num2;
}

double multiply(double &num1, double &num2) {
    return num1 * num2;
}