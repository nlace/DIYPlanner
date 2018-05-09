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
cdays = 350

pages = int(cdays/2)

#  timedelta(days=1) + startdate = next day, etc etc



canvas = canvas.Canvas("output2.pdf", pagesize=letter)
canvas.setPageSize((lHeight, lWidth))

side="A"
for leday in range(0,pages):
    canvas.setLineWidth(.3)
    canvas.setFont('Helvetica', 8)
    pad = 15
    bindpad = 45
    
    if side == 'A':
    
        day = startdate + timedelta(days=leday)
        day2 = startdate + timedelta(days=pages) + timedelta(days=leday)
        side = 'B'
        
    else:
        day2 = startdate + timedelta(days=leday)
        day = startdate + timedelta(days=pages) + timedelta(days=leday)
        side = 'A'
        
            
#    day = startdate + timedelta(days=leday)
#    day2 = startdate + timedelta(days=pages) + timedelta(days=leday)

    bx = bindpad
    by = pad
    
    tx = w/2 - (bindpad+pad)
    ty = h - pad*2
    
    print("Bottom x,y =%s,%s" %(bx, by))
    print("Top x,y =%s,%s" %(tx, ty))
    
    canvas.roundRect(bx, by, tx, ty, 9, stroke=1, fill=0)
    
    
    ts = day.strftime("%A %B %d, %Y")
    print(ts)
    
    canvas.drawString(bindpad+10,ty ,ts)
    #canvas.setFillColor(black)
    
    #ADD LINES
    hours = ['8','9','10','11','12','1','2','3','4','5',]
    i=0
    for hour in hours:
        i=i+1
        print(i)
        y = h - pad - i*50
        print(y)
        canvas.line(bx,y,w/2 -pad ,y)
        canvas.setFillColor(grey)

        canvas.drawString(bx+5,y+5,hour)
        canvas.setFillColor(black)

    
    #right side
    
    bx = w/2+bindpad
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

        canvas.line(bx,y,w-pad ,y)
        canvas.setFillColor(grey)

        canvas.drawString(bx+5,y+5,hour)
        canvas.setFillColor(black)
    #cut line
    canvas.line(w/2,1,w/2,h)
    
    canvas.showPage()
    
canvas.save()


