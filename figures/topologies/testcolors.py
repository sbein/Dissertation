from ROOT import *
h1 = TH1F('','',100,-3,3)
h1.FillRandom('gaus')
h1.Draw()
import sys
colors = [kYellow,kBlue,kGreen,kRed,kBlack,kBlack,kViolet,kCyan,kCyan+5,kCyan-5]
for color in colors:
    h1.SetLineColor(TColor.GetColorDark(color))
    h1.Draw()
    c1.Update()
    print 'color=',color
    sys.stdout.flush() 
    raw_input('')
