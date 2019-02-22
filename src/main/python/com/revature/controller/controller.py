#!/usr/bin/env python3

from service import service
import sys
import os
import logging
import os.path
import getpass

logging.basicConfig(filename = 'fileError.log', level = logging.DEBUG, format = '%(asctime)s : %(levelname)s : %(name)s : %(message)s', filemode = 'a')

logger = logging.getLogger('Logs')

save_path = 'users'

def menu():
	flag = True

	while(flag):
		print('------------------------------')
		print('Enter 1 to LOGIN')
		print('Enter 2 to CREATE AN ACCOUNT')
		print('Enter 3 if you FORGOT PASSWORD')
		print('Enter 4 to QUIT')
		selection = input('Enter your selection: ')	
		
		if(selection == '1'):
			logger.debug('Login function')
			information = login()
			if (information == False):
				print('Invalid username or password')
				logger.warning('Username or Password Failed')
			else:
				service.userMenu(information)
		elif(selection == '2'):
			logger.debug('Create User function')
			createUser()
			
		elif(selection == '3'):
			logger.debug('Forgot Password function')				
			forgotPassword()
		elif(selection == '4'):
			logger.info('Logged out')
			flag = False
			print('Goodbye')
		else:
			logger.warning('Selected invalid choice on first menu')
			print('Invalid choice')

def forgotPassword():
	username = input('Enter username: ')

	completeName = os.path.join(save_path, username + '.txt')

	try:
		f = open(completeName, 'r')
		f.close()
		newPassword = getpass.getpass('Enter new password: ')
		for line in open(completeName,'r').readlines():
			login_info = line.split()
			money = login_info[2]
		f = open(completeName, 'w')
				
		f.write(username + ' ' + newPassword + ' ' + str(money))
		f.close()
	except IOError:
		print('Username does not exist')
		logger.warning('Username does not exist')	


def createUser():
	username = input('Enter a new username: ')
	password = getpass.getpass('Enter a new password: ')
	
	completeName = os.path.join(save_path, username + '.txt')
	
	try:
		f = open(completeName, 'r')
		print('Username already taken')
		logger.warning('Username was taken')
		f.close()
	except IOError:
		file = open(completeName, 'w')
		file.write(username + ' ' + password + ' ' + '0.00')
		file.close()
		

def login():
	username = input('Enter username: ')
	password = getpass.getpass('Enter password: ')
	completeName = os.path.join(save_path, username + '.txt')

	try:
		f = open(completeName, 'r')
		for line in open(completeName, 'r').readlines():
			login_info = line.split()
			if username == login_info[0] and password == login_info[1]:
		
				return login_info
			else:
				logger.warning('Cannot login because wrong username or password')
				return False

	except IOError:
		return False
	
if __name__ == '__main__':
	main()
