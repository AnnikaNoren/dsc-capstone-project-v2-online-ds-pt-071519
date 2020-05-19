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
country_dummies = pd.get_dummies(df['Coffee Country'], prefix='CC')
df = pd.concat([df, country_dummies], axis=1)

# scatter plot: the ugly one

# trace = go.Scatter(x=df["Rating"], y=df["Prices Per Oz"], mode='markers')
# fig = go.Figure(data=trace)
# coffee_graph = dcc.Graph(figure=fig)


# THIS DOESN'T WORK WHEN THE DROPDOWNS ARE IN USE!!!!!!!!!!!

# fig.update_traces(textposition='top center')
# fig.update_layout(height=1000,title_text='Rating vs Prices Per Oz')

# Drop down menu options for coffee
features = df[['Flavor','Body','Aroma','Aftertaste','Acidity','Prices Per Oz','Agtron Ground',
               'CC_Kenya','CC_Ethiopia','CC_Colombia','CC_Panama','CC_Indonesia','CC_Guatemala']].copy()
f_options = [{'label' : i, 'value' : i} for i in features]

# Drop down menus for coffee graph
dropdown_color = dcc.Dropdown(
    id='color-axis-dropdown',
    options=f_options
)
dropdown_y = dcc.Dropdown(
    id='y-axis-dropdown',
    options=f_options
)

# Plotly express scatter
# Beautiful graph but to show it in same page need dcc.Graph() not .show()
# pretty_coffee = px.scatter(df, x='Rating', y='Prices Per Oz', color='Flavor')
# pretty_coffee.show()

# Main App
app = dash.Dash()

# input box for Hello World!
# this was for practice
#
# input_box = dcc.Input(
#     id='hello-world-input',
#     placeholder='Enter a y-axis value',
#     type='text',
#     value=''
# )  

app.layout = html.Div(children=[
    html.Div([
        html.H1('Finding The Perfect Cup of Coffee'),
        html.H2('Annika M Noren, May 2020'),
        html.Label(['My GitHub ', html.A('link', 
            href='https://github.com/AnnikaNoren/dsc-capstone-project-v2-online-ds-pt-071519')])],
        style = {'padding' : '50px' , 
                 'backgroundColor' : '#ffd45e'}),
    html.P(''),
    # input_box,
    # html.Div(id='hello-world'),
    html.H2(''),
    html.H3('The x-axis remains constant with the Rating feature'),
    html.H3('Select the feature to sort'),
    dropdown_color,
    html.H3('Select the y-axis'),
    dropdown_y,
    # dcc.Graph(figure=pretty_coffee),
    html.Div(id='coffee-graph')
])


@app.callback(Output('coffee-graph','children'),
    [Input('color-axis-dropdown','value'),
     Input('y-axis-dropdown','value')])
def render_coffee_scatter(color, y):
    if not color:
        color = 'Flavor'
    if not y:
        y = 'Prices Per Oz'

    pretty_coffee = px.scatter(df, x='Rating', y=y, color=color, height=700,
        color_continuous_scale='Rainbow')
    coffee_graph = dcc.Graph(figure=pretty_coffee)

    # This graph is not as pretty as the px one used above
    # trace = go.Scatter(x=df[x], y=df[y], mode='markers')
    # fig = go.Figure(data=trace)
    # coffee_graph = dcc.Graph(figure=fig)
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

# @app.callback(Output('hello-world', 'children'),
#     [Input('hello-world-input','value')])
# def render_header2(string):
#     if string =='':
#         string = 'World'
#     render_string = f"Hello {string}!"
#     return html.H2(render_string)

# More extra code
    # dcc.Graph(
    #     id='second plot',
    #     figure={
    #         'data': [trace2],
    #         'layout': go.Layout(
    #             title='Second Plot', 
    #             xaxis = {'title':'Rating'},
    #             yaxis = {'title':'Price'},
    #             barmode='stack')})

#  color https://plotly.com/python/builtin-colorscales/
