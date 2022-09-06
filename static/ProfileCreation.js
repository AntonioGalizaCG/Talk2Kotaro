var b_pt = document.getElementById("ptbr");
var b_jp = document.getElementById("jap");
var b_eng = document.getElementById("eng");
var b_esp = document.getElementById("esp");

b_pt.onclick = function() {
	console.log("text");
	document.getElementById("title").innerHTML= "Criação do Perfil";
	document.getElementById('truth').innerHTML= 'Seus dados serão utilizados para fins de pesquisa científica, portanto escreva somente a verdade';
	
	document.getElementById('fnamel').innerHTML= 'ID de Login (use apenas caracteres alfanuméricos):';
	document.getElementById('lnamel').innerHTML= 'Senha (não use ;):';
	document.getElementById('lagel').innerHTML= 'Idade:';
	document.getElementById('lgl').innerHTML= 'Sexo:';
	document.getElementById('ldokol').innerHTML= 'País/Região de origem:';
	document.getElementById('lmlangl').innerHTML= 'Língua materna:';
	document.getElementById('lolangl').innerHTML= 'Outros idiomas que fala:';
	document.getElementById('labrl').innerHTML= 'Se vive/viveu no estrangeiro, escreva onde:';
	document.getElementById('ldrl').innerHTML= 'Anos vividos no exterior:';

	document.getElementById('submit').value = 'Criar';
	document.getElementById('instructions').innerHTML= 'Clique no botão "Criar" para criar seu perfil.';
};

b_jp.onclick = function() {
	document.getElementById('title').innerHTML= 'プロファイル作成';
	document.getElementById('truth').innerHTML= 'このデータは研究で使用されますから、偽らないでください。';
	
	document.getElementById('fnamel').innerHTML= 'ログイン ID (半角英字): ';
	document.getElementById('lnamel').innerHTML= 'パスワード(「;」を入れないでください):';
	document.getElementById('lagel').innerHTML= "年齢:";
	document.getElementById('lgl').innerHTML= '性別:';
	document.getElementById('ldokol').innerHTML= '母国:';
	document.getElementById('lmlangl').innerHTML= '母国語:';
	document.getElementById('lolangl').innerHTML= 'わかる他の言語:';
	document.getElementById('labrl').innerHTML= '海外に住んでいましたか？どちらに';
	document.getElementById('ldrl').innerHTML= '何年間海外にすんでいましたか';

	document.getElementById('submit').value = '送信';
	document.getElementById('instructions').innerHTML= '「送信」ボタンをクリックするとプロファイルを作成します。';
};
b_eng.onclick = function() {
	document.getElementById('title').innerHTML= 'Profile Creation';
	document.getElementById('truth').innerHTML= 'Your data will be used for scientific research, so please, be truthful.';
	
	document.getElementById('fnamel').innerHTML= 'Login ID (use alphanumeric characters only):';
	document.getElementById('lnamel').innerHTML= 'Password (do not use ;):';
	document.getElementById('lagel').innerHTML= 'Age:';
	document.getElementById('lgl').innerHTML= 'Gender:';
	document.getElementById('ldokol').innerHTML= 'Country/Region of Origin:';
	document.getElementById('lmlangl').innerHTML= 'Mother language:';
	document.getElementById('lolangl').innerHTML= 'Other languages you speak:';
	document.getElementById('labrl').innerHTML= 'If you live or have lived abroad, write where:';
	document.getElementById('ldrl').innerHTML= 'Years living abroad:';

	document.getElementById('submit').value = 'Submit';
	document.getElementById('instructions').innerHTML= 'Click on the "Submit" button to create your profile.';
};

b_esp.onclick = function() {
	document.getElementById('title').innerHTML= 'Creación del Perfil';
	document.getElementById('truth').innerHTML= 'Tus datos serán utilizados con fines de investigación científica. Por favor escriba solo la verdad. ';
	
	document.getElementById('fnamel').innerHTML= 'ID de Login (solo utilice caracteres alfanuméricos): ';
	document.getElementById('lnamel').innerHTML= 'Contraseña(no utilice ;):';
	document.getElementById('lagel').innerHTML= 'Edad:';
	document.getElementById('lgl').innerHTML= 'Género:';
	document.getElementById('ldokol').innerHTML= 'País/Región de origen:';
	document.getElementById('lmlangl').innerHTML= 'Lengua materna:';
	document.getElementById('lolangl').innerHTML= 'Otros idiomas que hablas:';
	document.getElementById('labrl').innerHTML= 'Si has vivido/vives en el extranjero, escribe dónde:';
	document.getElementById('ldrl').innerHTML= 'Años viviendo en el extranjero:';

	document.getElementById('submit').value = 'Crear';
	document.getElementById('instructions').innerHTML= 'Haz clic en el botón "Crear" para crear tu perfil.';
};
