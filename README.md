# curldict
This script can be used for sniper attacks like Burp Suite's intruder. Difference is you can use this by any command spesifically with Curl.


You can specify location of your file using "{}"
You must write your command using quotes (')


Example: 
                $python3 dictcurl 'curl --data "email=test@test.com" --data "password={/usr/share/wordlists/rockyou.txt}" http://www.example.com  '
                
