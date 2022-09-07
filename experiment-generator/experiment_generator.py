#!/usr/bin/env python3
import sqlite3 as sql


def generate_questionnaire_page(prompts={},
                              page_name= "MyConsent.html",
                              page_title="Talk to Kotaro",
                              action_url="questionnaire_answer"):

    with open(page_name,"w") as f:
        f.write('''<!DOCTYPE html>
        <html>
        <head>
          <title>''' + str(page_title) + '''</title>
        </head>
        <style>

        	div {
        		display: flex;
        		justify-content: center;
        	}
          table,
          table td {
            border: 1px solid #cccccc;
          }
          td {
            height: 160px;
            width: 160px;
            text-align: center;
            vertical-align: middle;
          }
          input[type='radio'] {
            transform: scale(4);
        }
        </style>
        <form action="''' + action_url + '''" method = "POST">
        <div>
        <table>\n''')

        questionCounter = 1

        for prompt in prompts:
            promptText = prompt
            promptOptions = prompts[prompt]
            f.write("\t\t\t\t<tr>\n")
            f.write("\t\t\t\t\t<td><p id=q" + str(questionCounter) + ">" +
                str(promptText) + "</p></td>\n")
            optionCounter = 1
            for option in promptOptions:
                f.write('\t\t\t\t\t\t<td><p>' + str(option) +
                    '</p><input type="radio" id="A' + str(questionCounter) +
                    str(optionCounter) + '" name="q' + str(questionCounter) +
                    '" ' + 'value="' + str(optionCounter) +
                    '"><p>\n</p></td>\n')
                optionCounter+=1
            f.write("\t\t\t\t</tr>\n")
            questionCounter += 1

        f.write('''\t\t\t\t</table>
        </div>
            <div>
                <input id="go" type="submit" value="Submit" style="height:70px;width:200px;font-size : 20px; ">
            </div>
            </body>
        </html>''')


def generate_explanation_page(page_name="MyExplanation.html",
                              page_title="Talk to Kotaro",
                              action_url="MyConsent.html",
                              explanation_contents="Teste teste"):
    with open(page_name,"w") as f:
        f.write('''<!DOCTYPE html>
<html>
<head>
  <title>''' + page_title + '''</title>
</head>
<style>
	div {
		display: flex;
		justify-content: center;
	}
</style>
<body>
        <h1 id="Title">Experiment Instructions</h1>
        <div>
            <textarea id="exp" readonly name="w3review" rows="45" cols="75" style="resize: none;">'''+ explanation_contents+'''</textarea>
        </div>
        <div>
            <a href="''' + action_url + '''" id=test><button id="go" style="height:40px;width:100px">Understood</button></a>
        </div>
    </body>
</html>''')


def generate_consent_form(page_name="MyConsent.html",
                          page_title="Talk to Kotaro",
                          action_url="after_consent",
                          explanation_contents="Teste teste",
                          requires_signature=False):
    with open(page_name,"w") as f:
        f.write('''<!DOCTYPE html>
<html>
<head>
  <title>''' + page_title + '''</title>
</head>
<style>
	div {
		display: flex;
		justify-content: center;
	}
</style>
<body>
        <h1 id="Title">Consent Form</h1>
        <div>
            <textarea id="exp" readonly name="consent_explanation" rows="45" cols="75" style="resize: none;">'''+ explanation_contents+'''</textarea>
        </div>
        <div>''')

        if requires_signature:
            f.write('''<form enctype="multipart/form-data" action="''' + action_url + '''" method = "POST">
                    <hr>
                    <div style="text-align:center;">
                      <p>Upload a .png or .pdf file containing your signature.</p>
                      <input type="file" accept="image/*,.pdf" id="fFile" name="fFile">
                    </div>
                    <hr>
                  </div>
                  <div style="text-align: center">
                  <input id="submit" type="submit" value="I Agree">
                  </div>
              </body>
          </html>'''
            )
        else:
            f.write('''<a href="''' + action_url + '''" id=test><button id="go" style="height:40px;width:100px">I Agree</button></a>
        </div>
    </body>
</html>''')


def generate_data_deletion_page(page_name="MyDeletion.html",
                                page_title="Talk to Kotaro",
                                action_url="deletion_url",
                                cancel_url="cancel_url",
                                deletion_text='Press "Delete" to delete and cancel to give up.'):

    with open(page_name,"w") as f:
        f.write('''<!DOCTYPE html>
<html>
<head><title>''' + page_title + '''</title></head>
<style>
body{
width:100%;
text-align:center;
}
</style>
  <body>
<h2>''' + deletion_text + '''</h3>
<a href="''' + action_url + '''" id=test><button id="delete" style="height:40px;width:100px">Delete</button></a>
<a href="''' + cancel_url + '''" id=test><button id="cancel" style="height:40px;width:100px">Cancel</button></a>
  </body>
</html>''')

def generate_profile_page(fields=["ID","password","gender","age"],
                          page_name= "MyProfile.html",
                          page_title="Talk to Kotaro",
                          action_url="create_profile"):
    with open(page_name,"w") as f:
        f.write('''<!DOCTYPE html>
        <html>
        <head><title>Talk to Kotaro</title></head>
        <style>
        div {
          width: 500px;
          margin: auto;

        }
        </style>\n''')

        f.write('''<h1 id="title" style="text-align: center">Profile Creation</h1>
        <h3 id="truth" style="text-align: center">Your data will be used for scientific research, so please, be truthful.</h3>
        <form action="'''+action_url+'''" method = "POST">
        <div style="text-align: right">\n''')

        for field in fields:
            f.write('<label id="f' + field + '" for="f' + field+ '">'+field+': </label>\n')
            f.write('<input type="text" id="f' + field + '" name="f' + field + '"><br><br>\n')


        f.write('''<input id="submit" type="submit" value="Submit">
        <p id="instructions">Click on the "Submit" button to create your profile.</p>
        </div>
        </form>
        </body>
        </html>''')

def generate_database(db_name = "database.sql",
                      tables_fields={"profile":{"ID":"TEXT",
                                     "password":"BLOB"},
                                     "analysis":{"Number":"TEXT",
                                     "test":"TEXT"}}):
    db = sql.connect(db_name)
    cursor = db.cursor()
    for table in tables_fields:
        cursor_command = 'CREATE TABLE IF NOT EXISTS '+table+ ' (\n'
        for field in tables_fields[table]:
            cursor_command +=  str(field)+" "+str(tables_fields[table][field])+",\n"
        cursor_command = cursor_command[:-2]+"\n)"
        print(cursor_command)
        cursor.execute(cursor_command)
        db.commit()
    db.close()


def generate_experiment_page(page_name= "MyExperiment.html",
                             javascript_name = "MyExperiment.js",
                             page_title="Talk to Kotaro",
                             action_url="experiment_action",
                             record_audio=True,
                             record_video=True,
                             show_video=True,
                             avatar_images=[],
                             avatar_sequence="random",
                             exit_button = True,
                             explanation_button = True,
                             deletion_button = True,
                            ):
    pass
