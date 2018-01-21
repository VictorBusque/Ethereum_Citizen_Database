#!/usr/bin/python

#importing wx files
import wx
import sys
import os
import json
import time
import io
try:
    to_unicode = unicode
except NameError:
    to_unicode = str

sys.path.insert(0, 'UserInterface')

import models
import ethereumUtils
import injectContract
import generateUser
import executeFunction

class VisualizedFrame(models.frameVisualizedData):

    def __init__(self,parent,values, username):
        models.frameVisualizedData.__init__(self,parent)
        self.username = username
        self.values = values

        #print ('values != None')
        self.textName.SetValue(values["Name"])
        self.textFirstSurname.SetValue(values["FirstSurname"])
        self.textSecondSurname.SetValue(values["SecondSurname"])
        self.textDNI.SetValue(values["DNI"])
        self.choiceGender.SetSelection(int(values["Gender"]))
        self.textAge.SetValue(values["Age"])

        self.textCountry.SetValue(values["Country"])
        self.textProvince.SetValue(values["Province"])
        self.textCity.SetValue(values["City"])
        self.textAddress.SetValue(values["Address"])
        self.textPostalCode.SetValue(values["PostalCode"])
        self.textMoney.SetValue(values["Money"])

        #val = executeFunction.computeOutput(username, 0, "joinNet", [])
        ##print ("computeOutput(username, \"joinNet\"): " + str(val))


    def onModify(self,event):
        args = {}
        try:
            args = models.frameVisualizedData.onModify(self,event)

        except Exception,e:
            #print 'error' + str(e)
            Dialogs.ErrorMessage("ERROR",str(e))
            return

        frame = ModifyFrame(None,self.username,self.values)
        frame.Show(True)
        self.Destroy()


class ModifyFrame(models.frameModify):

    def __init__(self,parent,username,values = None):
        models.frameModify.__init__(self,parent,values)
        self.values = values
        self.username = username


    def onModify(self,event):
        try:
            args = models.frameModify.onModify(self,event)

            def setValue(value):
                return "\'" + str(value) + "\'"

            def setValue2(value):
                return str(value)

            mDades = [ \
                setValue(args.get("Name", "-1")), \
                setValue(args.get("FirstSurname", "-1")), \
                setValue(args.get("SecondSurname", "-1")), \
                setValue(args.get("DNI", "-1")), \
                setValue2(args.get("Gender", "-1")), \
                setValue2(args.get("Age", "-1")), \
                setValue(args.get("Country", "-1")), \
                setValue(args.get("Province", "-1")), \
                setValue(args.get("City", "-1")), \
                setValue(args.get("Address", "-1")), \
                setValue2(args.get("PostalCode", "-1")) ]

            #print ("mDades: " + str(mDades))
            mDades2 = [ \
                setValue(args.get("Name", "-1")), \
                setValue(args.get("FirstSurname", "-1")), \
                setValue(args.get("SecondSurname", "-1")), \
                setValue(args.get("DNI", "-1")), \
                setValue2(args.get("Gender", "-1")), \
                setValue2(args.get("Age", "-1")), \
                setValue(args.get("Country", "-1")), \
                setValue(args.get("Province", "-1")), \
                setValue(args.get("City", "-1")), \
                setValue(args.get("Address", "-1")), \
                setValue2(args.get("PostalCode", "-1")) ]

            while ('-1' in mDades2):
                mDades2.remove('-1')
            while ("'-1'" in mDades2):
                mDades2.remove("'-1'")

            #print ("mDades2: " + str(mDades2))

            if (mDades2 == []):
                Dialogs.ErrorMessage("Error","No changes have been made")

            else:
                #print ("mDades: " + str(mDades))
                res = executeFunction.computeOutput(self.username, 0, "setAttrs", mDades, gas="'4712388'")
                #print ("resName: " + str(res))
                Dialogs.CorrectMessage("Success","Changes have been submit")

                frame = VisualizedFrame(None,self.values,self.username)
                frame.Show(True)
                self.Destroy()
            
        except Exception, e:
            Dialogs.ErrorMessage("ERROR",str(e))
            #print 'error'

    def onBack(self,event):
        frame = VisualizedFrame(None,self.values,self.username)
        frame.Show(True)

        self.Destroy()


