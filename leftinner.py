from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas
from reportlab.lib.colors import magenta, red, black, blue, grey
import datetime
from datetime import timedelta

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

importantdates =[]
importantdates.append([[4,29], "Gabe's Birthday!"])
importantdates.append([[4,13], "Cat's Birthday!"])




lWidth, lHeight = letter    
h = lWidth
w = lHeight


startdate = datetime.datetime(2018, 5,7)
#days to process#
cdays = 365



pages = int(cdays/2)



pdfmetrics.registerFont(TTFont("Merp", "16304_GARA.ttf"))

canvas = canvas.Canvas("LIMoleskinStyle.pdf", pagesize=letter)
canvas.setPageSize((lHeight, lWidth))


Lineside=True
pad = 15
bindpad = 45

linecount = 35

page=0
for leday in range(0,pages):
    canvas.setLineWidth(.3)
    canvas.setFont('Merp', 8)


            
    day = startdate + timedelta(days=leday)
    day2 = startdate + timedelta(days=pages) + timedelta(days=leday)
    day1notes = ''
    day2notes = ''
    for iday in importantdates:
        
        idate = datetime.datetime(day.year, iday[0][0], iday[0][1])
        idate2 = datetime.datetime(day2.year, iday[0][0], iday[0][1])
        print(idate, idate2)
        if idate == day:
            #first side has important day add to list
            day1notes = day1notes + iday[1] + "\n"
        if idate2 == day2:
            #Second side has important day add to list
            day2notes = day2notes + iday[1] + "\n"

    bx = pad
    by = pad
    
    tx = w/2 - (bindpad+pad)
    ty = h - pad*2
    
    print("Bottom x,y =%s,%s" %(bx, by))
    print("Top x,y =%s,%s" %(tx, ty))
    
    canvas.roundRect(bx, by, tx, ty, 9, stroke=1, fill=0)
    
    
    ts = day.strftime("%A %B %d, %Y")
    print(ts)
    
    canvas.drawString(bx+10,ty ,ts)
    #canvas.setFillColor(black)
    
    #ADD LINES
    hours = ['8','9','10','11','12','1','2','3','4','5',]
    i=0
    for hour in hours:
        i=i+1
        print(i)
        y = h - pad - i*50
        print(y)
        canvas.line(bx,y,w/2 -bindpad ,y)
        #canvas.setFillColor(grey)

        canvas.drawString(bx+5,y+5,hour)
       # canvas.setFillColor(black)

    t = canvas.beginText()
    t.setFont('Merp', 8)
    #t.setCharSpace(3)
    t.setTextOrigin(bindpad+10,by+70 )
    t.textLines(day1notes)
    canvas.drawText(t)    
    
    
    #right side
    
    bx = w/2+pad
    by = pad
    
    tx = w/2 -  (bindpad+pad)
    ty = h - pad*2
    
    canvas.roundRect(bx, by, tx, ty , 4, stroke=1, fill=0)
    
    ts = day2.strftime("%A %B %d %Y")
    print(ts)
    canvas.drawString(bx+10,ty ,ts)
    
    i=0
    for hour in hours:
        i=i+1
        print(i)
        y = h - pad - i*50
        print(y)
        
        #canvas.setStrokeColor(blue)

        canvas.line(bx,y,w-bindpad ,y)
        #canvas.setFillColor(grey)

        canvas.drawString(bx+5,y+5,hour)
        #canvas.setFillColor(black)
    #cut line
  #  canvas.line(w/2,1,w/2,h)
    
    t = canvas.beginText()
    t.setFont('Merp', 8)
    #t.setCharSpace(3)
    t.setTextOrigin(w/2+bindpad+10,by+70 )
    
    t.textLines(day2notes)
    canvas.drawText(t)    

    canvas.showPage()

    
canvas.save()


