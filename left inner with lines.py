from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas
from reportlab.lib.colors import magenta, red, black, blue, grey
import datetime
from datetime import timedelta

lWidth, lHeight = letter    
h = lWidth
w = lHeight


startdate = datetime.datetime(2018, 5,7)
#days to process#
cdays = 25

pages = int(cdays/2)

#  timedelta(days=1) + startdate = next day, etc etc



canvas = canvas.Canvas("LIWLMoleskinStyle.pdf", pagesize=letter)
canvas.setPageSize((lHeight, lWidth))
canvas.setLineWidth(.3)
canvas.setFont('Helvetica', 8)

Lineside=True
pad = 15
bindpad = 45

linecount = 35

page=0
for leday in range(0,cdays):
    canvas.setLineWidth(.3)
    canvas.setFont('Helvetica', 8)

    if Lineside == True:
        
        step = int(h/linecount)
        
        i=0
        for hour in range(0,linecount):
            i=i+1
            print(i)
            y = h -  i*step
            print(y)
            canvas.line(bindpad,y,w/2 ,y)
            
            
        bx = w/2+bindpad
        by = pad
        
        i=0
        for hour in range(0,linecount):
            i=i+1
            print(i)
            y = h -  i*step
            print(y)
            
            #canvas.setStrokeColor(blue)
    
            canvas.line(bx,y,w ,y)

        #cut line
        canvas.setStrokeColor(blue)
        canvas.line(w/2,1,w/2,h)
        canvas.setStrokeColor(black)
        canvas.showPage()
        
        Lineside = False
    else:
        leday=page

                
        day = startdate + timedelta(days=leday)
        day2 = startdate + timedelta(days=pages) + timedelta(days=leday)
    
        page=page+1
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
        canvas.line(w/2,1,w/2,h)
        
        canvas.showPage()
        Lineside = True

    
canvas.save()


