var b_pt = document.getElementById("ptbr");
var b_jp = document.getElementById("jap");
var b_eng = document.getElementById("eng");
var b_esp = document.getElementById("esp");

b_pt.onclick = function() {
	document.getElementById("Title").innerHTML = "Formulário de Consentimento e Instruções do Experimento";
	document.getElementById('exp').value = "Sobre o Experimento e Formulário de consentimento\n\n"+

"Pesquisador Chefe: Professor Ikuo Mizuuchi\n\n"+
"Numero de Aprovacao do Comite de Etica: No. 210801-0321\n\n"+
"Temos o prazer de anunciar que esta pesquisas médica para participantes com mais de 16 anos será conduzida por nosso laboratório em conformidade com as diretrizes éticas e a legislação japonesas vigentes, com a aprovação do Comitê de Revisão Ética da Universidade de Agricultura e Tecnologia de Tóquio (doravante denominada TUAT) e a permissão do Presidente da TUAT.Com estas aprovações, gostaríamos de pedir a sua colaboração voluntária. Informamos que a pesquisa não causará cansaço ou prejuízos excessivos aos voluntários. Além disso, tomaremos o máximo cuidado para proteger as informações pessoais dos particpantes.\n\n"+
"1) Objetivo de Pesquisa\n"+
"Este experimento consiste em um avatar amigável semelhante a um robô (Kotaro), com o qual você pode conversar pelo tempo que desejar. Você pode ter quantas conversas quiser, ou seja, não há tempo mínimo ou máximo para a duração deste experimento.Vídeos de suas expressões faciais serão filmados pela câmera de seu computador ou smartphone e armazenadas no servidor de nosso laboratório, junto com as emoções reconhecidas pelo software de reconhecimento de expressão facial. Esses dados serão usados posteriormente para analisar como as expressões faciais mudam dependendo de como o avatar robô fala. Ademais, tudo o que você disser ao avatar também será gravado e armazenado para análise posterior, portanto, tome cuidado com o que disser.Todos os dados obtidos neste experimento serão associados apenas ao seu ID de login, de forma que os pesquisadores não serão capazes de identificá-lo, a não ser que conheçam seu rosto e sua voz.\n\n"+
"2) Participação voluntária e liberdade de desistência \n"+
"A participação nesta pesquisa é totalmente voluntária. Em outras palavras, se você quiser contribuir para o desenvolvimento da ciência, você pode participar; e você pode desistir quando quiser sem nenhuma repercussão. Os dados que você fornecer para este estudo serão armazenados com segurança por 5 anos, durante os quais você pode solicitar a exclusão deles. Todos os dados coletados estarão associados ao seu ID de login, não ao seu nome real. Portanto, a recuperação e exclusão de dados só podem ser feitas na plataforma web do Mizuuchi Lab, e os pesquisadores não serão capazes de saber a quem os dados pertencem.É importante ressaltar que os responsáveis de participantes com menos de 20 anos de idade podem requisitar a remoção de seus dados e que não possam mais participar do experimento.\n\n"+
"3) Métodos de pesquisa e Como participar do Experimento\n"+
"Período da pesquisa: a partir da data de aprovação pelo Comitê de Ética de Pesquisa até 31 de março de 2022\n\n"+
"Método de pesquisa\n\n"+
"Para o desenvolvimento do módulo de estimativa de impressões humanas, uma plataforma web chamada “Fale com o Kotaro!” hospedada nos servidores do Mizuuchi Lab foi criada. Essa plataforma consiste em um avatar semelhante a um robô com o qual os voluntários podem manter uma conversa. No entanto, antes que os voluntários possam participar do experimento, é preciso criar um perfil que requer algumas informações básicas: ID de login; senha; era; Gênero; país / região de origem; língua materna; outras línguas que o usuário fala; se o voluntário mora ou já morou no exterior e onde; e quantos anos o voluntário vive/viveu no exterior.\n\n"+
"Como participar do Experimento\n\n"+
"1. É preciso de uma webcam para participar;\n"+
"2. Realize o experimento em um local bem iluminado;\n"+
"3. Digite seu ID de login, senha e as demais informações pessoais para criar seu perfil.\n"+
"Da segunda vez em diante, faça o login com o ID de login e a senha que você criou;\n"+
"4. Quando estiver pronto para falar, clique no botão Falar (botão verde com o desenho de uma orelha);\n"+
"5. Quando terminar de falar, clique no botão (ele terá se tornado azul com o desenho de um balão de fala) novamente;\n"+
"6. O avatar falará, então ouça e reaja naturalmente;\n"+
"7. Você pode repetir as etapas 4 a 6 quantas vezes quiser, mas, por favor, não feche a página antes do avatar terminar de falar;\n"+
"8. Ao fazer o logout, se tiver tempo, preencha uma pesquisa de 10 itens.\n"+
"9. Se você deseja excluir todos os dados coletados, clique no botão ''Excluir dados'' a qualquer momento.\n"+
"Clique no botão ''OK'' para confirmar.\n\n"+
"4) Benefícios e encargos para os sujeitos do estudo\n\n"+
"Durante o experimento, os voluntários conversarão com um avatar semelhante a um robô que gera padrões de fala livre de semântica pelo tempo que desejarem. Esperamos que os voluntários gostem da experiência. Não haverá compensação financeira pela participação neste experimento.\n\n"+
"5) Proteção de informações pessoais\n\n"+
"Para esta pesquisa, os dados pessoais dos voluntários serão armazenados nos servidores do Mizuuchi Lab por não mais que 5 anos. Os dados mencionados consistem em:\n\n"+
"1. ID de login;\n"+
"2. Senha;\n"+
"3. Idade;\n"+
"4. Gênero;\n"+
"5. País / Região de Origem;\n"+
"6. Língua materna;\n"+
"7. Outros idiomas que você fala;\n"+
"8. Se você mora ou já morou no exterior, escreva onde;\n"+
"9. Anos vivendo no exterior.\n"+
"10. Registros de voz do que os voluntários da pesquisa dizem ao avatar robô;\n"+
"11. Vídeo das expressões faciais dos voluntários após ouvirem a fala do avatar robô.\n"+
"12. Respostas do questionário\n"+
"6) Método de divulgação de protocolos de pesquisa e informações sobre pesquisa\n"+
"O protocolo e métodos de pesquisa serão divulgados integralmente na plataforma web “Fale com o Kotaro!” após 31 de março de 2022 . O protocolo não pode ser compartilhado atualmente porque o conhecimento total do protocolo de pesquisa pode alterar seus resultados.\n\n"+
"7) Publicação dos resultados da pesquisa\n"+
"Os resultados desta pesquisa serão apresentados em congressos nacionais e internacionais, publicados em artigos científicos e em trabalhos acadêmicos.\n\n"+
"8) Atribuição de direitos de propriedade intelectual decorrentes de pesquisa\n\n"+
"Nenhuma propriedade intelectual será atribuída a voluntários. Qualquer propriedade intelectual decorrente deste experimento pertence à TUAT e aos pesquisadores.\n"+
"9) Política de tratamento de Dados após a conclusão da pesquisa\n"+
"Cinco anos após o início do experimento, os dados de perfil, gravações de áudio e vídeo de todos os voluntários serão excluídos por meio do software mais recente (BleachBit) para garantir que ninguém, nem mesmo os pesquisadores, consigam recuperar os dados.\n\n"+
"10) Financiamento de pesquisa e conflito de interesses\n"+
"Os pesquisadores envolvidos declaram não ter nenhum conflito de interesses em relação a esta pesquisa e experimento. Este experimento não foi financiado por nenhuma organização, senão a TUAT.\n\n"+
"11) Informações de contato:\n"+
"Para perguntas (envie questionamentos em Inglês ou Japonês) sobre este experimento e a pesquisa atual, entre em contato com:\n\n"+

"Ikuo Mizuuchi,\n"+
"Universidade de Agricultura e Tecnologia de Tóquio,\n"+
"Escola de Pós-Graduação em Engenharia,\n"+
"Departamento de Engenharia de Sistemas Mecânicos\n"+
"Email: office(arroba)mizuuchi.lab.tuat.ac.jp\n\n"+
"12. Consentimento para cooperação no experimento\n"+
"Se você leu a explicação acima, entendeu todos os itens e concordou em cooperar voluntariamente com a pesquisa, clique no botão [Concordo]. Se você não concorda, feche esta janela.\n\n";
	document.getElementById('go').innerText= "Concordo";
};

