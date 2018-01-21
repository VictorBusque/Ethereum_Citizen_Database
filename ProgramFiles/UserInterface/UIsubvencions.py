#!/usr/bin/python

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


class CreateSubvencionsFrame(models.ContractFrame):
    def __init__(self, parent, username):
        models.ContractFrame.__init__(self, parent)

        self.address, self.password = ethereumUtils.get_user_address_pass_entitat_sub(username)
        ethereumUtils.unlock_account(self.address, self.password)
        ##print ("username: " + str(username))
        #res = executeFunction.computeOutput(username, '0', "newSubvention", ['2222', '[0]', '[0]', '[22]'],  tipus = '2')
        ##print ("res: " + str(res))
    
    def onCancel( self, event ):
        ethereumUtils.kill_geth()
        self.Destroy()
    
    def onCreateContract( self, event ):
        ethereumUtils.unlock_account(self.address, self.password)

        bGender = self.checkBoxGender.GetValue()
        bAge = self.checkBoxAge.GetValue()
        bPostalCode = self.choicePostalCode.GetValue()

        money = self.textMoney.GetValue()

        ageLeft = self.textLeft.GetValue()
        ageRight = self.textRight.GetValue()
        value_postalCode = self.textPostalCode.GetValue()

        if not bGender and not bAge and not bPostalCode:
            Dialogs.ErrorMessage("Error","No conditions have been chosen")
        elif money == "" or money == "0":
            Dialogs.ErrorMessage("Error","It has not been specified how much money")
        elif (bAge and (ageLeft == "" and ageRight == "")) or (bPostalCode and value_postalCode == ""):
            Dialogs.ErrorMessage("Error","The condition has been chosen, but no value has been specified")
        else:
            l_variables = []
            l_operators = []
            l_values = []

            # variable:
            #   Age         ->  0
            #   Gender      ->  1
            #   PostalCode  ->  2
            # operator:
            # valor persona (op) valor subvencio
            #   ==  ->  0
            #   !=  ->  1
            #   <=  ->  2
            #   >=  ->  3
            #   <   ->  4
            #   >   ->  5
            if (bGender):
                l_variables.append(1)
                l_operators.append(0)
                l_values.append(self.choiceGender.GetSelection())
            if (bAge):

                #choiceLeftChoices = [ "<", "<=", "==", "!=" ]
                # valor subvencio (op) valor persona
                #   "<"  ->  0  -> 5
                #   "<=" ->  1  -> 3
                #   "==" ->  2  -> 0
                #   "!=" ->  3  -> 1
                if (ageLeft != ""):
                    l_variables.append(0)
                    leftCondition = self.choiceLeft.GetSelection()
                    if (leftCondition == 0):
                        l_operators.append(5)
                    elif (leftCondition == 1):
                        l_operators.append(3)
                    elif (leftCondition == 2):
                        l_operators.append(0)
                    else:
                        l_operators.append(1)
                    l_values.append(int(ageLeft))

                #choiceRightChoices = [ "<", "<=", "==", "!=" ]
                # valor persona (op) valor subvencio
                #   "<"  ->  0  -> 4
                #   "<=" ->  1  -> 2
                #   "==" ->  2  -> 0
                #   "!=" ->  3  -> 1
                if (ageRight != ""):
                    l_variables.append(0)
                    rightCondition = self.choiceRight.GetSelection()
                    if (rightCondition == 0):
                        l_operators.append(4)
                    elif (rightCondition == 1):
                        l_operators.append(2)
                    elif (rightCondition == 2):
                        l_operators.append(0)
                    else:
                        l_operators.append(1)
                    l_values.append(int(ageRight))
            if (bPostalCode):
                l_variables.append(2)
                l_operators.append(0)
                l_values.append(str(value_postalCode))

            mDades = [str(money), \
                str(l_variables), \
                str(l_operators), \
                str(l_values) ]
            
            inParams = ""
            if len(mDades) > 0:
                for parameter in mDades:
                    inParams += parameter+', '

            # uint amount, uint8[] variable, uint8[] operator, uint[] value
            #       '2222'             '[0]'             '[0]'       '[22]'
            #res = executeFunction.computeOutput("subvencio1", 0, "newSubvention", mDades)
            ##print ("computeOutput(\"newSubvention\"): " + str(res))
            #print ("mDades: " + str(mDades))
            ##print ("inParams: " + str(inParams))


            ethereumUtils.unlock_account(self.address, self.password)
            res = ethereumUtils.execute_function_on_Manager(self.address, "newSubvention", inParams, gas="'4712388'")
            #res2 = ethereumUtils.execute_function_on_Person(str(self.address), str(self.ca_address), "confirm", "8,"+res, gas="'4712388'")

            #ethereumUtils.unlock_account(self.address, self.password)
            #res = ethereumUtils.execute_function_on_Manager("0xa0350e18ffa0e79b37e887f99c0ebfc7e1beb0c3", "newSubvention", inParams)


            #print ("computeOutput(\"newSubvention\"): " + str(res))

            Dialogs.CorrectMessage("Success","Subvencion has been created successfully")
            ethereumUtils.kill_geth()
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
    frame = CreateSubvencionsFrame(None,username)
    frame.Show(True)
    app.MainLoop()


if __name__ == '__main__':
    run("subvencio1")

