from django.shortcuts import render, HttpResponse
def index(request):
    return HttpResponse('''
    <!DOCTYPE html>
<html lang="en">
<head>
    <link rel="shortcut icon" type="image/png" href="https://cdn.discordapp.com/attachments/1022412472822542359/1022412572999290962/favicon.ico">
    <title>메인페이지</title>
    <style>
        body{
            background-color: gray;
        }
    </style>
</head>
<body>
    <!--메뉴-->
    <div style="background-color:aqua;">
        &nbsp;&nbsp;
        &nbsp;
    </div>
    <div style="height: 100px;
background-color: aqua;">
&nbsp;&nbsp;&nbsp;&nbsp;
    <a href="/"><img src="https://cdn.discordapp.com/attachments/1022412472822542359/1022412574014312499/7ec8b220e4172bdb.png" class="img" style="height: 70px;"></a>
    <a href="/cat"><img src="https://cdn.discordapp.com/attachments/1022412472822542359/1022412572789583923/cat.jpg" class="img" style="height: 70px;"></a>

    <a href="/random"><img src="https://cdn.discordapp.com/attachments/1022412472822542359/1022412573343240223/random.png" class="img" style="height: 70px;"></a>

</div>

    <h1>여기는 메인페이지입니다 위 메뉴를 이용해주세요</h1>
    <a href="https://discord.gg/YjtVZzTpfc" style="background-color: white;color: red;">디스코드서버 들어오기 hyhy(하이히)</a>
</body>
</html>
    ''')

def cat(request):
    return HttpResponse('''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="shortcut icon" href="https://cdn.discordapp.com/attachments/1022412472822542359/1022412572999290962/favicon.ico">
    <title>우리 고양희 보깅♡♥</title>
    <style>
        .img{
            height: 70px;
        }
        .aaa{
            height: 150px;
        }
        body{
            background-color: gray;
        }
    </style>
</head>
<body>
    <div style="background-color:aqua;">
        &nbsp;&nbsp;
        &nbsp;
    </div>
</div>
<div style="height: 100px;
background-color: aqua;">
&nbsp;&nbsp;&nbsp;&nbsp;
    <a href="/"><img src="https://cdn.discordapp.com/attachments/1022412472822542359/1022412574014312499/7ec8b220e4172bdb.png" class="img" style="height: 70px;"></a>
    <a href="/cat"><img src="https://cdn.discordapp.com/attachments/1022412472822542359/1022412572789583923/cat.jpg" class="img" style="height: 70px;"></a>

    <a href="/random"><img src="https://cdn.discordapp.com/attachments/1022412472822542359/1022412573343240223/random.png" class="img" style="height: 70px;"></a>

</div>
    <img class="aaa" src="https://cdn.discordapp.com/attachments/1022412472822542359/1022412574509248553/1.jpg" alt="">
    <img class="aaa" src="https://cdn.discordapp.com/attachments/1022412472822542359/1022412574882533446/2.jpg" alt="">
    <img class="aaa" src="https://cdn.discordapp.com/attachments/1022412472822542359/1022412575369076798/3.jpg" alt="">
    <img class="aaa" src="https://cdn.discordapp.com/attachments/1022412472822542359/1022412572416299048/4.jpg" alt="">
</body>
</html>
    ''')
