var b_pt = document.getElementById("ptbr");
var b_jp = document.getElementById("jap");
var b_eng = document.getElementById("eng");
var b_esp = document.getElementById("esp");

b_pt.onclick = function() {
	document.getElementById("Title").innerHTML = "Instruções do Experimento";
	document.getElementById('exp').value = "Instruções do Experimento\n\n"+
"1. É preciso de uma webcam para participar;\n"+
"2. Realize o experimento em um local bem iluminado;\n"+
"3. Digite seu ID de login, senha e as demais informações pessoais para criar seu perfil;\n"+
"Da segunda vez em diante, faça o login com o ID de login e a senha que você criou;\n"+
"4. Quando estiver pronto para falar, clique no botão Falar;\n"+
"5. Quando terminar de falar, clique no botão novamente;\n"+
"6. O avatar falará, então ouça e reaja naturalmente;\n"+
"7. Você pode repetir as etapas 4 a 6 quantas vezes quiser, mas, por favor, não feche a página antes do avatar terminar de falar;\n"+
"8. Ao fazer o logout, se tiver tempo, preencha uma pesquisa de 10 itens;\n"+
"9. Se você deseja excluir todos os dados coletados, clique no botão ''Excluir dados'' a qualquer momento.\n"+
"Clique no botão ''OK'' para confirmar.\n\n";
	document.getElementById('go').innerText= "Retornar ao Experimento";
};

b_jp.onclick = function() {
	document.getElementById("Title").innerHTML = "実験説明書＆同意書";
	document.getElementById('exp').value = "実験方法\n\n"+
"1.参加するにはウェブカメラが必要です;\n"+
"2.実験は明るい場所で行ってください;\n"+
"3.ログインID、パスワードなどを入力し、プロフィールを作成します;\n"+
"2回目以降は、作成したログインIDとパスワードでログインしてください;\n"+
"4.話す準備ができたら、[トーク]ボタンをクリックします。\n"+
"5.話し終わったら、もう一度ボタンをクリックします。\n"+
"6.アバターが話すので、自然に耳を傾け、反応する\n"+
"7.4～6の手順は何度でも繰り返せますが、アバターが話すのをやめる前にページを閉じないでください; \n" +
"8.ログアウトする時間があれば、10項目のアンケートにご協力ください;\n"+
"9.収集したデータをすべて削除したい場合は、いつでも''データ削除''ボタンをクリックしてください;\n"+
"クリックし、''OK''ボタンをクリックして確定してください\n\n";
	document.getElementById('go').innerText = "実験戻る";
};
b_eng.onclick = function() {
	document.getElementById("Title").innerHTML = "Experiment Instructions";
	document.getElementById('exp').value = "Experiment Instructions\n\n"+
	"1. You need a webcam to participate;\n"+
	"2. Perform the experiment in a well-lit place;\n"+
	"3. Enter your login ID, password and more to create your profile.\n"+
	"From the second time onward, please log in with the login ID and *password you created;\n"+
	"4. When you are ready to speak, click the Talk button (green button with the drawing of an ear);\n"+
	"5. When you're done talking, click the button again (it will have become blue with the drawing of a speech bubble);\n"+
	"6. The avatar will speak, so listen and react naturally;\n"+
	"7. You can repeat steps 4-6 as often as you like, but please, do not close the page before the avatar stops speaking;\n"+
	"8. If you have time to log out, please complete a 10-item survey.\n"+
	"9. If you want to delete all the collected data, click the ''Delete data'' button at any time.\n";
	document.getElementById('go').innerText = 'Return to Experiment';
};

b_esp.onclick = function() {
	document.getElementById("Title").innerHTML = "Instrucciones del Experimento";
	document.getElementById('exp').value = "Instrucciones del Experimento\n\n"+
	"1. Debe tener una cámara web para participar;\n"+
	"2. Debe realizar el experimento en un lugar bien iluminado;\n"+
	"3. Escoge tu ID de inicio de sesión, contraseña y otra información personal para crear tu perfil.\n"+
	"A partir de la segunda vez, inicie sesión con el ID de inicio de sesión y la contraseña que creó;\n"+
	"4. Cuando esté listo para hablar, haz clic en el botón Hablar(botón verde con el diseño de una oreja);\n"+
	"5. Cuando termine de hablar, vuelva a hacer clic en el botón(se habrá vuelto azul con un dibujo de globo de diálogo);\n"+
	"6. El avatar hablará, así que escuche y reaccione con naturalidad;\n"+
	"7. Puede repetir los pasos 4 a 6 tantas veces como desee, pero no cierre la página antes de que el avatar haya terminado de hablar;\n"+
	"8. Al cerrar la sesión, si tiene tiempo, complete una encuesta de 10 elementos.\n"+
	"9. Si desea eliminar todos los datos recopilados, haga clic en el botón ''Eliminar datos'' en cualquier momento.\n"+
	"Haz clic en el botón ''Aceptar'' para confirmar la eliminación.\n";
	document.getElementById('go').innerText = "Volver al experimento";
};
