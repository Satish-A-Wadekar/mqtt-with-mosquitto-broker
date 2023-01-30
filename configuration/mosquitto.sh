'''to run the shell script, uncomment & run bellow command in terminal'''
# sh your_file_name_with_full_path.sh

###############################################################################################################

'''to start the mosquitto server on MAC''' 
    '''if you wants to mosquitto start server with "Default settings", uncomment & run below command'''
    #/usr/local/sbin/mosquitto -c /usr/local/etc/mosquitto/mosquitto.conf

    '''if you wants to mosquitto start server with your own "Custome settings", uncomment & run below command'''
    #/usr/local/sbin/mosquitto -c your_file_name_with_full_path

'''to stop mosquitto server, uncomment & run below line'''
#killall mosquitto

###############################################################################################################
'''
password file: to add authentication to access mosquitto server, you need to create password file where you need to add username & passwords with below mentione format
"username:password"
you can add as many credentials as you want but each credential should be on new line with username:password form
================================================================================================================
password utility: "mosquitto_passwd" is a utility which will convert your plain text passwords in encripted format
'''

'''to add authentication on mosquitto server, uncomment & run below command '''
#mosquitto_passwd -U your_file_name_with_full_path

###############################################################################################################

'''commands for windows OS'''
#net start mosquitto
#net stop mosquitto
