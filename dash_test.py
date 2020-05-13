import dash
import dash_core_components as dcc 
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go 
import plotly.express as px
import base64
from dash.dependencies import Input, Output

# Read in dataframe 
df = pd.read_csv('cleaned_coffee_reviews.csv')
df = df.drop(columns=['Unnamed: 0.1','Unnamed: 0.1.1','Unnamed: 0'], axis=1)


# scatter plot: the ugly one
# trace = go.Scatter(x=df["Rating"], y=df["Prices Per Oz"], mode='markers')
# fig = go.Figure(data=trace)
# coffee_graph = dcc.Graph(figure=fig)


# THIS DOESN'T WORK WHEN THE DROPDOWNS ARE IN USE!!!!!!!!!!!

# fig.update_traces(textposition='top center')
# fig.update_layout(height=1000,title_text='Rating vs Prices Per Oz')

# Drop down menu options
features = df[['Flavor','Body','Aroma','Aftertaste','Acidity','Prices Per Oz','Agtron Ground']].copy()
f_options = [{'label' : i, 'value' : i} for i in features]

# Drop down menus
dropdown_x = dcc.Dropdown(
    id='x-axis-dropdown',
    options=f_options
)
dropdown_y = dcc.Dropdown(
    id='y-axis-dropdown',
    options=f_options
)


# Main App
app = dash.Dash()

# input box
input_box = dcc.Input(
    id='hello-world-input',
    placeholder='Enter a y-axis value',
    type='text',
    value=''
)  

# Plotly express scatter
# Beautiful graph but to show it in same page need dcc.Graph() not .show()
test = px.scatter(df, x='Rating', y='Prices Per Oz', color='Flavor')
# test.show()

app.layout = html.Div(children=[
    html.Div([
        html.H1('Finding The Perfect Cup of Coffee'),
        html.P('Annika M Noren, May 2020')],
        style = {'padding' : '50px' , 
                 'backgroundColor' : '#907A1C'}),
    html.P(''),
    input_box,
    html.Div(id='hello-world'),
    html.H2(''),
    html.H3('Feature to Sort'),
    dropdown_x,
    html.H3('Choose y-axis'),
    dropdown_y,
    dcc.Graph(figure=test),
    html.Div(id='coffee-graph')
    # this one might be redundant
    # coffee_graph

    # dcc.Graph(
    #     id='second plot',
    #     figure={
    #         'data': [trace2],
    #         'layout': go.Layout(
    #             title='Second Plot', 
    #             xaxis = {'title':'Rating'},
    #             yaxis = {'title':'Price'},
    #             barmode='stack')})
])


@app.callback(Output('hello-world', 'children'),
    [Input('hello-world-input','value')])
def render_header2(string):
    if string =='':
        string = 'World'
    render_string = f"Hello {string}!"
    return html.H2(render_string)

# This was from ugly graph above, for x and y
# Need to try it with express to get the z axis instead of x
@app.callback(Output('coffee-graph','children'),
    [Input('x-axis-dropdown','value'),
     Input('y-axis-dropdown','value')])
def render_coffee_scatter(x,y):
    if not x:
        x = 'Rating'
    if not y:
        y = 'Prices Per Oz'
    trace = go.Scatter(x=df[x], y=df[y], mode='markers')
    fig = go.Figure(data=trace)
    coffee_graph = dcc.Graph(figure=fig)
    return coffee_graph

if __name__ == '__main__':
    app.run_server(debug = True)



# ---------------------------------------------------------------------------#
# Extra Code that is obsolete, didn't work or not needed

# Helpful tutorial: https://www.youtube.com/watch?v=hRH01ZzT2NI

# Bean image, couldn't get it bigger
# image_filename = 'beans_leaf.jpeg' # replace with your own image
# encoded_image = base64.b64encode(open(image_filename, 'rb').read())
# html.Img(src='data:image/png;base64,{}, style={'width':'20%'}'.format(encoded_image))


# app.layout = html.Div('Coffee')

# app.layout = html.Div(children=[
#     html.H1('The Perfect Cup of Coffee'),
#     coffee_graph,
#     dcc.Graph(
#         id='second plot',
#         figure={
#             'data': [trace2],
#             'layout': go.Layout(title='Second Plot', barmode='stack')
#         }
#     )
# ])

# app.layout = html.Div([
#                 # adding a header and a paragraph
#                 html.Div([
#                     html.H1("Finding the Perfect Cup of Coffee")], 
#                     style = {'padding' : '50px' , 
#                              'backgroundColor' : '#907A1C'})
# ])

#  bar plot #2, this is not right, it's not the mean of price but cumulative
#  https://pbpython.com/plotly-dash-intro.html
# trace2 = go.Bar(x=df['Rating'], y=df['Prices Per Oz'])

# I forget what I used this for??
# coffee_graph = dcc.Graph(figure= fig,
#     'layout': go.Layout(
#         title = 'Coffee Plot',
#         xaxis = {'title': 'Rating'},
#         yaxis = {'title':'Price'}))