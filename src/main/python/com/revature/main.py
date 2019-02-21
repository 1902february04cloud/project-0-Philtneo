#!/usr/bin/env python3
'''
This is your main script, this should call several other scripts within your packages.
'''
from controller import controller

def main():
	print('Welcome to the bank application')
	controller.menu()

	
	
if __name__ == '__main__':
	main()
