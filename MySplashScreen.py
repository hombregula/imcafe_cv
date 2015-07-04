'''
Created on 08/12/2013

@author: hombregula
'''
import wx
class MySplashScreen (wx.SplashScreen):
    def __init__(self, Milisegundos,parent=None):
        # This is a recipe to a the screen.
        # Modify the following variables as necessary.
        aBitmap = wx.Image(name = "Icons\SplashScreen_1.jpg").ConvertToBitmap()
        splashStyle = wx.SPLASH_CENTRE_ON_SCREEN | wx.SPLASH_TIMEOUT
        splashDuration = Milisegundos # milliseconds
        # Call the constructor with the above arguments in exactly the
        # following order.
        wx.SplashScreen.__init__(self, aBitmap, splashStyle,
                                 splashDuration, parent,size=(50, 400))
        self.Bind(wx.EVT_CLOSE, self.OnExit)

        wx.Yield()
    def OnExit(self, evt):
        self.Hide()
        # MyFrame is the main frame.
        '''MyFrame = MyGUI(None, -1, "Hello from wxPython")
        app.SetTopWindow(MyFrame)
        MyFrame.Show(True)
        # The program will freeze without this line.
        evt.Skip()  # Make sure the default handler runs too...        '''
        
        
        ##self.picture.SetBitmap(wx.Bitmap('L:\\Laboratorio\\Wx\\icons\\skybolt_cutaway_white_truss.jpg'))