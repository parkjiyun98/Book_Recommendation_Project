from django.shortcuts import render
from .models import CategoryOne
from .models import CategoryTwo
from .models import CategoryThree
from .models import CategoryFour
from .models import CategoryFive
from .models import CategorySix
from .models import CategorySeven
from .models import CategoryEight
from .models import CategoryNine
from .models import CategoryTen
from .models import CategoryEleven
from .models import CategoryTwelve
from .models import CategoryThirteen
from .models import CategoryFourteen
from .models import CategoryFifteen
from .models import CategorySixteen
from .models import CategorySeventeen
from .models import CategoryEighteen
from .models import CategoryNineteen
from .models import CategoryTwenty
from .models import CategoryTwentyone
from .models import CategoryTwentytwo
from .models import CategoryTwentythree
from .models import CategoryTwentyfour

# Create your views here.
def index(request):
    ones = CategoryOne.objects.get(id=0)
    twos = CategoryTwo.objects.get(id=0)
    threes = CategoryThree.objects.get(id=0)
    fours = CategoryFour.objects.get(id=0)
    fives = CategoryFive.objects.get(id=0)
    sixs = CategorySix.objects.get(id=0)
    sevens = CategorySeven.objects.get(id=0)
    eights = CategoryEight.objects.get(id=0)
    nines = CategoryNine.objects.get(id=0)
    tens = CategoryTen.objects.get(id=0)
    elevens = CategoryEleven.objects.get(id=0)
    twelves = CategoryTwelve.objects.get(id=0)
    thirteens = CategoryThirteen.objects.get(id=0)
    fourteens = CategoryFourteen.objects.get(id=0)
    fifteens = CategoryFifteen.objects.get(id=0)
    sixteens = CategorySixteen.objects.get(id=0)
    seventeens = CategorySeventeen.objects.get(id=0)
    eighteens = CategoryEighteen.objects.get(id=0)
    nineteens = CategoryNineteen.objects.get(id=0)
    twentys = CategoryTwenty.objects.get(id=0)
    twentyones = CategoryTwentyone.objects.get(id=0)
    twentytwos = CategoryTwentytwo.objects.get(id=0)
    twentythrees = CategoryTwentythree.objects.get(id=0)
    twentyfours = CategoryTwentyfour.objects.get(id=0)
    return render(request, 'category/index2.html', {'ones': ones, 'twos': twos, 'threes': threes, 'fours': fours, 'fives': fives, 'sixs': sixs, 'sevens': sevens, 'eights': eights, 'nines': nines, 'tens': tens, 'elevens': elevens, 'twelves': twelves, 'thirteens': thirteens, 'fourteens': fourteens, 'fifteens': fifteens, 'sixteens': sixteens, 'seventeens': seventeens, 'eighteens': eighteens, 'nineteens': nineteens, 'twentys': twentys, 'twentyones': twentyones, 'twentytwos': twentytwos, 'twentythrees': twentythrees, 'twentyfours': twentyfours})


def one(request):
    homes = CategoryOne.objects
    return render(request, 'category/category.html', {'home': homes})


def two(request):
    healths = CategoryTwo.objects
    return render(request, 'category/category2.html', {'health': healths})

def three(request):
    economys = CategoryThree.objects
    return render(request, 'category/category3.html', {'economy': economys})

def four(request):
    koreans = CategoryFour.objects
    return render(request, 'category/category4.html', {'korean': koreans})

def five(request):
    univs = CategoryFive.objects
    return render(request, 'category/category5.html', {'univ': univs})

def six(request):
    societys = CategorySix.objects
    return render(request, 'category/category6.html', {'society': societys})

def seven(request):
    novels = CategorySeven.objects
    return render(request, 'category/category7.html', {'novel': novels})

def eight(request):
    tests = CategoryEight.objects
    return render(request, 'category/category8.html', {'test': tests})

def nine(request):
    childs = CategoryNine.objects
    return render(request, 'category/category9.html', {'child': childs})

def ten(request):
    essays = CategoryTen.objects
    return render(request, 'category/category10.html', {'essay': essays})

def eleven(request):
    travels = CategoryEleven.objects
    return render(request, 'category/category11.html', {'travel': travels})

def twelve(request):
    historys = CategoryTwelve.objects
    return render(request, 'category/category12.html', {'history': historys})

def thirteen(request):
    arts = CategoryThirteen.objects
    return render(request, 'category/category13.html', {'art': arts})

def fourteen(request):
    babys = CategoryFourteen.objects
    return render(request, 'category/category14.html', {'baby': babys})

def fifteen(request):
    humans = CategoryFifteen.objects
    return render(request, 'category/category15.html', {'human': humans})

def sixteen(request):
    characters = CategorySixteen.objects
    return render(request, 'category/category16.html', {'character': characters})

def seventeen(request):
    selfs = CategorySeventeen.objects
    return render(request, 'category/category17.html', {'self': selfs})

def eighteen(request):
    natures = CategoryEighteen.objects
    return render(request, 'category/category18.html', {'nature': natures})

def nineteen(request):
    magazines = CategoryNineteen.objects
    return render(request, 'category/category19.html', {'magazine': magazines})

def twenty(request):
    religions = CategoryTwenty.objects
    return render(request, 'category/category20.html', {'religion': religions})

def twentyone(request):
    youths = CategoryTwentyone.objects
    return render(request, 'category/category21.html', {'youth': youths})

def twentytwo(request):
    mobiles = CategoryTwentytwo.objects
    return render(request, 'category/category22.html', {'mobile': mobiles})

def twentythree(request):
    elementarys = CategoryTwentythree.objects
    return render(request, 'category/category23.html', {'elementary': elementarys})

def twentyfour(request):
    middles = CategoryTwentyfour.objects
    return render(request, 'category/category24.html', {'middle': middles})