b_jp.onclick = function() {
	document.getElementById("Title").innerHTML = "実験説明書＆同意書";
	document.getElementById('exp').value = "実験説明書＆同意書\n\n"+
"研究責任者　水内 郁夫\n\n"+
"東京農工大学工学府水内研究室\n\n"+
"このたび本研究室では、16歳以上の方を対象に下記の医学系研究を東京農工大学倫理審査委員会の承認ならびに学長の許可のもと、日本国の倫理指針および法令を遵守して実施しますので、ご協力をお願いいたします。この研究を実施することによる被験者の方への過大な負担はありません。また、被験者の方の個人情報の保護については細心の注意を払います。\n\n"+
"１．研究目的\n"+
"この実験は会話のできる友好的なロボット風のアバターを提供するもので、あなたはこのアバターと好きなだけ会話をすることができます。実験期間に最小や最大はありません。あなたのパソコンやスマートフォンのカメラからキャプチャされ、表情認識ソフトウェアにより認識された表情の種類とともに、研究室のサーバーに保存されます。アバターの発話の仕方によって、どのように表情が異なるかを解析するために、後日これらのデータを使用します。あなたがアバターに話す内容は事後分析のために保存されるので、何を話すかは注意してください。あなたとロボットとのやり取りから得られたデータはログインIDに関連付けられるため、研究者はあなたの顔や声を知らない限りあなたを特定することはできません。\n\n"+
"２．研究協力の任意性と撤回の自由\n"+
"この研究への参加は完全に自由意志によるものです。つまり、科学の発展に貢献したいと思えば参加することができますし、何の影響もなく好きな時に参加をやめることができます。あなたがこの研究に貢献したデータは5年間安全に保管され、その間あなたはご自分のデータの削除を要求することができます。あなたが決めたログインIDでログインして、「データ削除」をクリックすることにより削除することも可能です。収集したデータは、実名ではなく、ログインIDに関連付けられます。そのため、データの検索や削除は、水内研究室のWebプラットフォーム上でのみ行うことができ、研究者はデータが誰のものであるかを把握できない可能性があります。 また、注意事項として、20歳未満の被験者は、自身のデータを消去し実験から退くことを、彼らの親権者または法的保護者から求められる場合があります。\n"+
"３．研究方法・研究協力事項\n"+
"研究実施期間：倫理審査委員会で許可された日から2022年3月31日まで\n"+
"研究方法\n"+
"人間印象推定モジュールの開発では、水内研究室のサーバーに設置された「コタローと話そう！」というWebプラットフォームを利用しました。このプラットフォームは、ロボットのようなアバターで構成されており、あなたはこのアバターと会話をすることができます。実験に参加するためには、ログインID、パスワード、年齢、性別、出身国・地域、母語、その他の言語、海外在住・滞在経験の有無と場所、滞在年数などのプロフィールを作成する必要があります。\n"+
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
"研究協力事項\n\n"+
"４．研究対象者にもたらされる利益および不利益\n"+
"実験にご協力いただける方は、意味を持たない音声生成ロボットのようなアバターと、好きなだけ会話をすることができます。私たちは、実験協力者の皆さんがこの体験を楽しんでくれることを願っています。この実験への参加に対して、金銭的な補償はありません。\n\n"+
"５．個人情報の保護\n"+
"本研究では、実験協力者の個人データを水内研究室のサーバーに保存します。保存されるデータは以下の通りです。\n"+
"ログインID\n"+
"パスワード\n"+
"年齢\n"+
"性別\n"+
"生産国／地域\n"+
"母国語\n"+
"あなたが話す他の言語\n"+
"海外に住んでいる、または住んでいたことがある場合は、その国名\n"+
"海外に住んでいた年数\n"+
"研究ボランティアがロボット・アバターに話しかけた内容の音声記録\n"+
"ロボット型アバターの発話を聞いた後のボランティアの表情のビデオ記録\n"+
"アンケートの回答\n\n"+
"６．研究計画書等の開示・研究に関する情報公開の方法\n"+
"研究プロトコルおよび研究方法の詳細は、2022年3月31日以降に、Talk to Kotaro Web Platformで公開されます。研究プロトコルを知ることで研究結果が変わる可能性があるため、現在はプロトコルを公開できません。\n\n"+
"７．研究成果の公表\n"+
"本研究の成果は、国内外の学会発表および学術論文として発表される予定です。\n\n"+
"８．研究から生じる知的財産権の帰属\n"+
"知的財産を実験協力者に帰属させることはできません。本研究実験から得られた知的財産は、東京農工大学および研究者に帰属します。\n\n"+
"９．研究終了後の試料・データ取扱の方針\n"+
"実験開始から5年後、実験協力者の皆様のプロファイルデータ、音声およびビデオの記録は、最新のソフトウェア（BleachBit）を使用して削除され、研究者でさえも誰もこれらのデータを復元できないことが保証されます。\n\n"+
"１０．費用負担及び利益相反に関する事項\n"+
"関係する研究者は、本研究および実験に関して利益相反がないことを宣言します。\n"+
"本実験は、東京農工大学以外のいかなる機関からも資金提供を受けていません。\n\n"+
"１１．問い合わせ先\n\n"+
"本実験および現在の研究に関するお問い合わせは、下記までお願いいたします。\n"+
"水内 郁夫\n"+
"東京農工大学工学部機械システム工学科水内研究室 \n"+
"E-mail: office@mizuuchi.lab.tuat.ac.jp\n\n"+
"１２．実験への協力の同意\n"+
"以上の説明文書を読んで、各項目について理解し、自らの意思により研究への協力に同意される場合は、[同意する]ボタンをクリックしてください。 同意できない場合は、このウィンドウを閉じてください。";
	document.getElementById('go').innerText = "同意";
};
b_eng.onclick = function() {
	document.getElementById("Title").innerHTML = "Consent Form and Experiment Instructions";
	document.getElementById('exp').value = "Experiment Instructions & Consent Form\n\n"+
"Head of Research: Professor Ikuo Mizuuchi\n\n"+
"Ethics Committee approval number: No. 210801-0321\n\n"+
	"We are pleased to announce that the following medical research for participants over the age of 16 will be conducted in our laboratory in compliance with the Japanese ethical guidelines, laws and  regulations; with the approval of the Tokyo University of Agriculture and Technology (hereon referred as TUAT) Ethics Review Committee and the permission of the President of TUAT.With the approval of the TUAT Ethics Review Committee and the permission of the President, we will conduct the following medical research in compliance with the ethical guidelines and laws and regulations. We would like to kindly ask for your cooperation.  There will be no excessive burden on the subjects by participating in this research. In addition, we will take the utmost care to protect the personal information of the subjects.\n\n"+
"1) Research Purpose\n"+
	"This experiment provides a friendly robot-like avatar (Kotaro), with whom you can talk to for as long as you like. You can have as many conversations as you wish, that is there is no minimum nor maximum time for the duration of this experiment.Video images of your facial expressions will be captured from the camera of your computer or smartphone and stored on the server of our laboratory, along with the emotions recognized be the facial expression recognition software.  This data will later be used to analyze how facial expressions change depending on how the robot avatar speaks. Additionally, what you say to the avatar will also be recorded and stored for posterior analysis, so please be careful with what you say. All data recorded in this experiment will be associated only with your login ID, so the researchers will not be able to identify you, unless they know your face and voice.\n\n"+
"2) Voluntary research cooperation and freedom of withdrawal\n"+
"Participation in this research is completely voluntary. In other words, if you want to contribute to the development of science, you can participate; and you can stop participating whenever you want without any repercussions. The data you contribute to this study will be securely stored for 5 years, during which time you can request the deletion of your data. All data collected will be associated with your login ID, not your real name. Therefore, data retrieval and deletion can only be done on the Mizuuchi Lab web platform, and the researcher  will not be able to know whom data belongs to. 	It is important to notice that participants under 20 years old can have the removal of their data and withdrawal from the experiment requested by their parents or legal guardians.\n\n"+
"3) Research methods and research Cooperation Items\n"+
"Research period: from the date approved by the Institutional Review Board to March 31, 2022\n\n"+
"Research Method\n\n"+
"For the development of the Human Impression estimation module, a web platform named “Talk to Kotaro!” hosted in Mizuuchi Lab’s servers was implemented. That platform consists of a robot-like avatar with whom volunteers may hold a conversation. However, before volunteers can participate in the experiment, they need to create a profile which requires some basic information: login ID; password; age; gender; country/region of origin; mother language; other languages the user speaks; if the volunteer lives or has lived abroad and where; and how many years the volunteer has lived abroad.\n\n"+
"Research Cooperation Items\n\n"+
"1. You need a webcam to participate;\n"+
"2. Perform the experiment in a well-lit place;\n"+
"3. Enter your login ID, password and more to create your profile.\n"+
"From the second time onward, please log in with the login ID and *password you created;\n"+
"4. When you are ready to speak, click the Talk button (green button with the drawing of an ear);\n"+
"5. When you're done talking, click the button again (it will have become blue with the drawing of a speech bubble);\n"+
"6. The avatar will speak, so listen and react naturally;\n"+
"7. You can repeat steps 4-6 as often as you like, but please, do not close the page before the avatar stops speaking;\n"+
"8. If you have time to log out, please complete a 10-item survey.\n"+
"9. If you want to delete all the collected data, click the ''Delete data'' button at any time.\n"+
"Click and click the ''OK'' button to confirm.\n\n"+
"4) Benefits and burdens for study subjects\n\n"+
"Research volunteers will  spend  time talking with a semantic-free speech generating robot-like avatar for as long as desired. We hope that the volunteers will enjoy the experience. There will be no financial compensation for participation in this experiment.\n\n"+
"5)Protection of personal information\n\n"+
"For this research, personal data of research voluntaries will be stored in Mizuuchi Lab’s servers. The aforementioned data  consists of:\n"+
"1. Login ID;\n"+
"2. Password;\n"+
"3. Age ;\n"+
"4. Gender;\n"+
"5. Country/Region of Origin;\n"+
"6. Mother Language;\n"+
"7. Other Languages you Speak;\n"+
"8. If you live or have lived abroad, write where;\n"+
"9. Years living abroad.\n"+
"10. Voice records of what research volunteers say to the robot avatar;\n"+
"11. Video records of voluntaries facial expressions after their listen to the speech of the robot-like avatar.\n"+
"12. Questionnaire answers\n\n"+
"6) Method of Disclosure of Research Protocols and Information on Research"+
"The full research protocol and methods will be disclosed after March 31th of 2022 at the “Talk to Kotaro” Web Platform. The protocol cannot currently be shared because full knowledge of the research protocol may alter results of the research.\n\n"+
"7) Publication of Research Results\n\n"+
"The results of this research will be presented at domestic and international conferences and published in academic papers.\n\n"+
"8) Attribution of Intellectual Property Rights arising from Research\n\n"+
"Intellectual property cannot be attributed to volunteers. Any intellectual property resulting from this research experiment belongs to TUAT and the researchers.\n\n"+
"9) Data Handling Policy after research completion\n\n"+
"Five years after the start of the experiment, the profile data, audio and video recordings of all volunteers will be deleted using the latest software (BleachBit) to guarantee that no one, not even the researchers, will be able to recover the data.\n\n"+
"10) Research funding and conflict of interest\n\n"+
"Researchers involved declare that they do not have any conflict of interest regarding this research and experiment. This experiment was not funded by any organization other than TUAT.\n\n"+
"11) Contact Information:\n\n"+
"For inquiries regarding this experiment and the current research, please contact the following:\n\n"+
"Ikuo Mizuuchi,\n"+
"Tokyo University of Agriculture and Technology,\n"+
"Graduate School of Engineering,\n"+
"Mechanical Systems Engineering Department\n"+
"Email:  office(at)mizuuchi.lab.tuat.ac.jp\n\n"+
"12. Consent for cooperation in the experiment\n\n"+
"If you have read the above explanation, understoo each item, and voluntarily agree to cooperate in the research, please click the [Agree] button. If you do not agree, please close this window.";
	document.getElementById('go').innerText = 'I Agree';
};

