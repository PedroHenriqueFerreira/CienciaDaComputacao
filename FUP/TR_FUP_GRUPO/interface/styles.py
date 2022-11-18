import PySimpleGUI as sg

from config import maskConfig

fontName = 'Rubik'

theme =  {
    'BACKGROUND': '#2E3440',
    'TEXT': '#D8DEE9',
    'INPUT': '#3B4252',
    'TEXT_INPUT': '#D8DEE9',
    'SCROLL': '#3B4252',
    'BUTTON': ('#3B4252', '#88C0D0'),
    'LIGHT_BUTTON': ('#88C0D0', '#3B4252'),
    'DANGER_BUTTON': ('#BF616A', '#3B4252'),
    'BUTTON_HOVER': ('#3B4252', '#B7EFFF'),
    'LIGHT_BUTTON_HOVER': ('#B7EFFF', '#3B4252'),
    'DANGER_BUTTON_HOVER': ('#EE9099', '#3B4252'),
    'BUTTON_DISABLED': ('#5B7A88', ''),
    'LIGHT_BUTTON_DISABLED': ('#5B7A88', ''),
    'DANGER_BUTTON_DISABLED': ('#774B55', ''),
    'PROGRESS': 0,
    'BORDER': 0,
    'SLIDER_DEPTH': 0,
    'PROGRESS_DEPTH': 0,
}

# Aplica o tema
sg.LOOK_AND_FEEL_TABLE['theme'] = theme
sg.theme('theme')

def Popup(layout):
    ''' Cria um popup '''
    
    return sg.Window(
        title='BuscBus', 
        layout=layout, 
        finalize=True, 
        keep_on_top=True
    )

def Page(layout, resizable=False):
    ''' Cria uma página '''
    
    return sg.Window(
        title='BuscBus', 
        layout=layout, 
        finalize=True, 
        resizable=resizable
    )  

def Column(layout):
    ''' Cria uma coluna '''
    
    return sg.Column(layout)

def Image(image):
    ''' Cria uma imagem '''
    
    return sg.Image(
        source=image, 
        pad=(5, 10), 
        key='-IMAGE-'
    )

def Title(text):
    ''' Cria um cabeçalho '''
    
    return sg.Text(
        text=text, 
        font=(fontName, 25, 'bold'), 
        pad=(5, 10)
    )

def Text(text):
    ''' Cria um texto '''
    
    return sg.Text(
        text=text, 
        font=(fontName, 15, 'normal'), 
        pad=(5, 10)
    )

def Separator():
    ''' Cria um separador '''
    
    return Text('  |  ')

def Push():
    ''' Cria um espaçamento '''
    
    return sg.Push()

def Input(key, password_char='', default_text=''):
    ''' Cria um campo de entrada de texto '''
        
    return sg.Input(
        size=(30, 1), 
        password_char=password_char, 
        key=key, 
        font=(fontName, 15, 'normal'), 
        pad=(5, 10), 
        enable_events=key in maskConfig, 
        default_text=default_text
    )   

def Storage(key, value):
    ''' Armazena um valor '''
    
    return sg.Input(
        visible=False, 
        key=key, 
        default_text=value
    )

def Button(text, key, type=0, disabled=False):
    ''' Cria um botão '''
    
    BUTTON = ['BUTTON', 'LIGHT_BUTTON', 'DANGER_BUTTON'][type]
    BUTTON_HOVER = ['BUTTON_HOVER', 'LIGHT_BUTTON_HOVER', 'DANGER_BUTTON_HOVER'][type]
    BUTTON_DISABLED = ['BUTTON_DISABLED', 'LIGHT_BUTTON_DISABLED', 'DANGER_BUTTON_DISABLED'][type]
    
    return sg.Button(
        text, 
        key=key, 
        font=('Rubik', 15, 'normal'), 
        pad=(5, 10), 
        disabled=disabled,  
        button_color=theme[BUTTON], 
        mouseover_colors=theme[BUTTON_HOVER], 
        disabled_button_color=theme[BUTTON_DISABLED]
    )

def Select(data, key):
    ''' Cria um campo de seleção '''
    
    return sg.Combo(
        values=data, 
        default_value=data[0], 
        font=(fontName, 15, 'normal'), 
        readonly=True, 
        key=key, 
        size=(22, 1), 
        pad=(5, 10)
    )


def Table(headings, values, col_widths, key):
    ''' Cria uma tabela '''
    
    return sg.Table(
        values=values, 
        headings=headings, 
        col_widths=col_widths, 
        font=('Rubik', 15, 'normal'), 
        key=key, 
        pad=(5, 10), 
        justification='c', 
        enable_events=True, 
        border_width=0, 
        header_border_width=0, 
        row_height=35, 
        num_rows=12, 
        header_font=(fontName, 15, 'bold'), 
        auto_size_columns=False, expand_x=True, expand_y=True)