def random(request):
    return HttpResponse('''
    <!DOCTYPE html>
<html lang="en">
<head>
    <title>랜덤숫자뽑기</title>
    <link rel="shortcut icon" type="image/png" href="https://cdn.discordapp.com/attachments/1022412472822542359/1022412572999290962/favicon.ico">
    <style>
        .img{
            height: 70px;
        }
        body{
            background-color: gray;
        }
    </style>
</head>
<body>
    <!--메뉴-->
    <div style="background-color:aqua;">
        &nbsp;&nbsp;
        &nbsp;
    </div>
</div>
<div style="height: 100px;
background-color: aqua;">
&nbsp;&nbsp;&nbsp;&nbsp;
    <a href="/"><img src="https://cdn.discordapp.com/attachments/1022412472822542359/1022412574014312499/7ec8b220e4172bdb.png" class="img" style="height: 70px;"></a>
    <a href="/cat"><img src="https://cdn.discordapp.com/attachments/1022412472822542359/1022412572789583923/cat.jpg" class="img" style="height: 70px;"></a>

    <a href="/random"><img src="https://cdn.discordapp.com/attachments/1022412472822542359/1022412573343240223/random.png" class="img" style="height: 70px;"></a>

</div>
	<h1 ID="aaa">랜덤 숫자뽑기</h1>
	<a href="1/"><img src="https://cdn.discordapp.com/attachments/955055398908473357/1003827484460060693/207_20220801201115.png" alt="1"></a>
	<div><a href="10/"><img src="https://cdn.discordapp.com/attachments/955055398908473357/1003827484200026192/207_20220801201132.png" alt="2"></a></div>
	<div><a href="100/"><img src="https://cdn.discordapp.com/attachments/955055398908473357/1003827483881250919/207_20220801201140.png" alt="3"></a></div>
</body>
</html>
    ''')
def one(request):
    return HttpResponse('''
        <!DOCTYPE html>
<html lang="ko">
<head>
    <title>무작위 숫자 뽑기</title>
    <link rel="shortcut icon" type="image/png" href="https://cdn.discordapp.com/attachments/1022412472822542359/1022412572999290962/favicon.ico">
    <script>
        var aaa=Math.floor(Math.random() * 10);
        var bbb=aaa
        document.write(String(aaa).fontsize(30)+"<br><br>"); 
    </script>
    <style>
        body{
            background-color: gray;
        }
        #ggg{
            font-size:100px;
        }
    </style>
</head>
<body>
    <input type="button" id="btn_1" value="다시하기" onclick="location.reload()">
    <div><a href="../" id="btn"><img src="https://cdn.discordapp.com/attachments/955055398908473357/1003827484816584814/206_20220801201019.png" alt=""></a></div>
</body>
</html>
    ''')
def than(request):
    return HttpResponse('''
    <!DOCTYPE html>
<html lang="ko">
<head>
    <title>무작위 숫자 뽑기</title>
    <link rel="shortcut icon" type="image/png" href="https://cdn.discordapp.com/attachments/1022412472822542359/1022412572999290962/favicon.ico">
    <script>
        var aaa=Math.floor(Math.random() * 100);
        var bbb=aaa
        document.write(String(aaa).fontsize(30)+"<br><br>"); 
    </script>
    <style>
        body{
            background-color: gray;
        }
        #ggg{
            font-size:100px;
        }
    </style>
</head>
<body>
    <input type="button" id="btn_1" value="다시하기" onclick="location.reload()">
    <div><a href="../" id="btn"><img src="https://cdn.discordapp.com/attachments/955055398908473357/1003827484816584814/206_20220801201019.png" alt=""></a></div>
</body>
</html>
    ''')
def Hundred(request):
    return HttpResponse("""
     <!DOCTYPE html>
<html lang="ko">
<head>
    <title>무작위 숫자 뽑기</title>
    <link rel="shortcut icon" type="image/png" href="https://cdn.discordapp.com/attachments/1022412472822542359/1022412572999290962/favicon.ico">
    <script>
        var aaa=Math.floor(Math.random() * 1000);
        var bbb=aaa
        document.write(String(aaa).fontsize(30)+"<br><br>"); 
    </script>
    <style>
        body{
            background-color: gray;
        }
        #ggg{
            font-size:100px;
        }
    </style>
</head>
<body>
    <input type="button" id="btn_1" value="다시하기" onclick="location.reload()">
    <div><a href="../" id="btn"><img src="https://cdn.discordapp.com/attachments/955055398908473357/1003827484816584814/206_20220801201019.png" alt=""></a></div>
</body>
</html>
    """)