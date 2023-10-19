import js

def util(text):
    e = js.document.getElementById(text).innerHTML = f"<h1>{text}</h1>"

def codeElement(id, codefile):
    code = f"""
        <py-repl src={codefile} id="{id}" output="{id}-output" stderr="{id}-err">
        </py-repl>

        <div id="{id}-output" class="border p-4"></div>
        <button type="button" class="btn btn-secondary m-1" onclick="document.getElementById('{id}-output').innerHTML='';
                                document.getElementById('{id}-err').innerHTML='';">
            Clear Output
        </button>
        """
    e = js.document.getElementById(id).innerHTML = f"<div>{code}</div>"