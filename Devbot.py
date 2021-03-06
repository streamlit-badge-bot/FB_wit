import streamlit as st
from streamlit_ace import st_ace
from wit import Wit

access_token="56MHVINSJPQIMHIHPGZCOHTPU64ZJUXY"
client = Wit(access_token)
intent=""
entity=""

LANGUAGES = ["python"]

THEMES = ["solarized_light","github","twilight","eclipse"]

KEYBINDINGS = [
    "sublime","emacs","vim", "vscode"
]

def output(intent,entity):
    if intent == 'create_list':
        return f"{entity} = []"
    elif intent=="range":
        return f"range({entity})" 
    elif intent=="sort_ascending":
        return f"sorted_list = {entity}.sort()"
    elif intent=="list_max":
        return f"max_element=max({entity})"
    elif intent=="list_len":
        return f"length=len({entity})" 
    elif intent=="list_reverse":
        return f"reverse_list={entity}.reverse()"
    else:
        return "#Instruct with text" 


st.title('FB Wit.ai App - DevCoder')
st.sidebar.title(":memo:Code Editor Settings") 
st.text('Editor')   
content = st_ace(
        placeholder= "Enter your code",
        height = 250,
        language=st.sidebar.selectbox("Select Language.", options=LANGUAGES),
        theme=st.sidebar.selectbox("Editor Theme.", options=THEMES),
        keybinding=st.sidebar.selectbox("Keybinding mode.", options=KEYBINDINGS),
        font_size=st.sidebar.slider("Font size.", 5, 24, 12),
        tab_size=st.sidebar.slider("Tab size.", 1, 8, 4),
        show_gutter=st.sidebar.checkbox("Show gutter.", value=True),
        show_print_margin=st.sidebar.checkbox("Show print margin.", value=True),
        key="ace-editor1",
        wrap=True
    )


MyText = st.text_input("Enter prompt","Ex: Sort the list 'elements'")
try:
    if st.button('Get Code'):
    	response = client.message(MyText)
    	intent = response['intents'][0]['name']
    	entity = response['entities']['list_name:list_name'][0]['value']
    	
    		
except:
        st.warning('Ambiguous query. Please try again')    

if len(MyText)>0:
    st_ace(value=output(intent,entity),height=50)
