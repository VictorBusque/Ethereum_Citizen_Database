#!/usr/bin/python

#importing wx files
import wx
import sys
import os
import json
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



class ListUsersFrame(models.usersListFrame):
    def __init__(self, parent, username):
        models.usersListFrame.__init__(self, parent)
        self.usernameEntitat = username

        self.address, self.password = ethereumUtils.get_user_address_pass_entitat_adm(username)
        ethereumUtils.unlock_account(self.address, self.password)
        #print ("self.address: " + str(self.address))
        #print ("self.password: " + str(self.password))
        #print ("username: " + str(username))

        self.llista_CA = executeFunction.computeOutput(username, 0, "getPersonsToModify", [], tipus = "1")
        #print ("computeOutput(username, \"getPersonsToModify\"): " + str(self.llista_CA))

        res1 = executeFunction.computeOutput(username, 0, "getPersons", [], tipus = "1")
        #print ("computeOutput(username, \"getPersons\"): " + str(res1))

        res2 = executeFunction.computeOutput(username, 0, "getSubventions", [], tipus = "1")
        #print ("computeOutput(username, \"getSubventions\"): " + str(res2))

        res3 = executeFunction.computeOutput(username, 0, "getCreators", [], tipus = "1")
        #print ("computeOutput(username, \"getCreators\"): " + str(res3))

        while ('' in self.llista_CA):
            self.llista_CA.remove('')

        self.Llista_names = {}
        for ca in self.llista_CA:
            names = ethereumUtils.execute_function_on_Person(str(ca), str(self.address), "getStr", " 0 ,")[0].split(",")
            #print ("names: " + str(names))
            nameOld = names[0]
            nameNew = names[1]
            if (nameOld != "-1" and nameOld != "None"):
                self.Llista_names[nameOld] = ca
            elif (nameNew != "-1"):
                self.Llista_names[nameNew] = ca


        usersBox = UsersBox(self, self.usernameEntitat)
        
        frameBox = wx.BoxSizer( wx.VERTICAL )
        frameBox.Add( usersBox, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        self.SetSizer( frameBox )
        self.Layout()
        
        self.Centre( wx.BOTH )



class UsersBox(models.usersListPanel):
    def __init__(self, parent, usernameEntitat):
        models.usersListPanel.__init__(self, parent, False, True)
        self.frame = parent
        self.usernameEntitat = usernameEntitat

        #print ("parent.Llista_names: " + str(parent.Llista_names))

        try:
            self.addUsers(parent.Llista_names)

        except Exception, e:
            Dialogs.ErrorMessage("Error",str(e))
            self.frame.Destroy()

    def addUsers(self, usuaris):
        for usuari in usuaris:
            address = usuaris[usuari]

            self.addUser(usuari, address, None)

            self.recalculateSize()

    def getModifyValues(self, address):

        res1 = ethereumUtils.execute_function_on_Person(str(address), str(self.frame.address), "whoDirty1", "")[0].split(",")
        #print ("res1:" + str(res1))

        res2 = ethereumUtils.execute_function_on_Person(str(address), str(self.frame.address), "whoDirty2", "")[0].split(",")
        #print ("res2:" + str(res2))

        bName = ("true" == res1[0])
        bFirstSurname = ("true" == res1[1])
        bSecondSurname = ("true" == res1[2])
        bDNI = ("true" == res1[3])
        bGender = ("true" == res1[4])
        bAge = ("true" == res1[5])

        bCountry = ("true" == res2[0])
        bProvince = ("true" == res2[1])
        bCity = ("true" == res2[2])
        bAddress = ("true" == res2[3])
        bPostalCode = ("true" == res2[4])

        modifyValues = {}

        if (bName):
            res3 = ethereumUtils.execute_function_on_Person(str(address), str(self.frame.address), "getStr", "0,")[0].split(",")
            #print ("res3: " + str(res3))
            modifyValues["Name"] = (res3[0], res3[1])

        if (bFirstSurname):
            res3 = ethereumUtils.execute_function_on_Person(str(address), str(self.frame.address), "getStr", "1,")[0].split(",")
            #print ("res3: " + str(res3))
            modifyValues["FirstSurname"] = (res3[0], res3[1])

        if (bSecondSurname):
            res3 = ethereumUtils.execute_function_on_Person(str(address), str(self.frame.address), "getStr", "2,")[0].split(",")
            #print ("res3: " + str(res3))
            modifyValues["SecondSurname"] = (res3[0], res3[1])

        if (bDNI):
            res3 = ethereumUtils.execute_function_on_Person(str(address), str(self.frame.address), "getStr", "3,")[0].split(",")
            #print ("res3: " + str(res3))
            modifyValues["DNI"] = (res3[0], res3[1])

        if (bGender):
            res3 = ethereumUtils.execute_function_on_Person(str(address), str(self.frame.address), "getInt", "4,")[0].split(",")
            #print ("res3: " + str(res3))
            modifyValues["Gender"] = (res3[0], res3[1])

        if (bAge):
            res3 = ethereumUtils.execute_function_on_Person(str(address), str(self.frame.address), "getInt", "5,")[0].split(",")
            #print ("res3: " + str(res3))
            modifyValues["Age"] = (res3[0], res3[1])


        if (bCountry):
            res3 = ethereumUtils.execute_function_on_Person(str(address), str(self.frame.address), "getStr", "6,")[0].split(",")
            #print ("res3: " + str(res3))
            modifyValues["Country"] = (res3[0], res3[1])

        if (bProvince):
            res3 = ethereumUtils.execute_function_on_Person(str(address), str(self.frame.address), "getStr", "7,")[0].split(",")
            #print ("res3: " + str(res3))
            modifyValues["Province"] = (res3[0], res3[1])

        if (bCity):
            res3 = ethereumUtils.execute_function_on_Person(str(address), str(self.frame.address), "getStr", "8,")[0].split(",")
            #print ("res3: " + str(res3))
            modifyValues["City"] = (res3[0], res3[1])

        if (bAddress):
            res3 = ethereumUtils.execute_function_on_Person(str(address), str(self.frame.address), "getStr", "9,")[0].split(",")
            #print ("res3: " + str(res3))
            modifyValues["Address"] = (res3[0], res3[1])

        if (bPostalCode):
            res3 = ethereumUtils.execute_function_on_Person(str(address), str(self.frame.address), "getInt", "10,")[0].split(",")
            #print ("res3: " + str(res3))
            modifyValues["PostalCode"] = (res3[0], res3[1])

        #print ("modifyValues: " + str(modifyValues))
        return modifyValues

    def addUser(self,dni, address, _):
        userBox = wx.BoxSizer(wx.HORIZONTAL)
        nameLabel = wx.StaticText( self.scrollWindows, wx.ID_ANY, dni, wx.DefaultPosition, wx.DefaultSize, 0 )
        nameLabel.Wrap( -1 )
        modifyButton = wx.Button(self.scrollWindows, wx.ID_ANY, "Modify", wx.DefaultPosition, wx.DefaultSize, 0 )

        def modifyUser(event):
            #address, _ = ethereumUtils.get_user_address_pass(id)

            modifyValues = self.getModifyValues(address)
            frame = ModifyUserFrame(None, self.frame.address, address, self.usernameEntitat, modifyValues)
            frame.Show(True)

            self.frame.Destroy()
        
        modifyButton.Bind(wx.EVT_BUTTON, modifyUser)
        userBox.Add(nameLabel,1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
        userBox.Add(modifyButton, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)

        if self.usersListBox.GetChildren():
            linia = wx.StaticLine( self.scrollWindows, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
            linia.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )
            self.usersListBox.Add(linia, 0, wx.EXPAND|wx.ALIGN_CENTRE_VERTICAL|wx.RIGHT|wx.LEFT, 10)

        self.usersListBox.Add(userBox, 0, wx.EXPAND|wx.ALIGN_CENTRE_VERTICAL|wx.ALL, 5)

class ModifyUserFrame(models.frameModifyUser):

    def __init__(self, parent, ca_address, address, usernameEntitat, values = None):
        models.frameModifyUser.__init__(self, parent, values)
        self.usernameEntitat = usernameEntitat
        self.values = values
        self.ca_address = ca_address
        self.address = address

    def onBack(self,event):
        frame = ListUsersFrame(None, )
        frame.Show(True)

        self.Destroy()


    def onModify( self, event ):
        if "Name" in self.values:
            res = self.getCheckButtonStateName()
            #print ("estat button Name: " + str(res))
            if (res != None):
                res2 = ethereumUtils.execute_function_on_Person(str(self.address), str(self.ca_address), "confirm", "0,"+res, gas="'4712388'")
                #print ("res2: " + str(res2))
        
        if "FirstSurname" in self.values:
            res = self.getCheckButtonStateFirstSurname()
            #print ("estat button FirstSurname: " + str(res))
            if (res != None):
                res2 = ethereumUtils.execute_function_on_Person(str(self.address), str(self.ca_address), "confirm", "1,"+res, gas="'4712388'")
                #print ("res2: " + str(res2))
        
        if "SecondSurname" in self.values:
            res = self.getCheckButtonStateSecondSurname()
            #print ("estat button SecondSurname: " + str(res))
            if (res != None):
                res2 = ethereumUtils.execute_function_on_Person(str(self.address), str(self.ca_address), "confirm", "2,"+res, gas="'4712388'")
                #print ("res2: " + str(res2))
        
        if "DNI" in self.values:
            res = self.getCheckButtonStateDNI()
            #print ("estat button DNI: " + str(res))
            if (res != None):
                res2 = ethereumUtils.execute_function_on_Person(str(self.address), str(self.ca_address), "confirm", "3,"+res, gas="'4712388'")
                #print ("res2: " + str(res2))
        
        if "Gender" in self.values:
            res = self.getCheckButtonStateGender()
            #print ("estat button Gender: " + str(res))
            if (res != None):
                res2 = ethereumUtils.execute_function_on_Person(str(self.address), str(self.ca_address), "confirm", "4,"+res, gas="'4712388'")
                #print ("res2: " + str(res2))
        
        if "Age" in self.values:
            res = self.getCheckButtonStateAge()
            #print ("estat button Age: " + str(res))
            if (res != None):
                res2 = ethereumUtils.execute_function_on_Person(str(self.address), str(self.ca_address), "confirm", "5,"+res, gas="'4712388'")
                #print ("res2: " + str(res2))
        
        if "Country" in self.values:
            res = self.getCheckButtonStateCountry()
            #print ("estat button Country: " + str(res))
            if (res != None):
                res2 = ethereumUtils.execute_function_on_Person(str(self.address), str(self.ca_address), "confirm", "6,"+res, gas="'4712388'")
                #print ("res2: " + str(res2))
        
        if "Province" in self.values:
            res = self.getCheckButtonStateProvince()
            #print ("estat button Province: " + str(res))
            if (res != None):
                res2 = ethereumUtils.execute_function_on_Person(str(self.address), str(self.ca_address), "confirm", "7,"+res, gas="'4712388'")
                #print ("res2: " + str(res2))
        
        if "City" in self.values:
            res = self.getCheckButtonStateCity()
            #print ("estat button City: " + str(res))
            if (res != None):
                res2 = ethereumUtils.execute_function_on_Person(str(self.address), str(self.ca_address), "confirm", "8,"+res, gas="'4712388'")
                #print ("res2: " + str(res2))
        
        if "Address" in self.values:
            res = self.getCheckButtonStateAddress()
            #print ("estat button Address: " + str(res))
            if (res != None):
                res2 = ethereumUtils.execute_function_on_Person(str(self.address), str(self.ca_address), "confirm", "9,"+res, gas="'4712388'")
                #print ("res2: " + str(res2))
        
        if "PostalCode" in self.values:
            res = self.getCheckButtonStatePostalCode()
            #print ("estat button PostalCode: " + str(res))
            if (res != None):
                res2 = ethereumUtils.execute_function_on_Person(str(self.address), str(self.ca_address), "confirm", "10,"+res, gas="'4712388'")
                #print ("res2: " + str(res2))


        Dialogs.CorrectMessage("Success","Changes has been updated successfully")

        frame = ListUsersFrame(None, self.usernameEntitat)
        frame.Show(True)

        self.Destroy()



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


def run(username):
    app = wx.App(False)
    frame = ListUsersFrame(None,username)
    frame.Show(True)
    app.MainLoop()


if __name__ == '__main__':
    run("entitat8")
