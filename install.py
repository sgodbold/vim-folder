import os
import subprocess

def bash(command):
	# allows for a bash command to be passed in as a string
	# and its stdout is returned
	output = subprocess.Popen([command], shell=True,
	stdout=subprocess.PIPE).communicate()[0]
	return output

def main():
	# Lets start this off by registering all the submodules
	bash("git submodule init")
	bash("git submodule update")
	bash("git submodule foreach git submodule init")
	bash("git submodule foreach git submodule update")

	# Now to place a simlink in for pathogen
	os.symlink("vim-pathogen/autoload", "autoload")
	os.symlink("vim-hybrid/colors", "colors")
	os.symlink('bundles/snipmate/snippets', 'snippets')

	# Get home dir and make me some simlinks
        home = '~/'
	os.remove(home + '.vimrc')
	bash('rm -rf ' + home + '.vim')
	os.symlink('./', home + '.vim')
	os.symlink('./vimrc', home + '.vimrc')

	return 0

if __name__ == '__main__':
	main()
