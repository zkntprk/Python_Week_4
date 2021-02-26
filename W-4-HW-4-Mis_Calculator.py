### All Rights Reserved ###

#Copyright (c) ${Mis_Calculator.2021} ${Ozkan TOPRAK}

#Created by InfotecAcademy

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.

import Sum, Divide, Minus, Multiple
while True:
    try:
        a = int(input('Which calculation you want to do: \n1-Sum \n2-Minus  \n3-Multiple  \n4-Divide\n'))
        t=1
        if 0<a<5:
            x = float(input('Please enter 1. value : '))
            y = float(input('Please enter 2. value : '))
        if a==1:
            print(f'Sum of {x} and {y} is = ', Sum.s(x,y))
        elif a==2:
            print(f'Minus of {x} and {y} is = ', Minus.mi(x, y))
        elif a==3:
            print(f'Multiple of {x} and {y} is = ', Multiple.mu(x, y))
        elif a==4:
            print(f'Division of {x} and {y} is = ', Divide.d(x, y))
        else:
            print('What do you really want to do? Please select one of four options.')
        while t==1:
            r=str(input('Do you want to make another calculation (Y/N): '))
            if r=='Y' or r=='y':
                t+=1
            elif r=='N' or r=='n':
                print('Thank you. Have a nice day.')
                t=5
            else:
                print('Please just select just "Y" or "N" ')
                t=2
        if t==5:
            break
    except ValueError:
        print('Not correct Value Entry, Please Try Again')
    except ZeroDivisionError:
        print('Zero Division is not possible mathematically! Please Try Different')

### All Rights Reserved ###

#Copyright (c) ${Mis_Calculator.2021} ${Ozkan TOPRAK}

#Created by InfotecAcademy

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.
