# This file contains the HTML and CSS code in the form of a string with unnecessary spaces 
# and paragraphs truncated to save memory on the Raspberry Pi Pico.
def getHTML(state):
    html =  """
    <!DOCTYPE html>
    <html>

    <head>
      <title>ChemBot</title>
    </head>
    <style>
      * {
        color: #2d9d96;
        font-family: Arial;
      }

      label {
        width: 120px;
        display: inline-block;
        color: blue
      }

      table,
      tr,
      td {
        border: 1px solid #96ceca;
        border-collapse: collapse;
        color: #96ceca;
        font-size:13px
      }

      input {
        width: 35px;
        height: 13px;
        background-color: transparent;
        border: none;
      }

      input[type=submit]:focus {
        background-color: #96ceca;
      }

      .buttons {
        color: #fff;
        width: 100px;
        padding: 20px;
        border-radius: 5px;
        margin: 20px
      }

      #container {

        height: 100px;
        position: absolute;
      }

      #navi,
      #infoi {
        width: 100%;
        height: 100%;
        position: absolute;
        top: 0;
        left: 0;
      }

      #infoi {
        z-index: 10;
      }
    </style>

    <body>
      <div style="width: 100%; background-color: #96ceca;"><img src="https://www.dropbox.com/s/63xe0abqjbkc5po/Chembot_Logo_t_t.png?dl=0&raw=1" height=100px /></div>
      <div style="margin: 20px"> Introduction text.
        <p>You selected {""" + str(state) + """}</p>
      </div>
      <div style="display: flex;">
        <form action="./startAnalysis">
          <input style="background-color: #96ceca;" type="submit" value="START" class="buttons" />
        </form>
        <form action="./resetSelection">
          <input style="background-color: #868687" type="submit" value="RESET" class="buttons" />
        </form>
      </div>
      <div id="container">
        <div id="navi">
          <iframe src="http://127.0.0.1:8000/" name="SELFHTML_in_a_box">
          </iframe>
        </div>
        <div id="infoi">
          <table>
            <tr>
              <td>
                <form action="./(0,0)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(0,1)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(0,2)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(0,3)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(0,4)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(0,5)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(0,6)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(0,7)"><input type="submit" value=""/></form>
              </td>
            </tr>
            <tr>
              <td>
                <form action="./(1,0)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(1,1)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(1,2)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(1,3)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(1,4)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(1,5)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(1,6)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(1,7)"><input type="submit" value=""/></form>
              </td>
            </tr>
            <tr>
              <td>
                <form action="./(2,0)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(2,1)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(2,2)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(2,3)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(2,4)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(2,5)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(2,6)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(2,7)"><input type="submit" value=""/></form>
              </td>
            </tr>
            <tr>
              <td>
                <form action="./(3,0)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(3,1)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(3,2)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(3,3)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(3,4)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(3,5)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(3,6)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(3,7)"><input type="submit" value=""/></form>
              </td>
            </tr>
            <tr>
              <td>
                <form action="./(4,0)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(4,1)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(4,2)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(4,3)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(4,4)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(4,5)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(4,6)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(4,7)"><input type="submit" value=""/></form>
              </td>
            </tr>
            <tr>
              <td>
                <form action="./(5,0)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(5,1)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(5,2)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(5,3)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(5,4)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(5,5)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(5,6)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(5,7)"><input type="submit" value=""/></form>
              </td>
            </tr>
            <tr>
              <td>
                <form action="./(6,0)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(6,1)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(6,2)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(6,3)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(6,4)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(6,5)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(6,6)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(6,7)"><input type="submit" value=""/></form>
              </td>
            </tr>
            <tr>
              <td>
                <form action="./(7,0)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(7,1)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(7,2)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(7,3)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(7,4)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(7,5)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(7,6)"><input type="submit" value=""/></form>
              </td>
              <td>
                <form action="./(7,7)"><input type="submit" value=""/></form>
              </td>
            </tr>
            
          </table>
        </div>
      </div>
    </body>

    </html>
    """
    replacements = ["                ", "                ", "    ", "  ", "\n"]
    for r in replacements:
        html = html.replace(r, "")
    print(html)
    return html

