from __future__ import with_statement
from fabric.api import *
import os, datetime

# defaults--same in every environment
env.hosts = ['yourname@yourhost.com']
app_name = "gamapi"

# dependencies is false by default since this could take a while, and doesn't need to be done every deploy
# example usage: `fab deploy_prod:True`
def deploy_prod(dependencies=False):
	# fill in these yourself:
	# site_root =
	# database_name =
	# database_user =
	# database_pass =
	settings_file_name = 'local_settings_prod.py' # create this file yourself
	deploy(site_root, app_name, database_name, database_user, database_pass, settings_file_name, dependencies)

def prepare_deploy():
	# test() # no tests in this project yet
	commit()
	push()

def test():
	local("python manage.py test")

def commit():
	local("git add --all")
	with settings(warn_only=True):
		# maybe there's nothing to commit? still want to push.
		local("git commit")

def push():
	local("git push origin master")

def mysqldump(database_name, database_user, database_pass):
	filename = "{0}_{1}.sql".format(database_name, datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S'))
	cmd = "mysqldump -u {0} {1} -p{2} > ~/tmp/{3}".format(database_user, database_name, database_pass, filename)
	run(cmd)

def deploy(site_root, app_name, database_name, database_user, database_pass, settings_file_name, dependencies):
	
	prepare_deploy()

	mysqldump(database_name, database_user, database_pass)

	with cd(site_root):
		run("git pull origin master")

	# manually copy target settings file, since it's not in git:
	this_dir = os.path.realpath(os.path.dirname(__file__))
	file_to_transfer = os.path.join(this_dir, app_name, settings_file_name)
	transfer_target = os.path.join(site_root, app_name, settings_file_name)
	with cd(site_root):
		put(file_to_transfer, app_name)

	# rename it from local_settings_prod.py to local_settings.py:
	copy_settings_file(site_root, app_name, settings_file_name)

	if dependencies:
		# if true, we need to install the dependencies before proceeding
		install_dependencies(site_root)

	with cd(site_root):
		run("python2.7 manage.py syncdb")
		run("python2.7 manage.py migrate")
		run("python2.7 manage.py collectstatic --noinput")

	wsgi_dir = os.path.join(site_root, app_name)
	with cd(wsgi_dir):
		run("touch wsgi.py")

def copy_settings_file(code_dir, app_name, newsettingsfilename):
	with cd(os.path.join(code_dir, app_name)):
		run("cp -f " + newsettingsfilename + " local_settings.py")

def install_dependencies(site_root):
	# this will work on WebFaction only
	# see http://docs.webfaction.com/software/python.html?highlight=pip#installing-packages-with-pip
	with cd(site_root):
		run('pip-2.7 install --install-option="--install-scripts=$PWD/bin" --install-option="--install-lib=$PWD/lib/python2.7" -r requirements.txt')
