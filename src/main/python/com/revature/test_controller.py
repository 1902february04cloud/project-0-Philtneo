#!/usr/bin/env python3

import os.path
import os
from controller import controller
from service import service

def main():
	testController()


def testController():

	completeName = os.path.join('testData', 'test.txt')
	file = open(completeName, 'w')
	file.write('test password 250.00')
	file.close()

	print('Starting money: $250.00')
	#print('Expected after 50 dollar withdraw')
	for line in open(completeName, 'r').readlines():
		login_info = line.split()
		

	login_info = service.withdraw(login_info) 

	os.remove(completeName)
	






if __name__ == '__main__':
	main()
