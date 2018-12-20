
function CheckFolder(){
	FOLDER=$1
	if [ -x $FOLDER ]
	then
		if [ "$2" == "y" ]
		then
			echo "$FOLDER EXIST"
		fi
	else
  		echo "$FOLDER NOT EXIST"
	fi
}
function CheckFile(){
	FILE=$1
	if [ -f $FILE ]
	then
		if [ "$2" == "y" ]
		then
			echo "$FILE EXSIT"
		fi	
	else
	  echo "$FILE NOT EXIST"
	fi
}

echo "Check FOLDER \c"
CheckFolder blogger
CheckFolder blogger/venv
CheckFolder blogger/app
CheckFolder blogger/app/templates
echo 'finish'

echo 'Check FILE \c'
CheckFile blogger/test.py
CheckFile blogger/venv.env
CheckFile blogger/blogger.py
CheckFile blogger/Gen_requirements.sh
CheckFile blogger/start_mail_server.sh
CheckFile blogger/install_requirements.sh
echo 'finish'


echo 'CheckFile in app FILE \c'
CheckFile blogger/app/__init__.py
CheckFile blogger/app/routes.py
CheckFile blogger/app/models.py
CheckFile blogger/app/errors.py
CheckFile blogger/app/config.py
echo 'finish'


echo 'CheckFile in app/templates FILE \c'
CheckFile blogger/app/templates/404.html
CheckFile blogger/app/templates/500.html
CheckFile blogger/app/templates/base.html
CheckFile blogger/app/templates/home.html
CheckFile blogger/app/templates/login.html
CheckFile blogger/app/templates/registor.html
CheckFile blogger/app/templates/user.html
CheckFile blogger/app/templates/edit_profile.html
echo 'finish'
git log
