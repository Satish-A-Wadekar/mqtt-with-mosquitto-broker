'''to run the shell script, uncomment & run bellow command in terminal'''
# sh your_file_name_with_full_path.sh

###############################################################################################################

'''to start the mosquitto server on MAC''' 
    '''if you wants to start mosquitto server with "Default settings", uncomment & run below command'''
    #/usr/local/sbin/mosquitto -c /usr/local/etc/mosquitto/mosquitto.conf

    '''if you wants to start mosquitto server with your own "Custome settings", uncomment & run below command'''
    #/usr/local/sbin/mosquitto -c your_file_name_with_full_path

'''to stop mosquitto server, uncomment & run below line'''
#killall mosquitto

###############################################################################################################
'''
password file: to add authentication access to your mosquitto server, you need to create password file where you can add username & passwords 
with below mentione format, you can add as many credentials as you want but each credential should be on new line with username:password form

"username1:password1"
"username2:password2"
"username3:password3"

'''
###############################################################################################################

'''to add authentication on mosquitto server, uncomment & run below mentioned utility command 
==================================================================================================================
"mosquitto_passwd" is a password utility which converts your plain text passwords into encripted format
'''
#mosquitto_passwd -U your_file_name_with_full_path

###############################################################################################################

'''commands for windows OS'''
#net start mosquitto
#net stop mosquitto
