import wx
import wx.xrc
import sys
import os.path
import json

sys.path.insert(0, 'PythonModules')

import ethereumUtils
import injectContract
import executeFunction

class mainFrame (wx.Frame):

	def __init__( self, parent, id, title, pos, size, style ):
		wx.Frame.__init__ ( self, parent, id = id, title =title, pos = pos, size = size, style = style )
		self.Bind( wx.EVT_CLOSE, self.onCloseEvent )

	def onCloseEvent( self, event ):
		ethereumUtils.kill_geth()
		event.Skip()


###########################################################################
## Class frameRegister
###########################################################################

class frameRegister ( mainFrame ):
	
	def __init__( self, parent ):
		mainFrame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Register", pos = wx.DefaultPosition, size = wx.Size( 870,370 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MAXIMIZE_BOX|wx.MINIMIZE_BOX|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( 870,370 )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		boxMain = wx.BoxSizer( wx.VERTICAL )
		
		boxData = wx.BoxSizer( wx.HORIZONTAL )
		
		boxPersonalData = wx.BoxSizer( wx.VERTICAL )
		
		boxName = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelName = wx.StaticText( self, wx.ID_ANY, u"Name:", wx.DefaultPosition, wx.Size( 175,-1 ), wx.ALIGN_RIGHT|wx.ST_ELLIPSIZE_END|wx.ST_NO_AUTORESIZE )
		self.labelName.Wrap( -1 )
		boxName.Add( self.labelName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		boxName.Add( self.textName, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		boxPersonalData.Add( boxName, 1, wx.EXPAND, 5 )
		
		boxFirstSurname = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelFirstSurname = wx.StaticText( self, wx.ID_ANY, u"First Surname", wx.DefaultPosition, wx.Size( 175,-1 ), wx.ALIGN_RIGHT|wx.ST_ELLIPSIZE_END|wx.ST_NO_AUTORESIZE )
		self.labelFirstSurname.Wrap( -1 )
		boxFirstSurname.Add( self.labelFirstSurname, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.textFirstSurname = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		boxFirstSurname.Add( self.textFirstSurname, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		boxPersonalData.Add( boxFirstSurname, 1, wx.EXPAND, 5 )
		
		boxSecondSurname = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelSecondSurname = wx.StaticText( self, wx.ID_ANY, u"Second Surname", wx.DefaultPosition, wx.Size( 175,-1 ), wx.ALIGN_RIGHT|wx.ST_ELLIPSIZE_END|wx.ST_NO_AUTORESIZE )
		self.labelSecondSurname.Wrap( -1 )
		boxSecondSurname.Add( self.labelSecondSurname, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.textSecondSurname = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		boxSecondSurname.Add( self.textSecondSurname, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		boxPersonalData.Add( boxSecondSurname, 1, wx.EXPAND, 5 )
		
		boxDNI = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelDNI = wx.StaticText( self, wx.ID_ANY, u"DNI/Passport:", wx.DefaultPosition, wx.Size( 175,-1 ), wx.ALIGN_RIGHT|wx.ST_ELLIPSIZE_END|wx.ST_NO_AUTORESIZE )
		self.labelDNI.Wrap( -1 )
		boxDNI.Add( self.labelDNI, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textDNI = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		boxDNI.Add( self.textDNI, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		boxPersonalData.Add( boxDNI, 1, wx.EXPAND, 5 )
		
		boxGender = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelGender = wx.StaticText( self, wx.ID_ANY, u"Gender:", wx.DefaultPosition, wx.Size( 175,-1 ), wx.ALIGN_RIGHT|wx.ST_ELLIPSIZE_END|wx.ST_NO_AUTORESIZE )
		self.labelGender.Wrap( -1 )
		boxGender.Add( self.labelGender, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		choiceGenderChoices = [ u"Male", u"Female" ]
		self.choiceGender = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceGenderChoices, 0 )
		self.choiceGender.SetSelection( 0 )
		boxGender.Add( self.choiceGender, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		boxPersonalData.Add( boxGender, 1, wx.EXPAND, 5 )
		
		boxAge = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelAge = wx.StaticText( self, wx.ID_ANY, u"Age:", wx.DefaultPosition, wx.Size( 175,-1 ), wx.ALIGN_RIGHT|wx.ST_ELLIPSIZE_END|wx.ST_NO_AUTORESIZE )
		self.labelAge.Wrap( -1 )
		boxAge.Add( self.labelAge, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textAge = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		boxAge.Add( self.textAge, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		boxPersonalData.Add( boxAge, 1, wx.EXPAND, 5 )
		
		
		boxData.Add( boxPersonalData, 1, wx.EXPAND|wx.TOP, 5 )
		
		boxAddressData = wx.BoxSizer( wx.VERTICAL )
		
		boxCountry = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelCountry = wx.StaticText( self, wx.ID_ANY, u"Country:", wx.DefaultPosition, wx.Size( 175,-1 ), wx.ALIGN_RIGHT|wx.ST_ELLIPSIZE_END|wx.ST_NO_AUTORESIZE )
		self.labelCountry.Wrap( -1 )
		boxCountry.Add( self.labelCountry, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textCountry = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		boxCountry.Add( self.textCountry, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		boxAddressData.Add( boxCountry, 1, wx.EXPAND, 5 )
		
		boxProvince = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelProvince = wx.StaticText( self, wx.ID_ANY, u"Province:", wx.DefaultPosition, wx.Size( 175,-1 ), wx.ALIGN_RIGHT|wx.ST_ELLIPSIZE_END|wx.ST_NO_AUTORESIZE )
		self.labelProvince.Wrap( -1 )
		boxProvince.Add( self.labelProvince, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textProvince = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		boxProvince.Add( self.textProvince, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		boxAddressData.Add( boxProvince, 1, wx.EXPAND, 5 )
		
		boxCity = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelCity = wx.StaticText( self, wx.ID_ANY, u"City:", wx.DefaultPosition, wx.Size( 175,-1 ), wx.ALIGN_RIGHT|wx.ST_ELLIPSIZE_END|wx.ST_NO_AUTORESIZE )
		self.labelCity.Wrap( -1 )
		boxCity.Add( self.labelCity, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textCity = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		boxCity.Add( self.textCity, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		boxAddressData.Add( boxCity, 1, wx.EXPAND, 5 )
		
		boxAddress = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelAddress = wx.StaticText( self, wx.ID_ANY, u"Address:", wx.DefaultPosition, wx.Size( 175,-1 ), wx.ALIGN_RIGHT|wx.ST_ELLIPSIZE_END|wx.ST_NO_AUTORESIZE )
		self.labelAddress.Wrap( -1 )
		boxAddress.Add( self.labelAddress, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textAddress = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		boxAddress.Add( self.textAddress, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		boxAddressData.Add( boxAddress, 1, wx.EXPAND, 5 )
		
		boxPostalCode = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelPostalCode = wx.StaticText( self, wx.ID_ANY, u"PostalCode:", wx.DefaultPosition, wx.Size( 175,-1 ), wx.ALIGN_RIGHT|wx.ST_ELLIPSIZE_END|wx.ST_NO_AUTORESIZE )
		self.labelPostalCode.Wrap( -1 )
		boxPostalCode.Add( self.labelPostalCode, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textPostalCode = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		boxPostalCode.Add( self.textPostalCode, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		boxAddressData.Add( boxPostalCode, 1, wx.EXPAND, 5 )
		
		BoxEmpty = wx.BoxSizer( wx.HORIZONTAL )
		
		
		BoxEmpty.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		boxAddressData.Add( BoxEmpty, 1, wx.EXPAND, 5 )
		
		
		boxData.Add( boxAddressData, 1, wx.EXPAND|wx.TOP|wx.RIGHT, 5 )
		
		
		boxMain.Add( boxData, 1, wx.EXPAND|wx.ALL, 5 )
		
		boxRegister = wx.BoxSizer( wx.HORIZONTAL )
		
		
		self.buttonBack = wx.Button( self, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.DefaultSize, 0 )
		boxRegister.Add( self.buttonBack, 0,  wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		boxRegister.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.buttonRegister = wx.Button( self, wx.ID_ANY, u"Register", wx.DefaultPosition, wx.DefaultSize, 0 )
		boxRegister.Add( self.buttonRegister, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		
		
		boxMain.Add( boxRegister, 1, wx.EXPAND|wx.ALL, 5 )
		
		
		self.SetSizer( boxMain )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.buttonRegister.Bind( wx.EVT_BUTTON, self.onRegister )
		self.buttonBack.Bind( wx.EVT_BUTTON, self.onBack )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onRegister( self, event ):
		mName 			= self.textName.GetValue()
		mFirstSurname 	= self.textFirstSurname.GetValue()
		mSecondSurname 	= self.textSecondSurname.GetValue()
		mDNI 			= self.textDNI.GetValue()
		mGender 		= self.choiceGender.GetSelection()
		mAge 	        = self.textAge.GetValue()

		mCountry 		= self.textCountry.GetValue()
		mProvince 		= self.textProvince.GetValue()
		mCity			= self.textCity.GetValue()
		mAddress 		= self.textAddress.GetValue()
		mPostalCode 	= self.textPostalCode.GetValue()


		##print ("mName: " 			+ str(mName))
		##print ("mFirstSurname: " 	+ str(mFirstSurname))
		##print ("mSecondSurname: " 	+ str(mSecondSurname))
		##print ("mDNI: " 			+ str(mDNI))
		##print ("mGender: " 			+ str(mGender))
		##print ("mAge: " 			+ str(mAge))
#
#
		##print ("mCountry: " 		+ str(mCountry))
		##print ("mProvince: " 		+ str(mProvince))
		##print ("mCity: " 			+ str(mCity))
		##print ("mAddress: " 		+ str(mAddress))
		##print ("mPostalCode: " 		+ str(mPostalCode))

		#if (mName           != None and mName           != "" and
		#	mFirstSurname   != None and mFirstSurname   != "" and
		#	mSecondSurname  != None and mSecondSurname  != "" and
		#	mDNI            != None and mDNI            != "" and
		#	#mGender        != None and #mGender        != "" and
		#	mAge            != None and mAge            != "" and
		#	mCountry        != None and mCountry        != "" and
		#	mProvince       != None and mProvince       != "" and
		#	mCity           != None and mCity           != "" and
		#	mAddress        != None and mAddress        != "" and
		#	mPostalCode     != None and mPostalCode     != ""):
			#os.system("python programa.py abc 1234")

		args = {}
		args["Name"] = mName
		args["FirstSurname"] = mFirstSurname#
		args["SecondSurname"] = mSecondSurname
		args["DNI"] = mDNI
		args["Gender"] = mGender
		args["Age"] = mAge
		args["Country"] = mCountry
		args["Province"] = mProvince
		args["City"] = mCity
		args["Address"] = mAddress
		args["PostalCode"] = mPostalCode

		#print ("args:\n" + str(args))

		return args

		#else:
		#	return None
		#	Dialogs.InfoMessage("ERROR","Falten camps per omplir!")
		#	#print ("falten camps per omplir")

	# Virtual event handlers, overide them in your derived class
	def onBack( self, event ):
		event.Skip()



###########################################################################
## Class frameModify
###########################################################################
class frameModify ( wx.Frame ):
	
	def __init__( self, parent, modifyValues ):
		width = 60 + len(modifyValues)*40
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Modify user", pos = wx.DefaultPosition, size = wx.Size( 870,width ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MAXIMIZE_BOX|wx.MINIMIZE_BOX|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( 870,width )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		boxMain = wx.BoxSizer( wx.VERTICAL )
		
		boxData = wx.BoxSizer( wx.VERTICAL )

		#### camp Name ####
		if (modifyValues.has_key("Name")):
			boxName = wx.BoxSizer( wx.HORIZONTAL )
			
			self.labelName = wx.StaticText( self, wx.ID_ANY, u"Name:", wx.DefaultPosition, wx.Size( 175,-1 ), wx.ALIGN_RIGHT|wx.ST_ELLIPSIZE_END|wx.ST_NO_AUTORESIZE )
			self.labelName.Wrap( -1 )
			boxName.Add( self.labelName, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
			
			self.textOldName = wx.TextCtrl( self, wx.ID_ANY, modifyValues["Name"], wx.DefaultPosition, wx.DefaultSize, 0 )
			self.textOldName.Enable( False )
			boxName.Add( self.textOldName, 2, wx.ALL, 5 )
			
			self.NewToOldName = wx.StaticText( self, wx.ID_ANY, u"->", wx.DefaultPosition, wx.DefaultSize, 0 )
			self.NewToOldName.Wrap( -1 )
			boxName.Add( self.NewToOldName, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.textNewName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
			self.textNewName.Enable( True )
			boxName.Add( self.textNewName, 2, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
					
			
			boxData.Add( boxName, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		#### camp FirstSurname ####
		if (modifyValues.has_key("FirstSurname")):
			boxFirstSurname = wx.BoxSizer( wx.HORIZONTAL )
			
			self.labelFirstSurname = wx.StaticText( self, wx.ID_ANY, u"First Surname:", wx.DefaultPosition, wx.Size( 175,-1 ), wx.ALIGN_RIGHT|wx.ST_ELLIPSIZE_END|wx.ST_NO_AUTORESIZE )
			self.labelFirstSurname.Wrap( -1 )
			boxFirstSurname.Add( self.labelFirstSurname, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
			
			self.textOldFirstSurname = wx.TextCtrl( self, wx.ID_ANY, modifyValues["FirstSurname"], wx.DefaultPosition, wx.DefaultSize, 0 )
			self.textOldFirstSurname.Enable( False )
			boxFirstSurname.Add( self.textOldFirstSurname, 2, wx.ALL, 5 )
			
			self.NewToOldFirstSurname = wx.StaticText( self, wx.ID_ANY, u"->", wx.DefaultPosition, wx.DefaultSize, 0 )
			self.NewToOldFirstSurname.Wrap( -1 )
			boxFirstSurname.Add( self.NewToOldFirstSurname, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.textNewFirstSurname = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
			self.textNewFirstSurname.Enable( True )
			boxFirstSurname.Add( self.textNewFirstSurname, 2, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
					
			
			boxData.Add( boxFirstSurname, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		#### camp SecondSurname ####
		if (modifyValues.has_key("SecondSurname")):
			boxSecondSurname = wx.BoxSizer( wx.HORIZONTAL )
			
			self.labelSecondSurname = wx.StaticText( self, wx.ID_ANY, u"Second Surname:", wx.DefaultPosition, wx.Size( 175,-1 ), wx.ALIGN_RIGHT|wx.ST_ELLIPSIZE_END|wx.ST_NO_AUTORESIZE )
			self.labelSecondSurname.Wrap( -1 )
			boxSecondSurname.Add( self.labelSecondSurname, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
			
			self.textOldSecondSurname = wx.TextCtrl( self, wx.ID_ANY, modifyValues["SecondSurname"], wx.DefaultPosition, wx.DefaultSize, 0 )
			self.textOldSecondSurname.Enable( False )
			boxSecondSurname.Add( self.textOldSecondSurname, 2, wx.ALL, 5 )
			
			self.NewToOldSecondSurname = wx.StaticText( self, wx.ID_ANY, u"->", wx.DefaultPosition, wx.DefaultSize, 0 )
			self.NewToOldSecondSurname.Wrap( -1 )
			boxSecondSurname.Add( self.NewToOldSecondSurname, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.textNewSecondSurname = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
			self.textNewSecondSurname.Enable( True )
			boxSecondSurname.Add( self.textNewSecondSurname, 2, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
					
			
			boxData.Add( boxSecondSurname, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		#### camp DNI ####
		if (modifyValues.has_key("DNI")):
			boxDNI = wx.BoxSizer( wx.HORIZONTAL )
			
			self.labelDNI = wx.StaticText( self, wx.ID_ANY, u"DNI:", wx.DefaultPosition, wx.Size( 175,-1 ), wx.ALIGN_RIGHT|wx.ST_ELLIPSIZE_END|wx.ST_NO_AUTORESIZE )
			self.labelDNI.Wrap( -1 )
			boxDNI.Add( self.labelDNI, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
			
			self.textOldDNI = wx.TextCtrl( self, wx.ID_ANY, modifyValues["DNI"], wx.DefaultPosition, wx.DefaultSize, 0 )
			self.textOldDNI.Enable( False )
			boxDNI.Add( self.textOldDNI, 2, wx.ALL, 5 )
			
			self.NewToOldDNI = wx.StaticText( self, wx.ID_ANY, u"->", wx.DefaultPosition, wx.DefaultSize, 0 )
			self.NewToOldDNI.Wrap( -1 )
			boxDNI.Add( self.NewToOldDNI, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.textNewDNI = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
			self.textNewDNI.Enable( True )
			boxDNI.Add( self.textNewDNI, 2, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
					
			
			boxData.Add( boxDNI, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		#### camp Gender ####
		if (modifyValues.has_key("Gender")):
			boxGender = wx.BoxSizer( wx.HORIZONTAL )
			
			self.labelGender = wx.StaticText( self, wx.ID_ANY, u"Gender:", wx.DefaultPosition, wx.Size( 175,-1 ), wx.ALIGN_RIGHT|wx.ST_ELLIPSIZE_END|wx.ST_NO_AUTORESIZE )
			self.labelGender.Wrap( -1 )
			boxGender.Add( self.labelGender, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
			

			choiceGenderChoices = [ u"Male", u"Female" ]
			#print ("modifyValues[Gender][0]: " + str(modifyValues["Gender"]))
			self.textOldGender = wx.TextCtrl( self, wx.ID_ANY, choiceGenderChoices[int(modifyValues["Gender"])], wx.DefaultPosition, wx.DefaultSize, 0 )
			self.textOldGender.Enable( False )
			boxGender.Add( self.textOldGender, 2, wx.ALL, 5 )
			
			self.NewToOldGender = wx.StaticText( self, wx.ID_ANY, u"->", wx.DefaultPosition, wx.DefaultSize, 0 )
			self.NewToOldGender.Wrap( -1 )
			boxGender.Add( self.NewToOldGender, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

			self.choiceNewGender = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceGenderChoices, 0 )
			self.choiceNewGender.SetSelection( int(modifyValues["Gender"]) )
			boxGender.Add( self.choiceNewGender, 2, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
					
			
			boxData.Add( boxGender, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		#### camp Age ####
		if (modifyValues.has_key("Age")):
			boxAge = wx.BoxSizer( wx.HORIZONTAL )
			
			self.labelAge = wx.StaticText( self, wx.ID_ANY, u"Age:", wx.DefaultPosition, wx.Size( 175,-1 ), wx.ALIGN_RIGHT|wx.ST_ELLIPSIZE_END|wx.ST_NO_AUTORESIZE )
			self.labelAge.Wrap( -1 )
			boxAge.Add( self.labelAge, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
			
			self.textOldAge = wx.TextCtrl( self, wx.ID_ANY, modifyValues["Age"], wx.DefaultPosition, wx.DefaultSize, 0 )
			self.textOldAge.Enable( False )
			boxAge.Add( self.textOldAge, 2, wx.ALL, 5 )
			
			self.NewToOldAge = wx.StaticText( self, wx.ID_ANY, u"->", wx.DefaultPosition, wx.DefaultSize, 0 )
			self.NewToOldAge.Wrap( -1 )
			boxAge.Add( self.NewToOldAge, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.textNewAge = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
			self.textNewAge.Enable( True )
			boxAge.Add( self.textNewAge, 2, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
					
			
			boxData.Add( boxAge, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		#### camp Country ####
		if (modifyValues.has_key("Country")):
			boxCountry = wx.BoxSizer( wx.HORIZONTAL )
			
			self.labelCountry = wx.StaticText( self, wx.ID_ANY, u"Country:", wx.DefaultPosition, wx.Size( 175,-1 ), wx.ALIGN_RIGHT|wx.ST_ELLIPSIZE_END|wx.ST_NO_AUTORESIZE )
			self.labelCountry.Wrap( -1 )
			boxCountry.Add( self.labelCountry, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
			
			self.textOldCountry = wx.TextCtrl( self, wx.ID_ANY, modifyValues["Country"], wx.DefaultPosition, wx.DefaultSize, 0 )
			self.textOldCountry.Enable( False )
			boxCountry.Add( self.textOldCountry, 2, wx.ALL, 5 )
			
			self.NewToOldCountry = wx.StaticText( self, wx.ID_ANY, u"->", wx.DefaultPosition, wx.DefaultSize, 0 )
			self.NewToOldCountry.Wrap( -1 )
			boxCountry.Add( self.NewToOldCountry, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.textNewCountry = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
			self.textNewCountry.Enable( True )
			boxCountry.Add( self.textNewCountry, 2, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
					
			
			boxData.Add( boxCountry, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		#### camp Province ####
		if (modifyValues.has_key("Province")):
			boxProvince = wx.BoxSizer( wx.HORIZONTAL )
			
			self.labelProvince = wx.StaticText( self, wx.ID_ANY, u"Province:", wx.DefaultPosition, wx.Size( 175,-1 ), wx.ALIGN_RIGHT|wx.ST_ELLIPSIZE_END|wx.ST_NO_AUTORESIZE )
			self.labelProvince.Wrap( -1 )
			boxProvince.Add( self.labelProvince, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
			
			self.textOldProvince = wx.TextCtrl( self, wx.ID_ANY, modifyValues["Province"], wx.DefaultPosition, wx.DefaultSize, 0 )
			self.textOldProvince.Enable( False )
			boxProvince.Add( self.textOldProvince, 2, wx.ALL, 5 )
			
			self.NewToOldProvince = wx.StaticText( self, wx.ID_ANY, u"->", wx.DefaultPosition, wx.DefaultSize, 0 )
			self.NewToOldProvince.Wrap( -1 )
			boxProvince.Add( self.NewToOldProvince, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.textNewProvince = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
			self.textNewProvince.Enable( True )
			boxProvince.Add( self.textNewProvince, 2, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
					
			
			boxData.Add( boxProvince, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		#### camp City ####
		if (modifyValues.has_key("City")):
			boxCity = wx.BoxSizer( wx.HORIZONTAL )
			
			self.labelCity = wx.StaticText( self, wx.ID_ANY, u"City:", wx.DefaultPosition, wx.Size( 175,-1 ), wx.ALIGN_RIGHT|wx.ST_ELLIPSIZE_END|wx.ST_NO_AUTORESIZE )
			self.labelCity.Wrap( -1 )
			boxCity.Add( self.labelCity, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
			
			self.textOldCity = wx.TextCtrl( self, wx.ID_ANY, modifyValues["City"], wx.DefaultPosition, wx.DefaultSize, 0 )
			self.textOldCity.Enable( False )
			boxCity.Add( self.textOldCity, 2, wx.ALL, 5 )
			
			self.NewToOldCity = wx.StaticText( self, wx.ID_ANY, u"->", wx.DefaultPosition, wx.DefaultSize, 0 )
			self.NewToOldCity.Wrap( -1 )
			boxCity.Add( self.NewToOldCity, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.textNewCity = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
			self.textNewCity.Enable( True )
			boxCity.Add( self.textNewCity, 2, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
					
			
			boxData.Add( boxCity, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		#### camp Address ####
		if (modifyValues.has_key("Address")):
			boxAddress = wx.BoxSizer( wx.HORIZONTAL )
			
			self.labelAddress = wx.StaticText( self, wx.ID_ANY, u"Address:", wx.DefaultPosition, wx.Size( 175,-1 ), wx.ALIGN_RIGHT|wx.ST_ELLIPSIZE_END|wx.ST_NO_AUTORESIZE )
			self.labelAddress.Wrap( -1 )
			boxAddress.Add( self.labelAddress, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
			
			self.textOldAddress = wx.TextCtrl( self, wx.ID_ANY, modifyValues["Address"], wx.DefaultPosition, wx.DefaultSize, 0 )
			self.textOldAddress.Enable( False )
			boxAddress.Add( self.textOldAddress, 2, wx.ALL, 5 )
			
			self.NewToOldAddress = wx.StaticText( self, wx.ID_ANY, u"->", wx.DefaultPosition, wx.DefaultSize, 0 )
			self.NewToOldAddress.Wrap( -1 )
			boxAddress.Add( self.NewToOldAddress, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.textNewAddress = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
			self.textNewAddress.Enable( True )
			boxAddress.Add( self.textNewAddress, 2, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
					
			
			boxData.Add( boxAddress, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		#### camp PostalCode ####
		if (modifyValues.has_key("PostalCode")):
			boxPostalCode = wx.BoxSizer( wx.HORIZONTAL )
			
			self.labelPostalCode = wx.StaticText( self, wx.ID_ANY, u"Postal Code:", wx.DefaultPosition, wx.Size( 175,-1 ), wx.ALIGN_RIGHT|wx.ST_ELLIPSIZE_END|wx.ST_NO_AUTORESIZE )
			self.labelPostalCode.Wrap( -1 )
			boxPostalCode.Add( self.labelPostalCode, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
			
			self.textOldPostalCode = wx.TextCtrl( self, wx.ID_ANY, modifyValues["PostalCode"], wx.DefaultPosition, wx.DefaultSize, 0 )
			self.textOldPostalCode.Enable( False )
			boxPostalCode.Add( self.textOldPostalCode, 2, wx.ALL, 5 )
			
			self.NewToOldPostalCode = wx.StaticText( self, wx.ID_ANY, u"->", wx.DefaultPosition, wx.DefaultSize, 0 )
			self.NewToOldPostalCode.Wrap( -1 )
			boxPostalCode.Add( self.NewToOldPostalCode, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.textNewPostalCode = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
			self.textNewPostalCode.Enable( True )
			boxPostalCode.Add( self.textNewPostalCode, 2, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
					
			
			boxData.Add( boxPostalCode, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )



		boxMain.Add( boxData, 1, wx.EXPAND|wx.ALL, 5 )
		
		boxModify = wx.BoxSizer( wx.HORIZONTAL )
		
		self.buttonBack = wx.Button( self, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.DefaultSize, 0 )
		boxModify.Add( self.buttonBack, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		boxModify.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.boxModify = wx.Button( self, wx.ID_ANY, u"Modify", wx.DefaultPosition, wx.DefaultSize, 0 )
		boxModify.Add( self.boxModify, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		boxMain.Add( boxModify, 1, wx.EXPAND|wx.ALL, 5 )
		
		
		self.SetSizer( boxMain )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.buttonBack.Bind( wx.EVT_BUTTON, self.onBack )
		self.boxModify.Bind( wx.EVT_BUTTON, self.onModify )
	
	def __del__( self ):
		pass

	#### altres butons ####
	def onBack( self, event ):
		event.Skip()
	
	def onModify( self, event ):
		choiceGenderChoices = [ "Male", "Female" ]
		# old values
		oldName = self.textOldName.GetValue()
		oldFirstSurname = self.textOldFirstSurname.GetValue()
		oldSecondSurname = self.textOldSecondSurname.GetValue()
		oldDNI = self.textOldDNI.GetValue()
		oldGender = self.textOldGender.GetValue()
		oldAge = self.textOldAge.GetValue()

		oldCountry = self.textOldCountry.GetValue()
		oldProvince = self.textOldProvince.GetValue()
		oldCity = self.textOldCity.GetValue()
		oldAddress = self.textOldAddress.GetValue()
		oldPostalCode = self.textOldPostalCode.GetValue()

		# modified values
		newName = self.textNewName.GetValue()
		newFirstSurname = self.textNewFirstSurname.GetValue()
		newSecondSurname = self.textNewSecondSurname.GetValue()
		newDNI = self.textNewDNI.GetValue()
		newGender = choiceGenderChoices[self.choiceNewGender.GetSelection()]
		newAge = self.textNewAge.GetValue()

		newCountry = self.textNewCountry.GetValue()
		newProvince = self.textNewProvince.GetValue()
		newCity = self.textNewCity.GetValue()
		newAddress = self.textNewAddress.GetValue()
		newPostalCode = self.textNewPostalCode.GetValue()


		args = {}	

		if (newName != "" and oldName != newName):
			args["Name"] = newName
		if (newFirstSurname != "" and oldFirstSurname != newFirstSurname):
			args["FirstSurname"] = newFirstSurname
		if (newSecondSurname != "" and oldSecondSurname != newSecondSurname):
			args["SecondSurname"] = newSecondSurname
		if (newDNI != "" and oldDNI != newDNI):
			args["DNI"] = newDNI
		if (oldGender != newGender):
			args["Gender"] = newGender
		if (newAge != "" and oldAge != newAge):
			args["Age"] = newAge

		if (newCountry != "" and oldCountry != newCountry):
			args["Country"] = newCountry
		if (newProvince != "" and oldProvince != newProvince):
			args["Province"] = newProvince
		if (newCity != "" and oldCity != newCity):
			args["City"] = newCity
		if (newAddress != "" and oldAddress != newAddress):
			args["Address"] = newAddress
		if (newPostalCode != "" and oldPostalCode != newPostalCode):
			args["PostalCode"] = newPostalCode

		#print ("args:\n" + str(args))

		return args



###########################################################################
## Class frameVisualizedData
###########################################################################

class frameVisualizedData ( mainFrame ):
	
	def __init__( self, parent ):
		mainFrame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Visualized Data", pos = wx.DefaultPosition, size = wx.Size( 870,370 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MAXIMIZE_BOX|wx.MINIMIZE_BOX|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( 870,370 )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		boxMain = wx.BoxSizer( wx.VERTICAL )
		
		boxData = wx.BoxSizer( wx.HORIZONTAL )
		
		boxPersonalData = wx.BoxSizer( wx.VERTICAL )
		
		boxName = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelName = wx.StaticText( self, wx.ID_ANY, u"Name:", wx.DefaultPosition, wx.Size( 175,-1 ), wx.ALIGN_RIGHT|wx.ST_ELLIPSIZE_END|wx.ST_NO_AUTORESIZE )
		self.labelName.Wrap( -1 )
		boxName.Add( self.labelName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textName.Enable( False )
		
		boxName.Add( self.textName, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		boxPersonalData.Add( boxName, 1, wx.EXPAND, 5 )
		
		boxFirstSurname = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelFirstSurname = wx.StaticText( self, wx.ID_ANY, u"First Surname", wx.DefaultPosition, wx.Size( 175,-1 ), wx.ALIGN_RIGHT|wx.ST_ELLIPSIZE_END|wx.ST_NO_AUTORESIZE )
		self.labelFirstSurname.Wrap( -1 )
		boxFirstSurname.Add( self.labelFirstSurname, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.textFirstSurname = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textFirstSurname.Enable( False )
		
		boxFirstSurname.Add( self.textFirstSurname, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		boxPersonalData.Add( boxFirstSurname, 1, wx.EXPAND, 5 )
		
		boxSecondSurname = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelSecondSurname = wx.StaticText( self, wx.ID_ANY, u"Second Surname", wx.DefaultPosition, wx.Size( 175,-1 ), wx.ALIGN_RIGHT|wx.ST_ELLIPSIZE_END|wx.ST_NO_AUTORESIZE )
		self.labelSecondSurname.Wrap( -1 )
		boxSecondSurname.Add( self.labelSecondSurname, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.textSecondSurname = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textSecondSurname.Enable( False )
		
		boxSecondSurname.Add( self.textSecondSurname, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		boxPersonalData.Add( boxSecondSurname, 1, wx.EXPAND, 5 )
		
		boxDNI = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelDNI = wx.StaticText( self, wx.ID_ANY, u"DNI/Passport:", wx.DefaultPosition, wx.Size( 175,-1 ), wx.ALIGN_RIGHT|wx.ST_ELLIPSIZE_END|wx.ST_NO_AUTORESIZE )
		self.labelDNI.Wrap( -1 )
		boxDNI.Add( self.labelDNI, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textDNI = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textDNI.Enable( False )
		
		boxDNI.Add( self.textDNI, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		boxPersonalData.Add( boxDNI, 1, wx.EXPAND, 5 )
		
		boxGender = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelGender = wx.StaticText( self, wx.ID_ANY, u"Gender:", wx.DefaultPosition, wx.Size( 175,-1 ), wx.ALIGN_RIGHT|wx.ST_ELLIPSIZE_END|wx.ST_NO_AUTORESIZE )
		self.labelGender.Wrap( -1 )
		boxGender.Add( self.labelGender, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		choiceGenderChoices = [ u"Male", u"Female" ]
		self.choiceGender = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceGenderChoices, 0 )
		self.choiceGender.SetSelection( 0 )
		self.choiceGender.Enable( False )
		
		boxGender.Add( self.choiceGender, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		boxPersonalData.Add( boxGender, 1, wx.EXPAND, 5 )
		
		boxAge = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelAge = wx.StaticText( self, wx.ID_ANY, u"Age:", wx.DefaultPosition, wx.Size( 175,-1 ), wx.ALIGN_RIGHT|wx.ST_ELLIPSIZE_END|wx.ST_NO_AUTORESIZE )
		self.labelAge.Wrap( -1 )
		boxAge.Add( self.labelAge, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textAge = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textAge.Enable( False )
		
		boxAge.Add( self.textAge, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		boxPersonalData.Add( boxAge, 1, wx.EXPAND, 5 )
		
		
		boxData.Add( boxPersonalData, 1, wx.EXPAND|wx.TOP, 5 )
		
		boxAddressData = wx.BoxSizer( wx.VERTICAL )
		
		boxCountry = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelCountry = wx.StaticText( self, wx.ID_ANY, u"Country:", wx.DefaultPosition, wx.Size( 175,-1 ), wx.ALIGN_RIGHT|wx.ST_ELLIPSIZE_END|wx.ST_NO_AUTORESIZE )
		self.labelCountry.Wrap( -1 )
		boxCountry.Add( self.labelCountry, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textCountry = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textCountry.Enable( False )
		
		boxCountry.Add( self.textCountry, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		boxAddressData.Add( boxCountry, 1, wx.EXPAND, 5 )
		
		boxProvince = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelProvince = wx.StaticText( self, wx.ID_ANY, u"Province:", wx.DefaultPosition, wx.Size( 175,-1 ), wx.ALIGN_RIGHT|wx.ST_ELLIPSIZE_END|wx.ST_NO_AUTORESIZE )
		self.labelProvince.Wrap( -1 )
		boxProvince.Add( self.labelProvince, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textProvince = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textProvince.Enable( False )
		
		boxProvince.Add( self.textProvince, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		boxAddressData.Add( boxProvince, 1, wx.EXPAND, 5 )
		
		boxCity = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelCity = wx.StaticText( self, wx.ID_ANY, u"City:", wx.DefaultPosition, wx.Size( 175,-1 ), wx.ALIGN_RIGHT|wx.ST_ELLIPSIZE_END|wx.ST_NO_AUTORESIZE )
		self.labelCity.Wrap( -1 )
		boxCity.Add( self.labelCity, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textCity = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textCity.Enable( False )
		
		boxCity.Add( self.textCity, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		boxAddressData.Add( boxCity, 1, wx.EXPAND, 5 )
		
		boxAddress = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelAddress = wx.StaticText( self, wx.ID_ANY, u"Address:", wx.DefaultPosition, wx.Size( 175,-1 ), wx.ALIGN_RIGHT|wx.ST_ELLIPSIZE_END|wx.ST_NO_AUTORESIZE )
		self.labelAddress.Wrap( -1 )
		boxAddress.Add( self.labelAddress, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textAddress = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textAddress.Enable( False )
		
		boxAddress.Add( self.textAddress, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		boxAddressData.Add( boxAddress, 1, wx.EXPAND, 5 )
		
		boxPostalCode = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelPostalCode = wx.StaticText( self, wx.ID_ANY, u"PostalCode:", wx.DefaultPosition, wx.Size( 175,-1 ), wx.ALIGN_RIGHT|wx.ST_ELLIPSIZE_END|wx.ST_NO_AUTORESIZE )
		self.labelPostalCode.Wrap( -1 )
		boxPostalCode.Add( self.labelPostalCode, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textPostalCode = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textPostalCode.Enable( False )
		
		boxPostalCode.Add( self.textPostalCode, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		boxAddressData.Add( boxPostalCode, 1, wx.EXPAND, 5 )



		#linia = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		#linia.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )
		#boxAddressData.Add( linia, 0, wx.EXPAND |wx.ALL, 5 )

		
		boxMoney = wx.BoxSizer( wx.HORIZONTAL )
		
		self.labelMoney = wx.StaticText( self, wx.ID_ANY, u"Money:", wx.DefaultPosition, wx.Size( 175,-1 ), wx.ALIGN_RIGHT|wx.ST_ELLIPSIZE_END|wx.ST_NO_AUTORESIZE )
		self.labelMoney.Wrap( -1 )
		boxMoney.Add( self.labelMoney, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textMoney = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textMoney.Enable( False )
		
		boxMoney.Add( self.textMoney, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		boxAddressData.Add( boxMoney, 1, wx.EXPAND, 5 )



		
		
		boxData.Add( boxAddressData, 1, wx.EXPAND|wx.TOP|wx.RIGHT, 5 )
		
		
		boxMain.Add( boxData, 1, wx.EXPAND|wx.ALL, 5 )
		
		boxModify = wx.BoxSizer( wx.HORIZONTAL )
		
		self.buttonExit = wx.Button( self, wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.DefaultSize, 0 )
		boxModify.Add( self.buttonExit, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		boxModify.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.boxModify = wx.Button( self, wx.ID_ANY, u"Modify", wx.DefaultPosition, wx.DefaultSize, 0 )
		boxModify.Add( self.boxModify, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		boxMain.Add( boxModify, 1, wx.EXPAND|wx.ALL, 5 )
		
		
		self.SetSizer( boxMain )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.buttonExit.Bind( wx.EVT_BUTTON, self.onExit )
		self.boxModify.Bind( wx.EVT_BUTTON, self.onModify )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onModify(self,event):
		mName           = self.textName.GetValue()
		mFirstSurname   = self.textFirstSurname.GetValue()
		mSecondSurname  = self.textSecondSurname.GetValue()
		mDNI            = self.textDNI.GetValue()
		mGender         = self.choiceGender.GetSelection()
		mAge            = self.textAge.GetValue()

		mCountry        = self.textCountry.GetValue()
		mProvince       = self.textProvince.GetValue()
		mCity           = self.textCity.GetValue()
		mAddress        = self.textAddress.GetValue()
		mPostalCode     = self.textPostalCode.GetValue()


		#print ("mName: "            + str(mName))
		#print ("mFirstSurname: "    + str(mFirstSurname))
		#print ("mSecondSurname: "   + str(mSecondSurname))
		#print ("mDNI: "             + str(mDNI))
		#print ("mGender: "          + str(mGender))
		#print ("mAge: "             + str(mAge))


		#print ("mCountry: "         + str(mCountry))
		#print ("mProvince: "        + str(mProvince))
		#print ("mCity: "            + str(mCity))
		#print ("mAddress: "         + str(mAddress))
		#print ("mPostalCode: "      + str(mPostalCode))

		args = {}
		args["Name"] = mName
		args["FirstSurname"] = mFirstSurname
		args["SecondSurname"] = mSecondSurname
		args["DNI"] = mDNI
		args["Gender"] = mGender
		args["Age"] = mAge
		args["Country"] = mCountry
		args["Province"] = mProvince
		args["City"] = mCity
		args["Address"] = mAddress
		args["PostalCode"] = mPostalCode

		return args
	
	def onExit( self, event ):
		ethereumUtils.kill_geth()
		self.Destroy()


###########################################################################
## Class usersListFrame
###########################################################################

class usersListFrame ( mainFrame ):
	
	def __init__( self, parent ):
		mainFrame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MAXIMIZE_BOX|wx.MINIMIZE_BOX|wx.TAB_TRAVERSAL )
		
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		self.SetSizeHints( 300,500 )
		self.SetMinSize( wx.Size( 300,500 ) )
		self.SetMaxSize( wx.Size( 300,500 ) )
	
	def __del__( self ):
		pass
	



###########################################################################
## Class usersListPanel
###########################################################################

class usersListPanel ( wx.Panel ):
	
	def __init__( self, parent, recalculate = True, onlyExit = False ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 300,500 ), style = wx.TAB_TRAVERSAL )
		
		self.frame = parent

		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		self.SetMinSize( wx.Size( 300,500 ) )
		self.SetMaxSize( wx.Size( 300,500 ) )
		
		self.mainBox = wx.BoxSizer( wx.VERTICAL )
		
		self.scrollWindows = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.VSCROLL )
		self.scrollWindows.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		self.scrollWindows.SetScrollRate( 5, 5 )

		buttonsBox = wx.BoxSizer( wx.HORIZONTAL )
		
		self.exitButton = wx.Button( self, wx.ID_ANY, "Exit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.exitButton.Bind(wx.EVT_BUTTON, self.onExit)
		buttonsBox.Add( self.exitButton, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		if not onlyExit:
			buttonsBox.Add( ( 0, 0), 1, wx.EXPAND|wx.ALIGN_BOTTOM, 5 )
			self.registerButton = wx.Button( self, wx.ID_ANY, "Register", wx.DefaultPosition, wx.DefaultSize, 0 )
			self.registerButton.Bind(wx.EVT_BUTTON, self.onRegister)		
			buttonsBox.Add( self.registerButton, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		linia = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		linia.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )
		self.usersListBox = wx.BoxSizer( wx.VERTICAL )

		self.scrollWindows.SetSizer( self.usersListBox )
		self.scrollWindows.Layout()
		self.usersListBox.Fit( self.scrollWindows )
		self.mainBox.Add( self.scrollWindows, 1, wx.EXPAND |wx.ALL, 10 )

		self.mainBox.Add( linia, 0, wx.EXPAND |wx.LEFT|wx.RIGHT, 10 )

		if not onlyExit:
			self.mainBox.Add( buttonsBox, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 10 )
		else:
			self.mainBox.Add( buttonsBox, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 10 )

		self.recalculateSize()

	def recalculateSize(self):
		self.SetSizer( self.mainBox )
		self.Layout()

	def onExit(self,event):
		ethereumUtils.kill_geth()
		self.frame.Destroy()

	def onRegister(self,event):
		event.Skip()

	def addUser(self,username, password, address):
		pass

	def getUsers(self):
		dataBase = "Data/UserDB.db"
		if (os.path.isfile(dataBase)):
			f = open(dataBase, 'r')
			usuaris = {}
			for line in f:
				username, address, password = line.split('~')
				password,_ = password.split('\n')
				usuaris[username] = (password,address)
				#print ("username: " + str(username))
				#print ("address: " + str(address))
				#print ("password: " + str(password))
			f.close()
			return usuaris
		else:
			raise Exception("No such file or directory: 'Data/UserDB.db'")


	def getPendingRegisterUsers(self):
		dataBase = "Data/PendingRegisterUserDB.db"
		if (os.path.isfile(dataBase)):
			f = open("Data/PendingRegisterUserDB.db","r")
			data = json.load(f)
			f.close()
			return data

			"""
			f = open(dataBase, 'r')
			usuaris = []
			for user in f:
				username,_ = user.split('\n')
				usuaris.append(username)
				#print ("username: " + str(username))
			f.close()
			return usuaris
			"""
		else:
			return {}
	
	def __del__( self ):
		pass
	

###########################################################################
## Class SetUsernameFrame
###########################################################################

class SetUsernameFrame ( mainFrame ):
	
	def __init__( self, parent, isEntitat=False ):
		mainFrame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 280,300 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MAXIMIZE_BOX|wx.MINIMIZE_BOX|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( 280,300 )
		self.SetMinSize( wx.Size( 280,300 ) )
		self.SetMaxSize( wx.Size( 280,300 ) )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		boxMain = wx.BoxSizer( wx.VERTICAL )
		
		boxTitle = wx.BoxSizer( wx.VERTICAL )
		
		
		boxTitle.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.labelTitle = wx.StaticText( self, wx.ID_ANY, u"Specify Username\nand Password", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.labelTitle.Wrap( -1 )
		boxTitle.Add( self.labelTitle, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		boxTitle.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		boxMain.Add( boxTitle, 2, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		boxContent = wx.BoxSizer( wx.HORIZONTAL )
		
		boxUsername = wx.BoxSizer( wx.VERTICAL )
		
		self.labelUsername = wx.StaticText( self, wx.ID_ANY, u"Username:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelUsername.Wrap( -1 )
		boxUsername.Add( self.labelUsername, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		
		boxUsername.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.labelPassword = wx.StaticText( self, wx.ID_ANY, u"Password:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelPassword.Wrap( -1 )
		boxUsername.Add( self.labelPassword, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		boxContent.Add( boxUsername, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
		
		boxPassword = wx.BoxSizer( wx.VERTICAL )
		
		self.textUsername = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		boxPassword.Add( self.textUsername, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		
		boxPassword.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.textPassword = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER|wx.TE_PASSWORD )
		boxPassword.Add( self.textPassword, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		boxContent.Add( boxPassword, 1, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		
		boxMain.Add( boxContent, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 10 )

		if (isEntitat):
			boxCheckButtons = wx.BoxSizer( wx.HORIZONTAL )

			self.checkButtonAdm = wx.RadioButton( self, wx.ID_ANY, u"Administracio", wx.DefaultPosition, wx.DefaultSize, 0 )
			boxCheckButtons.Add( self.checkButtonAdm, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.checkButtonSub = wx.RadioButton( self, wx.ID_ANY, u"Subvencio", wx.DefaultPosition, wx.DefaultSize, 0 )
			boxCheckButtons.Add( self.checkButtonSub, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


			self.checkButtonAdm.Bind( wx.EVT_RADIOBUTTON, self.onCheckButtonAdm )
			self.checkButtonSub.Bind( wx.EVT_RADIOBUTTON, self.onCheckButtonSub )

			boxMain.Add( boxCheckButtons, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.EXPAND, 10 )

		
		boxButtons = wx.BoxSizer( wx.HORIZONTAL )
		
		self.buttonBack = wx.Button( self, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.DefaultSize, 0 )
		boxButtons.Add( self.buttonBack, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		
		boxButtons.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.buttonNext = wx.Button( self, wx.ID_ANY, u"Next", wx.DefaultPosition, wx.DefaultSize, 0 )
		boxButtons.Add( self.buttonNext, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		
		boxMain.Add( boxButtons, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.EXPAND, 10 )
		#self.mainBox.Add( buttonsBox, 0, wx.ALL|wx.EXPAND, 10 )
		
		
		self.SetSizer( boxMain )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.textPassword.Bind( wx.EVT_TEXT_ENTER, self.onNext )
		self.buttonBack.Bind( wx.EVT_BUTTON, self.OnBack )
		self.buttonNext.Bind( wx.EVT_BUTTON, self.onNext )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onCheckButtonSub( self, event ):
		self.checkButtonAdm.SetValue( False )
	
	def onCheckButtonAdm( self, event ):
		self.checkButtonSub.SetValue( False )



	def OnBack( self, event ):
		event.Skip()
	
	def onNext( self, event ):
		event.Skip()
	

###########################################################################
## Class ContractFrame
###########################################################################

class ContractFrame ( mainFrame ):
	
	def __init__( self, parent ):
		mainFrame.__init__ ( self, parent, id = wx.ID_ANY, title = "Specify Grant Conditions", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MAXIMIZE_BOX|wx.MINIMIZE_BOX|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( 500,300 )
		self.SetMinSize( wx.Size( 500,300 ) )
		self.SetMaxSize( wx.Size( 500,300 ) )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		boxMain = wx.BoxSizer( wx.VERTICAL )

		boxMoney = wx.BoxSizer( wx.HORIZONTAL )
		

		self.labelMoney = wx.StaticText( self, wx.ID_ANY, u"Money: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelMoney.Wrap( -1 )
		
		boxMoney.Add( self.labelMoney, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.textMoney = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )

		boxMoney.Add( self.textMoney, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		boxMain.Add( boxMoney, 1, wx.ALL|wx.EXPAND, 5 )

		
		boxGender = wx.BoxSizer( wx.HORIZONTAL )
		
		self.checkBoxGender = wx.CheckBox( self, wx.ID_ANY, u"Gender?", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		boxGender.Add( self.checkBoxGender, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		choiceGenderChoices = [ u"Male", u"Female" ]
		self.choiceGender = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceGenderChoices, 0 )
		self.choiceGender.SetSelection( 0 )
		self.choiceGender.Enable( False )
		
		boxGender.Add( self.choiceGender, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		boxMain.Add( boxGender, 1, wx.EXPAND, 5 )
		
		boxAge = wx.BoxSizer( wx.VERTICAL )
		
		self.checkBoxAge = wx.CheckBox( self, wx.ID_ANY, u"Age?", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		boxAge.Add( self.checkBoxAge, 0, wx.ALL, 5 )
		
		boxAgeValues = wx.BoxSizer( wx.HORIZONTAL )
		
		self.textLeft = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textLeft.Enable( False )
		
		boxAgeValues.Add( self.textLeft, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		choiceLeftChoices = [ u"<", u"<=", u"==", u"!=" ]
		self.choiceLeft = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceLeftChoices, 0 )
		self.choiceLeft.SetSelection( 0 )
		self.choiceLeft.Enable( False )
		
		boxAgeValues.Add( self.choiceLeft, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.labelAge = wx.StaticText( self, wx.ID_ANY, u"AGE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelAge.Wrap( -1 )
		self.labelAge.Enable( False )
		
		boxAgeValues.Add( self.labelAge, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		choiceRightChoices = [ u"<", u"<=", u"==", u"!=" ]
		self.choiceRight = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceRightChoices, 0 )
		self.choiceRight.SetSelection( 0 )
		self.choiceRight.Enable( False )
		
		boxAgeValues.Add( self.choiceRight, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.textRight = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textRight.Enable( False )
		
		boxAgeValues.Add( self.textRight, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		boxAge.Add( boxAgeValues, 1, wx.ALL|wx.EXPAND, 10 )
		
		
		boxMain.Add( boxAge, 1, wx.EXPAND, 5 )
		
		boxPostalCode = wx.BoxSizer( wx.HORIZONTAL )
		
		self.choicePostalCode = wx.CheckBox( self, wx.ID_ANY, u"Postal Code?", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		boxPostalCode.Add( self.choicePostalCode, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.textPostalCode = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textPostalCode.Enable( False )

		boxPostalCode.Add( self.textPostalCode, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		boxMain.Add( boxPostalCode, 1, wx.ALL|wx.EXPAND, 5 )
		
		boxButtons = wx.BoxSizer( wx.HORIZONTAL )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		boxButtons.Add( self.buttonCancel, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		boxButtons.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.buttonCreateContract = wx.Button( self, wx.ID_ANY, u"Create", wx.DefaultPosition, wx.DefaultSize, 0 )
		boxButtons.Add( self.buttonCreateContract, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		boxMain.Add( boxButtons, 1, wx.ALL|wx.EXPAND, 10 )
		
		
		self.SetSizer( boxMain )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.checkBoxGender.Bind( wx.EVT_CHECKBOX, self.onGenderCheckBox )
		self.checkBoxAge.Bind( wx.EVT_CHECKBOX, self.onAgeCheckBox )
		self.choicePostalCode.Bind( wx.EVT_CHECKBOX, self.onPostalCodeCheckBox )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.onCancel )
		self.buttonCreateContract.Bind( wx.EVT_BUTTON, self.onCreateContract )
	
	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def onGenderCheckBox( self, event ):
		#print ("onGenderCheckBox: " + str(self.checkBoxGender.GetValue()))
		self.choiceGender.Enable( self.checkBoxGender.GetValue() )

	def onAgeCheckBox( self, event ):
		#print ("onAgeCheckBox: " + str(self.checkBoxAge.GetValue()))
		self.textLeft.Enable( self.checkBoxAge.GetValue() )
		self.choiceLeft.Enable( self.checkBoxAge.GetValue() )
		self.labelAge.Enable( self.checkBoxAge.GetValue() )
		self.choiceRight.Enable( self.checkBoxAge.GetValue() )
		self.textRight.Enable( self.checkBoxAge.GetValue() )

	def onPostalCodeCheckBox( self, event ):
		#print ("onPostalCodeCheckBox: " + str(self.choicePostalCode.GetValue()))
		self.textPostalCode.Enable( self.choicePostalCode.GetValue() )

	def onCancel( self, event ):
		event.Skip()
	
	def onCreateContract( self, event ):
		event.Skip()


###########################################################################
## Class AskPassword
###########################################################################

class AskPassword ( mainFrame ):
	
	def __init__( self, parent, password, address ):
		mainFrame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 280,172 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MAXIMIZE_BOX|wx.MINIMIZE_BOX|wx.TAB_TRAVERSAL )
		
		self.frame = parent

		self.password = password
		self.address = address
		self.SetSizeHints(  280,172 )
		
		boxMain = wx.BoxSizer( wx.VERTICAL )
		
		boxPassword = wx.BoxSizer( wx.VERTICAL )
		
		self.labelPassword = wx.StaticText( self, wx.ID_ANY, u"Enter password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.labelPassword.Wrap( -1 )
		boxPassword.Add( self.labelPassword, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.textPassword = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER|wx.TE_PASSWORD )
		boxPassword.Add( self.textPassword, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		boxButtons = wx.BoxSizer( wx.HORIZONTAL )
		
		self.buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		boxButtons.Add( self.buttonCancel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 10 )
		
		
		boxButtons.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.buttonEnter = wx.Button( self, wx.ID_ANY, u"Log In", wx.DefaultPosition, wx.DefaultSize, 0 )
		boxButtons.Add( self.buttonEnter, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 10 )
		
		
		boxPassword.Add( boxButtons, 1, wx.EXPAND, 5 )

		
		boxMain.Add( boxPassword, 1, wx.ALL|wx.EXPAND, 10 )
		
		
		self.SetSizer( boxMain )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.textPassword.Bind( wx.EVT_TEXT_ENTER, self.onLogIn )
		self.buttonEnter.Bind( wx.EVT_BUTTON, self.onLogIn )
		self.buttonCancel.Bind( wx.EVT_BUTTON, self.onCancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onLogIn( self, event ):
		event.Skip()
	
	def onCancel( self, event ):
		event.Skip()





###########################################################################
## Class frameModifyUser
###########################################################################
class frameModifyUser ( wx.Frame ):
	
	def __init__( self, parent, modifyValues ):
		width = 60 + len(modifyValues)*50
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Visualized Data", pos = wx.DefaultPosition, size = wx.Size( 870,width ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MAXIMIZE_BOX|wx.MINIMIZE_BOX|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( 870,width )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		boxMain = wx.BoxSizer( wx.VERTICAL )
		
		boxData = wx.BoxSizer( wx.VERTICAL )

		#### camp Name ####
		if (modifyValues.has_key("Name")):
			boxName = wx.BoxSizer( wx.HORIZONTAL )
			
			self.labelName = wx.StaticText( self, wx.ID_ANY, u"Name:", wx.DefaultPosition, wx.Size( 175,-1 ), wx.ALIGN_RIGHT|wx.ST_ELLIPSIZE_END|wx.ST_NO_AUTORESIZE )
			self.labelName.Wrap( -1 )
			boxName.Add( self.labelName, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
			
			self.textOldName = wx.TextCtrl( self, wx.ID_ANY, modifyValues["Name"][0], wx.DefaultPosition, wx.DefaultSize, 0 )
			self.textOldName.Enable( False )
			boxName.Add( self.textOldName, 1, wx.ALL, 5 )
			
			self.NewToOldName = wx.StaticText( self, wx.ID_ANY, u"->", wx.DefaultPosition, wx.DefaultSize, 0 )
			self.NewToOldName.Wrap( -1 )
			boxName.Add( self.NewToOldName, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.textNewName = wx.TextCtrl( self, wx.ID_ANY, modifyValues["Name"][1], wx.DefaultPosition, wx.DefaultSize, 0 )
			self.textNewName.Enable( False )
			boxName.Add( self.textNewName, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.lineName = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
			boxName.Add( self.lineName, 0, wx.EXPAND |wx.ALL, 5 )
			
			self.checkButtonNAName = wx.RadioButton( self, wx.ID_ANY, u"N/A", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
			boxName.Add( self.checkButtonNAName, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.checkButtonConfirmName = wx.RadioButton( self, wx.ID_ANY, u"Confirm", wx.DefaultPosition, wx.DefaultSize, 0 )
			boxName.Add( self.checkButtonConfirmName, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.checkButtonRejectName = wx.RadioButton( self, wx.ID_ANY, u"Reject", wx.DefaultPosition, wx.DefaultSize, 0 )
			boxName.Add( self.checkButtonRejectName, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


			self.checkButtonNAName.Bind( wx.EVT_RADIOBUTTON, self.onCheckButtonNAName )
			self.checkButtonConfirmName.Bind( wx.EVT_RADIOBUTTON, self.onCheckButtonConfirmName )
			self.checkButtonRejectName.Bind( wx.EVT_RADIOBUTTON, self.onCheckButtonRejectName )

			
			boxData.Add( boxName, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		#### camp First Surname ####
		if (modifyValues.has_key("FirstSurname")):
			boxFirstSurname = wx.BoxSizer( wx.HORIZONTAL )
			
			self.labelFirstSurname = wx.StaticText( self, wx.ID_ANY, u"First Surname:", wx.DefaultPosition, wx.Size( 175,-1 ), wx.ALIGN_RIGHT|wx.ST_ELLIPSIZE_END|wx.ST_NO_AUTORESIZE )
			self.labelFirstSurname.Wrap( -1 )
			boxFirstSurname.Add( self.labelFirstSurname, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
			
			self.textOldFirstSurname = wx.TextCtrl( self, wx.ID_ANY, modifyValues["FirstSurname"][0], wx.DefaultPosition, wx.DefaultSize, 0 )
			self.textOldFirstSurname.Enable( False )
			boxFirstSurname.Add( self.textOldFirstSurname, 1, wx.ALL, 5 )
			
			self.NewToOldFirstSurname = wx.StaticText( self, wx.ID_ANY, u"->", wx.DefaultPosition, wx.DefaultSize, 0 )
			self.NewToOldFirstSurname.Wrap( -1 )
			boxFirstSurname.Add( self.NewToOldFirstSurname, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.textNewFirstSurname = wx.TextCtrl( self, wx.ID_ANY, modifyValues["FirstSurname"][1], wx.DefaultPosition, wx.DefaultSize, 0 )
			self.textNewFirstSurname.Enable( False )
			boxFirstSurname.Add( self.textNewFirstSurname, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.lineFirstSurname = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
			boxFirstSurname.Add( self.lineFirstSurname, 0, wx.EXPAND |wx.ALL, 5 )
			
			self.checkButtonNAFirstSurname = wx.RadioButton( self, wx.ID_ANY, u"N/A", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
			boxFirstSurname.Add( self.checkButtonNAFirstSurname, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.checkButtonConfirmFirstSurname = wx.RadioButton( self, wx.ID_ANY, u"Confirm", wx.DefaultPosition, wx.DefaultSize, 0 )
			boxFirstSurname.Add( self.checkButtonConfirmFirstSurname, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.checkButtonRejectFirstSurname = wx.RadioButton( self, wx.ID_ANY, u"Reject", wx.DefaultPosition, wx.DefaultSize, 0 )
			boxFirstSurname.Add( self.checkButtonRejectFirstSurname, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


			self.checkButtonNAFirstSurname.Bind( wx.EVT_RADIOBUTTON, self.onCheckButtonNAFirstSurname )
			self.checkButtonConfirmFirstSurname.Bind( wx.EVT_RADIOBUTTON, self.onCheckButtonConfirmFirstSurname )
			self.checkButtonRejectFirstSurname.Bind( wx.EVT_RADIOBUTTON, self.onCheckButtonRejectFirstSurname )
					
			
			boxData.Add( boxFirstSurname, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		#### camp Second Surname ####
		if (modifyValues.has_key("SecondSurname")):
			boxSecondSurname = wx.BoxSizer( wx.HORIZONTAL )
			
			self.labelSecondSurname = wx.StaticText( self, wx.ID_ANY, u"Second Surname:", wx.DefaultPosition, wx.Size( 175,-1 ), wx.ALIGN_RIGHT|wx.ST_ELLIPSIZE_END|wx.ST_NO_AUTORESIZE )
			self.labelSecondSurname.Wrap( -1 )
			boxSecondSurname.Add( self.labelSecondSurname, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
			
			self.textOldSecondSurname = wx.TextCtrl( self, wx.ID_ANY, modifyValues["SecondSurname"][0], wx.DefaultPosition, wx.DefaultSize, 0 )
			self.textOldSecondSurname.Enable( False )
			boxSecondSurname.Add( self.textOldSecondSurname, 1, wx.ALL, 5 )
			
			self.NewToOldSecondSurname = wx.StaticText( self, wx.ID_ANY, u"->", wx.DefaultPosition, wx.DefaultSize, 0 )
			self.NewToOldSecondSurname.Wrap( -1 )
			boxSecondSurname.Add( self.NewToOldSecondSurname, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.textNewSecondSurname = wx.TextCtrl( self, wx.ID_ANY, modifyValues["SecondSurname"][1], wx.DefaultPosition, wx.DefaultSize, 0 )
			self.textNewSecondSurname.Enable( False )
			boxSecondSurname.Add( self.textNewSecondSurname, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.lineSecondSurname = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
			boxSecondSurname.Add( self.lineSecondSurname, 0, wx.EXPAND |wx.ALL, 5 )
			
			self.checkButtonNASecondSurname = wx.RadioButton( self, wx.ID_ANY, u"N/A", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
			boxSecondSurname.Add( self.checkButtonNASecondSurname, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.checkButtonConfirmSecondSurname = wx.RadioButton( self, wx.ID_ANY, u"Confirm", wx.DefaultPosition, wx.DefaultSize, 0 )
			boxSecondSurname.Add( self.checkButtonConfirmSecondSurname, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.checkButtonRejectSecondSurname = wx.RadioButton( self, wx.ID_ANY, u"Reject", wx.DefaultPosition, wx.DefaultSize, 0 )
			boxSecondSurname.Add( self.checkButtonRejectSecondSurname, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


			self.checkButtonNASecondSurname.Bind( wx.EVT_RADIOBUTTON, self.onCheckButtonNASecondSurname )
			self.checkButtonConfirmSecondSurname.Bind( wx.EVT_RADIOBUTTON, self.onCheckButtonConfirmSecondSurname )
			self.checkButtonRejectSecondSurname.Bind( wx.EVT_RADIOBUTTON, self.onCheckButtonRejectSecondSurname )
					
			
			boxData.Add( boxSecondSurname, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		#### camp DNI ####
		if (modifyValues.has_key("DNI")):
			boxDNI = wx.BoxSizer( wx.HORIZONTAL )
			
			self.labelDNI = wx.StaticText( self, wx.ID_ANY, u"DNI:", wx.DefaultPosition, wx.Size( 175,-1 ), wx.ALIGN_RIGHT|wx.ST_ELLIPSIZE_END|wx.ST_NO_AUTORESIZE )
			self.labelDNI.Wrap( -1 )
			boxDNI.Add( self.labelDNI, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
			
			self.textOldDNI = wx.TextCtrl( self, wx.ID_ANY, modifyValues["DNI"][0], wx.DefaultPosition, wx.DefaultSize, 0 )
			self.textOldDNI.Enable( False )
			boxDNI.Add( self.textOldDNI, 1, wx.ALL, 5 )
			
			self.NewToOldDNI = wx.StaticText( self, wx.ID_ANY, u"->", wx.DefaultPosition, wx.DefaultSize, 0 )
			self.NewToOldDNI.Wrap( -1 )
			boxDNI.Add( self.NewToOldDNI, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.textNewDNI = wx.TextCtrl( self, wx.ID_ANY, modifyValues["DNI"][1], wx.DefaultPosition, wx.DefaultSize, 0 )
			self.textNewDNI.Enable( False )
			boxDNI.Add( self.textNewDNI, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.lineDNI = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
			boxDNI.Add( self.lineDNI, 0, wx.EXPAND |wx.ALL, 5 )
			
			self.checkButtonNADNI = wx.RadioButton( self, wx.ID_ANY, u"N/A", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
			boxDNI.Add( self.checkButtonNADNI, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.checkButtonConfirmDNI = wx.RadioButton( self, wx.ID_ANY, u"Confirm", wx.DefaultPosition, wx.DefaultSize, 0 )
			boxDNI.Add( self.checkButtonConfirmDNI, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.checkButtonRejectDNI = wx.RadioButton( self, wx.ID_ANY, u"Reject", wx.DefaultPosition, wx.DefaultSize, 0 )
			boxDNI.Add( self.checkButtonRejectDNI, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


			self.checkButtonNADNI.Bind( wx.EVT_RADIOBUTTON, self.onCheckButtonNADNI )
			self.checkButtonConfirmDNI.Bind( wx.EVT_RADIOBUTTON, self.onCheckButtonConfirmDNI )
			self.checkButtonRejectDNI.Bind( wx.EVT_RADIOBUTTON, self.onCheckButtonRejectDNI )
					
			
			boxData.Add( boxDNI, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		#### camp Gender ####
		if (modifyValues.has_key("Gender")):
			boxGender = wx.BoxSizer( wx.HORIZONTAL )
			
			self.labelGender = wx.StaticText( self, wx.ID_ANY, u"Gender:", wx.DefaultPosition, wx.Size( 175,-1 ), wx.ALIGN_RIGHT|wx.ST_ELLIPSIZE_END|wx.ST_NO_AUTORESIZE )
			self.labelGender.Wrap( -1 )
			boxGender.Add( self.labelGender, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
			

			choiceGenderChoices = [ u"Male", u"Female" ]
			self.textOldGender = wx.TextCtrl( self, wx.ID_ANY, choiceGenderChoices[int(modifyValues["Gender"][0])], wx.DefaultPosition, wx.DefaultSize, 0 )
			self.textOldGender.Enable( False )
			boxGender.Add( self.textOldGender, 1, wx.ALL, 5 )
			
			self.NewToOldGender = wx.StaticText( self, wx.ID_ANY, u"->", wx.DefaultPosition, wx.DefaultSize, 0 )
			self.NewToOldGender.Wrap( -1 )
			boxGender.Add( self.NewToOldGender, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.textNewGender = wx.TextCtrl( self, wx.ID_ANY, choiceGenderChoices[int(modifyValues["Gender"][1])], wx.DefaultPosition, wx.DefaultSize, 0 )
			self.textNewGender.Enable( False )
			boxGender.Add( self.textNewGender, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.lineGender = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
			boxGender.Add( self.lineGender, 0, wx.EXPAND |wx.ALL, 5 )
			
			self.checkButtonNAGender = wx.RadioButton( self, wx.ID_ANY, u"N/A", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
			boxGender.Add( self.checkButtonNAGender, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.checkButtonConfirmGender = wx.RadioButton( self, wx.ID_ANY, u"Confirm", wx.DefaultPosition, wx.DefaultSize, 0 )
			boxGender.Add( self.checkButtonConfirmGender, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.checkButtonRejectGender = wx.RadioButton( self, wx.ID_ANY, u"Reject", wx.DefaultPosition, wx.DefaultSize, 0 )
			boxGender.Add( self.checkButtonRejectGender, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


			self.checkButtonNAGender.Bind( wx.EVT_RADIOBUTTON, self.onCheckButtonNAGender )
			self.checkButtonConfirmGender.Bind( wx.EVT_RADIOBUTTON, self.onCheckButtonConfirmGender )
			self.checkButtonRejectGender.Bind( wx.EVT_RADIOBUTTON, self.onCheckButtonRejectGender )
					
			
			boxData.Add( boxGender, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		#### camp Age ####
		if (modifyValues.has_key("Age")):
			boxAge = wx.BoxSizer( wx.HORIZONTAL )
			
			self.labelAge = wx.StaticText( self, wx.ID_ANY, u"Age:", wx.DefaultPosition, wx.Size( 175,-1 ), wx.ALIGN_RIGHT|wx.ST_ELLIPSIZE_END|wx.ST_NO_AUTORESIZE )
			self.labelAge.Wrap( -1 )
			boxAge.Add( self.labelAge, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
			
			self.textOldAge = wx.TextCtrl( self, wx.ID_ANY, modifyValues["Age"][0], wx.DefaultPosition, wx.DefaultSize, 0 )
			self.textOldAge.Enable( False )
			boxAge.Add( self.textOldAge, 1, wx.ALL, 5 )
			
			self.NewToOldAge = wx.StaticText( self, wx.ID_ANY, u"->", wx.DefaultPosition, wx.DefaultSize, 0 )
			self.NewToOldAge.Wrap( -1 )
			boxAge.Add( self.NewToOldAge, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.textNewAge = wx.TextCtrl( self, wx.ID_ANY, modifyValues["Age"][1], wx.DefaultPosition, wx.DefaultSize, 0 )
			self.textNewAge.Enable( False )
			boxAge.Add( self.textNewAge, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.lineAge = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
			boxAge.Add( self.lineAge, 0, wx.EXPAND |wx.ALL, 5 )
			
			self.checkButtonNAAge = wx.RadioButton( self, wx.ID_ANY, u"N/A", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
			boxAge.Add( self.checkButtonNAAge, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.checkButtonConfirmAge = wx.RadioButton( self, wx.ID_ANY, u"Confirm", wx.DefaultPosition, wx.DefaultSize, 0 )
			boxAge.Add( self.checkButtonConfirmAge, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.checkButtonRejectAge = wx.RadioButton( self, wx.ID_ANY, u"Reject", wx.DefaultPosition, wx.DefaultSize, 0 )
			boxAge.Add( self.checkButtonRejectAge, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


			self.checkButtonNAAge.Bind( wx.EVT_RADIOBUTTON, self.onCheckButtonNAAge )
			self.checkButtonConfirmAge.Bind( wx.EVT_RADIOBUTTON, self.onCheckButtonConfirmAge )
			self.checkButtonRejectAge.Bind( wx.EVT_RADIOBUTTON, self.onCheckButtonRejectAge )
					
			
			boxData.Add( boxAge, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		#### camp Country ####
		if (modifyValues.has_key("Country")):
			boxCountry = wx.BoxSizer( wx.HORIZONTAL )
			
			self.labelCountry = wx.StaticText( self, wx.ID_ANY, u"Country:", wx.DefaultPosition, wx.Size( 175,-1 ), wx.ALIGN_RIGHT|wx.ST_ELLIPSIZE_END|wx.ST_NO_AUTORESIZE )
			self.labelCountry.Wrap( -1 )
			boxCountry.Add( self.labelCountry, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
			
			self.textOldCountry = wx.TextCtrl( self, wx.ID_ANY, modifyValues["Country"][0], wx.DefaultPosition, wx.DefaultSize, 0 )
			self.textOldCountry.Enable( False )
			boxCountry.Add( self.textOldCountry, 1, wx.ALL, 5 )
			
			self.NewToOldCountry = wx.StaticText( self, wx.ID_ANY, u"->", wx.DefaultPosition, wx.DefaultSize, 0 )
			self.NewToOldCountry.Wrap( -1 )
			boxCountry.Add( self.NewToOldCountry, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.textNewCountry = wx.TextCtrl( self, wx.ID_ANY, modifyValues["Country"][1], wx.DefaultPosition, wx.DefaultSize, 0 )
			self.textNewCountry.Enable( False )
			boxCountry.Add( self.textNewCountry, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.lineCountry = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
			boxCountry.Add( self.lineCountry, 0, wx.EXPAND |wx.ALL, 5 )
			
			self.checkButtonNACountry = wx.RadioButton( self, wx.ID_ANY, u"N/A", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
			boxCountry.Add( self.checkButtonNACountry, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.checkButtonConfirmCountry = wx.RadioButton( self, wx.ID_ANY, u"Confirm", wx.DefaultPosition, wx.DefaultSize, 0 )
			boxCountry.Add( self.checkButtonConfirmCountry, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.checkButtonRejectCountry = wx.RadioButton( self, wx.ID_ANY, u"Reject", wx.DefaultPosition, wx.DefaultSize, 0 )
			boxCountry.Add( self.checkButtonRejectCountry, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


			self.checkButtonNACountry.Bind( wx.EVT_RADIOBUTTON, self.onCheckButtonNACountry )
			self.checkButtonConfirmCountry.Bind( wx.EVT_RADIOBUTTON, self.onCheckButtonConfirmCountry )
			self.checkButtonRejectCountry.Bind( wx.EVT_RADIOBUTTON, self.onCheckButtonRejectCountry )
					
			
			boxData.Add( boxCountry, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		#### camp Province ####
		if (modifyValues.has_key("Province")):
			boxProvince = wx.BoxSizer( wx.HORIZONTAL )
			
			self.labelProvince = wx.StaticText( self, wx.ID_ANY, u"Province:", wx.DefaultPosition, wx.Size( 175,-1 ), wx.ALIGN_RIGHT|wx.ST_ELLIPSIZE_END|wx.ST_NO_AUTORESIZE )
			self.labelProvince.Wrap( -1 )
			boxProvince.Add( self.labelProvince, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
			
			self.textOldProvince = wx.TextCtrl( self, wx.ID_ANY, modifyValues["Province"][0], wx.DefaultPosition, wx.DefaultSize, 0 )
			self.textOldProvince.Enable( False )
			boxProvince.Add( self.textOldProvince, 1, wx.ALL, 5 )
			
			self.NewToOldProvince = wx.StaticText( self, wx.ID_ANY, u"->", wx.DefaultPosition, wx.DefaultSize, 0 )
			self.NewToOldProvince.Wrap( -1 )
			boxProvince.Add( self.NewToOldProvince, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.textNewProvince = wx.TextCtrl( self, wx.ID_ANY, modifyValues["Province"][1], wx.DefaultPosition, wx.DefaultSize, 0 )
			self.textNewProvince.Enable( False )
			boxProvince.Add( self.textNewProvince, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.lineProvince = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
			boxProvince.Add( self.lineProvince, 0, wx.EXPAND |wx.ALL, 5 )
			
			self.checkButtonNAProvince = wx.RadioButton( self, wx.ID_ANY, u"N/A", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
			boxProvince.Add( self.checkButtonNAProvince, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.checkButtonConfirmProvince = wx.RadioButton( self, wx.ID_ANY, u"Confirm", wx.DefaultPosition, wx.DefaultSize, 0 )
			boxProvince.Add( self.checkButtonConfirmProvince, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.checkButtonRejectProvince = wx.RadioButton( self, wx.ID_ANY, u"Reject", wx.DefaultPosition, wx.DefaultSize, 0 )
			boxProvince.Add( self.checkButtonRejectProvince, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


			self.checkButtonNAProvince.Bind( wx.EVT_RADIOBUTTON, self.onCheckButtonNAProvince )
			self.checkButtonConfirmProvince.Bind( wx.EVT_RADIOBUTTON, self.onCheckButtonConfirmProvince )
			self.checkButtonRejectProvince.Bind( wx.EVT_RADIOBUTTON, self.onCheckButtonRejectProvince )
					
			
			boxData.Add( boxProvince, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		#### camp City ####
		if (modifyValues.has_key("City")):
			boxCity = wx.BoxSizer( wx.HORIZONTAL )
			
			self.labelCity = wx.StaticText( self, wx.ID_ANY, u"City:", wx.DefaultPosition, wx.Size( 175,-1 ), wx.ALIGN_RIGHT|wx.ST_ELLIPSIZE_END|wx.ST_NO_AUTORESIZE )
			self.labelCity.Wrap( -1 )
			boxCity.Add( self.labelCity, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
			
			self.textOldCity = wx.TextCtrl( self, wx.ID_ANY, modifyValues["City"][0], wx.DefaultPosition, wx.DefaultSize, 0 )
			self.textOldCity.Enable( False )
			boxCity.Add( self.textOldCity, 1, wx.ALL, 5 )
			
			self.NewToOldCity = wx.StaticText( self, wx.ID_ANY, u"->", wx.DefaultPosition, wx.DefaultSize, 0 )
			self.NewToOldCity.Wrap( -1 )
			boxCity.Add( self.NewToOldCity, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.textNewCity = wx.TextCtrl( self, wx.ID_ANY, modifyValues["City"][1], wx.DefaultPosition, wx.DefaultSize, 0 )
			self.textNewCity.Enable( False )
			boxCity.Add( self.textNewCity, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.lineCity = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
			boxCity.Add( self.lineCity, 0, wx.EXPAND |wx.ALL, 5 )
			
			self.checkButtonNACity = wx.RadioButton( self, wx.ID_ANY, u"N/A", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
			boxCity.Add( self.checkButtonNACity, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.checkButtonConfirmCity = wx.RadioButton( self, wx.ID_ANY, u"Confirm", wx.DefaultPosition, wx.DefaultSize, 0 )
			boxCity.Add( self.checkButtonConfirmCity, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.checkButtonRejectCity = wx.RadioButton( self, wx.ID_ANY, u"Reject", wx.DefaultPosition, wx.DefaultSize, 0 )
			boxCity.Add( self.checkButtonRejectCity, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


			self.checkButtonNACity.Bind( wx.EVT_RADIOBUTTON, self.onCheckButtonNACity )
			self.checkButtonConfirmCity.Bind( wx.EVT_RADIOBUTTON, self.onCheckButtonConfirmCity )
			self.checkButtonRejectCity.Bind( wx.EVT_RADIOBUTTON, self.onCheckButtonRejectCity )
					
			
			boxData.Add( boxCity, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		#### camp Address ####
		if (modifyValues.has_key("Address")):
			boxAddress = wx.BoxSizer( wx.HORIZONTAL )
			
			self.labelAddress = wx.StaticText( self, wx.ID_ANY, u"Address:", wx.DefaultPosition, wx.Size( 175,-1 ), wx.ALIGN_RIGHT|wx.ST_ELLIPSIZE_END|wx.ST_NO_AUTORESIZE )
			self.labelAddress.Wrap( -1 )
			boxAddress.Add( self.labelAddress, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
			
			self.textOldAddress = wx.TextCtrl( self, wx.ID_ANY, modifyValues["Address"][0], wx.DefaultPosition, wx.DefaultSize, 0 )
			self.textOldAddress.Enable( False )
			boxAddress.Add( self.textOldAddress, 1, wx.ALL, 5 )
			
			self.NewToOldAddress = wx.StaticText( self, wx.ID_ANY, u"->", wx.DefaultPosition, wx.DefaultSize, 0 )
			self.NewToOldAddress.Wrap( -1 )
			boxAddress.Add( self.NewToOldAddress, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.textNewAddress = wx.TextCtrl( self, wx.ID_ANY, modifyValues["Address"][1], wx.DefaultPosition, wx.DefaultSize, 0 )
			self.textNewAddress.Enable( False )
			boxAddress.Add( self.textNewAddress, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.lineAddress = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
			boxAddress.Add( self.lineAddress, 0, wx.EXPAND |wx.ALL, 5 )
			
			self.checkButtonNAAddress = wx.RadioButton( self, wx.ID_ANY, u"N/A", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
			boxAddress.Add( self.checkButtonNAAddress, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.checkButtonConfirmAddress = wx.RadioButton( self, wx.ID_ANY, u"Confirm", wx.DefaultPosition, wx.DefaultSize, 0 )
			boxAddress.Add( self.checkButtonConfirmAddress, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.checkButtonRejectAddress = wx.RadioButton( self, wx.ID_ANY, u"Reject", wx.DefaultPosition, wx.DefaultSize, 0 )
			boxAddress.Add( self.checkButtonRejectAddress, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


			self.checkButtonNAAddress.Bind( wx.EVT_RADIOBUTTON, self.onCheckButtonNAAddress )
			self.checkButtonConfirmAddress.Bind( wx.EVT_RADIOBUTTON, self.onCheckButtonConfirmAddress )
			self.checkButtonRejectAddress.Bind( wx.EVT_RADIOBUTTON, self.onCheckButtonRejectAddress )
					
			
			boxData.Add( boxAddress, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		#### camp PostalCode ####
		if (modifyValues.has_key("PostalCode")):
			boxPostalCode = wx.BoxSizer( wx.HORIZONTAL )
			
			self.labelPostalCode = wx.StaticText( self, wx.ID_ANY, u"Postal Code:", wx.DefaultPosition, wx.Size( 175,-1 ), wx.ALIGN_RIGHT|wx.ST_ELLIPSIZE_END|wx.ST_NO_AUTORESIZE )
			self.labelPostalCode.Wrap( -1 )
			boxPostalCode.Add( self.labelPostalCode, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
			
			self.textOldPostalCode = wx.TextCtrl( self, wx.ID_ANY, modifyValues["PostalCode"][0], wx.DefaultPosition, wx.DefaultSize, 0 )
			self.textOldPostalCode.Enable( False )
			boxPostalCode.Add( self.textOldPostalCode, 1, wx.ALL, 5 )
			
			self.NewToOldPostalCode = wx.StaticText( self, wx.ID_ANY, u"->", wx.DefaultPosition, wx.DefaultSize, 0 )
			self.NewToOldPostalCode.Wrap( -1 )
			boxPostalCode.Add( self.NewToOldPostalCode, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.textNewPostalCode = wx.TextCtrl( self, wx.ID_ANY, modifyValues["PostalCode"][1], wx.DefaultPosition, wx.DefaultSize, 0 )
			self.textNewPostalCode.Enable( False )
			boxPostalCode.Add( self.textNewPostalCode, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.linePostalCode = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
			boxPostalCode.Add( self.linePostalCode, 0, wx.EXPAND |wx.ALL, 5 )
			
			self.checkButtonNAPostalCode = wx.RadioButton( self, wx.ID_ANY, u"N/A", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
			boxPostalCode.Add( self.checkButtonNAPostalCode, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.checkButtonConfirmPostalCode = wx.RadioButton( self, wx.ID_ANY, u"Confirm", wx.DefaultPosition, wx.DefaultSize, 0 )
			boxPostalCode.Add( self.checkButtonConfirmPostalCode, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			
			self.checkButtonRejectPostalCode = wx.RadioButton( self, wx.ID_ANY, u"Reject", wx.DefaultPosition, wx.DefaultSize, 0 )
			boxPostalCode.Add( self.checkButtonRejectPostalCode, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


			self.checkButtonNAPostalCode.Bind( wx.EVT_RADIOBUTTON, self.onCheckButtonNAPostalCode )
			self.checkButtonConfirmPostalCode.Bind( wx.EVT_RADIOBUTTON, self.onCheckButtonConfirmPostalCode )
			self.checkButtonRejectPostalCode.Bind( wx.EVT_RADIOBUTTON, self.onCheckButtonRejectPostalCode )
					
			
			boxData.Add( boxPostalCode, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		boxMain.Add( boxData, 1, wx.EXPAND|wx.ALL, 5 )
		
		boxModify = wx.BoxSizer( wx.HORIZONTAL )
		
		self.buttonBack = wx.Button( self, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.DefaultSize, 0 )
		boxModify.Add( self.buttonBack, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		boxModify.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.boxModify = wx.Button( self, wx.ID_ANY, u"Modify", wx.DefaultPosition, wx.DefaultSize, 0 )
		boxModify.Add( self.boxModify, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		boxMain.Add( boxModify, 1, wx.EXPAND|wx.ALL, 5 )
		
		
		self.SetSizer( boxMain )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.buttonBack.Bind( wx.EVT_BUTTON, self.onBack )
		self.boxModify.Bind( wx.EVT_BUTTON, self.onModify )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	#### CheckButtons Name ####
	def getCheckButtonStateName( self ):
		if self.checkButtonConfirmName.GetValue():
			return "true,"
		elif self.checkButtonRejectName.GetValue():
			return "false,"
		else:
			return None

	def onCheckButtonNAName( self, event ):
		self.checkButtonConfirmName.SetValue( False )
		self.checkButtonRejectName.SetValue( False )
	
	def onCheckButtonConfirmName( self, event ):
		self.checkButtonNAName.SetValue( False )
		self.checkButtonRejectName.SetValue( False )
	
	def onCheckButtonRejectName( self, event ):
		self.checkButtonNAName.SetValue( False )
		self.checkButtonConfirmName.SetValue( False )


	#### CheckButtons FirstSurname ####
	def getCheckButtonStateFirstSurname( self ):
		if self.checkButtonConfirmFirstSurname.GetValue():
			return "true,"
		elif self.checkButtonRejectFirstSurname.GetValue():
			return "false,"
		else:
			return None

	def onCheckButtonNAFirstSurname( self, event ):
		self.checkButtonConfirmFirstSurname.SetValue( False )
		self.checkButtonRejectFirstSurname.SetValue( False )
	
	def onCheckButtonConfirmFirstSurname( self, event ):
		self.checkButtonNAFirstSurname.SetValue( False )
		self.checkButtonRejectFirstSurname.SetValue( False )
	
	def onCheckButtonRejectFirstSurname( self, event ):
		self.checkButtonNAFirstSurname.SetValue( False )
		self.checkButtonConfirmFirstSurname.SetValue( False )

		
	#### CheckButtons SecondSurname ####
	def getCheckButtonStateSecondSurname( self ):
		if self.checkButtonConfirmSecondSurname.GetValue():
			return "true,"
		elif self.checkButtonRejectSecondSurname.GetValue():
			return "false,"
		else:
			return None

	def onCheckButtonNASecondSurname( self, event ):
		self.checkButtonConfirmSecondSurname.SetValue( False )
		self.checkButtonRejectSecondSurname.SetValue( False )
	
	def onCheckButtonConfirmSecondSurname( self, event ):
		self.checkButtonNASecondSurname.SetValue( False )
		self.checkButtonRejectSecondSurname.SetValue( False )
	
	def onCheckButtonRejectSecondSurname( self, event ):
		self.checkButtonNASecondSurname.SetValue( False )
		self.checkButtonConfirmSecondSurname.SetValue( False )


	#### CheckButtons DNI ####
	def getCheckButtonStateDNI( self ):
		if self.checkButtonConfirmDNI.GetValue():
			return "true,"
		elif self.checkButtonRejectDNI.GetValue():
			return "false,"
		else:
			return None

	def onCheckButtonNADNI( self, event ):
		self.checkButtonConfirmDNI.SetValue( False )
		self.checkButtonRejectDNI.SetValue( False )
	
	def onCheckButtonConfirmDNI( self, event ):
		self.checkButtonNADNI.SetValue( False )
		self.checkButtonRejectDNI.SetValue( False )
	
	def onCheckButtonRejectDNI( self, event ):
		self.checkButtonNADNI.SetValue( False )
		self.checkButtonConfirmDNI.SetValue( False )


	#### CheckButtons Gender ####
	def getCheckButtonStateGender( self ):
		if self.checkButtonConfirmGender.GetValue():
			return "true,"
		elif self.checkButtonRejectGender.GetValue():
			return "false,"
		else:
			return None

	def onCheckButtonNAGender( self, event ):
		self.checkButtonConfirmGender.SetValue( False )
		self.checkButtonRejectGender.SetValue( False )
	
	def onCheckButtonConfirmGender( self, event ):
		self.checkButtonNAGender.SetValue( False )
		self.checkButtonRejectGender.SetValue( False )
	
	def onCheckButtonRejectGender( self, event ):
		self.checkButtonNAGender.SetValue( False )
		self.checkButtonConfirmGender.SetValue( False )


	#### CheckButtons Age ####
	def getCheckButtonStateAge( self ):
		if self.checkButtonConfirmAge.GetValue():
			return "true,"
		elif self.checkButtonRejectAge.GetValue():
			return "false,"
		else:
			return None

	def onCheckButtonNAAge( self, event ):
		self.checkButtonConfirmAge.SetValue( False )
		self.checkButtonRejectAge.SetValue( False )
	
	def onCheckButtonConfirmAge( self, event ):
		self.checkButtonNAAge.SetValue( False )
		self.checkButtonRejectAge.SetValue( False )
	
	def onCheckButtonRejectAge( self, event ):
		self.checkButtonNAAge.SetValue( False )
		self.checkButtonConfirmAge.SetValue( False )

		
	#### CheckButtons Country ####
	def getCheckButtonStateCountry( self ):
		if self.checkButtonConfirmCountry.GetValue():
			return "true,"
		elif self.checkButtonRejectCountry.GetValue():
			return "false,"
		else:
			return None

	def onCheckButtonNACountry( self, event ):
		self.checkButtonConfirmCountry.SetValue( False )
		self.checkButtonRejectCountry.SetValue( False )
	
	def onCheckButtonConfirmCountry( self, event ):
		self.checkButtonNACountry.SetValue( False )
		self.checkButtonRejectCountry.SetValue( False )
	
	def onCheckButtonRejectCountry( self, event ):
		self.checkButtonNACountry.SetValue( False )
		self.checkButtonConfirmCountry.SetValue( False )

		
	#### CheckButtons Province ####
	def getCheckButtonStateProvince( self ):
		if self.checkButtonConfirmProvince.GetValue():
			return "true,"
		elif self.checkButtonRejectProvince.GetValue():
			return "false,"
		else:
			return None

	def onCheckButtonNAProvince( self, event ):
		self.checkButtonConfirmProvince.SetValue( False )
		self.checkButtonRejectProvince.SetValue( False )
	
	def onCheckButtonConfirmProvince( self, event ):
		self.checkButtonNAProvince.SetValue( False )
		self.checkButtonRejectProvince.SetValue( False )
	
	def onCheckButtonRejectProvince( self, event ):
		self.checkButtonNAProvince.SetValue( False )
		self.checkButtonConfirmProvince.SetValue( False )


	#### CheckButtons City ####
	def getCheckButtonStateCity( self ):
		if self.checkButtonConfirmCity.GetValue():
			return "true,"
		elif self.checkButtonRejectCity.GetValue():
			return "false,"
		else:
			return None

	def onCheckButtonNACity( self, event ):
		self.checkButtonConfirmCity.SetValue( False )
		self.checkButtonRejectCity.SetValue( False )
	
	def onCheckButtonConfirmCity( self, event ):
		self.checkButtonNACity.SetValue( False )
		self.checkButtonRejectCity.SetValue( False )
	
	def onCheckButtonRejectCity( self, event ):
		self.checkButtonNACity.SetValue( False )
		self.checkButtonConfirmCity.SetValue( False )

		
	#### CheckButtons Address ####
	def getCheckButtonStateAddress( self ):
		if self.checkButtonConfirmAddress.GetValue():
			return "true,"
		elif self.checkButtonRejectAddress.GetValue():
			return "false,"
		else:
			return None

	def onCheckButtonNAAddress( self, event ):
		self.checkButtonConfirmAddress.SetValue( False )
		self.checkButtonRejectAddress.SetValue( False )
	
	def onCheckButtonConfirmAddress( self, event ):
		self.checkButtonNAAddress.SetValue( False )
		self.checkButtonRejectAddress.SetValue( False )
	
	def onCheckButtonRejectAddress( self, event ):
		self.checkButtonNAAddress.SetValue( False )
		self.checkButtonConfirmAddress.SetValue( False )


	#### CheckButtons PostalCode ####
	def getCheckButtonStatePostalCode( self ):
		if self.checkButtonConfirmPostalCode.GetValue():
			return "true,"
		elif self.checkButtonRejectPostalCode.GetValue():
			return "false,"
		else:
			return None

	def onCheckButtonNAPostalCode( self, event ):
		self.checkButtonConfirmPostalCode.SetValue( False )
		self.checkButtonRejectPostalCode.SetValue( False )
	
	def onCheckButtonConfirmPostalCode( self, event ):
		self.checkButtonNAPostalCode.SetValue( False )
		self.checkButtonRejectPostalCode.SetValue( False )
	
	def onCheckButtonRejectPostalCode( self, event ):
		self.checkButtonNAPostalCode.SetValue( False )
		self.checkButtonConfirmPostalCode.SetValue( False )

	#### altres butons ####
	def onBack( self, event ):
		event.Skip()
	
	def onModify( self, event ):
		event.Skip()

