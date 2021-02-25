### All Rights Reserved ###

#Copyright (c) ${PasswordGenerator.2021} ${Ozkan TOPRAK}

#Created by InfotecAcademy

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.

from tkinter import *
import random, string
#import pyperclip

root =Tk()
root.geometry("350x350")
root.title("InfoTechAcademy - RANDOM PASSWORD GENERATOR")

Label(root, text = 'PASSWORD GENERATOR' , font ='arial 15 bold').pack()

Label(root, text ='InfoTechAcamedy', font ='arial 13 bold').pack(side = BOTTOM)

pass_str = StringVar()
def Generator():
    password = ''
    for x in range (0,6):
        password = random.choice(string.ascii_uppercase)+random.choice(string.ascii_uppercase)+random.choice(string.digits)+random.choice(string.digits)+random.choice(string.punctuation)+random.choice(string.punctuation)
    for y in range(4):
        password = password+random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)

Button(root, text = "GENERATE PASSWORD" , command = Generator ).pack(pady= 10)
Entry(root , textvariable = pass_str).pack()

root.mainloop()

### All Rights Reserved ###

#Copyright (c) ${PasswordGenerator.2021} ${Ozkan TOPRAK}

#Created by InfotecAcademy

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.