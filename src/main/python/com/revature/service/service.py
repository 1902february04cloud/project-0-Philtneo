#!/usr/bin/env python3

import sys
import os
import logging
import os.path
import getpass
import datetime

logging.basicConfig(filename = 'fileError.log', level = logging.DEBUG, format = '%(asctime)s : %(levelname)s : %(name)s : %(message)s', filemode = 'a')


logger = logging.getLogger('Logs')

save_path = 'users'
transaction_path = 'io'


'''
This is the service script.
'''

def userMenu(user):
	flag = True
	
	while(flag):
		print('------------------------------')
		print('Enter 1 to VIEW BALANCE')
		print('Enter 2 to WITHDRAW')
		print('Enter 3 to DEPOSIT')
		print('Enter 4 to VIEW TRANSACTION')
		print('Enter 5 to LOGOUT')
		selection = input('Enter your selection: ')
	
		if(selection == '1'):
			print('Balance: ${0:.2f}'.format(float(user[2])))
					
		elif(selection == '2'):
			withdraw(user)		
			logger.debug('Withdraw function called')
		elif(selection == '3'):
			deposit(user)
			logger.debug('Deposit function called')
		elif(selection == '4'):
			viewTransaction(user)
			logger.debug('View Transaction function called')
			
		elif(selection == '5'):
			print('Successfully logged out')
			flag = False

			completeName = os.path.join(save_path, user[0] + '.txt')
			file = open(completeName,'w')
			file.write(user[0] + ' ' + user[1] + ' ' + str(user[2]))
			file.close()
		else:
			logger.warning('Invalid choice on user menu')
			print('Invalid choice')


def withdraw(user):
	
	withdraw = input('How much to withdraw: $')
	if(float(withdraw) > float(user[2])):
		print('Not enough money to withdraw')
		logger.warning('Not enough money to withdraw')
	else:
		ioPath = os.path.join(transaction_path, user[0] + '.txt')
		user[2] = float(user[2]) - float(withdraw)
		f = open(ioPath, 'a')
		today = datetime.datetime.now()
		f.write(str(today) + ' - Withdrew: ${0:.2f}'.format(float(withdraw)) + ', Total Amount: ${0:.2f}'.format(float(user[2])) + '\n')
		f.close()
		print('Withdraw: ${0:.2f}'.format(float(withdraw)))
		print('Current Balance: ${0:.2f}'.format(float(user[2])))
		return user

def deposit(user):
	deposit = input('How much to deposit: $')
	if(float(deposit) < 0):
		print('Must deposit more than 0')
		logger.warning('Must deposit more than 0')
	else:
		ioPath = os.path.join(transaction_path, user[0] + '.txt')
		user[2] = float(user[2]) + float(deposit)
		f = open(ioPath, 'a')
		today = datetime.datetime.now()
		f.write(str(today) + ' - Deposit: ${0:.2f}'.format(float(deposit)) + ', Total Amount: ${0:.2f}'.format(float(user[2])) + '\n')
		f.close()
		print('Deposit: ${0:.2f}'.format(float(deposit)))
		print('Current Balance: ${0:.2f}'.format(float(user[2])))
		return user


def viewTransaction(user):
	ioPath = os.path.join(transaction_path, user[0] +'.txt')
	fI = open(ioPath, 'r')
	print(fI.read())


if __name__ == '__main__':
	main()