class RegisterFrame(models.frameRegister):

    def __init__(self,parent,username):
        models.frameRegister.__init__(self,parent)
        self.username = username

        address, password = ethereumUtils.get_user_address_pass(username)
        ethereumUtils.unlock_account(address, password)


    def onRegister(self,event):
        try:
            args = models.frameRegister.onRegister(self,event)

            #if args != None:
            if not None in args.values() and not "" in args.values():

                f = open("Data/PendingRegisterUserDB.db","r")
                data = json.load(f)
                data[self.username] = args
                f.close()
                
                with io.open('Data/PendingRegisterUserDB.db', 'w', encoding='utf8') as outfile:
                    strJson = json.dumps(data, indent=4, sort_keys=True, separators=(',', ': '), ensure_ascii=False)
                    outfile.write(to_unicode(strJson))

                frame = ListUsersFrame(None)
                frame.Show(True)

                self.Destroy()

            else:
                #print ("falten camps per omplir")
                Dialogs.InfoMessage("ERROR","Falten camps per omplir!")
            
        except Exception, e:
            Dialogs.ErrorMessage("ERROR",str(e))
            #print 'error'

    def onBack(self,event):
        frame = CreateUsernameFrame(None)
        frame.Show(True)

        self.Destroy()



class ListUsersFrame(models.usersListFrame):
    def __init__(self, parent):
        models.usersListFrame.__init__(self, parent)
        usersBox = UsersBox(self)
        
        frameBox = wx.BoxSizer( wx.VERTICAL )
        frameBox.Add( usersBox, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        self.SetSizer( frameBox )
        self.Layout()
        
        self.Centre( wx.BOTH )



class PasswordLogInFrame ( models.AskPassword ):
    def __init__( self, parent, username, password, address ):
        models.AskPassword.__init__(self, parent, password, address)
        self.username = username
    
    # Virtual event handlers, overide them in your derived class
    def onLogIn( self, event ):
        if (self.password == self.textPassword.GetValue()):
            ethereumUtils.unlock_account(self.address, self.password)


            args1 = executeFunction.computeOutput(self.username, 0, "getAll_verified1", [])[0].split(",")
            #print ("computeOutput(username, \"getAll_verified1\"): " + str(args1))

            args2 = executeFunction.computeOutput(self.username, 0, "getAll_verified2", [])[0].split(",")
            #print ("computeOutput(username, \"getAll_verified2\"): " + str(args2))

            values = {}

            values["Name"] = args1[0]
            values["FirstSurname"] = args1[1]
            values["SecondSurname"] = args1[2]
            values["DNI"] = args1[3]
            values["Gender"] = args1[4]
            values["Age"] = args1[5]

            values["Country"] = args2[0]
            values["Province"] = args2[1]
            values["City"] = args2[2]
            values["Address"] = args2[3]
            values["PostalCode"] = args2[4]
            values["Money"] = args2[5]

            #print ("values: " + str(values))

            frame = VisualizedFrame(None, values, self.username)
            frame.Show(True)
            
            self.frame.Destroy()
            self.Destroy()
        else:
            Dialogs.ErrorMessage("Wrong Password","The password is not correct, try again")
            #print(self.password)
            #print(str(self.textPassword.GetValue()))

    def onCancel( self, event ):
        self.Destroy()



class UsersBox(models.usersListPanel):
    def __init__(self, parent):
        models.usersListPanel.__init__(self, parent, False)
        self.frame = parent

        try:
            usuaris1 = self.getUsers()
            usuaris2 = self.getPendingRegisterUsers()

            for user in usuaris2.keys():
                value = usuaris1.pop(user, None)
                #print ("user: " + str(user) + " -> " + str(value))

            self.addUsers(usuaris1)
            self.addPendingRegisterUsers(usuaris2)
        except Exception, e:
            Dialogs.ErrorMessage("Error",str(e))
            self.frame.Destroy()

    def addUsers(self, usuaris):
        for usuari in usuaris:
            (p, a) = usuaris[usuari]
            self.addUser(usuari,p,a)
            self.recalculateSize()

    def addPendingRegisterUsers(self, usuaris):
        if usuaris != None:
            for usuari, args in usuaris.items():
                self.addPendingRegisterUser(usuari, args)
                self.recalculateSize()
    
    def onRegister(self,event):
        frame = CreateUsernameFrame(None)
        frame.Show(True)

        self.frame.Destroy()

    def addUser(self,username, password, address):
        userBox = wx.BoxSizer(wx.HORIZONTAL)
        nameLabel = wx.StaticText( self.scrollWindows, wx.ID_ANY, username, wx.DefaultPosition, wx.DefaultSize, 0 )
        nameLabel.Wrap( -1 )
        logInButton = wx.Button(self.scrollWindows, wx.ID_ANY, "LogIn", wx.DefaultPosition, wx.DefaultSize, 0 )

        def checkUser(event):
            #print ("password: " + str(password))
            frame = PasswordLogInFrame(self.frame, username, password, address)
            frame.Show(True)

        logInButton.Bind(wx.EVT_BUTTON, checkUser)
        userBox.Add(nameLabel,1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
        userBox.Add(logInButton, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)

        if self.usersListBox.GetChildren():
            linia = wx.StaticLine( self.scrollWindows, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
            linia.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )
            self.usersListBox.Add(linia, 0, wx.EXPAND|wx.ALIGN_CENTRE_VERTICAL|wx.RIGHT|wx.LEFT, 10)

        self.usersListBox.Add(userBox, 0, wx.EXPAND|wx.ALIGN_CENTRE_VERTICAL|wx.ALL, 5)

    def addPendingRegisterUser(self,username, args):

        registerPanel = wx.Panel( self.scrollWindows, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )

        buttonText = ""
        if (args == None):
            registerPanel.SetBackgroundColour( wx.Colour( 208, 208, 208 ) )
            buttonText = "Register"
        else:
            registerPanel.SetBackgroundColour( wx.Colour( 228, 174, 57 ) )
            buttonText = "LogIn"

        
        userBox = wx.BoxSizer( wx.HORIZONTAL )
        
        nameLabel = wx.StaticText( registerPanel, wx.ID_ANY, username, wx.DefaultPosition, wx.DefaultSize, 0 )
        nameLabel.Wrap( -1 )
        userBox.Add(nameLabel,1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)


        def registerPendingUser(event):
            #print ("registerPendingUser()")
            if (args == None):
                frame = RegisterFrame(None, username)
                frame.Show(True)

                self.frame.Destroy()
            else:
                try:
                    time.sleep(5)
                    address,password = ethereumUtils.get_user_address_pass(username)

                    #print ("username: " + str(username))
                    #print ("password: " + str(password))
                    #print ("address: " + str(address))
                    ethereumUtils.unlock_account(address,password)

                    time.sleep(5)

                    ret = ethereumUtils.get_contract_info(username)
                    #print ("ret: " + str(ret))

                    if (ret == None):
                        #print ("th == None -> injectContract.run()")

                        def setString(s):
                            return ("\'" + str(s) + "\'")

                        argsAux = [setString(args["Name"]) , \
                        setString(args["FirstSurname"]) , \
                        setString(args["SecondSurname"]) , \
                        setString(args["DNI"]) , \
                        str(args["Gender"]) , \
                        str(args["Age"]), \
                        setString(args["Country"]) , \
                        setString(args["Province"]) , \
                        setString(args["City"]) , \
                        setString(args["Address"]) , \
                        str(args["PostalCode"]), \
                        setString(ethereumUtils.getManagerAddress())]

                        #print (argsAux)

                        res = injectContract.run("./SolidityContracts/Person.sol", username, argsAux, gas="'4712388'")
                        #print ("res: " + str(res))


                        if (res == 0):
                            address, _ = ethereumUtils.get_user_address_pass(username)
                            Dialogs.InfoMessage("Information","Please, go to any administration and provide the following address:\n"+str(address))
                        elif (res == 1):
                            Dialogs.InfoMessage("Information","Contract is not mine yet, wait 10 seconds and try it again")

                    else:
                        _,th,_ = ret
                        #print ("th != None -> ethereumUtils.retrieve_contract_address()")
                        try:
                            th = str(th)
                            #print ("th: " + str(th))
                            res = ethereumUtils.retrieve_contract_address(th)
                            if res != None:
                                f = open("Data/PendingRegisterUserDB.db","r")
                                data = json.load(f)
                                data.pop(username, None)
                                f.close()
                                
                                with io.open('Data/PendingRegisterUserDB.db', 'w', encoding='utf8') as outfile:
                                    strJson = json.dumps(data, indent=4, sort_keys=True, separators=(',', ': '), ensure_ascii=False)
                                    outfile.write(to_unicode(strJson))

                                val = executeFunction.computeOutput(username, 0, "joinNet", [])
                                #print ("computeOutput(username, \"joinNet\"): " + str(val))

                                frame = ListUsersFrame(None)
                                frame.Show(True)

                                self.frame.Destroy()

                        except Exception, e:
                            #print ("error1: " + str(e))
                            Dialogs.ErrorMessage("Error",str(e))



                except Exception, e:
                    #print ("error2: " + str(e))
                    Dialogs.ErrorMessage("Error",str(e))

        registerButton = wx.Button( registerPanel, wx.ID_ANY, buttonText, wx.DefaultPosition, wx.DefaultSize, 0 )
        registerButton.Bind(wx.EVT_BUTTON, registerPendingUser)
        userBox.Add(registerButton, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
        
        
        registerPanel.SetSizer( userBox )
        registerPanel.Layout()
        userBox.Fit( registerPanel )

        if self.usersListBox.GetChildren():
            linia = wx.StaticLine( self.scrollWindows, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
            linia.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )
            self.usersListBox.Add(linia, 0, wx.EXPAND|wx.ALIGN_CENTRE_VERTICAL|wx.RIGHT|wx.LEFT, 10)

        self.usersListBox.Add(registerPanel, 0, wx.EXPAND|wx.ALIGN_CENTRE_VERTICAL|wx.ALL, 5)


class CreateUsernameFrame(models.SetUsernameFrame):
    def __init__(self, parent):
        models.SetUsernameFrame.__init__(self, parent)

    def OnBack( self, event ):
        frame = ListUsersFrame(None)
        frame.Show(True)

        self.Destroy()
    
    def onNext( self, event ):
        try:
            username = self.textUsername.GetValue()
            password = self.textPassword.GetValue()
            generateUser.createUser(username, password)


            dataBase = "Data/PendingRegisterUserDB.db"
            if (os.path.isfile(dataBase)):
                f = open(dataBase,"r")
                data = json.load(f)
                f.close()
                
                if not data.has_key(username):
                    data[username] = None
                    with io.open(dataBase, 'w', encoding='utf8') as outfile:
                        strJson = json.dumps(data, indent=4, sort_keys=True, separators=(',', ': '), ensure_ascii=False)
                        outfile.write(to_unicode(strJson))
                else:
                    Dialogs.ErrorMessage("Error", "Username already exists.")
            else:
                data = {}
                data[username] = None
                with io.open(dataBase, 'w', encoding='utf8') as outfile:
                    strJson = json.dumps(data, indent=4, sort_keys=True, separators=(',', ': '), ensure_ascii=False)
                    outfile.write(to_unicode(strJson))

            frame = RegisterFrame(None, username)
            frame.Show(True)

            self.Destroy()

        except Exception, e:
            Dialogs.ErrorMessage("Error",str(e))


class Dialogs():

    @staticmethod
    def ErrorMessage(title, message):
        Dialogs.Message(title, message, wx.ICON_ERROR)

    @staticmethod
    def CorrectMessage(title, message):
        Dialogs.Message(title, message, wx.OK)

    @staticmethod
    def InfoMessage(title, message):
        Dialogs.Message(title, message, wx.ICON_INFORMATION)

    @staticmethod
    def Message(title, message, style):
        dlg = wx.MessageDialog(parent=None, message=message, caption=title, style=style)
        dlg.ShowModal()
        dlg.Destroy()

def run():
    app = wx.App(False)
    frame = ListUsersFrame(None)
    frame.Show(True)
    app.MainLoop()


if __name__ == '__main__':
    run()

