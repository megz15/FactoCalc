'''
    Program: FactoCalc
    Version: 1.4
    Author : Meghraj Goswami
    Github : github.com/megz15/FactoCalc
'''

try:
    import PySimpleGUI as sg
    from webbrowser import open as wb
    sg.theme('DarkBlack1')
    
    #Factorial Function (Used while loop instead of recursion or predefined method)
    def fctrl(k):
        if k==0 or k==1:
            return 1
        elif k<0:
            return('Error: Factorial of negative integer not possible')
        else:
            j=1
            while k>1:
                j*=k
                k-=1
            return(j)
        
        
    menu_def = [['&Menu', ['&Clear All','&About','E&xit','---','Su&rprise']]]
    
    layout = [[sg.Menu(menu_def,tearoff=False)],
              [sg.Text('Calculate factorial of:'),sg.InputText(size=(4,None)),sg.Button(' ! ',tooltip='Calculate factorial\nFactorial of n is n*(n-1)*(n-2)*(n-3)...upto n-(n-1)')],
              [sg.Text('-'*55,font=('Calibri', 11))],
              [sg.Radio('Permutation','ftype',default=True,enable_events=True,tooltip='Permutation - arranging elements from a set, such that the order of selection matters'),sg.Text(),sg.Radio('Combination','ftype',enable_events=True,tooltip='Combination - selecting elements from a set, such that the order of selection does not matter')],
              [sg.Text(' '*7),sg.InputText(size=(3,None)),sg.Text(' '*16),sg.Button('Calculate',tooltip='Calculate nPr or nCr')],
              [sg.Text(' '*12),sg.Text('P',key='-R-'),sg.Text(' '*15),sg.Button('About'.center(11),tooltip='Shows information and description about the project')],
              [sg.Text(' '*13),sg.InputText(size=(3,None)),sg.Text(' '*10),sg.Button('Exit'.center(14))]]
    
    window = sg.Window('FactoCalc',layout,font=('Helvetica', 14))
    
    while True:
        event, values = window.read()
        
        if event==sg.WIN_CLOSED:
            break
        if event in ('Exit'.center(14),'Exit'):
            if sg.popup_yes_no('Are you sure you want to exit?',title='Exit')=='Yes':
                sg.popup_auto_close('Goodbye!',auto_close_duration=1)
                break
        
        elif event==' ! ':
            a = int(values[1])
            b = ''
            while a>1:
                b+=str(a)+' * '
                a-=1
            if int(values[1])>1:
                b+='1 = '
            sg.popup(b,fctrl(int(values[1])),title='Factorial')
       
        elif event in ('About'.center(11),'About'):
            sg.popup('FactoCalc 1.2:\nGet factorials, permutations and combinations of numbers\n\nMade in Python 3.7.7 by Meghraj Goswami',title='About Program')
       
        elif event=='Calculate':
            if values[2]==True and values[3]==False:
                ans = int(fctrl(int(values[4]))/fctrl(int(values[4])-int(values[5])))
                sg.popup(values[4]+' P '+values[5]+' = '+str(ans),title='Permutation')
            elif values[2]==False and values[3]==True:
                ans = int(fctrl(int(values[4]))/(fctrl(int(values[4])-int(values[5]))*fctrl(int(values[5]))))
                sg.popup(values[4]+' C '+values[5]+' = '+str(ans),title='Combination')
       
        elif event=='Clear All':
            window[1].update('')
            window[4].update('')
            window[5].update('')
            window[2].update(True)
            window['-R-'].update('P')
        
        elif event=='Surprise':
            sg.popup_timed(image='qrick.png',auto_close_duration=3,button_type=5,title='Free BTC')
            
        elif event==2:
            window['-R-'].update('P')
        elif event==3:
            window['-R-'].update('C')
        
    window.close()

except BaseException as e:
    print(e)
    window.close()
