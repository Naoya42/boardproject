from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import BoardModel, MyProfileModel
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DetailView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
#functionの場合どのobjectを使用するか指定しなければならない
def signupfunc(request):
	#通信がPOSTかどうかの判断
	if request.method == 'POST':
		#POSTで送られてきた名前とパスを変数に格納
		username2 = request.POST['username']
		password2 = request.POST['password']
		#エラーの可能性がある場合に書く処理
		#renderはrequestをどこに、どんなデータで返すのか指定できる
		try:
			User.objects.get(username=username2)#一致するか判定
			return render(request, 'signup.html', {'error':'このユーザーは登録されています'})
		except:
			user = User.objects.create_user(username2, '', password2)
			return render(request, 'signup.html', {'true':'ユーザーの作成に成功しました'})
	return render(request, 'signup.html', {'some':100})
	#上記のsomeは直接データを書いてもいいし、modelsからデータをよみ込んでくることも可能
def loginfunc(request):
		if request.method == 'POST':
			username2 = request.POST['username']
			password2 = request.POST['password']
			#ログインのためにPOSTで受け取ったusernameとpasswordをauthenticateで認証を行う
			user = authenticate(request, username=username2, password=password2)
			if user is not None:#ユーザがいる場合login
				login(request, user)
				return redirect('list')
			else:
				return redirect('login')
		return render(request, 'login.html')
@login_required#loginしているかチェックするデコレーター
def listfunc(request):
	object_list = BoardModel.objects.all()
	return render(request, 'list.html', {'object_list':object_list})

def logoutfunc(request):
	logout(request)
	return redirect('login')

def detailfunc(request, pk):#指定の投稿を開くための関数。pkは必要
	object = BoardModel.objects.get(pk=pk)
	return render(request, 'detail.html', {'object':object})

def goodfunc(request, pk):#指定の投稿のいいね数を増やすためpkが必要
	likecount = BoardModel.objects.get(pk=pk)#変数にmodelからpkをとってきて格納
	likecount.good = likecount.good + 1#変数のgood属性の数値を+1
	likecount.save()#保存してmodelにデータの値を更新
	return redirect('list')#urlsでlistと命名したページに戻る

def readfunc(request, pk):
	readcount = BoardModel.objects.get(pk=pk)
	loginuser = request.user.get_username()#現在ログインしているユーザーの情報を片酢に入れる
	if loginuser in readcount.readtext:#既読者一覧にユーザーがいないか
		return redirect('list')#いた場合listページに飛ばす
	else:#いない場合
		readcount.read += 1 #既読の数値を追加
		readcount.readtext = readcount.readtext + '' + loginuser
		#readtext（既読者一覧）にユーザー名を追加
		readcount.save()
		return redirect('list')

class BoardCreate(CreateView):
#BoardCreateクラスを定義（CreateViewを継承）
	template_name = 'create.html'#呼び出すhtmlファイルを指定
	model = BoardModel#modelsファイルからデータの取り出し
	fields = ('title', 'content', 'author', 'images')#classで取り扱うデータを指定
	success_url = reverse_lazy('list')#作成完了後どのページに遷移するか決める


def commentfunc(request, pk):
	if request.method == 'POST':#method判定
		com = BoardModel.objects.get(pk=pk)#コメントを記入する投稿のデータ取得
		Newcom = request.POST['commentuser']
		Newcom = Newcom + ':' + request.POST['Newcomment']#ユーザーに入力してもらったコメントを変数に
		com.comment = com.comment + '\n' + Newcom#後でコメントを枠で分ける
		com.save()
		return redirect('list')
	else:
		object = BoardModel.objects.get(pk=pk)
	return render(request, 'comment.html', {'object':object})

class FirstSet(CreateView):#マイページ初回登録
	template_name = 'firstset.html'
	model = MyProfileModel
	fields = ('age','hobby','occupation','Residence', 'myimages','author')
	success_url = reverse_lazy('list')

class OnlyYouMixin(UserPassesTestMixin):#マイページのユーザー認証
    raise_exception = True

    def test_func(self):
        # 今ログインしてるユーザーのpkと、そのユーザー情報ページのpkが同じか、又はスーパーユーザーなら許可
        user = self.request.user
        return user.pk == self.kwargs['pk']

class DetailProfile(OnlyYouMixin, DetailView):
	model = MyProfileModel
	template_name = 'myprofile.html'
	fields = ('age','hobby','occupation','Residence', 'myimages','author')

class UpdateProfile(OnlyYouMixin, UpdateView):
	model = MyProfileModel
	template_name = 'myprofile.html'
	fields = ('age','hobby','occupation','Residence', 'myimages','author')
	success_url = reverse_lazy('list')


def myprofilefunc(request):#初回か表示か判別
	plofdate = MyProfileModel.objects.all()#全てのプロフ情報をとってくる
	loginuser = request.user.get_username()#現在ログインしているユーザーの情報
	if loginuser in plofdate.listofcreators:#プロフ作成者一覧に名前があるか判定
		return redirect('DetailProfile')#あるのであれば、表示するクラスへ	
	else:#なければ追加して新規作成classへ
		plofdate.listofcreators = plofdate.listofcreators + ' ' + loginuser
		return redirect('firstset')