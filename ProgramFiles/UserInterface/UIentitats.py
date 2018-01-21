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
import UIadministracio
import UIsubvencions
import models
import ethereumUtils
import injectContract
import generateUser
import executeFunction


class ListEntitatsFrame(models.usersListFrame):
    def __init__(self, parent):
        models.usersListFrame.__init__(self, parent)
        entitatsBox = EntitatsBox(self)
        
        frameBox = wx.BoxSizer( wx.VERTICAL )
        frameBox.Add( entitatsBox, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        self.SetSizer( frameBox )
        self.Layout()
        
        self.Centre( wx.BOTH )



class PasswordLogInFrame ( models.AskPassword ):
    def __init__( self, parent, username, password, address, isAdm ):
        models.AskPassword.__init__(self, parent, password, address)
        self.username = username
        self.isAdm = isAdm
    
    # Virtual event handlers, overide them in your derived class
    def onLogIn( self, event ):
        if (self.password == self.textPassword.GetValue()):
            if (self.isAdm):
                frame = UIadministracio.ListUsersFrame(None,self.username)
                frame.Show(True)
            else:
                frame = UIsubvencions.CreateSubvencionsFrame(None,self.username)
                frame.Show(True)

            self.frame.Destroy()
            self.Destroy()

        else:
            Dialogs.ErrorMessage("Wrong Password","The password is not correct, try again")
            #print(self.password)
            #print(str(self.textPassword.GetValue()))

    def onCancel( self, event ):
        self.Destroy()



class EntitatsBox(models.usersListPanel):
    def __init__(self, parent):
        models.usersListPanel.__init__(self, parent, False)
        self.frame = parent

        try:
            entitatsAdm = self.getEntitatsAdm()
            entitatsSub = self.getEntitatsSub()

            #print ("entitatsAdm: " + str(entitatsAdm))
            #print ("entitatsSub: " + str(entitatsSub))

            self.addEntitatsAdm(entitatsAdm)
            self.addEntitatsSub(entitatsSub)            
        except Exception, e:
            Dialogs.ErrorMessage("Error",str(e))

            ethereumUtils.kill_geth()
            self.frame.Destroy()
    
    def onRegister(self,event):
        frame = CreateUsernameFrame(self.frame)
        frame.Show(True)

        #self.frame.Destroy()

    def addEntitatsAdm(self, entitats):
        for entitat in entitats:
            (p, a) = entitats[entitat]
            self.addEntitatAdm(entitat,p,a)
            self.recalculateSize()

    def addEntitatsSub(self, entitats):
        for entitat in entitats:
            (p, a) = entitats[entitat]
            self.addEntitatSub(entitat,p,a)
            self.recalculateSize()

    def getEntitatsAdm(self):
        dataBase = "Data/EntitatsDB.db"
        if (os.path.isfile(dataBase)):
            f = open(dataBase, 'r')
            entitats = {}
            for line in f:
                username, address, password = line.split('~')
                password,_ = password.split('\n')
                entitats[username] = (password,address)
                #print ("username: " + str(username))
                #print ("address: " + str(address))
                #print ("password: " + str(password))
            f.close()
            return entitats
        else:
            raise Exception("No such file or directory: 'Data/EntitatsDB.db'")


    def getEntitatsSub(self):
        dataBase = "Data/SubvencionsDB.db"
        if (os.path.isfile(dataBase)):
            f = open(dataBase, 'r')
            entitats = {}
            for line in f:
                username, address, password = line.split('~')
                password,_ = password.split('\n')
                entitats[username] = (password,address)
                #print ("username: " + str(username))
                #print ("address: " + str(address))
                #print ("password: " + str(password))
            f.close()
            return entitats
        else:
            raise Exception("No such file or directory: 'Data/SubvencionsDB.db'")

    def addEntitatAdm(self,username, password, address):
        registerPanel = wx.Panel( self.scrollWindows, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )

        registerPanel.SetBackgroundColour( wx.Colour( 228, 174, 57 ) )
        buttonText = "LogIn"

        userBox = wx.BoxSizer( wx.HORIZONTAL )
        
        nameLabel = wx.StaticText( registerPanel, wx.ID_ANY, username, wx.DefaultPosition, wx.DefaultSize, 0 )
        nameLabel.Wrap( -1 )
        logInButton = wx.Button( registerPanel, wx.ID_ANY, buttonText, wx.DefaultPosition, wx.DefaultSize, 0 )

        def checkEntitat(event):
            #print ("password: " + str(password))
            frame = PasswordLogInFrame(self.frame, username, password, address, True)
            frame.Show(True)

        logInButton.Bind(wx.EVT_BUTTON, checkEntitat)
        userBox.Add(nameLabel,1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
        userBox.Add(logInButton, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
        
        registerPanel.SetSizer( userBox )
        registerPanel.Layout()
        userBox.Fit( registerPanel )

        if self.usersListBox.GetChildren():
            linia = wx.StaticLine( self.scrollWindows, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
            linia.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )
            self.usersListBox.Add(linia, 0, wx.EXPAND|wx.ALIGN_CENTRE_VERTICAL|wx.RIGHT|wx.LEFT, 10)

        self.usersListBox.Add(registerPanel, 0, wx.EXPAND|wx.ALIGN_CENTRE_VERTICAL|wx.ALL, 5)



    def addEntitatSub(self,username, password, address):
        registerPanel = wx.Panel( self.scrollWindows, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )

        registerPanel.SetBackgroundColour( wx.Colour( 208, 208, 208 ) )
        buttonText = "LogIn"

        userBox = wx.BoxSizer( wx.HORIZONTAL )
        
        nameLabel = wx.StaticText( registerPanel, wx.ID_ANY, username, wx.DefaultPosition, wx.DefaultSize, 0 )
        nameLabel.Wrap( -1 )
        logInButton = wx.Button( registerPanel, wx.ID_ANY, buttonText, wx.DefaultPosition, wx.DefaultSize, 0 )

        def checkEntitat(event):
            #print ("password: " + str(password))
            frame = PasswordLogInFrame(self.frame, username, password, address, False)
            frame.Show(True)

        logInButton.Bind(wx.EVT_BUTTON, checkEntitat)
        userBox.Add(nameLabel,1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
        userBox.Add(logInButton, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
        
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
        models.SetUsernameFrame.__init__(self, parent, True)
        self.parent = parent
        self.buttonNext.SetLabel("Create")

    def OnBack( self, event ):
        self.Destroy()
    
    def onNext( self, event ):
        try:
            username = self.textUsername.GetValue()
            password = self.textPassword.GetValue()


            if (self.checkButtonAdm == None and self.checkButtonSub == None):
                Dialogs.ErrorMessage("Error", "Something go wrong, try it later.")
            elif (self.checkButtonAdm.GetValue()):
                generateUser.createEntitatAdm(username, password)
            elif (self.checkButtonSub.GetValue()):
                generateUser.createEntitatSub(username, password)
            else:
                Dialogs.ErrorMessage("Error", "Something go wrong, try it later.")

            frame = ListEntitatsFrame(None)
            frame.Show(True)

            self.parent.Destroy()
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


app = wx.App(False)
frame = ListEntitatsFrame(None)
frame.Show(True)
app.MainLoop()