b_esp.onclick = function() {
	document.getElementById("Title").innerHTML = "Instrucciones del Experimento y formulario de consentimiento";
	document.getElementById('exp').value = "Acerca del Experimento y formulario de consentimiento\n\n"+
"Investigador jefe: profesor Ikuo Mizuuchi\n\n"+
"Número de aprobación del Comité de Ética: No. 210801-0321\n\n"+
"Es con gran placer anunciar que esta investigación médica para participantes mayores de 16 años será realizada por nuestro laboratorio de acuerdo con las guías éticas y la legislación japonesas vigentes, con la aprobación del Comité de Revisor de Ética de la Universidade de Agricultura y Tecnología  de Tokyo (en adelante llamada de TUAT) y el permiso del Presidente de TUAT.Con estas aprobaciones, nos gustaría solicitar su colaboración voluntaria. Le informamos que la investigación no causará fatiga excesiva ni daño a los voluntarios. Además, tomaremos el máximo cuidado para proteger sus informaciónes personales.\n\n"+
"1) Objetivo de la Investigación Científica\n"+
"Este experimento consiste en un simpático avatar parecido a un robot (Kotaro), con el cual puedes hablar por el tiempo que quieras. Puede tener tantas conversaciones como desee, lo que significa que no hay un tiempo mínimo o máximo para la duración de este experimento.Los videos de sus expresiones faciales serán filmados por la cámara de su computadora o su teléfono inteligente y almacenados en el servidor de nuestro laboratorio, junto con las emociones reconocidas por el software de reconocimiento de expresiones faciales. Estos datos se utilizarán más adelante para analizar cómo cambian las expresiones faciales en función de cómo habla el avatar del robot. Además, todo lo que le diga al avatar también se grabará y se almacenará para investigación posterior, así que tenga cuidado con lo que decís.Todos los datos obtenidos en este experimento solo serán asociados a su ID de inicio de sesión, por lo que los investigadores no podrán identificar voluntarios a menos que conozcan sus rostros o su voces.\n\n"+
"2) Participación voluntaria y libertad de retractación\n"+
"La participación en este experimento  es completamente voluntario. En otras palabras, si quieres contribuir al desarrollo de la ciencia, puedes participar; y puedes abandonarlo cuando quieras sin ninguna repercusión. Los datos que proporciones para este estudio se almacenarán de forma segura durante 5 años, durante los cuales podrás solicitar su eliminación. Todos los datos recopilados se asociarán con su ID de inicio de sesión, no con su nombre real. Por lo tanto, la recuperación y eliminación de datos solo se puede realizar en la plataforma web de Mizuuchi Lab, y los investigadores no sabrán a quién pertenecen los datos.Es importante destacar que los responsables de los participantes menores de 20 años pueden solicitar la eliminación de sus datos y que ya no pueden participar en el experimento.\n\n"+
"3) Métodos de investigación y cómo participar en el experimento\n"+
"Período de investigación: desde la fecha de aprobación por el Comité de Ética en Investigación hasta el 31 de marzo de 2022\n\n"+
"Método de investigación\n\n"+
"Para el desarrollo del módulo de estimación de impresiones humanas, una plataforma web llamada ''¡Habla con Kotaro!'' alojada en los servidores de Mizuuchi Lab fue desarrollada. Esta plataforma consiste en un avatar similar a un robot con el que los voluntarios pueden mantener una conversación. Sin embargo, antes de que los voluntarios puedan participar en el experimento, deben crear un perfil que requiere cierta información básica: ID de inicio de sesión; contraseña; edad; Género; país / región de origen; lengua materna; otros idiomas que habla; si el voluntario vive o ha vivido en el extranjero y dónde; y cuántos años vive / ha vivido el voluntario en el extranjero.\n\n"+

"Cómo participar en el Experimento\n"+
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
"Haz clic en el botón ''Aceptar'' para confirmar la eliminación.\n"+

"4) Beneficios y cargos para los voluntarios.\n"+

"Durante el experimento, los voluntarios hablarán durante el tiempo que deseen con un avatar parecido a un robot que genera patrones de habla sin semántica. Esperamos que los voluntarios disfruten de la experiencia. No habrá compensación financiera por participar en este experimento.\n\n"+

"5) Protección de la información personal\n"+

"Para esta investigación, los datos personales de los voluntarios se almacenarán en los servidores de Mizuuchi Lab durante no más que 5 años. Los datos mencionados son:\n\n"+

"1. ID de inicio de sesión;\n"+
"2. Contraseña;\n"+
"3. Edad;\n"+
"4. Género;\n"+
"5. País / Región de origen;\n"+
"6. Lengua materna;\n"+
"7. Otros idiomas que habla;\n"+
"8. Si vive o ha vivido en el extranjero, escriba dónde;\n"+
"9. Años viviendo en el extranjero.\n"+
"10. Registros de voz de lo que los voluntarios de la investigación le dicen al avatar del robot;\n"+
"11. Video de las expresiones faciales de los voluntarios después de escuchar el discurso del avatar robot.\n"+
"12. Respuestas al cuestionario\n\n"+
"6) Método de difusión de protocolos de investigación e información de investigación\n"+
"El protocolo y los métodos de investigación se divulgarán en su totalidad en la plataforma web ''¡Habla con Kotaro!'' después del 31 de marzo de 2022. Actualmente, el protocolo no se puede compartir porque el conocimiento completo del protocolo de investigación puede alterar los resultados del experimento.\n\n"+
"7) Publicación de resultados de investigación\n"+
"Los resultados de esta investigación serán presentados en congresos nacionales y internacionales, publicados en artículos científicos y en trabajos académicos.\n\n"+
"8) Cesión de derechos de propiedad intelectual derivados de la investigación\n"+
"No se asignará propiedad intelectual a los voluntarios. Cualquier propiedad intelectual que surja de este experimento pertenece a TUAT y a los investigadores.\n\n"+
"9) Política de procesamiento de datos al completar la investigación científica\n"+
"Cinco años después del inicio del experimento, los datos de perfil, las grabaciones de audio y video de todos los voluntarios se eliminarán utilizando el software más reciente (BleachBit) para garantizar que nadie, ni siquiera los investigadores, puedan recuperar los datos.\n\n"+
"10) Financiamiento de la investigación y conflicto de intereses\n\n"+
"Los investigadores involucrados declaran no tener ningún conflicto de intereses en relación con esta investigación y experimento. Este experimento no fue financiado por ninguna otra organización que no sea TUAT.\n\n"+

"11) Información de contacto:\n\n"+

"Si tiene preguntas (envíe consultas en Inglés o Japonés) sobre este experimento y la investigación actual, comuníquese con:\n\n"+

"Ikuo Mizuuchi,\n"+
"Universidad de Agricultura y Tecnología de Tokio,\n"+
"Escuela de Graduados en Ingeniería,\n"+
"Departamento de Ingeniería de Sistemas Mecánicos\n"+
"Correo electrónico: office(arroba)mizuuchi.lab.tuat.ac.jp\n\n"+

"12. Consentimiento para la cooperación en el experimento.\n"+
"Si ha leído la explicación anterior, ha entendido todos los elementos y ha aceptado voluntariamente cooperar con la encuesta, haga clic en el botón [Acepto]. Si no está de acuerdo, cierre esta pantalla.";
	document.getElementById('go').innerText = "Acepto";
};
