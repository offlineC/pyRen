import os
import shutil

print('File rename system!')
print('Files renamed only in path specified.')
# set mode
print('Letter casing or spacing mode?')
renMode = input('Enter "letter" or "spacing": ')
print('Set to ' + renMode + ' mode!')

# set location
print("File location?")
location = input('File is in path: ')
print('Lcoation set to: ' + location)
os.chdir(location)

def setMode(mode):
	if mode == 'letter':
		casingMode()
	elif mode == 'spacing':
		spacingMode()
	else :
		print('please enter one of the modes')

def casingMode():
	print('Set files to uppercase or lowercase?')
	letterCase = input('Select "upper" or "lower": ')
	print('Setting files to ' + letterCase);

	if letterCase == 'upper':
		for u in os.listdir():
			os.rename(u, u.upper())
	elif letterCase == 'lower':
		for l in os.listdir():
			os.rename(l, l.lower())


def spacingMode():
	print('To replace spaces with character entered');
	spaceType = input('Enter character to replace space: ');
	print('Replace any existing spacers? e.g. "-" or "_" ');
	existingRep = input('Enter "no" if nothing to replace: ')

	if (existingRep == 'no'):
		for s in os.listdir():
			os.rename(s,s.replace(' ', spaceType))
	else:
		for es in os.listdir():
			spacers = ['-', '_' + ' ']
			for schar in spacers:
				if (schar in es):
					print(es)
					os.rename(es, es.replace(schar, spaceType))


setMode(renMode)