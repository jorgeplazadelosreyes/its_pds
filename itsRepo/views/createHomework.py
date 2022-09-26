from django.shortcuts import render, redirect
from django.views import View

from itsRepo.models import Homework

dataJSON = """{"attrs":{"width":1890,"height":2000},"className":"Stage","children":[{"attrs":{},"className":"Layer","children":[{"attrs":{"points":[0.5,0,0.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[30.5,0,30.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[60.5,0,60.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[90.5,0,90.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[120.5,0,120.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[150.5,0,150.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[180.5,0,180.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[210.5,0,210.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[240.5,0,240.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[270.5,0,270.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[300.5,0,300.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[330.5,0,330.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[360.5,0,360.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[390.5,0,390.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[420.5,0,420.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[450.5,0,450.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[480.5,0,480.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[510.5,0,510.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[540.5,0,540.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[570.5,0,570.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[600.5,0,600.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[630.5,0,630.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[660.5,0,660.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[690.5,0,690.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[720.5,0,720.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[750.5,0,750.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[780.5,0,780.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[810.5,0,810.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[840.5,0,840.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[870.5,0,870.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[900.5,0,900.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[930.5,0,930.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[960.5,0,960.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[990.5,0,990.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[1020.5,0,1020.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[1050.5,0,1050.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[1080.5,0,1080.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[1110.5,0,1110.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[1140.5,0,1140.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[1170.5,0,1170.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[1200.5,0,1200.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[1230.5,0,1230.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[1260.5,0,1260.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[1290.5,0,1290.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[1320.5,0,1320.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[1350.5,0,1350.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[1380.5,0,1380.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[1410.5,0,1410.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[1440.5,0,1440.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[1470.5,0,1470.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[1500.5,0,1500.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[1530.5,0,1530.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[1560.5,0,1560.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[1590.5,0,1590.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[1620.5,0,1620.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[1650.5,0,1650.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[1680.5,0,1680.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[1710.5,0,1710.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[1740.5,0,1740.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[1770.5,0,1770.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[1800.5,0,1800.5,729],"stroke":"#000000","strokeWidth":1},"className":"Line"},{"attrs":{"points":[0,0,10,10]},"className":"Line"},{"attrs":{"points":[0,0,1805,0],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,30,1805,30],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,60,1805,60],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,90,1805,90],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,120,1805,120],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,150,1805,150],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,180,1805,180],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,210,1805,210],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,240,1805,240],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,270,1805,270],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,300,1805,300],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,330,1805,330],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,360,1805,360],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,390,1805,390],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,420,1805,420],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,450,1805,450],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,480,1805,480],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,510,1805,510],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,540,1805,540],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,570,1805,570],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,600,1805,600],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,630,1805,630],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,660,1805,660],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,690,1805,690],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,720,1805,720],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,750,1805,750],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,780,1805,780],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,810,1805,810],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,840,1805,840],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,870,1805,870],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,900,1805,900],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,930,1805,930],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,960,1805,960],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,990,1805,990],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,1020,1805,1020],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,1050,1805,1050],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,1080,1805,1080],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,1110,1805,1110],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,1140,1805,1140],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,1170,1805,1170],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,1200,1805,1200],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,1230,1805,1230],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,1260,1805,1260],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,1290,1805,1290],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,1320,1805,1320],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,1350,1805,1350],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,1380,1805,1380],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,1410,1805,1410],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,1440,1805,1440],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,1470,1805,1470],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,1500,1805,1500],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,1530,1805,1530],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,1560,1805,1560],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,1590,1805,1590],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,1620,1805,1620],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,1650,1805,1650],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,1680,1805,1680],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,1710,1805,1710],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,1740,1805,1740],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,1770,1805,1770],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,1800,1805,1800],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,1830,1805,1830],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"points":[0,1860,1805,1860],"stroke":"#000000","strokeWidth":0.5},"className":"Line"},{"attrs":{"x":30,"y":30},"className":"Group","children":[{"attrs":{"width":30,"height":30,"fill":"gray","stroke":"black","strokeWidth":4},"className":"Rect"},{"attrs":{"x":5,"y":35,"text":"1 mt","fontSize":10,"fontFamily":"Calibri","fill":"black"},"className":"Text"},{"attrs":{"x":35,"y":5,"text":"1 mt","fontSize":10,"fontFamily":"Calibri","fill":"black"},"className":"Text"}]},{"attrs":{"width":30,"height":30,"fill":"#FF7B17","opacity":0.6,"stroke":"#CF6412","strokeWidth":3,"dash":[20,2],"visible":false},"className":"Rect"},{"attrs":{"points":[1805,0,1805,600],"stroke":"red","strokeWidth":4,"lineCap":"round","lineJoin":"round"},"className":"Line"},{"attrs":{"x":1838,"y":65,"text":"Fuerza","fontFamily":"Calibri","fill":"balck"},"className":"Text"},{"attrs":{"x":1847,"y":125,"text":"Fijo","fontFamily":"Calibri","fill":"balck"},"className":"Text"},{"attrs":{"x":1830,"y":185,"text":"Deslizante","fontFamily":"Calibri","fill":"balck"},"className":"Text"},{"attrs":{"x":1810,"y":245,"text":"Empotramiento","fontFamily":"Calibri","fill":"balck"},"className":"Text"},{"attrs":{"x":1840,"y":305,"text":"Rotula","fontFamily":"Calibri","fill":"balck"},"className":"Text"},{"attrs":{"x":1845,"y":365,"text":"Biela","fontFamily":"Calibri","fill":"balck"},"className":"Text"},{"attrs":{"x":1835,"y":420,"text":"Momento","fontFamily":"Calibri","fill":"balck"},"className":"Text"},{"attrs":{"x":1852.5,"y":35,"points":[0,0,20,10],"pointerLength":2,"pointerWidth":2,"rotation":62,"fill":"black","stroke":"black","strokeWidth":4,"shadowColor":"black","shadowBlur":2,"shadowOffsetX":1,"shadowOffsetY":1,"shadowOpacity":0.4},"className":"Arrow"},{"attrs":{"x":1855,"y":110,"sides":3,"radius":15,"fill":"gray","stroke":"black"},"className":"RegularPolygon"},{"attrs":{"x":1840,"y":180},"className":"Group","children":[{"attrs":{"x":15,"y":-10,"sides":3,"radius":15,"fill":"gray","stroke":"black"},"className":"RegularPolygon"},{"attrs":{"points":[0,0,30,0],"stroke":"red","strokeWidth":4,"lineCap":"round","lineJoin":"round"},"className":"Line"}]},{"attrs":{"x":1840,"y":240},"className":"Group","children":[{"attrs":{"points":[15,0,15,-25],"stroke":"red","strokeWidth":4,"lineCap":"round","lineJoin":"round"},"className":"Line"},{"attrs":{"points":[0,0,30,0],"stroke":"red","strokeWidth":4,"lineCap":"round","lineJoin":"round"},"className":"Line"}]},{"attrs":{"x":1855,"y":285,"radius":7.5,"fill":"red","stroke":"black"},"className":"Circle"},{"attrs":{"x":1855,"y":345,"radius":7.5,"fill":"green","stroke":"black"},"className":"Circle"},{"attrs":{"x":1857,"y":390,"innerRadius":10,"outerRadius":20,"angle":180,"fill":"yellow","stroke":"black","strokeWidth":4,"shadowColor":"black","shadowBlur":2,"shadowOffsetX":1,"shadowOffsetY":1,"shadowOpacity":0.4},"className":"Arc"}]}]}"""


class CreateHomework(View):

    def get(self, request):
        homeworks = Homework.objects.all()
        if request.user.student.role == 0:
            return redirect("student_home")
        context = {
            "json": dataJSON,
            "homeworks": homeworks
        }
        return render(request, "create_homework.html", context)

    def post(self, request):
        if request.POST.get("json"):
            data = request.POST.get("json")
            new_homework = Homework(diagram = data)
            new_homework.save()
            return redirect("edit_diagram", homework_id=new_homework.id)

