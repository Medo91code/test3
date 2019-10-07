import dash
import dash_core_components as dcc
import  dash_html_components as html

app= dash.Dash()                          #   []      {}

colors={'text1':'#ff0000','text2':'#1122F2','bg1':'#12F319 ','bg2':'#F2F211 '}

app.layout= html.Div\
([

    html.H1('Hallo',style={'textAlign':'center' ,'color':colors['text1']}),
    html.P('here is medo',style={'textAlign':'center' ,'color':colors['text1']}),

    dcc.Graph (
        id='graph mexo',
        figure={

                'data':[
                           {'x':[1,2,3,4,5],'y':[1,2,3,4,5] , 'type':'bar' , 'name':'first','marker': {'color': colors['text2'],'size': int(2)}
                            },
                           {'x':[5,4,3,2,1],'y':[1,2,3,4,5],'name':'second','type':'marker'}
                       ],
                'layout':{
                           'title':'meme',
                           'plot_bgcolor':colors['bg1'],
                           'paper_bgcolor':colors['bg2'],
                           'font':{'color':colors['text2']}
                         }
               }
              ),



])

app.run_server()


