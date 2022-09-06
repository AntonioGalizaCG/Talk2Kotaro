var b_pt = document.getElementById("ptbr");
var b_jp = document.getElementById("jap");
var b_eng = document.getElementById("eng");
var b_esp = document.getElementById("esp");

b_pt.onclick = function() {
	document.getElementById('go').value = "Enviar";
	document.getElementById("expLik").innerHTML = 'Se você tiver tempo para nos ajudar ainda mais, por favor responda a este questionário.';
	document.getElementById("q1").innerHTML = 'Conversar com o avatar foi interessante. ';
	document.getElementById("q2").innerHTML = 'Variações nas características da fala do avatar fizeram a conversa soar mais natural.';
	document.getElementById("q3").innerHTML = 'Algumas falas aleatoriamente geradas soaram menos interessantes que outras.';
	document.getElementById("q4").innerHTML = 'Algumas características da fala, tais como velocidade, volume ou tom influenciaram a aprazibilidade da fala mais que outras. ';
	document.getElementById("q5").innerHTML = 'Diferentes palavras aleatórias não impactaram a qualidade da conversa.';
	document.getElementById("q6").innerHTML = 'Você sentiu que o robô respondia a suas falas adequadamente.';
	document.getElementById("q7").innerHTML = 'Frases mais longas foram as mais interessantes.';
	document.getElementById("q8").innerHTML = 'A conversa em turnos não pareceu natural.';
	document.getElementById("q9").innerHTML = 'Fonemas que soam estrangeiros pareceram mais interessantes.';
	document.getElementById("q10").innerHTML = 'O robô parece ser inteligente.';
};

b_jp.onclick = function() {
	document.getElementById('go').value = "出す";
	document.getElementById("expLik").innerHTML = 'お時間のある方は、ぜひこのアンケートにご協力ください。';
	document.getElementById("q1").innerHTML = 'ロボットのアバターと話すのは面白かった。';
	document.getElementById("q2").innerHTML = '言葉の特徴の変化は会話をより自然なものにした。';
	document.getElementById("q3").innerHTML = 'ランダムに生成された単語の中には、他の単語より気持ちが悪いものもあります。';
	document.getElementById("q4").innerHTML = 'スピード、ラウドネス、ピッチなど、一部の音声特性は他のものよりも影響を与えます。';
	document.getElementById("q5").innerHTML = 'いろいろな言葉が喜びに影響を与えなかった';
	document.getElementById("q6").innerHTML = 'あなたは、ロボットがそれに応じてスピーチに答えているのを感じました。';
	document.getElementById("q7").innerHTML = '長い言い回しのほうがもっとおもしろい。';
	document.getElementById("q8").innerHTML = 'ターンベースの会話は不自然だった。';
	document.getElementById("q9").innerHTML = '外国の音素はもっとおもしろいように思えた。';
	document.getElementById("q10").innerHTML = '.そのロボットは知的に見えた。';
};
b_eng.onclick = function() {
	document.getElementById('go').value = 'Send';
	document.getElementById("expLik").innerHTML = 'If you have time to help us even more, answer this questionnaire.';
	document.getElementById("q1").innerHTML = 'Talking with the robot avatar was interesting';
	document.getElementById("q2").innerHTML = 'Variation of the speech characteristics made conversation more natural';
	document.getElementById("q3").innerHTML = 'Some randomly generated words are less pleasant than others';
	document.getElementById("q4").innerHTML = 'Some speech 	characteristics, such as speed, loudness or pitch influence more than others';
	document.getElementById("q5").innerHTML = 'Different random words didn’t have an impact on your enjoyment';
	document.getElementById("q6").innerHTML = 'You felt that the robot was answering your speech accordingly';
	document.getElementById("q7").innerHTML = 'Longer phrases were more interesting';
	document.getElementById("q8").innerHTML = 'The turn-based conversation felt unnatural';
	document.getElementById("q9").innerHTML = 'Foreign sounding phonemes were more interesting';
	document.getElementById("q10").innerHTML = 'The robot seemed to be intelligent';
};

b_esp.onclick = function() {
	document.getElementById('go').value= "Enviar";
	document.getElementById("expLik").innerHTML = 'Si tienes tiempo para ayudarnos aún más, responde a este cuestionario';
	document.getElementById("q1").innerHTML = 'Hablar con el avatar robot fue interesante';
	document.getElementById("q2").innerHTML = 'La variación de las características del habla hizo que la conversación fuera más natural';
	document.getElementById("q3").innerHTML = 'Algunas palabras generadas aleatoriamente son menos agradables que otras';
	document.getElementById("q4").innerHTML = 'Algunas características del habla, como la velocidad, el volumen o el tono, influyen más que otras en el disfrute de la conversación.';
	document.getElementById("q5").innerHTML = 'Las diferentes palabras generadas aleatoriamente no influyeron en el disfrute de la conversación.';
	document.getElementById("q6").innerHTML = 'Tenías la sensación de que el robot respondía a tu discurso adecuadamente.';
	document.getElementById("q7").innerHTML = 'Las frases más largas fueron más interesantes.';
	document.getElementById("q8").innerHTML = 'La conversación por turnos no resultaba natural.';
	document.getElementById("q9").innerHTML = 'Los fonemas que suenan estranjeros son más interesantes.';
	document.getElementById("q10").innerHTML = 'El robot pareció inteligente.";';
};
