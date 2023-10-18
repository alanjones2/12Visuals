import js

def util(text):
    e = js.document.getElementById(text).innerHTML = f"<h1>{text}</h1>"

def codeElement(id, codefile):
    code = f"""
        <py-repl src={codefile} id="{id}" output="{id}" stderr="{id}">
        </py-repl>

        <div id="{id}" class="border p-4"></div>
        <button type="button" class="btn btn-secondary m-1" onclick="document.getElementById('output4').innerHTML='';
                                document.getElementById('{id}').innerHTML='';">
            Clear Output
        </button>
        """
    e = js.document.getElementById(id).innerHTML = f"<div>{code}</div>"