from pyscript import when, display, document

@when("click", "processButton")

def show_message(e):
    first = document.querySelector("#Fname").value
    age = document.querySelector("#Age").value
    campus = document.querySelector("#campus").value

    document.querySelector("#output").innerText = ""

    message = f"""👤 Student Profile
    Name   : {first}
    Age    : {age}
    Campus : {campus}

    ✏️ Notes:
    {first} is currently {age} years old and studies at {campus}.
    This information was gathered through input fields and displayed using
    a multiline string in Python via PyScript.
    """

    display(message, target="output")