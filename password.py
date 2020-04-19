def password(length):
    import random
    class password(): # makes class to hold important varibles.
        char_lst = ['1','2','3','4','5','6','7','8','9','0','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M','!','*','~','_','-']
        pass_lst = []
    def make_pass(): # makes the password into list
        loop = 0
        while loop != length:
            password.pass_lst.append(random.choice(password.char_lst))
            loop = loop + 1
        x = ''
        print(x.join(password.pass_lst))
    make_pass()
