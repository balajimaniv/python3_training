#!/bin/sh

# function definition
Hello() {
	echo "Hello World $1 $2"
	return 100
}


# function call
Hello Balaji Mani

# get return value
echo "returned value: $?"

